
sysbench test result  
------------------------------------

# 1. dev virtual machine 测试  
``` text  
dev@ubuntu:~/data/mrepo/CocosBCX/feature_test/machine_performance$ python3 main.py
----------------------------------------------------------------
------------------- sysbench cpu ------------------------
>>> cat /proc/cpuinfo| grep "cpu cores"| uniq
>>> sysbench --num-threads=1 --max-requests=20000 --test=cpu --cpu-max-prime=50000 run
>>> sysbench --num-threads=2 --max-requests=20000 --test=cpu --cpu-max-prime=50000 run
>>> sysbench --num-threads=4 --max-requests=20000 --test=cpu --cpu-max-prime=50000 run
['线程数', '最大请求数', '计算最大素数', '时间', '最小', '最大', '平均']
['1', 20000, 50000, '149.3717s', '6.73ms', '15.00ms', '7.47ms']
['2', 20000, 50000, '81.9942s', '6.94ms', '41.18ms', '8.20ms']
['4', 20000, 50000, '51.7005s', '8.89ms', '57.32ms', '10.34ms']
------------------- sysbench io -------------------------
>>> cat /proc/cpuinfo| grep "cpu cores"| uniq
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqwr prepare
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqwr run
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqwr cleanup
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqwr prepare
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqwr run
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqwr cleanup
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqwr prepare
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqwr run
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqwr cleanup
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqrewr prepare
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqrewr run
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqrewr cleanup
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqrewr prepare
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqrewr run
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqrewr cleanup
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqrewr prepare
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqrewr run
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqrewr cleanup
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqrd prepare
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqrd run
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqrd cleanup
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqrd prepare
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqrd run
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqrd cleanup
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqrd prepare
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqrd run
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqrd cleanup
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndrd prepare
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndrd run
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndrd cleanup
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndrd prepare
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndrd run
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndrd cleanup
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndrd prepare
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndrd run
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndrd cleanup
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndwr prepare
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndwr run
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndwr cleanup
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndwr prepare
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndwr run
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndwr cleanup
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndwr prepare
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndwr run
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndwr cleanup
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndrw prepare
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndrw run
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndrw cleanup
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndrw prepare
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndrw run
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndrw cleanup
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndrw prepare
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndrw run
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndrw cleanup
['线程数', '测试模式', '文件大小', '传输速度', '总执行时间', '最小', '最大', '平均']
['1', 'seqwr', '3G', '47.731Mb/sec', '64.3613s', '0.01ms', '1136.00ms', '0.22ms']
['2', 'seqwr', '3G', '46.661Mb/sec', '65.8368s', '0.01ms', '196.30ms', '0.35ms']
['4', 'seqwr', '3G', '61.491Mb/sec', '49.9586s', '0.01ms', '713.17ms', '0.54ms']
['1', 'seqrewr', '3G', '47.346Mb/sec', '64.8842s', '0.00ms', '573.71ms', '0.18ms']
['2', 'seqrewr', '3G', '55.313Mb/sec', '55.5386s', '0.00ms', '875.79ms', '0.32ms']
['4', 'seqrewr', '3G', '47.587Mb/sec', '64.5552s', '0.00ms', '951.31ms', '0.79ms']
['1', 'seqrd', '3G', '4.3183Gb/sec', '0.6947s', '0.00ms', '1.34ms', '0.00ms']
['2', 'seqrd', '3G', '5.918Gb/sec', '0.5069s', '0.00ms', '0.34ms', '0.00ms']
['4', 'seqrd', '3G', '7.5313Gb/sec', '0.3983s', '0.00ms', '1.56ms', '0.01ms']
['1', 'rndrd', '3G', '2.9509Gb/sec', '0.0517s', '0.00ms', '0.26ms', '0.00ms']
['2', 'rndrd', '3G', '4.4864Gb/sec', '0.0340s', '0.00ms', '0.19ms', '0.01ms']
['4', 'rndrd', '3G', '7.0748Gb/sec', '0.0220s', '0.00ms', '0.70ms', '0.01ms']
['1', 'rndwr', '3G', '17.303Mb/sec', '9.0302s', '0.00ms', '0.55ms', '0.01ms']
['2', 'rndwr', '3G', '60.608Mb/sec', '2.5796s', '0.01ms', '1.12ms', '0.01ms']
['4', 'rndwr', '3G', '63.003Mb/sec', '2.4947s', '0.01ms', '1.22ms', '0.02ms']
['1', 'rndrw', '3G', '72.954Mb/sec', '2.1417s', '0.00ms', '0.33ms', '0.01ms']
['2', 'rndrw', '3G', '63.987Mb/sec', '2.4441s', '0.00ms', '0.47ms', '0.01ms']
['4', 'rndrw', '3G', '95.335Mb/sec', '1.6462s', '0.00ms', '2.80ms', '0.02ms']
------------------- sysbench memory -------------------------
>>> sysbench --test=memory --memory-total-size=200G --memory-oper=read run
>>> sysbench --test=memory --memory-total-size=200G --memory-oper=write run
['线程数', '测试模式', '总测试数据', '传输性能', '传输速度', '总执行时间', '最小', '最大', '平均']
['1', 'read', '200G', '4446223.22 ops/sec', '4342.01 MB/sec', '47.1670s', '0.00ms', '0.98ms', '0.00ms']
['1', 'write', '200G', '3029082.57 ops/sec', '2958.09 MB/sec', '69.2339s', '0.00ms', '10.32ms', '0.00ms']

```  

# 2. ck-chain-slave-prod-001 测试  
``` text  
root@ck-chain-slave-prod-001:/data/test# python3 main.py
----------------------------------------------------------------
------------------- sysbench cpu ------------------------
>>> cat /proc/cpuinfo| grep "cpu cores"| uniq
>>> sysbench --num-threads=1 --max-requests=20000 --test=cpu --cpu-max-prime=50000 run
>>> sysbench --num-threads=2 --max-requests=20000 --test=cpu --cpu-max-prime=50000 run
>>> sysbench --num-threads=4 --max-requests=20000 --test=cpu --cpu-max-prime=50000 run
['线程数', '最大请求数', '计算最大素数', '时间', '最小', '最大', '平均']
['1', 20000, 50000, '150.2375s', '7.43ms', '39.18ms', '7.51ms']
['2', 20000, 50000, '75.6026s', '7.43ms', '31.57ms', '7.56ms']
['4', 20000, 50000, '49.9942s', '7.44ms', '63.41ms', '10.00ms']
------------------- sysbench io -------------------------
>>> cat /proc/cpuinfo| grep "cpu cores"| uniq
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqwr prepare
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqwr run
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqwr cleanup
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqwr prepare
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqwr run
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqwr cleanup
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqwr prepare
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqwr run
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqwr cleanup
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqrewr prepare
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqrewr run
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqrewr cleanup
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqrewr prepare
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqrewr run
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqrewr cleanup
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqrewr prepare
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqrewr run
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqrewr cleanup
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqrd prepare
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqrd run
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqrd cleanup
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqrd prepare
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqrd run
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqrd cleanup
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqrd prepare
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqrd run
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqrd cleanup
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndrd prepare
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndrd run
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndrd cleanup
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndrd prepare
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndrd run
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndrd cleanup
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndrd prepare
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndrd run
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndrd cleanup
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndwr prepare
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndwr run
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndwr cleanup
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndwr prepare
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndwr run
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndwr cleanup
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndwr prepare
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndwr run
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndwr cleanup
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndrw prepare
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndrw run
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndrw cleanup
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndrw prepare
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndrw run
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndrw cleanup
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndrw prepare
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndrw run
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndrw cleanup
['线程数', '测试模式', '文件大小', '传输速度', '总执行时间', '最小', '最大', '平均']
['1', 'seqwr', '3G', '133.59Mb/sec', '22.9957s', '0.01ms', '18.00ms', '0.05ms']
['2', 'seqwr', '3G', '134.13Mb/sec', '22.9026s', '0.01ms', '214.69ms', '0.08ms']
['4', 'seqwr', '3G', '133.06Mb/sec', '23.0869s', '0.01ms', '652.60ms', '0.16ms']
['1', 'seqrewr', '3G', '138.38Mb/sec', '22.1992s', '0.00ms', '497.63ms', '0.05ms']
['2', 'seqrewr', '3G', '138.39Mb/sec', '22.1983s', '0.00ms', '616.88ms', '0.08ms']
['4', 'seqrewr', '3G', '138.43Mb/sec', '22.1910s', '0.00ms', '151.34ms', '0.15ms']
['1', 'seqrd', '3G', '3.9288Gb/sec', '0.7636s', '0.00ms', '0.07ms', '0.00ms']
['2', 'seqrd', '3G', '6.6101Gb/sec', '0.4539s', '0.00ms', '0.79ms', '0.00ms']
['4', 'seqrd', '3G', '8.5594Gb/sec', '0.3505s', '0.00ms', '13.66ms', '0.01ms']
['1', 'rndrd', '3G', '2.9915Gb/sec', '0.0510s', '0.00ms', '0.07ms', '0.00ms']
['2', 'rndrd', '3G', '4.1664Gb/sec', '0.0368s', '0.00ms', '0.08ms', '0.01ms']
['4', 'rndrd', '3G', '4.9708Gb/sec', '0.0309s', '0.00ms', '7.85ms', '0.01ms']
['1', 'rndwr', '3G', '17.465Mb/sec', '8.9463s', '0.01ms', '0.35ms', '0.01ms']
['2', 'rndwr', '3G', '33.521Mb/sec', '4.6677s', '0.01ms', '1.37ms', '0.01ms']
['4', 'rndwr', '3G', '59.746Mb/sec', '2.6278s', '0.01ms', '1.45ms', '0.02ms']
['1', 'rndrw', '3G', '31.175Mb/sec', '5.0120s', '0.00ms', '0.16ms', '0.01ms']
['2', 'rndrw', '3G', '54.605Mb/sec', '2.8674s', '0.00ms', '1.91ms', '0.01ms']
['4', 'rndrw', '3G', '82.522Mb/sec', '1.9084s', '0.00ms', '1.14ms', '0.01ms']
------------------- sysbench memory -------------------------
>>> sysbench --test=memory --memory-total-size=200G --memory-oper=read run
>>> sysbench --test=memory --memory-total-size=200G --memory-oper=write run
['线程数', '测试模式', '总测试数据', '传输性能', '传输速度', '总执行时间', '最小', '最大', '平均']
['1', 'read', '200G', '2696856.01 ops/sec', '2633.65 MB/sec', '77.7628s', '0.00ms', '2.08ms', '0.00ms']
['1', 'write', '200G', '2020774.02 ops/sec', '1973.41 MB/sec', '103.7796s', '0.00ms', '2.03ms', '0.00ms']

``` 

# 3. ck ubuntu 测试
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/machine_performance$ python3 main.py 
----------------------------------------------------------------
------------------- sysbench cpu ------------------------
>>> cat /proc/cpuinfo| grep "cpu cores"| uniq
>>> sysbench --num-threads=1 --max-requests=20000 --test=cpu --cpu-max-prime=50000 run
>>> sysbench --num-threads=2 --max-requests=20000 --test=cpu --cpu-max-prime=50000 run
>>> sysbench --num-threads=4 --max-requests=20000 --test=cpu --cpu-max-prime=50000 run
['线程数', '最大请求数', '计算最大素数', '时间', '最小', '最大', '平均']
['1', 20000, 50000, '252.9125s', '10.37ms', '96.17ms', '12.65ms']
['2', 20000, 50000, '112.5096s', '10.62ms', '56.78ms', '11.25ms']
['4', 20000, 50000, '56.6034s', '10.81ms', '98.30ms', '11.32ms']
------------------- sysbench io -------------------------
>>> cat /proc/cpuinfo| grep "cpu cores"| uniq
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqwr prepare
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqwr run
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqwr cleanup
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqwr prepare
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqwr run
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqwr cleanup
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqwr prepare
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqwr run
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqwr cleanup
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqrewr prepare
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqrewr run
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqrewr cleanup
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqrewr prepare
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqrewr run
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqrewr cleanup
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqrewr prepare
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqrewr run
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqrewr cleanup
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqrd prepare
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqrd run
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=seqrd cleanup
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqrd prepare
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqrd run
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=seqrd cleanup
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqrd prepare
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqrd run
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=seqrd cleanup
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndrd prepare
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndrd run
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndrd cleanup
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndrd prepare
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndrd run
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndrd cleanup
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndrd prepare
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndrd run
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndrd cleanup
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndwr prepare
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndwr run
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndwr cleanup
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndwr prepare
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndwr run

>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndwr cleanup
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndwr prepare
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndwr run
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndwr cleanup
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndrw prepare
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndrw run
>>> sysbench --num-threads=1 --test=fileio --file-total-size=3G --file-test-mode=rndrw cleanup
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndrw prepare
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndrw run
>>> sysbench --num-threads=2 --test=fileio --file-total-size=3G --file-test-mode=rndrw cleanup
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndrw prepare
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndrw run
>>> sysbench --num-threads=4 --test=fileio --file-total-size=3G --file-test-mode=rndrw cleanup
['线程数', '测试模式', '文件大小', '传输速度', '总执行时间', '最小', '最大', '平均']
['1', 'seqwr', '3G', '99.722Mb/sec', '30.8056s', '0.05ms', '198.54ms', '0.07ms']
['2', 'seqwr', '3G', '106.52Mb/sec', '28.8402s', '0.05ms', '176.35ms', '0.13ms']
['4', 'seqwr', '3G', '102.93Mb/sec', '29.8463s', '0.05ms', '109.10ms', '0.25ms']
['1', 'seqrewr', '3G', '113.91Mb/sec', '26.9688s', '0.04ms', '899.03ms', '0.07ms']
['2', 'seqrewr', '3G', '115.41Mb/sec', '26.6170s', '0.04ms', '172.25ms', '0.11ms']
['4', 'seqrewr', '3G', '107.85Mb/sec', '28.4827s', '0.05ms', '1328.23ms', '0.24ms']
['1', 'seqrd', '3G', '4.869Gb/sec', '0.6161s', '0.00ms', '0.05ms', '0.00ms']
['2', 'seqrd', '3G', '6.7201Gb/sec', '0.4464s', '0.00ms', '0.04ms', '0.00ms']
['4', 'seqrd', '3G', '10.817Gb/sec', '0.2773s', '0.00ms', '0.05ms', '0.01ms']
['1', 'rndrd', '3G', '3.9029Gb/sec', '0.0391s', '0.00ms', '0.04ms', '0.00ms']
['2', 'rndrd', '3G', '6.1195Gb/sec', '0.0249s', '0.00ms', '0.06ms', '0.00ms']
['4', 'rndrd', '3G', '9.0658Gb/sec', '0.0172s', '0.00ms', '0.12ms', '0.01ms']
['1', 'rndwr', '3G', '2.0306Mb/sec', '76.9480s', '0.04ms', '9.98ms', '0.05ms']
['2', 'rndwr', '3G', '3.0167Mb/sec', '51.7946s', '0.05ms', '11.07ms', '0.07ms']
['4', 'rndwr', '3G', '3.7083Mb/sec', '42.1651s', '0.05ms', '28.39ms', '0.12ms']
['1', 'rndrw', '3G', '4.5099Mb/sec', '34.6463s', '0.00ms', '0.12ms', '0.02ms']
['2', 'rndrw', '3G', '6.5751Mb/sec', '23.7638s', '0.00ms', '8.89ms', '0.03ms']
['4', 'rndrw', '3G', '6.7792Mb/sec', '23.0529s', '0.00ms', '250.31ms', '0.08ms']
------------------- sysbench memory -------------------------
>>> sysbench --test=memory --memory-total-size=200G --memory-oper=read run
>>> sysbench --test=memory --memory-total-size=200G --memory-oper=write run
['线程数', '测试模式', '总测试数据', '传输性能', '传输速度', '总执行时间', '最小', '最大', '平均']
['1', 'read', '200G', '4147751.54 ops/sec', '4050.54 MB/sec', '50.5612s', '0.00ms', '13.60ms', '0.00ms']
['1', 'write', '200G', '2958079.82 ops/sec', '2888.75 MB/sec', '70.8957s', '0.00ms', '6.78ms', '0.00ms']

```  



