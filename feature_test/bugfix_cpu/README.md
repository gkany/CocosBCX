# 1. bugfix:  
主要是磁盘文件的读写，从串行改成并行多任务模式：  
对应接口主要是：open和flush  
主要逻辑修改如下：  
**修改前：**  
``` c++  
void object_database::flush()
{
   fc::create_directories( _data_dir/ "object_database.tmp" / "lock" );
   for( uint32_t space = 1; space <graphene::chain::reserved_spaces::RESERVED_SPACES_COUNT; ++space )
   {
      fc::create_directories( _data_dir / "object_database.tmp" / fc::to_string(space) );
      const auto types = _index[space].size();
      for( uint32_t type = 0; type  <  types; ++type )
         if( _index[space][type] )
            _index[space][type]->save( _data_dir / "object_database.tmp" / fc::to_string(space)/fc::to_string(type) );
   }
    //......
}

void object_database::open(const fc::path& data_dir)
{ 
    try {
        _data_dir = data_dir;
        //......
        
        for( uint32_t space = 1; space < graphene::chain::reserved_spaces::RESERVED_SPACES_COUNT; ++space )
            for( uint32_t type = 0; type  < _index[space].size(); ++type )
                if( _index[space][type] )
                    _index[space][type]->open( _data_dir / "object_database" / fc::to_string(space)/fc::to_string(type) );
    } FC_CAPTURE_AND_RETHROW( (data_dir) ) 
}
```  

**修改后：**  
``` c++  
void object_database::flush()
{
   fc::create_directories( _data_dir / "object_database.tmp" / "lock" );
   std::vector<fc::future<void>> tasks;
   tasks.reserve(200);
   for( uint32_t space = 0; space < _index.size(); ++space )
   {
      fc::create_directories( _data_dir / "object_database.tmp" / fc::to_string(space) );
      const auto types = _index[space].size();
      for( uint32_t type = 0; type  <  types; ++type )
         if( _index[space][type] )
            tasks.push_back( fc::do_parallel( [this,space,type] () {
               _index[space][type]->save( _data_dir / "object_database.tmp" / fc::to_string(space)/fc::to_string(type) );
            } ) );
   }
   for( auto& task : tasks )
      task.wait();
    //......
}

void object_database::open(const fc::path& data_dir)
{
    try {
        _data_dir = data_dir;
        // ...
        std::vector<fc::future<void>> tasks;
        tasks.reserve(200);
        for( uint32_t space = 0; space < _index.size(); ++space )
            for( uint32_t type = 0; type  < _index[space].size(); ++type )
                if( _index[space][type] )
                    tasks.push_back( fc::do_parallel( [this,space,type] () {
                        _index[space][type]->open( _data_dir / "object_database" / fc::to_string(space)/fc::to_string(type) );
                    } ) );
        for( auto& task : tasks )
            task.wait();
    } FC_CAPTURE_AND_RETHROW( (data_dir) ) 
}
```  

并行逻辑说明：  
不同的数据对象类型开辟新的线程处理，但有两点需要特殊指出：  
* io性能的瓶颈仍然取决于机器性能，推荐使用SSD；  
* 对于写操作：  
** 数据对象的写操作是累积一部分数据后，flush到磁盘，如果该部分数据中主要为某一类型的数据，性能优化效果不明显。  
* 对于读操作，存在和写操作同样的道理，木桶短板效应。  

--------------------

# 2. 功能测试：  
# 2.1 测试环境：  
``` text  
root@ck-chain-slave-prod-001:/data/bugfix_slow_open# pwd
/data/bugfix_slow_open
root@ck-chain-slave-prod-001:/data/bugfix_slow_open# ls
bugfix_open_slow   config.ini    mainnet  README.md      start.sh  testnet                witness_node.log
cli_wallet.tar.gz  genesis.json  main.py  start_init.sh  tar.sh    witness_node_data_dir  witness_node.tar.gz
root@ck-chain-slave-prod-001:/data/bugfix_slow_open# df -h
Filesystem      Size  Used Avail Use% Mounted on
udev            7.9G     0  7.9G   0% /dev
tmpfs           1.6G  4.0M  1.6G   1% /run
/dev/vda1        98G   86G  7.9G  92% /
tmpfs           7.9G   48K  7.9G   1% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           7.9G     0  7.9G   0% /sys/fs/cgroup
tmpfs           1.6G     0  1.6G   0% /run/user/1000
tmpfs           1.6G     0  1.6G   0% /run/user/1002
tmpfs           1.6G     0  1.6G   0% /run/user/0
overlay          98G   86G  7.9G  92% /var/lib/docker/overlay2/97efa517cc823d5bd2efc3ac6ea0e01a91d50bc01af96f82c2bad56c8302a14e/merged
/dev/vdb1        99G  1.7G   92G   2% /data
overlay          98G   86G  7.9G  92% /var/lib/docker/overlay2/337324ee8cae2215c935b2e1ac8490096b1147304f1df13448276829014a4a25/merged
root@ck-chain-slave-prod-001:/data/bugfix_slow_open#
root@ck-chain-slave-prod-001:/data/bugfix_slow_open# lsscsi
[0:0:1:0]    cd/dvd  QEMU     QEMU DVD-ROM     2.5+  /dev/sr0
root@ck-chain-slave-prod-001:/data/bugfix_slow_open#
```  

## 2.2 同步区块测试：  
### 2.2.1 节点服务进程：  
``` text  
root@ck-chain-slave-prod-001:/data/bugfix_slow_open# ps -ef | grep "bugfix"
root     30547     1 99 06:25 pts/0    00:05:02 ./bugfix_open_slow --genesis-json genesis.json -d witness_node_data_dir
root     31760  5695  0 06:29 pts/0    00:00:00 grep --color=auto bugfix
root@ck-chain-slave-prod-001:/data/bugfix_slow_open#
```  

### 2.2.2 节点同步log:  
``` text  
root@ck-chain-slave-prod-001:/data/bugfix_slow_open# tail -f witness_node.log
1763127ms th_a       application.cpp:538           handle_block         ] Got block: #5700000 time: 2020-04-11T19:27:00 latency: 9370943127 ms from: chainplay-bp  irreversible: 5699992 (-8), now: 2020-07-29T06:29:23
1768657ms th_a       application.cpp:538           handle_block         ] Got block: #5710000 time: 2020-04-12T01:33:44 latency: 9348944657 ms from: dongdongxixi2020  irreversible: 5709992 (-8), now: 2020-07-29T06:29:28
1775835ms th_a       application.cpp:538           handle_block         ] Got block: #5720000 time: 2020-04-12T07:40:08 latency: 9326967835 ms from: dongdongxixi2020  irreversible: 5719992 (-8), now: 2020-07-29T06:29:35
1782814ms th_a       application.cpp:538           handle_block         ] Got block: #5730000 time: 2020-04-12T13:46:36 latency: 9304986814 ms from: cpower  irreversible: 5729992 (-8), now: 2020-07-29T06:29:42
1788917ms th_a       application.cpp:538           handle_block         ] Got block: #5740000 time: 2020-04-12T19:53:02 latency: 9283006917 ms from: tokenplanet1  irreversible: 5739991 (-9), now: 2020-07-29T06:29:48
1794569ms th_a       application.cpp:538           handle_block         ] Got block: #5750000 time: 2020-04-13T01:59:16 latency: 9261038569 ms from: dongdongxixi2020  irreversible: 5749991 (-9), now: 2020-07-29T06:29:54
1801251ms th_a       application.cpp:538           handle_block         ] Got block: #5760000 time: 2020-04-13T08:05:38 latency: 9239063251 ms from: ladys-bp  irreversible: 5759989 (-11), now: 2020-07-29T06:30:01
1809694ms th_a       application.cpp:538           handle_block         ] Got block: #5770000 time: 2020-04-13T14:12:14 latency: 9217075694 ms from: unitedlabs.witness  irreversible: 5769988 (-12), now: 2020-07-29T06:30:09
1815826ms th_a       application.cpp:538           handle_block         ] Got block: #5780000 time: 2020-04-13T20:18:40 latency: 9195095826 ms from: bigcocos  irreversible: 5779990 (-10), now: 2020-07-29T06:30:15
1821878ms th_a       application.cpp:538           handle_block         ] Got block: #5790000 time: 2020-04-14T02:25:02 latency: 9173119878 ms from: ladys-bp  irreversible: 5789990 (-10), now: 2020-07-29T06:30:21
1828156ms th_a       application.cpp:538           handle_block         ] Got block: #5800000 time: 2020-04-14T08:31:34 latency: 9151134156 ms from: cpower  irreversible: 5799989 (-11), now: 2020-07-29T06:30:28

```  

### 2.2.3 top查看CPU使用情况：  
``` text  
top - 06:27:27 up 103 days, 20:33,  4 users,  load average: 1.42, 0.96, 0.64
Tasks: 170 total,   2 running, 168 sleeping,   0 stopped,   0 zombie
%Cpu0  : 97.3 us,  2.0 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.7 si,  0.0 st
%Cpu1  : 12.9 us,  2.7 sy,  0.0 ni, 84.0 id,  0.3 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu2  : 11.2 us,  3.4 sy,  0.0 ni, 84.7 id,  0.3 wa,  0.0 hi,  0.3 si,  0.0 st
%Cpu3  : 12.9 us,  2.0 sy,  0.0 ni, 85.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem : 16432236 total,  2448528 free,  3826980 used, 10156728 buff/cache
KiB Swap:        0 total,        0 free,        0 used. 12203460 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
30547 root      20   0 2091860 455252  21492 R 143.0  2.8   2:46.12 bugfix_open_slo
16087 dev       20   0 3424076 2.563g   8504 S   6.0 16.4   3011:13 python3
 6826 root      10 -10  147976  26708   7916 S   1.7  0.2 472:41.39 AliYunDun
 3601 dev       20   0  778688  38864   7488 S   0.7  0.2   1250:03 python3
28128 root      20   0 7773124 346476   9888 S   0.7  2.1 987:44.78 java
29482 root      20   0 1833356  32540  16472 S   0.7  0.2   0:04.25 witness_node
   13 root      20   0       0      0      0 S   0.3  0.0   2:26.77 ksoftirqd/1
  987 root      20   0 2223704  21840   6364 S   0.3  0.1 442:57.48 exe
29446 dev       20   0  781816  37976   7800 S   0.3  0.2 514:06.13 python3
30812 root      20   0  361080  12424   3900 S   0.3  0.1   0:00.20 barad_agent
    1 root      20   0  119780   5708   3756 S   0.0  0.0  16:17.29 systemd
    2 root      20   0       0      0      0 S   0.0  0.0   0:06.40 kthreadd
    3 root      20   0       0      0      0 S   0.0  0.0   2:29.19 ksoftirqd/0
    5 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 kworker/0:0H

```  

### 2.2.4 log分析  

## 2.3 节点重启  
### 2.3.1 log  

### 2.3.2 top cup资源占用  

### 2.3.3 log耗时分析  


--------------------


# 3. 数据兼容性测试  
## 3.1 新节点，空数据，同步到最新区块测试  

## 3.2 基于节点旧数据的同步测试  

