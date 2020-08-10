
# 简介 
bitshares单节点链搭建和cli_wallet初始脚本。

# 初始配置目录文件  
``` text  
dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$ tree
.
├── cli_wallet.tar.gz
├── config.ini
├── genesis-dev.json
├── genesis.json
├── main.py
├── README.md
├── tar.sh
└── witness_node.tar.gz

0 directories, 8 files
dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$
```  

# 依赖
> python3  

# 示例  
## 链节点  
###  链节点初始化  
``` text  
dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$ python3 main.py init
>> ['main.py', 'init']
>>> pkill witness_node; sleep 2
>>> rm -rf witness_node_data_dir *.log witness_node
node clean done.
>>> tar -zxvf witness_node.tar.gz; chmod +x witness_node
witness_node
>>> mkdir witness_node_data_dir; cp config.ini witness_node_data_dir/
>>> nohup ./witness_node --genesis-json genesis.json -d witness_node_data_dir >> witness_node.log 2>&1 &
>>> sleep 2; grep -n "Chain ID is" witness_node.log >> chain_id.log
chain id: 28e71bdb98ef0e00ea92021e769d49f2e4759f36af4cacb5f0c4b4c6004013a4

dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$ tail -f witness_node.log
1173190ms th_a       application.cpp:1172          startup_plugins      ] Plugin witness started
1173190ms th_a       main.cpp:187                  main                 ] Started BitShares node on a chain with 0 blocks.
1173190ms th_a       main.cpp:188                  main                 ] Chain ID is 28e71bdb98ef0e00ea92021e769d49f2e4759f36af4cacb5f0c4b4c6004013a4
1174000ms th_a       db_maint.cpp:856              update_call_orders_h ] Updating all call orders for hardfork core-343 at block 1
1174000ms th_a       db_maint.cpp:874              update_call_orders_h ] Done updating all call orders for hardfork core-343 at block 1
1174000ms th_a       db_maint.cpp:895              match_call_orders    ] Matching call orders at block 1
1174000ms th_a       db_maint.cpp:905              match_call_orders    ] Done matching call orders at block 1
1174000ms th_a       db_maint.cpp:895              match_call_orders    ] Matching call orders at block 1
1174000ms th_a       db_maint.cpp:905              match_call_orders    ] Done matching call orders at block 1
1174000ms th_a       witness.cpp:277               block_production_loo ] Generated block #1 with 0 transaction(s) and timestamp 2020-08-10T09:19:34 at time 2020-08-10T09:19:34
1185001ms th_a       witness.cpp:277               block_production_loo ] Generated block #2 with 0 transaction(s) and timestamp 2020-08-10T09:19:45 at time 2020-08-10T09:19:45
1188000ms th_a       witness.cpp:277               block_production_loo ] Generated block #3 with 0 transaction(s) and timestamp 2020-08-10T09:19:48 at time 2020-08-10T09:19:48

```  

### 链节点重启
```text  
dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$ python3 main.py
>> ['main.py']
>>> pkill witness_node; sleep 2
>>> nohup ./witness_node --genesis-json genesis.json -d witness_node_data_dir >> witness_node.log 2>&1 &
chain id: 28e71bdb98ef0e00ea92021e769d49f2e4759f36af4cacb5f0c4b4c6004013a4
dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$ 
```  

### 链清理
``` text  
dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$ python3 main.py clean
>> ['main.py', 'clean']
>>> pkill witness_node; sleep 2
>>> rm -rf witness_node_data_dir *.log witness_node
node clean done.
dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$ ls
cli_wallet  cli_wallet.tar.gz  config.ini  genesis-dev.json  genesis.json  main.py  README.md  tar.sh  witness_node.tar.gz
dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$
```  

## 钱包(wallet)  
### 钱包初始化  
 包括：cli_wallet启动，set_password, unlock, import_key, import_balances

``` text
dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$ python3 main.py wallet init
>> ['main.py', 'wallet', 'init']
>>> pkill cli_wallet; sleep 2; rm -rf wallet; mkdir wallet; cp cli_wallet.tar.gz wallet/; cd wallet; tar -zxvf cli_wallet.tar.gz; chmod +x cli_wallet
cli_wallet
chain id: 28e71bdb98ef0e00ea92021e769d49f2e4759f36af4cacb5f0c4b4c6004013a4
>>> cd wallet; pkill cli_wallet; nohup ./cli_wallet --chain-id 28e71bdb98ef0e00ea92021e769d49f2e4759f36af4cacb5f0c4b4c6004013a4 -s ws://127.0.0.1:8049 -r 0.0.0.0:8048 -d >> cli_wallet.log  2>&1 &
cli_wallet_url: http://127.0.0.1:8048
>> set_password [123456]
{'id': 1, 'jsonrpc': '2.0', 'result': None}

>> unlock [123456]
{'id': 1, 'jsonrpc': '2.0', 'result': None}

>> import_key ['nathan', '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3']
{'id': 1, 'jsonrpc': '2.0', 'result': True}

>> import_key ['init0', '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3']
{'id': 1, 'jsonrpc': '2.0', 'result': True}

>> import_key ['init1', '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3']
{'id': 1, 'jsonrpc': '2.0', 'result': True}

>> import_key ['init2', '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3']
{'id': 1, 'jsonrpc': '2.0', 'result': True}

>> import_key ['init3', '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3']
{'id': 1, 'jsonrpc': '2.0', 'result': True}

>> import_key ['init4', '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3']
{'id': 1, 'jsonrpc': '2.0', 'result': True}

>> import_key ['init5', '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3']
{'id': 1, 'jsonrpc': '2.0', 'result': True}

>> import_key ['init6', '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3']
{'id': 1, 'jsonrpc': '2.0', 'result': True}

>> import_key ['init7', '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3']
{'id': 1, 'jsonrpc': '2.0', 'result': True}

>> import_key ['init8', '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3']
{'id': 1, 'jsonrpc': '2.0', 'result': True}

>> import_key ['init9', '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3']
{'id': 1, 'jsonrpc': '2.0', 'result': True}

>> import_key ['init10', '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3']
{'id': 1, 'jsonrpc': '2.0', 'result': True}

>> import_balance ['nathan', ['5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3'], 'true']
{'id': 1, 'jsonrpc': '2.0', 'result': [{'ref_block_num': 10, 'ref_block_prefix': 1336392115, 'expiration': '2020-08-10T09:42:57', 'operations': [[37, {'fee': {'amount': 0, 'asset_id': '1.3.0'}, 'deposit_to_account': '1.2.17', 'balance_to_claim': '1.15.0', 'balance_owner_key': 'BTS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV', 'total_claimed': {'amount': '1000000000000000', 'asset_id': '1.3.0'}}]], 'extensions': [], 'signatures': ['204e97847a5dd10fb1171771568a3f1d920c648a6dad1abcc1e5b4638a82cd8e28204f0466b62de97ab7c14b2f3e91a71939142794263f4b1f55acd91627e6a12f']}]}

>> list_account_balances ['nathan']
{'id': 1, 'jsonrpc': '2.0', 'result': [{'amount': '1000000000000000', 'asset_id': '1.3.0'}]}

>>> echo ./cli_wallet --chain-id 28e71bdb98ef0e00ea92021e769d49f2e4759f36af4cacb5f0c4b4c6004013a4 -s ws://127.0.0.1:8049 -r 0.0.0.0:8047  >> ./wallet/start.sh && chmod +x ./wallet/start.sh
dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$ ls
chain_id.log  cli_wallet.tar.gz  genesis-dev.json  main.py    tar.sh  witness_node           witness_node.log
cli_wallet    config.ini         genesis.json      README.md  wallet  witness_node_data_dir  witness_node.tar.gz
dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$
```

### 钱包重启  
 包括：cli_wallet启动， unlock
``` text
dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$ python3 main.py wallet
>> ['main.py', 'wallet']
chain id: 28e71bdb98ef0e00ea92021e769d49f2e4759f36af4cacb5f0c4b4c6004013a4
>>> cd wallet; pkill cli_wallet; nohup ./cli_wallet --chain-id 28e71bdb98ef0e00ea92021e769d49f2e4759f36af4cacb5f0c4b4c6004013a4 -s ws://127.0.0.1:8049 -r 0.0.0.0:8048 -d >> cli_wallet.log  2>&1 &
>> unlock [123456]
{'id': 1, 'jsonrpc': '2.0', 'result': None}

dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$ ps -ef | grep "cli_wallet"
dev       25534   6195  0 02:45 pts/0    00:00:00 ./cli_wallet --chain-id 28e71bdb98ef0e00ea92021e769d49f2e4759f36af4cacb5f0c4b4c6004013a4 -s ws://127.0.0.1:8049 -r 0.0.0.0:8048 -d
dev       25545   8946  0 02:46 pts/0    00:00:00 grep --color=auto cli_wallet
dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$
```

### 钱包api测试  
``` text  
dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$ python3 main.py wallet test
>> ['main.py', 'wallet', 'test']
{'id': '1.2.17', 'membership_expiration_date': '1970-01-01T00:00:00', 'registrar': '1.2.4', 'referrer': '1.2.0', 'lifetime_referrer': '1.2.0', 'network_fee_percentage': 2000, 'lifetime_referrer_fee_percentage': 3000, 'referrer_rewards_percentage': 0, 'name': 'nathan', 'owner': {'weight_threshold': 1, 'account_auths': [], 'key_auths': [['BTS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV', 1]], 'address_auths': []}, 'active': {'weight_threshold': 1, 'account_auths': [], 'key_auths': [['BTS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV', 1]], 'address_auths': []}, 'options': {'memo_key': 'BTS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV', 'voting_account': '1.2.5', 'num_witness': 0, 'num_committee': 0, 'votes': [], 'extensions': []}, 'num_committee_voted': 0, 'statistics': '2.6.17', 'whitelisting_accounts': [], 'blacklisting_accounts': [], 'whitelisted_accounts': [], 'blacklisted_accounts': [], 'owner_special_authority': [0, {}], 'active_special_authority': [0, {}], 'top_n_control_flags': 0}
>> list_account_balances ['nathan']
{'id': 1, 'jsonrpc': '2.0', 'result': [{'amount': '1000000000000000', 'asset_id': '1.3.0'}]}

dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$
```

### 钱包清理  
``` text  
dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$ python3 main.py wallet clean
>> ['main.py', 'wallet', 'clean']
>>> pkill cli_wallet; sleep 2
>>> rm -rf wallet
wallet clean done.
dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$
dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$ ls
chain_id.log  cli_wallet.tar.gz  genesis-dev.json  main.py    tar.sh        witness_node_data_dir  witness_node.tar.gz
cli_wallet    config.ini         genesis.json      README.md  witness_node  witness_node.log
dev@ubuntu:~/data/repo/CocosBCX/chain_init/bitshares$ 
```  

### 其他  
**import_key**  
``` text  
    ["init0", "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"],
    ["init1", "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"],
    ["init2", "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"],
    ["init3", "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"],
    ["init4", "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"],
    ["init5", "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"],
    ["init6", "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"],
    ["init7", "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"],
    ["init8", "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"],
    ["init9", "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"],
    ["init10","5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"]
```   

``` text  
private-key = ["BTS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV","5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"]  
```  

**init balance:**  
``` text  
import_balance nathan ["5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"] true  
```  

**nathan account keys:**    
``` text  
unlocked >>> suggest_brain_key 
{
  "brain_priv_key": "RASTLE AMPLIFY DOUCELY CENTENA CODICIL PITWOOD LULLER BEPAT LALANG MUFFET EMBAR BAS DOVER JINA CASING GRANARY",
  "wif_priv_key": "5JZnD1HbgKSVrCacVNDCFjjnmqzajQ51doEjabs1m3rvs3GaVcJ",
  "pub_key": "BTS8hBsNjWFunqSDNhrKneG6xUvN5vEmc3MZdGXTHC5VGhnFTzjfa"
}
unlocked >>> 
```  


