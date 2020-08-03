
# 简介 
单节点链搭建和cli_wallet初始脚本。

# 初始配置目录文件  
``` text  
    # tree .
    |-- cli_wallet.tar.gz
    |-- config.ini
    |-- genesis.json
    |-- main.py
    `-- witness_node.tar.gz
```  

# 依赖
``` shell
    pip install requests
```

# 示例  
## 链节点  
###  链节点初始化  
``` text  
    root@7ef1cba5083e:~/data/test/env/witness# python main.py init
    >> ['main.py', 'init']
    >>> pkill witness_node; sleep 2
    >>> rm -rf witness_node_data_dir *.log witness_node
    node clean done.
    >>> tar -zxvf witness_node.tar.gz; chmod +x witness_node
    witness_node
    >>> mkdir witness_node_data_dir; cp config.ini witness_node_data_dir/
    >>> nohup ./witness_node --genesis-json genesis.json -d witness_node_data_dir >> witness_node.log 2>&1 &
    >>> sleep 2; grep -n "Chain ID is" witness_node.log >> chain_id.log
    chain id: c1ac4bb7bd7d94874a1cb98b39a8a582421d03d022dfa4be8c70567076e03ad0

    root@7ef1cba5083e:~/data/test/env/witness# ps -ef | grep "witness_node"
    root      5414     0  0 06:20 pts/1    00:00:00 ./witness_node --genesis-json genesis.json -d witness_node_data_dir
    root      5475   266  0 06:20 pts/1    00:00:00 grep --color=auto witness_node
    root@7ef1cba5083e:~/data/test/env/witness# 
```  

### 链节点重启
```text  
    root@7ef1cba5083e:~/data/test/env/witness# python main.py 
    >> ['main.py']
    >>> pkill witness_node; sleep 2
    >>> nohup ./witness_node --genesis-json genesis.json -d witness_node_data_dir >> witness_node.log 2>&1 &
    chain id: c1ac4bb7bd7d94874a1cb98b39a8a582421d03d022dfa4be8c70567076e03ad0
    root@7ef1cba5083e:~/data/test/env/witness#
```  

### 链清理
``` text  
    root@7ef1cba5083e:~/data/test/env/witness# python main.py clean
    >> ['main.py', 'clean']
    >>> pkill witness_node; sleep 2
    >>> rm -rf witness_node_data_dir *.log witness_node
    node clean done.
    root@7ef1cba5083e:~/data/test/env/witness#
```  

## 钱包(wallet)  
### 钱包初始化  
 包括：cli_wallet启动，set_password, unlock, import_key, import_balances

``` text
    root@7ef1cba5083e:~/data/test/env/witness# python main.py wallet init
    >> ['main.py', 'wallet', 'init']
    >>> pkill cli_wallet; sleep 2; rm -rf wallet; mkdir wallet; cp cli_wallet.tar.gz wallet/; cd wallet; tar -zxvf cli_wallet.tar.gz; chmod +x cli_wallet
    cli_wallet
    chain id: c1ac4bb7bd7d94874a1cb98b39a8a582421d03d022dfa4be8c70567076e03ad0
    >>> cd wallet; pkill cli_wallet; nohup ./cli_wallet --chain-id c1ac4bb7bd7d94874a1cb98b39a8a582421d03d022dfa4be8c70567076e03ad0 -s ws://127.0.0.1:8049 -r 0.0.0.0:8048 -d >> cli_wallet.log  2>&1 &
    cli_wallet_url: http://127.0.0.1:8048
    >> set_password [123456]
    None
    >> unlock [123456]
    None
    >> import_key ['nicotest', '5J2SChqa9QxrCkdMor9VC2k9NT4R4ctRrJA6odQCPkb3yL89vxo']
    True
    >> import_balance ['nicotest', ['5KAUeN3Yv51FzpLGGf4S1ByKpMqVFNzXTJK7euqc3NnaaLz1GJm'], 'true']
    [{u'ref_block_prefix': 0, u'operations': [[29, {u'deposit_to_account': u'1.2.16', u'total_claimed': {u'asset_id': u'1.3.0', u'amount': u'9780000000000000'}, u'balance_to_claim': u'1.15.0', u'balance_owner_key': u'COCOS7yE9skpBAirth3eSNMRtwq1jYswEE3uSbbuAtXTz88HtbpQsZf'}]], u'signatures': [u'205ceaedb53cbb84a6ae6edb0e5e3884ab058aa0ffc77fead3e2b9d7729e0ed04d6e0465cb1fe14c8597d45bc9260fead9b4e599fb9dbdf64422e32e331b4f3a58', u'2060ca4849e8591965c9b3385147e6b0642caf8a4b9a69e37a2167b109bb95305d7c33f9cb9a323efaf91b2f61620d8ef1563b832b2db89bb2631d549b8a13e6e6'], u'ref_block_num': 0, u'extensions': [], u'expiration': u'2019-11-26T06:48:20'}]
    >> list_account_balances ['nicotest']
    [{u'asset_id': u'1.3.0', u'amount': u'9780000000000000'}]
    root@7ef1cba5083e:~/data/test/env/witness# ps -ef | grep "wallet"
    root      5691     0  0 06:27 pts/1    00:00:00 ./cli_wallet --chain-id c1ac4bb7bd7d94874a1cb98b39a8a582421d03d022dfa4be8c70567076e03ad0 -s ws://127.0.0.1:8049 -r 0.0.0.0:8048 -d
    root      5723   266  0 06:28 pts/1    00:00:00 grep --color=auto wallet
    root@7ef1cba5083e:~/data/test/env/witness# 
```

### 钱包重启  
 包括：cli_wallet启动， unlock
``` text
    root@7ef1cba5083e:~/data/test/env/witness# python main.py wallet     
    >> ['main.py', 'wallet']
    chain id: c1ac4bb7bd7d94874a1cb98b39a8a582421d03d022dfa4be8c70567076e03ad0
    >>> cd wallet; pkill cli_wallet; nohup ./cli_wallet --chain-id c1ac4bb7bd7d94874a1cb98b39a8a582421d03d022dfa4be8c70567076e03ad0 -s ws://127.0.0.1:8049 -r 0.0.0.0:8048 -d >> cli_wallet.log  2>&1 &
    >> unlock [123456]
    None
    root@7ef1cba5083e:~/data/test/env/witness# 
```

### 钱包api测试  
``` text  
    root@7ef1cba5083e:~/data/test/env/witness# python main.py wallet test
    >> ['main.py', 'wallet', 'test']
    {u'statistics': u'2.6.16', u'name': u'nicotest', u'options': {u'memo_key': u'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', u'extensions': [], u'votes': []}, u'active': {u'weight_threshold': 1, u'account_auths': [], u'key_auths': [[u'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]], u'address_auths': []}, u'registrar': u'1.2.4', u'asset_locked': {u'contract_lock_details': [], u'locked_total': []}, u'owner': {u'weight_threshold': 1, u'account_auths': [], u'key_auths': [[u'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]], u'address_auths': []}, u'membership_expiration_date': u'1970-01-01T00:00:00', u'id': u'1.2.16'}
    >> list_account_balances ['nicotest']
    [{u'asset_id': u'1.3.0', u'amount': u'9780000000000000'}]
    root@7ef1cba5083e:~/data/test/env/witness# 
```

### 钱包清理  
``` text  
    root@7ef1cba5083e:~/data/test/env/witness# python main.py wallet clean
    >> ['main.py', 'wallet', 'clean']
    >>> pkill cli_wallet; sleep 2
    >>> rm -rf wallet 
    wallet clean done.
    root@7ef1cba5083e:~/data/test/env/witness#
```  

### 其他  
**import_key**  
``` text  
import_key init0 5Kj5s6xAkjbFcsGXhP4ioWUk7dZm5aYyKDEWDbWAa5nwA8Paewc
import_key init1 5K5fqjvMrH5UtUisCgSZHQjiQf9BvtZ5vsKPhCErDy7P2gnLQmw
import_key init2 5Jdq6Fn8u2m1RUqHLEb5bjqvVvbg6oVDGmwz6Z16Q9KfPuzfDzt
import_key init3 5JCb6e445N1iLsNqF7w5URJ1sgEZgChzGQKKy2zrCVTHA4SRyiQ
import_key init4 5JAxJ8dH7mR81u3D3cTpXxTjbv12F9VF4Z4CWgUmvk52D2twxqt
import_key init5 5KVEqMvCQf5CP4Stkd9CW479uwQnDbhCiFxbdRLXgkxS3RchZ6X
import_key init6 5Jdvatdk3qpZ8Ek9tQyqh3QwQ5mWNZ7kfnwSVwMUsLLmdUAfUwo
import_key init7 5JWkfkjwaMZDVPtpcLrFW5PNCXfMxxEH3f4HugbcAdJ8o6DrDnD
import_key init8 5JWX8nDv8WwgdAb4xnXHxaoXRDVvfEtVmCcnKvfnjcoQy4D6h5v
import_key init9 5JBYS1qMJfjR9orv2Z74w5D7w1vUBzjgme85qSkBc71urkLHLyV
import_key init10 5HrCGXRsxFFccSyQSuqzmvL98o2RrbgxEDUzxjjS6Uvb1kkAkjS
```  

### 链环境  
#### 测试网  
``` text  
./cli_wallet --chain-id 1ae3653a3105800f5722c5bda2b55530d0e9e8654314e2f3dc6d2b010da641c5 -s wss://test.cocosbcx.net  -r 0.0.0.0:8037

```  

#### 主网  
``` text  
./cli_wallet --chain-id 6057d856c398875cac2650fe33caef3d5f6b403d184c5154abbff526ec1143c4 -s wss://api.cocosbcx.net  -r 0.0.0.0:8036

``` 
 

