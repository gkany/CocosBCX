# 1.测试准备  
> 基于测试网数据  

fn节点同步测试网数据到最新后，停止该节点，修改该节点的config.ini配置：  
* 添加见证人和对应的区块签名秘钥对  
* 移除现有测试网的p2p节点配置  
使其成为独立的bp节点  

**硬分叉时间：**
``` text
head_block_time: 2020-07-09T05:43:22, hard_fork time: 2020-07-09T12:00:00
```

# 2. 硬分叉之前旧逻辑测试  
## 2.1 节点正常出块测试  
``` text
......
684041ms th_a       witness.cpp:97                plugin_initialize    ] Public Key: COCOS6Y5gjJG6YageUeVeoHMMLpESXFi3LdhHWB7dZsKfWQ8giEWN1z
684041ms th_a       witness.cpp:97                plugin_initialize    ] Public Key: COCOS8aJKupmQ4XjWyAbsn58wLb2oLHfEDGMFtd7dDbFtxFpBzMGUda
684041ms th_a       witness.cpp:97                plugin_initialize    ] Public Key: COCOS5fW5NuvGjaVQTGwcJLwogxheq2KMjm3y5ccAShJqQnB3gNkGbL
684042ms th_a       witness.cpp:97                plugin_initialize    ] Public Key: COCOS5rYpiyVtxuX5PDbxHrPEsjVd6Ucz5fWJTdhvAxoPtZGSxvkE82
684042ms th_a       witness.cpp:97                plugin_initialize    ] Public Key: COCOS6e4j3DaruANMUNsK8PMit8Sp3kA1Dw3EhJb3mpCHeZb7nTgUnP
684042ms th_a       witness.cpp:115               plugin_initialize    ] witness plugin:  plugin_initialize() end
684042ms th_a       object_database.cpp:105       open                 ] Opening object database from /home/ck/xukang/testnet/bp/witness_node_data_dir/blockchain ...
709784ms th_a       object_database.cpp:110       open                 ] Done opening object database.
709784ms th_a       application.cpp:339           operator()           ] Initializing database...
709792ms th_a       db_management.cpp:344         open                 ] init global property extensions
709792ms th_a       db_management.cpp:165         reindex              ] reindexing blockchain
709792ms th_a       db_management.cpp:174         reindex              ] Replaying blocks, starting at 7430450...
709793ms th_a       db_management.cpp:239         reindex              ] Done reindexing, elapsed time: 0.00046200000000000 sec
709795ms th_a       application.cpp:166           reset_p2p_node       ] Adding seed node 192.168.90.46:8091
709795ms th_a       application.cpp:166           reset_p2p_node       ] Adding seed node 192.168.90.46:8092
709795ms th_a       application.cpp:166           reset_p2p_node       ] Adding seed node 192.168.90.46:8093
709796ms th_a       application.cpp:166           reset_p2p_node       ] Adding seed node 192.168.90.46:8094
709796ms th_a       application.cpp:204           reset_p2p_node       ] Configured p2p node to listen on 0.0.0.0:8091                                                               
709796ms th_a       application.cpp:284           reset_websocket_serv ] Configured websocket rpc to listen on 0.0.0.0:8152
709797ms th_a       witness.cpp:120               plugin_startup       ] witness plugin:  plugin_startup() begin
709797ms th_a       witness.cpp:126               plugin_startup       ] Launching block production for 11 witnesses.
709797ms th_a       witness.cpp:140               plugin_startup       ] witness plugin:  plugin_startup() end
709797ms th_a       main.cpp:270                  main                 ] Started node on a chain with 7430457 blocks.
709797ms th_a       main.cpp:271                  main                 ] Chain ID is 1ae3653a3105800f5722c5bda2b55530d0e9e8654314e2f3dc6d2b010da641c5
710001ms th_a       witness.cpp:220               block_production_loo ] Generated block #7430458 with timestamp 2020-07-09T03:11:50 at time 2020-07-09T03:11:50
712001ms th_a       witness.cpp:220               block_production_loo ] Generated block #7430459 with timestamp 2020-07-09T03:11:52 at time 2020-07-09T03:11:52
714001ms th_a       witness.cpp:220               block_production_loo ] Generated block #7430460 with timestamp 2020-07-09T03:11:54 at time 2020-07-09T03:11:54
716001ms th_a       witness.cpp:220               block_production_loo ] Generated block #7430461 with timestamp 2020-07-09T03:11:56 at time 2020-07-09T03:11:56
718001ms th_a       witness.cpp:220               block_production_loo ] Generated block #7430462 with timestamp 2020-07-09T03:11:58 at time 2020-07-09T03:11:58
720001ms th_a       witness.cpp:220               block_production_loo ] Generated block #7430463 with timestamp 2020-07-09T03:12:00 at time 2020-07-09T03:12:00
724001ms th_a       witness.cpp:220               block_production_loo ] Generated block #7430464 with timestamp 2020-07-09T03:12:04 at time 2020-07-09T03:12:04
728001ms th_a       witness.cpp:220               block_production_loo ] Generated block #7430465 with timestamp 2020-07-09T03:12:08 at time 2020-07-09T03:12:08
730001ms th_a       witness.cpp:220               block_production_loo ] Generated block #7430466 with timestamp 2020-07-09T03:12:10 at time 2020-07-09T03:12:10
732002ms th_a       witness.cpp:220               block_production_loo ] Generated block #7430467 with timestamp 2020-07-09T03:12:12 at time 2020-07-09T03:12:12
734001ms th_a       witness.cpp:220               block_production_loo ] Generated block #7430468 with timestamp 2020-07-09T03:12:14 at time 2020-07-09T03:12:14
......
```

**已连续正常出块**  

## 2.2 合约部署测试  
[测试合约](https://github.com/gkany/Cocos-Contracts-API/blob/master/contract_34_contract_fee_share_test.lua)    

**合约部署过程和结果**  
```  text  
ck@ubuntu:~/xukang/Cocos-Contracts-API$ python3 contract_test.py 
>> unlock ['123456']

{'id': 1, 'result': None, 'jsonrpc': '2.0'}


>> list_my_accounts []

...... 数据太大，忽略 ......


>> import_key ['nicotest', '5J2SChqa9QxrCkdMor9VC2k9NT4R4ctRrJA6odQCPkb3yL89vxo']

{'id': 1, 'result': True, 'jsonrpc': '2.0'}


setUpClass done

ssssssssssssssssssssssssssssssss>> get_contract ['contract.testapi.contractfeeshare']

{'id': 1, 'error': {'message': 'unspecified: Assert Exception: contract_itr != con_index.end(): The contract (contract.testapi.contractfeeshare) does not exist', 'code': 1}, 'jsonrpc': '2.0'}


>> create_contract_from_file ['nicotest', 'contract.testapi.contractfeeshare', 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', '/home/ck/xukang/Cocos-Contracts-API/contract_34_contract_fee_share_test.lua', 'true']

{'id': 1, 'result': ['a35ec599e10cc181bc4149f037d1cde8a73a52b4ad7da76b034f22566c1a0317', {'expiration': '2020-07-09T03:42:46', 'extensions': [], 'ref_block_num': 25137, 'ref_block_prefix': 3213692590, 'operations': [[34, {'name': 'contract.testapi.contractfeeshare', 'extensions': [], 'contract_authority': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'owner': '1.2.16', 'data': "function test_set_percent(percent)     chainhelper:log('set_invoke_share_percent')     chainhelper:set_invoke_share_percent(percent) end  function test_helloworld()     chainhelper:log('Hi, Cocos-BCX contract') end  function test_contract_fee_share()     chainhelper:log('contract_fee_share_test')     chainhelper:contract_fee_share_test() end "}]], 'signatures': ['20721bf79ce424a7c1d3ecaad1b3bb9e3423b66ad94d113f745cc00532f461c72265a85836e725dc077bd58e1b57ab0e3345bbcf187c258a62447afea72b7ec399']}], 'jsonrpc': '2.0'}


test_contract_34_contract_fee_share done

.ss>> lock []

{'id': 1, 'result': None, 'jsonrpc': '2.0'}


tearDownClass done


----------------------------------------------------------------------
Ran 35 tests in 2.043s
```  

**通过cli_wallet查询，已创建合约成功**  
**查询结果如下：**  
``` text
unlocked >>> 
get_contract contract.testapi.contractfeeshare 
unlocked >>> get_contract contract.testapi.contractfeeshare 
{
  "id": "1.16.121",
  "creation_date": "2020-07-09T03:22:16",
  "owner": "1.2.16",
  "name": "contract.testapi.contractfeeshare",
  "user_invoke_share_percent": 100,
  "current_version": "a35ec599e10cc181bc4149f037d1cde8a73a52b4ad7da76b034f22566c1a0317",
  "contract_authority": "COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx",
  "is_release": false,
  "check_contract_authority": false,
  "contract_data": [],
  "contract_ABI": [[{
        "key": [
          2,{
            "v": "test_contract_fee_share"
          }
        ]
      },[
        5,{
          "is_var_arg": false,
          "arglist": []
        }
      ]
    ],[{
        "key": [
          2,{
            "v": "test_helloworld"
          }
        ]
      },[
        5,{
          "is_var_arg": false,
          "arglist": []
        }
      ]
    ],[{
        "key": [
          2,{
            "v": "test_set_percent"
          }
        ]
      },[
        5,{
          "is_var_arg": false,
          "arglist": [
            "percent"
          ]
        }
      ]
    ]
  ],
  "lua_code_b_id": "2.2.121"
}

unlocked >>> 
get_transaction_in_block_info a35ec599e10cc181bc4149f037d1cde8a73a52b4ad7da76b034f22566c1a0317
unlocked >>> get_transaction_in_block_info a35ec599e10cc181bc4149f037d1cde8a73a52b4ad7da76b034f22566c1a0317
{
  "id": "3.1.824835",
  "block_num": 7430716,
  "trx_in_block": 0,
  "trx_hash": "a35ec599e10cc181bc4149f037d1cde8a73a52b4ad7da76b034f22566c1a0317"
}
get_block 7430716
unlocked >>> get_block 7430716
{
  "previous": "0071623b9af78f06a13dfdfc5c0c5c74c3363cb7",
  "timestamp": "2020-07-09T03:22:20",
  "witness": "1.6.10",
  "transaction_merkle_root": "3a63fc7c06b2a869b086df8b65738cbbeb14190a",
  "witness_signature": "2072b9cacf2da8d13b7a371af8dae16b1eb3a3759174ed26843dcb4b69619177676f6d1aaa047f487698f5c0ef139f937b147b622d0a83b114c02c78f872dcc59e",
  "block_id": "0071623c8cf612badf82a1d521afa216648aad51",
  "transactions": [[
      "a35ec599e10cc181bc4149f037d1cde8a73a52b4ad7da76b034f22566c1a0317",{
        "ref_block_num": 25137,
        "ref_block_prefix": 3213692590,
        "expiration": "2020-07-09T03:42:46",
        "operations": [[
            34,{
              "owner": "1.2.16",
              "name": "contract.testapi.contractfeeshare",
              "data": "function test_set_percent(percent)     chainhelper:log('set_invoke_share_percent')     chainhelper:set_invoke_share_percent(percent) end  function test_helloworld()     chainhelper:log('Hi, Cocos-BCX contract') end  function test_contract_fee_share()     chainhelper:log('contract_fee_share_test')     chainhelper:contract_fee_share_test() end ",
              "contract_authority": "COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx",
              "extensions": []
            }
          ]
        ],
        "extensions": [],
        "signatures": [
          "20721bf79ce424a7c1d3ecaad1b3bb9e3423b66ad94d113f745cc00532f461c72265a85836e725dc077bd58e1b57ab0e3345bbcf187c258a62447afea72b7ec399"
        ],
        "operation_results": [[
            2,{
              "fees": [{
                  "amount": 133789,
                  "asset_id": "1.3.1"
                }
              ],
              "result": "1.16.121",
              "real_running_time": 949
            }
          ]
        ]
      }
    ]
  ]
}

unlocked >>> 
```  

## 2.2 合约重置测试  
**测试合约：**  
``` lua  
function test_set_percent(percent)
    chainhelper:log('set_invoke_share_percent')
    chainhelper:set_invoke_share_percent(percent)
end

function test_helloworld()
    chainhelper:log('Hi, Cocos-BCX contract')
end

function test_contract_fee_share()
    chainhelper:log('contract_fee_share_test')
end
```  

**重置合约测试：**
``` text
ck@ubuntu:~/xukang/Cocos-Contracts-API$ python3 contract_test.py 
>> unlock ['123456']

{'id': 1, 'result': None, 'jsonrpc': '2.0'}


>> list_my_accounts []

数据太大，忽略


setUpClass done

ssssssssssssssssssssssssssssssss>> get_contract ['contract.testapi.contractfeeshare']

{'id': 1, 'result': {'id': '1.16.121', 'creation_date': '2020-07-09T03:22:16', 'lua_code_b_id': '2.2.121', 'owner': '1.2.16', 'is_release': False, 'contract_data': [], 'check_contract_authority': False, 'user_invoke_share_percent': 100, 'name': 'contract.testapi.contractfeeshare', 'current_version': 'a35ec599e10cc181bc4149f037d1cde8a73a52b4ad7da76b034f22566c1a0317', 'contract_ABI': [[{'key': [2, {'v': 'test_contract_fee_share'}]}, [5, {'arglist': [], 'is_var_arg': False}]], [{'key': [2, {'v': 'test_helloworld'}]}, [5, {'arglist': [], 'is_var_arg': False}]], [{'key': [2, {'v': 'test_set_percent'}]}, [5, {'arglist': ['percent'], 'is_var_arg': False}]]], 'contract_authority': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx'}, 'jsonrpc': '2.0'}


>> get_contract ['contract.testapi.contractfeeshare']

{'id': 1, 'result': {'id': '1.16.121', 'creation_date': '2020-07-09T03:22:16', 'lua_code_b_id': '2.2.121', 'owner': '1.2.16', 'is_release': False, 'contract_data': [], 'check_contract_authority': False, 'user_invoke_share_percent': 100, 'name': 'contract.testapi.contractfeeshare', 'current_version': 'a35ec599e10cc181bc4149f037d1cde8a73a52b4ad7da76b034f22566c1a0317', 'contract_ABI': [[{'key': [2, {'v': 'test_contract_fee_share'}]}, [5, {'arglist': [], 'is_var_arg': False}]], [{'key': [2, {'v': 'test_helloworld'}]}, [5, {'arglist': [], 'is_var_arg': False}]], [{'key': [2, {'v': 'test_set_percent'}]}, [5, {'arglist': ['percent'], 'is_var_arg': False}]]], 'contract_authority': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx'}, 'jsonrpc': '2.0'}


>> revise_contract_from_file ['nicotest', 'contract.testapi.contractfeeshare', '/home/ck/xukang/Cocos-Contracts-API/contract_34_contract_fee_share_test.lua', 'true']

{'id': 1, 'result': ['7feed5235f0e1338d33775109673e80aa6d27618f6f4e1d460e64ad6cdb206a1', {'ref_block_num': 25411, 'operations': [[50, {'contract_id': '1.16.121', 'reviser': '1.2.16', 'extensions': [], 'data': "function test_set_percent(percent)     chainhelper:log('set_invoke_share_percent')     chainhelper:set_invoke_share_percent(percent) end  function test_helloworld()     chainhelper:log('Hi, Cocos-BCX contract') end  function test_contract_fee_share()     chainhelper:log('contract_fee_share_test') end "}]], 'extensions': [], 'signatures': ['2015aa14c087642a14e35e01d41ad3679596348c0d332f0ebd685f7c7692bf49561796af5fc52ad0e8fc88cd5f785c0b5af9ba2013c7e751dfd1ed422f9ab9b129'], 'expiration': '2020-07-09T03:53:50', 'ref_block_prefix': 2148676969}], 'jsonrpc': '2.0'}


test_contract_34_contract_fee_share done

.sss>> lock []

{'id': 1, 'result': None, 'jsonrpc': '2.0'}


tearDownClass done


----------------------------------------------------------------------
Ran 36 tests in 2.033s

OK (skipped=35)

```  

**通过cli_wallet查看重置结果**  
``` text  
unlocked >>> 
get_transaction_in_block_info 7feed5235f0e1338d33775109673e80aa6d27618f6f4e1d460e64ad6cdb206a1 
locked >>> get_transaction_in_block_info 7feed5235f0e1338d33775109673e80aa6d27618f6f4e1d460e64ad6cdb206a1 
{
  "id": "3.1.824836",
  "block_num": 7430989,
  "trx_in_block": 0,
  "trx_hash": "7feed5235f0e1338d33775109673e80aa6d27618f6f4e1d460e64ad6cdb206a1"
}

locked >>> 
get_block 7430989 
locked >>> get_block 7430989 
{
  "previous": "0071634c6962cdea7af5ca327b434c362c12e8fa",
  "timestamp": "2020-07-09T03:33:24",
  "witness": "1.6.1",
  "transaction_merkle_root": "9fd27734341ffd3de1932624ec2db2510e233ae4",
  "witness_signature": "2020b8dc4d9ba530643775a6ad975a19a3795154f554263166e3e33791cb38a98d4cb355107ff148375a368b35cb1525d49c72ade82dc9e384ab58c5cff297177d",
  "block_id": "0071634d044d18a097b67674d071ea2431d4b2ab",
  "transactions": [[
      "7feed5235f0e1338d33775109673e80aa6d27618f6f4e1d460e64ad6cdb206a1",{
        "ref_block_num": 25411,
        "ref_block_prefix": 2148676969,
        "expiration": "2020-07-09T03:53:50",
        "operations": [[
            50,{
              "reviser": "1.2.16",
              "contract_id": "1.16.121",
              "data": "function test_set_percent(percent)     chainhelper:log('set_invoke_share_percent')     chainhelper:set_invoke_share_percent(percent) end  function test_helloworld()     chainhelper:log('Hi, Cocos-BCX contract') end  function test_contract_fee_share()     chainhelper:log('contract_fee_share_test') end ",
              "extensions": []
            }
          ]
        ],
        "extensions": [],
        "signatures": [
          "2015aa14c087642a14e35e01d41ad3679596348c0d332f0ebd685f7c7692bf49561796af5fc52ad0e8fc88cd5f785c0b5af9ba2013c7e751dfd1ed422f9ab9b129"
        ],
        "operation_results": [[
            5,{
              "fees": [{
                  "amount": 129687,
                  "asset_id": "1.3.1"
                }
              ],
              "message": "a35ec599e10cc181bc4149f037d1cde8a73a52b4ad7da76b034f22566c1a0317",
              "real_running_time": 840
            }
          ]
        ]
      }
    ]
  ]
}

locked >>> 

locked >>> 
```  

## 2.3 合约调用测试  
**[自动测试程序](https://github.com/gkany/CocosBCX/blob/master/feature_test/contract_fee_share/builder_tx.py)**    

### 2.3.1 单个合约调用测试    
**测试main代码：**  
``` python  
if __name__ == '__main__':
    # print('>> {}'.format(sys.argv))
    unlock("123456")

    # main_build_tx()
    # get_contract_function_call_op_test()

    test_helloworld()
    test_helloworld(caller="init1")
```

**测试合约所有者和非合约所有者调用合约**   

**测试过程和结果**      
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 builder_tx.py 
>> unlock ['123456']
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['67b94ebb1e9c9bd65085e2fad6897655b8d5bc8c76fbd387ef32a45e025c9d47', {'signatures': ['2051e065b3f230727a9f0bcaa74c9d35eccae9a1912d6e31ddd20a12ac3ebc3fb97bb4ce98a9e1740ef15750ae7c9fcd1151ba7bff9fd244db4b65b6f9fe409ec8'], 'expiration': '2020-07-09T06:54:06', 'ref_block_num': 29832, 'operations': [[35, {'extensions': [], 'caller': '1.2.16', 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'value_list': []}]], 'ref_block_prefix': 4256105538, 'extensions': []}]}

>> get_transaction_in_block_info ['67b94ebb1e9c9bd65085e2fad6897655b8d5bc8c76fbd387ef32a45e025c9d47']
{'jsonrpc': '2.0', 'id': 1, 'result': {'trx_hash': '67b94ebb1e9c9bd65085e2fad6897655b8d5bc8c76fbd387ef32a45e025c9d47', 'trx_in_block': 0, 'block_num': 7435413, 'id': '3.1.824841'}}

>> get_transaction_in_block_info 67b94ebb1e9c9bd65085e2fad6897655b8d5bc8c76fbd387ef32a45e025c9d47
 {'trx_hash': '67b94ebb1e9c9bd65085e2fad6897655b8d5bc8c76fbd387ef32a45e025c9d47', 'trx_in_block': 0, 'block_num': 7435413, 'id': '3.1.824841'}

>> get_block [7435413]
{'jsonrpc': '2.0', 'id': 1, 'result': {'previous': '0071749444af26f09ddc819db5c14947c4213a71', 'block_id': '0071749535e95181dccf037bbec6255a9471c7a0', 'witness': '1.6.10', 'timestamp': '2020-07-09T06:33:40', 'witness_signature': '203d25e96a96908f2c4dcd62a56ea35f6d7a8a3d6ae6f002968cb2fb9448c86d1f54c1a3ea410f2b1f83f5bb76dd35eeddd7893533efdb8ae68c9e35f3a1d4a45c', 'transactions': [['67b94ebb1e9c9bd65085e2fad6897655b8d5bc8c76fbd387ef32a45e025c9d47', {'signatures': ['2051e065b3f230727a9f0bcaa74c9d35eccae9a1912d6e31ddd20a12ac3ebc3fb97bb4ce98a9e1740ef15750ae7c9fcd1151ba7bff9fd244db4b65b6f9fe409ec8'], 'expiration': '2020-07-09T06:54:06', 'ref_block_num': 29832, 'operations': [[35, {'extensions': [], 'caller': '1.2.16', 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'value_list': []}]], 'ref_block_prefix': 4256105538, 'extensions': [], 'operation_results': [[4, {'fees': [{'amount': 20976, 'asset_id': '1.3.1'}], 'process_value': '', 'real_running_time': 460, 'existed_pv': False, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}]], 'contract_id': '1.16.121', 'relevant_datasize': 35}]]}]], 'transaction_merkle_root': '9648af591fe314891d66b358480382b206f7c312'}}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['b2698b8fa2a56872beb6bc5f4f69e0372585c65a9c23b557628ab82b9e57b081', {'signatures': ['1f6ace32f0a3615a5fd596491da447a6a2447384c7751e483cc4c630212d62117256f40cd431db187f4eec7c8259756fa2dcb594856506d6a5e3ba630f2e3d98ad'], 'expiration': '2020-07-09T06:54:10', 'ref_block_num': 29835, 'operations': [[35, {'extensions': [], 'caller': '1.2.6', 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'value_list': []}]], 'ref_block_prefix': 2929412308, 'extensions': []}]}

>> get_transaction_in_block_info ['b2698b8fa2a56872beb6bc5f4f69e0372585c65a9c23b557628ab82b9e57b081']
{'jsonrpc': '2.0', 'id': 1, 'result': {'trx_hash': 'b2698b8fa2a56872beb6bc5f4f69e0372585c65a9c23b557628ab82b9e57b081', 'trx_in_block': 0, 'block_num': 7435414, 'id': '3.1.824842'}}

>> get_transaction_in_block_info b2698b8fa2a56872beb6bc5f4f69e0372585c65a9c23b557628ab82b9e57b081
 {'trx_hash': 'b2698b8fa2a56872beb6bc5f4f69e0372585c65a9c23b557628ab82b9e57b081', 'trx_in_block': 0, 'block_num': 7435414, 'id': '3.1.824842'}

>> get_block [7435414]
{'jsonrpc': '2.0', 'id': 1, 'result': {'previous': '0071749535e95181dccf037bbec6255a9471c7a0', 'block_id': '00717496b5a96a6c33fa02bab0b7a35ba06b8bd4', 'witness': '1.6.1', 'timestamp': '2020-07-09T06:33:42', 'witness_signature': '2007f5dd7d1a86da7be4955988c2b6e1b94cab4d330c76e77af4a9edf8d8a10db062cd577c941c1ee2a67463eab8e99df30b48b07642c2e4d8f8e7abd240d8377b', 'transactions': [['b2698b8fa2a56872beb6bc5f4f69e0372585c65a9c23b557628ab82b9e57b081', {'signatures': ['1f6ace32f0a3615a5fd596491da447a6a2447384c7751e483cc4c630212d62117256f40cd431db187f4eec7c8259756fa2dcb594856506d6a5e3ba630f2e3d98ad'], 'expiration': '2020-07-09T06:54:10', 'ref_block_num': 29835, 'operations': [[35, {'extensions': [], 'caller': '1.2.6', 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'value_list': []}]], 'ref_block_prefix': 2929412308, 'extensions': [], 'operation_results': [[4, {'fees': [{'amount': 20925, 'asset_id': '1.3.0'}], 'process_value': '', 'real_running_time': 409, 'existed_pv': False, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}]], 'contract_id': '1.16.121', 'relevant_datasize': 35}]]}]], 'transaction_merkle_root': '0dd829633da0298f19d4aeed731df706b93eedeb'}}

ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```  
合约创建者和非合约创建者均调用成功  
其中，合约创建者有足够的GAS，调用合约消耗的是GAS；非合约创建者由于没有GAS，调用合约消耗的是COCOS  

### 2.3.2 一个交易中有多个operation和合约调用的测试    
**测试main代码：**    
``` python  
if __name__ == '__main__':
    # print('>> {}'.format(sys.argv))
    unlock("123456")

    main_build_tx()

    # test_helloworld()
    # test_helloworld(caller="init1")
```  

**交易中包含：**  
* 两次转账操作  
* 合约创建者调用合约操作  
* 非合约创建者调用合约操作  

**测试过程和结果**      
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 builder_tx.py 
>> unlock ['123456']
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> begin_builder_transaction []
{'jsonrpc': '2.0', 'id': 1, 'result': 0}

>> transfer ['nicotest', 'init0', 23, 'COCOS', ['', False], False]
{'jsonrpc': '2.0', 'id': 1, 'result': ['4351d142b450784371a19a12d84e97bb0f49ebe089ae31f75d47e034b9452670', {'ref_block_num': 30085, 'signatures': ['1f7cbff9fe251f7b6fdff4efff9847cd7660dd78e2bc8f6b98c3899f665ed68d1d1987d47a5ad72ff1c46696e640650085249a2923bf83215938a40cf6cc07b388'], 'extensions': [], 'ref_block_prefix': 2813313823, 'operations': [[0, {'to': '1.2.5', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}}]], 'expiration': '2020-07-09T07:04:14'}]}

>> add_operation_to_builder_transaction [0, [0, {'to': '1.2.5', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}}]]
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], False]
{'jsonrpc': '2.0', 'id': 1, 'result': ['daa706398e5ca678b0f9759c05020dc554f02cc8db50bfcb219665243d2b1622', {'ref_block_num': 30085, 'signatures': ['1f14e267762a08fd40c761e5425cb98c03a9e3019b3e4ed0ea7f24c9e3a267eedb7316d4b3e94b8e888d5eed63c6a56bea69cd49b42d5d7687507179bc5cd91b01'], 'extensions': [], 'ref_block_prefix': 2813313823, 'operations': [[35, {'extensions': [], 'value_list': [], 'caller': '1.2.16', 'contract_id': '1.16.121', 'function_name': 'test_helloworld'}]], 'expiration': '2020-07-09T07:04:14'}]}

>> add_operation_to_builder_transaction [0, [35, {'extensions': [], 'value_list': [], 'caller': '1.2.16', 'contract_id': '1.16.121', 'function_name': 'test_helloworld'}]]
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], False]
{'jsonrpc': '2.0', 'id': 1, 'result': ['879af584af8537b55c04e2e144f9f43dfb1d51c7794808a468ca26a247e6174b', {'ref_block_num': 30085, 'signatures': ['202fceddad337fae18d2dff1e8e0cb61d1c86259a25363a9626ccb84177fee74002d98b0c42f1908d6d08d415307a0e8ec033c80073d8f26eda85df001e39ecd9d'], 'extensions': [], 'ref_block_prefix': 2813313823, 'operations': [[35, {'extensions': [], 'value_list': [], 'caller': '1.2.6', 'contract_id': '1.16.121', 'function_name': 'test_helloworld'}]], 'expiration': '2020-07-09T07:04:14'}]}

>> add_operation_to_builder_transaction [0, [35, {'extensions': [], 'value_list': [], 'caller': '1.2.6', 'contract_id': '1.16.121', 'function_name': 'test_helloworld'}]]
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> transfer ['nicotest', 'init1', 78, 'COCOS', ['', False], False]
{'jsonrpc': '2.0', 'id': 1, 'result': ['19d33c8f8a4a1183cc26d0082dd0cf2acfbb4f5e37a623395cbe56b57e416908', {'ref_block_num': 30085, 'signatures': ['1f43da353ea4e09da54f7adad7250d1b34ca39ad1d2f8a6a09fb9c9f341517030313a9d0e7b276d48a57affc08dc58dba65502a799874450616a37ae2f240183c2'], 'extensions': [], 'ref_block_prefix': 2813313823, 'operations': [[0, {'to': '1.2.6', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}}]], 'expiration': '2020-07-09T07:04:14'}]}

>> add_operation_to_builder_transaction [0, [0, {'to': '1.2.6', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}}]]
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> preview_builder_transaction [0]
{'jsonrpc': '2.0', 'id': 1, 'result': {'ref_block_prefix': 0, 'ref_block_num': 0, 'operations': [[0, {'to': '1.2.5', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}}], [35, {'extensions': [], 'value_list': [], 'caller': '1.2.16', 'contract_id': '1.16.121', 'function_name': 'test_helloworld'}], [35, {'extensions': [], 'value_list': [], 'caller': '1.2.6', 'contract_id': '1.16.121', 'function_name': 'test_helloworld'}], [0, {'to': '1.2.6', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}}]], 'extensions': [], 'expiration': '1970-01-01T00:00:00'}}

>> sign_builder_transaction [0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['655fd36f797b521ed308a8124430f1b0f81eadeac3968fc0ce3441ca1869e561', {'ref_block_num': 30085, 'signatures': ['1f47bda34244ec52c5821aeb722afb98e8dc5f91335f2f8ee9d5143ffa60bcb3605639c50303c00577972632d5186ba13bcc52829cd52c6f1cea15a2ced2d4f223', '1f0cd5b33132c88193c9f903c6c28385ef7553c94040072960f5bb5efa25c286b91227c3e6448838a62491d962adbec0e11690acc3a10154b6eec566e60e400898'], 'extensions': [], 'ref_block_prefix': 2813313823, 'operations': [[0, {'to': '1.2.5', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}}], [35, {'extensions': [], 'value_list': [], 'caller': '1.2.16', 'contract_id': '1.16.121', 'function_name': 'test_helloworld'}], [35, {'extensions': [], 'value_list': [], 'caller': '1.2.6', 'contract_id': '1.16.121', 'function_name': 'test_helloworld'}], [0, {'to': '1.2.6', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}}]], 'expiration': '2020-07-09T07:04:14'}]}

>> get_transaction_in_block_info ['655fd36f797b521ed308a8124430f1b0f81eadeac3968fc0ce3441ca1869e561']
{'jsonrpc': '2.0', 'id': 1, 'result': {'trx_hash': '655fd36f797b521ed308a8124430f1b0f81eadeac3968fc0ce3441ca1869e561', 'block_num': 7435663, 'trx_in_block': 0, 'id': '3.1.824843'}}

>> get_transaction_in_block_info 655fd36f797b521ed308a8124430f1b0f81eadeac3968fc0ce3441ca1869e561
 {'trx_hash': '655fd36f797b521ed308a8124430f1b0f81eadeac3968fc0ce3441ca1869e561', 'block_num': 7435663, 'trx_in_block': 0, 'id': '3.1.824843'}

>> get_block [7435663]
{'jsonrpc': '2.0', 'id': 1, 'result': {'block_id': '0071758f3d218c9460caba0bc8874164a69da025', 'transaction_merkle_root': 'bca1a07959d04ceacfe3841490980eee7da6afd2', 'witness': '1.6.5', 'timestamp': '2020-07-09T06:43:46', 'witness_signature': '206663b3b207a3e63c3adcb29cd8306f9baba6cd54d0185b65d2a997732156c16d5cdf627bf374732e81a55f1126642e8dc62d54d0471b10aadd0e097e6facee68', 'previous': '0071758e7009f48ec1da309ed4ad92ce207a7b82', 'transactions': [['655fd36f797b521ed308a8124430f1b0f81eadeac3968fc0ce3441ca1869e561', {'ref_block_num': 30085, 'signatures': ['1f47bda34244ec52c5821aeb722afb98e8dc5f91335f2f8ee9d5143ffa60bcb3605639c50303c00577972632d5186ba13bcc52829cd52c6f1cea15a2ced2d4f223', '1f0cd5b33132c88193c9f903c6c28385ef7553c94040072960f5bb5efa25c286b91227c3e6448838a62491d962adbec0e11690acc3a10154b6eec566e60e400898'], 'extensions': [], 'operation_results': [[1, {'fees': [{'asset_id': '1.3.1', 'amount': 10000}], 'real_running_time': 64}], [4, {'process_value': '', 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'Hi, Cocos-BCX contract'}]], 'fees': [{'asset_id': '1.3.1', 'amount': 20767}], 'real_running_time': 251, 'relevant_datasize': 35, 'contract_id': '1.16.121', 'existed_pv': False}], [4, {'process_value': '', 'contract_affecteds': [[3, {'affected_account': '1.2.6', 'message': 'Hi, Cocos-BCX contract'}]], 'fees': [{'asset_id': '1.3.0', 'amount': 20818}], 'real_running_time': 302, 'relevant_datasize': 35, 'contract_id': '1.16.121', 'existed_pv': False}], [1, {'fees': [{'asset_id': '1.3.1', 'amount': 10000}], 'real_running_time': 42}]], 'ref_block_prefix': 2813313823, 'operations': [[0, {'to': '1.2.5', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}}], [35, {'extensions': [], 'value_list': [], 'caller': '1.2.16', 'contract_id': '1.16.121', 'function_name': 'test_helloworld'}], [35, {'extensions': [], 'value_list': [], 'caller': '1.2.6', 'contract_id': '1.16.121', 'function_name': 'test_helloworld'}], [0, {'to': '1.2.6', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}}]], 'expiration': '2020-07-09T07:04:14'}]]}}

ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```  

交易中包含的4中操作均执行成功  

---------------------

# 3. 硬分叉之后新逻辑测试  

## 3.1 合约调用测试  
### 3.1.1 单个合约调用测试  
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 builder_tx.py 
>> unlock ['123456']
{'id': 1, 'result': None, 'jsonrpc': '2.0'}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'id': 1, 'result': ['9b267e38086a322fd02021dbd727881bdf70dd8f8e98da4f7f7129e78ed6735e', {'expiration': '2020-07-10T01:57:48', 'signatures': ['205d32f251fa5dc6a1a1a94782c84f2ba001a3e4332958e08d3bda76c0f5aa8f06714d4a8c419a3921bc25d42e369d75d94ae78e65f9c069ae9999cd5864cae2b1'], 'extensions': [], 'ref_block_prefix': 1142558052, 'ref_block_num': 58033, 'operations': [[35, {'caller': '1.2.16', 'function_name': 'test_helloworld', 'value_list': [], 'extensions': [], 'contract_id': '1.16.121'}]]}], 'jsonrpc': '2.0'}

>> get_transaction_in_block_info ['9b267e38086a322fd02021dbd727881bdf70dd8f8e98da4f7f7129e78ed6735e']
{'id': 1, 'result': {'id': '3.1.824854', 'block_num': 7463610, 'trx_in_block': 0, 'trx_hash': '9b267e38086a322fd02021dbd727881bdf70dd8f8e98da4f7f7129e78ed6735e'}, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info 9b267e38086a322fd02021dbd727881bdf70dd8f8e98da4f7f7129e78ed6735e
 {'id': '3.1.824854', 'block_num': 7463610, 'trx_in_block': 0, 'trx_hash': '9b267e38086a322fd02021dbd727881bdf70dd8f8e98da4f7f7129e78ed6735e'}

>> get_block [7463610]
{'id': 1, 'result': {'transactions': [['9b267e38086a322fd02021dbd727881bdf70dd8f8e98da4f7f7129e78ed6735e', {'expiration': '2020-07-10T01:57:48', 'operation_results': [[4, {'process_value': '', 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'fees': [{'amount': 21073, 'asset_id': '1.3.0'}], 'message': '100%', 'affected_account': '1.2.16'}]], 'relevant_datasize': 35, 'contract_id': '1.16.121', 'existed_pv': False, 'fees': [{'amount': 21073, 'asset_id': '1.3.0'}], 'real_running_time': 557}], [1, {'fees': [{'amount': 100000, 'asset_id': '1.3.1'}], 'real_running_time': 115}]], 'signatures': ['205d32f251fa5dc6a1a1a94782c84f2ba001a3e4332958e08d3bda76c0f5aa8f06714d4a8c419a3921bc25d42e369d75d94ae78e65f9c069ae9999cd5864cae2b1'], 'extensions': [], 'ref_block_prefix': 1142558052, 'ref_block_num': 58033, 'operations': [[35, {'caller': '1.2.16', 'function_name': 'test_helloworld', 'value_list': [], 'extensions': [], 'contract_id': '1.16.121'}]]}]], 'previous': '0071e2b9742f21eb503323c845ab50d4c9d9a521', 'witness': '1.6.8', 'transaction_merkle_root': '955cbe0dd33f148a9c84a02eaea2da798ead8142', 'timestamp': '2020-07-10T01:37:20', 'witness_signature': '1f337eb8bbcfcfddf1152eb0b20fc529658a0583a9eea94d463d57d2cc751ec22f1fc26f313a8825f5232bfe0f5de62d524c013454ee965fb2b1878ad9dbf808de', 'block_id': '0071e2ba1e8199256b613fd625ce31357d10757b'}, 'jsonrpc': '2.0'}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'id': 1, 'result': ['1de538f351cc1a2edcc53375cb5f464433ef1a45c597994d7dd14c12021fbf72', {'expiration': '2020-07-10T01:57:50', 'signatures': ['206648008c1ca45b2948baed126287be20fba1730a549924e4d4c2629d87873e9701f3aafb9b1d68523530778bf2086cfb01a55eddd05736ec4ab2809591f5199e'], 'extensions': [], 'ref_block_prefix': 2601007674, 'ref_block_num': 58034, 'operations': [[35, {'caller': '1.2.6', 'function_name': 'test_helloworld', 'value_list': [], 'extensions': [], 'contract_id': '1.16.121'}]]}], 'jsonrpc': '2.0'}

>> get_transaction_in_block_info ['1de538f351cc1a2edcc53375cb5f464433ef1a45c597994d7dd14c12021fbf72']
{'id': 1, 'result': {'id': '3.1.824855', 'block_num': 7463611, 'trx_in_block': 0, 'trx_hash': '1de538f351cc1a2edcc53375cb5f464433ef1a45c597994d7dd14c12021fbf72'}, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info 1de538f351cc1a2edcc53375cb5f464433ef1a45c597994d7dd14c12021fbf72
 {'id': '3.1.824855', 'block_num': 7463611, 'trx_in_block': 0, 'trx_hash': '1de538f351cc1a2edcc53375cb5f464433ef1a45c597994d7dd14c12021fbf72'}

>> get_block [7463611]
{'id': 1, 'result': {'transactions': [['1de538f351cc1a2edcc53375cb5f464433ef1a45c597994d7dd14c12021fbf72', {'expiration': '2020-07-10T01:57:50', 'operation_results': [[4, {'process_value': '', 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}], [5, {'fees': [{'amount': 20995, 'asset_id': '1.3.0'}], 'message': '100%', 'affected_account': '1.2.6'}]], 'relevant_datasize': 35, 'contract_id': '1.16.121', 'existed_pv': False, 'fees': [{'amount': 20995, 'asset_id': '1.3.0'}], 'real_running_time': 479}]], 'signatures': ['206648008c1ca45b2948baed126287be20fba1730a549924e4d4c2629d87873e9701f3aafb9b1d68523530778bf2086cfb01a55eddd05736ec4ab2809591f5199e'], 'extensions': [], 'ref_block_prefix': 2601007674, 'ref_block_num': 58034, 'operations': [[35, {'caller': '1.2.6', 'function_name': 'test_helloworld', 'value_list': [], 'extensions': [], 'contract_id': '1.16.121'}]]}]], 'previous': '0071e2ba1e8199256b613fd625ce31357d10757b', 'witness': '1.6.5', 'transaction_merkle_root': 'ecd9a43bfbb9e80140c8f3746d44dc4bc17ecbf0', 'timestamp': '2020-07-10T01:37:22', 'witness_signature': '200c2a44d96a7d97287ef29a0afdeedf8a02639834145855df663ef584d173a4f14fbcf2c1e2d8e66b1c75e1cfe744866044d1c7c9723bfa369c464835d2190915', 'block_id': '0071e2bb13321549cda4fb88435178d09e0e3dc9'}, 'jsonrpc': '2.0'}
```  
合约所有者和非合约所有者调用合约均成功，并且合约调用费用在block中的operation_results中均有记录。  

### 3.1.2 一个交易中有多个operation和合约调用的测试    
**测试main代码：**    
``` python  
if __name__ == '__main__':
    # print('>> {}'.format(sys.argv))
    unlock("123456")

    main_build_tx()

    # test_helloworld()
    # test_helloworld(caller="init1")
```  

**交易中包含：**  
* 两次转账操作  
* 合约创建者调用合约操作  
* 非合约创建者调用合约操作  

**测试过程和结果如下：**  
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 builder_tx.py 
>> unlock ['123456']
{'result': None, 'id': 1, 'jsonrpc': '2.0'}

>> begin_builder_transaction []
{'result': 0, 'id': 1, 'jsonrpc': '2.0'}

>> transfer ['nicotest', 'init0', 23, 'COCOS', ['', False], False]
{'result': ['4bdfbf3fb77aca0199b5b976d197aac773b7d8deff4328d0c94c50b91c4d8579', {'extensions': [], 'expiration': '2020-07-10T02:06:40', 'ref_block_prefix': 3485242763, 'ref_block_num': 58251, 'operations': [[0, {'extensions': [], 'amount': {'asset_id': '1.3.0', 'amount': 2300000}, 'from': '1.2.16', 'to': '1.2.5'}]], 'signatures': ['206979be2b8279ea833177af9c69c9dab4b9057fb39204b4cb342984aacf4e8ae41c3c62ee3e7460d287b336291bd98000121b1e5d5c360bdd31af355c1d218c20']}], 'id': 1, 'jsonrpc': '2.0'}

>> add_operation_to_builder_transaction [0, [0, {'extensions': [], 'amount': {'asset_id': '1.3.0', 'amount': 2300000}, 'from': '1.2.16', 'to': '1.2.5'}]]
{'result': None, 'id': 1, 'jsonrpc': '2.0'}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], False]
{'result': ['3399062d47e196cd0175a06990123deb7ee39d4460c8ef95d3f36e71c0934e3f', {'extensions': [], 'expiration': '2020-07-10T02:06:40', 'ref_block_prefix': 3485242763, 'ref_block_num': 58251, 'operations': [[35, {'contract_id': '1.16.121', 'value_list': [], 'caller': '1.2.16', 'extensions': [], 'function_name': 'test_helloworld'}]], 'signatures': ['1f1d346ce3fe96fedd0932561c11bda638a445d65c49d49a0d600b868cbc6c2a8d0c274427c1b3015f930583f4053550e94979e9a8480f716b934bb2bac652b7ce']}], 'id': 1, 'jsonrpc': '2.0'}

>> add_operation_to_builder_transaction [0, [35, {'contract_id': '1.16.121', 'value_list': [], 'caller': '1.2.16', 'extensions': [], 'function_name': 'test_helloworld'}]]
{'result': None, 'id': 1, 'jsonrpc': '2.0'}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], False]
{'result': ['5e19d40cc1ff7b2ec516b92adfac0122764319017dc0ed34b6c42a606c195fe5', {'extensions': [], 'expiration': '2020-07-10T02:06:40', 'ref_block_prefix': 3485242763, 'ref_block_num': 58251, 'operations': [[35, {'contract_id': '1.16.121', 'value_list': [], 'caller': '1.2.6', 'extensions': [], 'function_name': 'test_helloworld'}]], 'signatures': ['1f1d2cd076763d76c01b2a6d3d2e2139a8b5164e8bd0fdd7069a69892a7d226c7f65053598d67db23f5dafad5b2b67ef07e36a2146894ea6444d5f84ffa5c22d93']}], 'id': 1, 'jsonrpc': '2.0'}

>> add_operation_to_builder_transaction [0, [35, {'contract_id': '1.16.121', 'value_list': [], 'caller': '1.2.6', 'extensions': [], 'function_name': 'test_helloworld'}]]
{'result': None, 'id': 1, 'jsonrpc': '2.0'}

>> transfer ['nicotest', 'init1', 78, 'COCOS', ['', False], False]
{'result': ['9777d203ab3dca1bc8435bc54d7f7e36d908b65f6490c442b0feacf02c8af28a', {'extensions': [], 'expiration': '2020-07-10T02:06:40', 'ref_block_prefix': 3485242763, 'ref_block_num': 58251, 'operations': [[0, {'extensions': [], 'amount': {'asset_id': '1.3.0', 'amount': 7800000}, 'from': '1.2.16', 'to': '1.2.6'}]], 'signatures': ['1f325f8bc8ee8d6c593f75da533a9e81a5afb65bbc8f7e771883f1f67820e25f470857811951fbb1710b2b8a23c13e7fb340de23971a7f5f15382e8cea54bc85ff']}], 'id': 1, 'jsonrpc': '2.0'}

>> add_operation_to_builder_transaction [0, [0, {'extensions': [], 'amount': {'asset_id': '1.3.0', 'amount': 7800000}, 'from': '1.2.16', 'to': '1.2.6'}]]
{'result': None, 'id': 1, 'jsonrpc': '2.0'}

>> preview_builder_transaction [0]
{'result': {'extensions': [], 'operations': [[0, {'extensions': [], 'amount': {'asset_id': '1.3.0', 'amount': 2300000}, 'from': '1.2.16', 'to': '1.2.5'}], [35, {'contract_id': '1.16.121', 'value_list': [], 'caller': '1.2.16', 'extensions': [], 'function_name': 'test_helloworld'}], [35, {'contract_id': '1.16.121', 'value_list': [], 'caller': '1.2.6', 'extensions': [], 'function_name': 'test_helloworld'}], [0, {'extensions': [], 'amount': {'asset_id': '1.3.0', 'amount': 7800000}, 'from': '1.2.16', 'to': '1.2.6'}]], 'ref_block_num': 0, 'ref_block_prefix': 0, 'expiration': '1970-01-01T00:00:00'}, 'id': 1, 'jsonrpc': '2.0'}

>> sign_builder_transaction [0, True]
{'result': ['4cf325acd4b8e6f4ae6d89e0284b46a213a505887f3a843924bb020616f61321', {'extensions': [], 'expiration': '2020-07-10T02:06:40', 'ref_block_prefix': 3485242763, 'ref_block_num': 58251, 'operations': [[0, {'extensions': [], 'amount': {'asset_id': '1.3.0', 'amount': 2300000}, 'from': '1.2.16', 'to': '1.2.5'}], [35, {'contract_id': '1.16.121', 'value_list': [], 'caller': '1.2.16', 'extensions': [], 'function_name': 'test_helloworld'}], [35, {'contract_id': '1.16.121', 'value_list': [], 'caller': '1.2.6', 'extensions': [], 'function_name': 'test_helloworld'}], [0, {'extensions': [], 'amount': {'asset_id': '1.3.0', 'amount': 7800000}, 'from': '1.2.16', 'to': '1.2.6'}]], 'signatures': ['1f47455f6845d89bcb178458710770ba277e0f38b739fed3ff1ed5e864147ab5a02db3488414037374bafc4bea096bbf7631f5ed6a67de354a8e760a77b926b80c', '1f5aaf5f71d370c333cf209f4fa5e1f65c672e716cebd0220cf82aa7e878220fd659aa4c7a50c821c92a52efd4e01f3e5efc95473f45113ab4b4f2db4fd4120580']}], 'id': 1, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info ['4cf325acd4b8e6f4ae6d89e0284b46a213a505887f3a843924bb020616f61321']
{'result': {'trx_hash': '4cf325acd4b8e6f4ae6d89e0284b46a213a505887f3a843924bb020616f61321', 'trx_in_block': 0, 'id': '3.1.824856', 'block_num': 7463828}, 'id': 1, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info 4cf325acd4b8e6f4ae6d89e0284b46a213a505887f3a843924bb020616f61321
 {'trx_hash': '4cf325acd4b8e6f4ae6d89e0284b46a213a505887f3a843924bb020616f61321', 'trx_in_block': 0, 'id': '3.1.824856', 'block_num': 7463828}

>> get_block [7463828]
{'result': {'block_id': '0071e394f3446eec20341c1551e153b819706d78', 'timestamp': '2020-07-10T01:46:12', 'transaction_merkle_root': 'fc2b908627a02512cb77d881e36ed5686af9a7d1', 'previous': '0071e393a385da02a1df4439c8ddcc39baa5e6b7', 'transactions': [['4cf325acd4b8e6f4ae6d89e0284b46a213a505887f3a843924bb020616f61321', {'extensions': [], 'operation_results': [[1, {'fees': [{'asset_id': '1.3.1', 'amount': 10000}], 'real_running_time': 117}], [4, {'contract_id': '1.16.121', 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'fees': [{'asset_id': '1.3.0', 'amount': 20935}], 'message': '100%', 'affected_account': '1.2.16'}]], 'fees': [{'asset_id': '1.3.0', 'amount': 20935}], 'process_value': '', 'real_running_time': 419, 'relevant_datasize': 35, 'existed_pv': False}], [4, {'contract_id': '1.16.121', 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}], [5, {'fees': [{'asset_id': '1.3.0', 'amount': 20920}], 'message': '100%', 'affected_account': '1.2.6'}]], 'fees': [{'asset_id': '1.3.0', 'amount': 20920}], 'process_value': '', 'real_running_time': 404, 'relevant_datasize': 35, 'existed_pv': False}], [1, {'fees': [{'asset_id': '1.3.1', 'amount': 10000}], 'real_running_time': 95}]], 'expiration': '2020-07-10T02:06:40', 'ref_block_prefix': 3485242763, 'ref_block_num': 58251, 'operations': [[0, {'extensions': [], 'amount': {'asset_id': '1.3.0', 'amount': 2300000}, 'from': '1.2.16', 'to': '1.2.5'}], [35, {'contract_id': '1.16.121', 'value_list': [], 'caller': '1.2.16', 'extensions': [], 'function_name': 'test_helloworld'}], [35, {'contract_id': '1.16.121', 'value_list': [], 'caller': '1.2.6', 'extensions': [], 'function_name': 'test_helloworld'}], [0, {'extensions': [], 'amount': {'asset_id': '1.3.0', 'amount': 7800000}, 'from': '1.2.16', 'to': '1.2.6'}]], 'signatures': ['1f47455f6845d89bcb178458710770ba277e0f38b739fed3ff1ed5e864147ab5a02db3488414037374bafc4bea096bbf7631f5ed6a67de354a8e760a77b926b80c', '1f5aaf5f71d370c333cf209f4fa5e1f65c672e716cebd0220cf82aa7e878220fd659aa4c7a50c821c92a52efd4e01f3e5efc95473f45113ab4b4f2db4fd4120580']}]], 'witness_signature': '1f707706951c833f2c55411b76d6acbaa8ac09b3d9a2e37d40329c0c4b43a78f120a32a572f406db8b5a0b6d4fa123bab0d6c19c3717213263c612dd1189a191a9', 'witness': '1.6.5'}, 'id': 1, 'jsonrpc': '2.0'}
```  
调用合约成功，并且合约调用费用在block中的operation_results中均有记录。  


## 3.2 重新设置合约费用分摊百分比测试  
### 3.2.1 非合约所有者设置合约分摊比例  
**测试接口：**  
``` python  
test_set_percent(owner="init1")
```  

**测试过程和结果：**
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 builder_tx.py 
>> unlock ['123456']
{'id': 1, 'jsonrpc': '2.0', 'result': None}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_set_percent', [[1, {'v': 30}]], True]
{'id': 1, 'jsonrpc': '2.0', 'error': {'code': 1, 'message': 'unspecified: unspecified: Try the contract resolution execution failure,[2,{"v":"Assert Exception: is_owner(): You`re not the contract`s owner"}]'}}

KeyError('result',)
Traceback (most recent call last):
  File "builder_tx.py", line 303, in <module>
    test_set_percent(owner="init1")
  File "builder_tx.py", line 271, in test_set_percent
    block = get_block_by_transaction_id(call_result[0])
TypeError: 'NoneType' object is not subscriptable
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```  

**cli_wallet报错如下：**  
``` text  
unlocked >>> 
474106ms th_a       wallet.cpp:1788               sign_transaction     ] Caught exception while broadcasting tx 7f0051cdcddced8391b0c4f79bc71cb84657085a:  0 exception: unspecified
unspecified: Try the contract resolution execution failure,[2,{"v":"Assert Exception: is_owner(): You`re not the contract`s owner"}]
    {"error":"unspecified: Try the contract resolution execution failure,[2,{\"v\":\"Assert Exception: is_owner(): You`re not the contract`s owner\"}]","data":{"id":102,"jsonrpc":"2.0","error":{"code":102,"message":"unspecified: Try the contract resolution execution failure,[2,{\"v\":\"Assert Exception: is_owner(): You`re not the contract`s owner\"}]"}}}
    th_a  state.cpp:38 handle_reply
474106ms th_a       websocket_api.cpp:158         on_message           ] websocket api exception :{"code":0,"name":"exception","message":"unspecified","stack":[{"context":{"level":"error","file":"state.cpp","line":38,"method":"handle_reply","hostname":"","thread_name":"th_a","timestamp":"2020-07-10T02:07:54"},"format":"${error}","data":{"error":"unspecified: Try the contract resolution execution failure,[2,{\"v\":\"Assert Exception: is_owner(): You`re not the contract`s owner\"}]","data":{"id":102,"jsonrpc":"2.0","error":{"code":102,"message":"unspecified: Try the contract resolution execution failure,[2,{\"v\":\"Assert Exception: is_owner(): You`re not the contract`s owner\"}]"}}}},{"context":{"level":"warn","file":"wallet.cpp","line":2090,"method":"call_contract_function","hostname":"","thread_name":"th_a","timestamp":"2020-07-10T02:07:54"},"format":"","data":{"account_id_or_name":"init1","contract_id_or_name":"contract.testapi.contractfeeshare","function_name":"test_set_percent","value_list":[[1,{"v":"30.00000000000000000"}]],"broadcast":true}},{"context":{"level":"warn","file":"websocket_api.cpp","line":154,"method":"on_message","hostname":"","thread_name":"th_a","timestamp":"2020-07-10T02:07:54"},"format":"","data":{"call.method":"call_contract_function","call.params":["init1","contract.testapi.contractfeeshare","test_set_percent",[[1,{"v":30}]],true]}}]}

```
非合约所有者设置不成功。  

### 3.2.2 合约所有者设置合约分摊比例  
**测试接口：**  
``` python  
test_set_percent()
```  

**测试过程和结果：**
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 builder_tx.py 
>> unlock ['123456']
{'jsonrpc': '2.0', 'result': None, 'id': 1}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_set_percent', [[1, {'v': 30}]], True]
{'jsonrpc': '2.0', 'result': ['531e178d101f03f4353d106bf462864c1e1de72ea9dfe7810e5d7cd7f0dec486', {'extensions': [], 'ref_block_prefix': 1794589528, 'expiration': '2020-07-10T02:33:16', 'ref_block_num': 58903, 'operations': [[35, {'function_name': 'test_set_percent', 'contract_id': '1.16.121', 'extensions': [], 'value_list': [[1, {'v': '30.00000000000000000'}]], 'caller': '1.2.16'}]], 'signatures': ['1f30856bd4b98e4ca0432d5a00b4a992a19bca3a168266d4cf2704e4ebe547ca747cefb1bb99a9668e614e66646fd0a92e0a5564f7f308db4bf8f9392c08651de6']}], 'id': 1}

>> get_transaction_in_block_info ['531e178d101f03f4353d106bf462864c1e1de72ea9dfe7810e5d7cd7f0dec486']
{'jsonrpc': '2.0', 'result': {'trx_hash': '531e178d101f03f4353d106bf462864c1e1de72ea9dfe7810e5d7cd7f0dec486', 'trx_in_block': 0, 'id': '3.1.824858', 'block_num': 7464480}, 'id': 1}

>> get_transaction_in_block_info 531e178d101f03f4353d106bf462864c1e1de72ea9dfe7810e5d7cd7f0dec486
 {'trx_hash': '531e178d101f03f4353d106bf462864c1e1de72ea9dfe7810e5d7cd7f0dec486', 'trx_in_block': 0, 'id': '3.1.824858', 'block_num': 7464480}

>> get_block [7464480]
{'jsonrpc': '2.0', 'result': {'transaction_merkle_root': '34f81c512918d64a22fbdc140b70424c9ae3a860', 'timestamp': '2020-07-10T02:12:48', 'witness_signature': '1f2037c549806982c8242835493eea247491f5938c7219dc9f56469f709af35eaf626c2f50c3c03bd8e04ce3da6a00c779ade893a241aa5973844d3e247712d27f', 'block_id': '0071e620888db3a4ecbe4fe5d6b43ae9a6bd27a5', 'witness': '1.6.2', 'previous': '0071e61f077bfa4d1751211c68a4e2d075dd4a04', 'transactions': [['531e178d101f03f4353d106bf462864c1e1de72ea9dfe7810e5d7cd7f0dec486', {'extensions': [], 'ref_block_prefix': 1794589528, 'expiration': '2020-07-10T02:33:16', 'ref_block_num': 58903, 'operations': [[35, {'function_name': 'test_set_percent', 'contract_id': '1.16.121', 'extensions': [], 'value_list': [[1, {'v': '30.00000000000000000'}]], 'caller': '1.2.16'}]], 'signatures': ['1f30856bd4b98e4ca0432d5a00b4a992a19bca3a168266d4cf2704e4ebe547ca747cefb1bb99a9668e614e66646fd0a92e0a5564f7f308db4bf8f9392c08651de6'], 'operation_results': [[4, {'process_value': '', 'relevant_datasize': 37, 'real_running_time': 446, 'existed_pv': False, 'fees': [{'amount': 21080, 'asset_id': '1.3.0'}], 'contract_id': '1.16.121', 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'set_invoke_share_percent'}], [5, {'affected_account': '1.2.16', 'fees': [{'amount': 21080, 'asset_id': '1.3.0'}], 'message': '100%'}]]}]]}]]}, 'id': 1}

ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```  
合约调用成功  

**cli_wallet查看合约信息**  
``` text  
unlocked >>> 
get_object 1.16.121
unlocked >>> get_object 1.16.121
[{
    "id": "1.16.121",
    "creation_date": "2020-07-09T03:22:16",
    "owner": "1.2.16",
    "name": "contract.testapi.contractfeeshare",
    "user_invoke_share_percent": 30,
    "current_version": "7feed5235f0e1338d33775109673e80aa6d27618f6f4e1d460e64ad6cdb206a1",
    "contract_authority": "COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx",
    "is_release": false,
    "check_contract_authority": false,
    "contract_data": [],
    "contract_ABI": [[{
          "key": [
            2,{
              "v": "test_contract_fee_share"
            }
          ]
        },[
          5,{
            "is_var_arg": false,
            "arglist": []
          }
        ]
      ],[{
          "key": [
            2,{
              "v": "test_helloworld"
            }
          ]
        },[
          5,{
            "is_var_arg": false,
            "arglist": []
          }
        ]
      ],[{
          "key": [
            2,{
              "v": "test_set_percent"
            }
          ]
        },[
          5,{
            "is_var_arg": false,
            "arglist": [
              "percent"
            ]
          }
        ]
      ]
    ],
    "lua_code_b_id": "2.2.121"
  }
]

unlocked >>> 
```  
可以看到，已经设置成功为30% (之前的是100%)

### 3.2.3 修改分摊比例后合约调用测试  
**测试main代码：**    
``` python  
if __name__ == '__main__':
    # print('>> {}'.format(sys.argv))
    unlock("123456")

    main_build_tx()

    test_helloworld()
    test_helloworld(caller="init1")
```  

**测试过程和结果：**
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 builder_tx.py 
>> unlock ['123456']
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> begin_builder_transaction []
{'jsonrpc': '2.0', 'id': 1, 'result': 2}

>> transfer ['nicotest', 'init0', 23, 'COCOS', ['', False], False]
{'jsonrpc': '2.0', 'id': 1, 'result': ['4c1a18292c9b593a53299a71d74414f2a93c97849dec3aa335e66de022c8d396', {'expiration': '2020-07-10T02:39:38', 'signatures': ['205c486ae75fa8e3ccc75910f2a872cbd611f1842d221385a89dac13417dc0c40403f0734f875358ad1e4d77ecf3e3fdbb832a735e5840dbbd9e6b6b7b40efbd7d'], 'ref_block_prefix': 387154614, 'extensions': [], 'ref_block_num': 59057, 'operations': [[0, {'to': '1.2.5', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}, 'from': '1.2.16', 'extensions': []}]]}]}

>> add_operation_to_builder_transaction [2, [0, {'to': '1.2.5', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}, 'from': '1.2.16', 'extensions': []}]]
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], False]
{'jsonrpc': '2.0', 'id': 1, 'result': ['98f088f0f770adf17bdc99a9975127b16038985695672bded294f06c263a12aa', {'expiration': '2020-07-10T02:39:38', 'signatures': ['206eef3f113e174cab55b9aa5e4bd22a83806dd886903a81c439f3c467935dfeeb65b5f2d53182103e5a8f97766d17ada0916f65831b8cbb5d2c94bc2692b60a2e'], 'ref_block_prefix': 387154614, 'extensions': [], 'ref_block_num': 59057, 'operations': [[35, {'caller': '1.2.16', 'value_list': [], 'contract_id': '1.16.121', 'extensions': [], 'function_name': 'test_helloworld'}]]}]}

>> add_operation_to_builder_transaction [2, [35, {'caller': '1.2.16', 'value_list': [], 'contract_id': '1.16.121', 'extensions': [], 'function_name': 'test_helloworld'}]]
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], False]
{'jsonrpc': '2.0', 'id': 1, 'result': ['f904d7934a83e5166733db52d0191892e69a0149738fda199d2eee8386ee65f0', {'expiration': '2020-07-10T02:39:38', 'signatures': ['1f3beca80be0d1dcc08d27417372a2e5804953e290e2aaee48e477048181e339db04340915c97c95fdd11e00f4e887b896722538ad8181bde3b70e2de6808561f6'], 'ref_block_prefix': 387154614, 'extensions': [], 'ref_block_num': 59057, 'operations': [[35, {'caller': '1.2.6', 'value_list': [], 'contract_id': '1.16.121', 'extensions': [], 'function_name': 'test_helloworld'}]]}]}

>> add_operation_to_builder_transaction [2, [35, {'caller': '1.2.6', 'value_list': [], 'contract_id': '1.16.121', 'extensions': [], 'function_name': 'test_helloworld'}]]
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> transfer ['nicotest', 'init1', 78, 'COCOS', ['', False], False]
{'jsonrpc': '2.0', 'id': 1, 'result': ['ba9b2fd0b29aadc9cc024d1e56eb07cac9866927823ed4b7df19729f59ebadde', {'expiration': '2020-07-10T02:39:38', 'signatures': ['204fbc17f6d806b7caf193d0aca628caff4bb3c606d2d669c4e66692c8f524a2af27b480f329f5a766a5e01187f9707e37b9f97217d84bcc8cf57d8ba7ac31b8e1'], 'ref_block_prefix': 387154614, 'extensions': [], 'ref_block_num': 59057, 'operations': [[0, {'to': '1.2.6', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}, 'from': '1.2.16', 'extensions': []}]]}]}

>> add_operation_to_builder_transaction [2, [0, {'to': '1.2.6', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}, 'from': '1.2.16', 'extensions': []}]]
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> preview_builder_transaction [2]
{'jsonrpc': '2.0', 'id': 1, 'result': {'expiration': '1970-01-01T00:00:00', 'operations': [[0, {'to': '1.2.5', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}, 'from': '1.2.16', 'extensions': []}], [35, {'caller': '1.2.16', 'value_list': [], 'contract_id': '1.16.121', 'extensions': [], 'function_name': 'test_helloworld'}], [35, {'caller': '1.2.6', 'value_list': [], 'contract_id': '1.16.121', 'extensions': [], 'function_name': 'test_helloworld'}], [0, {'to': '1.2.6', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}, 'from': '1.2.16', 'extensions': []}]], 'ref_block_prefix': 0, 'extensions': [], 'ref_block_num': 0}}

>> sign_builder_transaction [2, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['25512ba394dfaea61658c9eb296214ea9e2bafe4fc1d9a035830409a9e32f0da', {'expiration': '2020-07-10T02:39:38', 'signatures': ['2058151ca2e3be32747bff610bfe4538c01d7649c5a050442454839acef40a15963a4baf70a5679f2fc6dffa471cd1ca2cc5cdd3121de25f7da8a3c6593d78ab81', '1f77a05554b7d7b8fb9c923510efe1e1d02138f58d38f447575bf5ae7458337b6621fc182db520714ecb560a24811e78555e540f3a5137eb0c78e5e2bc6775f721'], 'ref_block_prefix': 387154614, 'extensions': [], 'ref_block_num': 59057, 'operations': [[0, {'to': '1.2.5', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}, 'from': '1.2.16', 'extensions': []}], [35, {'caller': '1.2.16', 'value_list': [], 'contract_id': '1.16.121', 'extensions': [], 'function_name': 'test_helloworld'}], [35, {'caller': '1.2.6', 'value_list': [], 'contract_id': '1.16.121', 'extensions': [], 'function_name': 'test_helloworld'}], [0, {'to': '1.2.6', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}, 'from': '1.2.16', 'extensions': []}]]}]}

>> get_transaction_in_block_info ['25512ba394dfaea61658c9eb296214ea9e2bafe4fc1d9a035830409a9e32f0da']
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> get_transaction_in_block_info 25512ba394dfaea61658c9eb296214ea9e2bafe4fc1d9a035830409a9e32f0da
 None

>> get_transaction_in_block_info ['25512ba394dfaea61658c9eb296214ea9e2bafe4fc1d9a035830409a9e32f0da']
{'jsonrpc': '2.0', 'id': 1, 'result': {'trx_hash': '25512ba394dfaea61658c9eb296214ea9e2bafe4fc1d9a035830409a9e32f0da', 'block_num': 7464635, 'id': '3.1.824859', 'trx_in_block': 0}}

>> get_transaction_in_block_info 25512ba394dfaea61658c9eb296214ea9e2bafe4fc1d9a035830409a9e32f0da
 {'trx_hash': '25512ba394dfaea61658c9eb296214ea9e2bafe4fc1d9a035830409a9e32f0da', 'block_num': 7464635, 'id': '3.1.824859', 'trx_in_block': 0}

>> get_block [7464635]
{'jsonrpc': '2.0', 'id': 1, 'result': {'timestamp': '2020-07-10T02:19:12', 'block_id': '0071e6bba9b08edc0f9d2c853b2ce75356fdeb32', 'previous': '0071e6ba28d234c1e7d63d36f7c2aa0488f9a6f4', 'transactions': [['25512ba394dfaea61658c9eb296214ea9e2bafe4fc1d9a035830409a9e32f0da', {'expiration': '2020-07-10T02:39:38', 'signatures': ['2058151ca2e3be32747bff610bfe4538c01d7649c5a050442454839acef40a15963a4baf70a5679f2fc6dffa471cd1ca2cc5cdd3121de25f7da8a3c6593d78ab81', '1f77a05554b7d7b8fb9c923510efe1e1d02138f58d38f447575bf5ae7458337b6621fc182db520714ecb560a24811e78555e540f3a5137eb0c78e5e2bc6775f721'], 'ref_block_prefix': 387154614, 'operation_results': [[1, {'fees': [{'asset_id': '1.3.1', 'amount': 10000}], 'real_running_time': 85}], [4, {'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'Hi, Cocos-BCX contract'}], [5, {'affected_account': '1.2.16', 'fees': [{'asset_id': '1.3.0', 'amount': 20809}], 'message': '100%'}]], 'process_value': '', 'contract_id': '1.16.121', 'relevant_datasize': 35, 'fees': [{'asset_id': '1.3.0', 'amount': 20809}], 'existed_pv': False, 'real_running_time': 293}], [4, {'contract_affecteds': [[3, {'affected_account': '1.2.6', 'message': 'Hi, Cocos-BCX contract'}], [5, {'affected_account': '1.2.6', 'fees': [{'asset_id': '1.3.0', 'amount': 6220}], 'message': '30%'}], [5, {'affected_account': '1.2.16', 'fees': [{'asset_id': '1.3.0', 'amount': 14512}], 'message': '70%'}]], 'process_value': '', 'contract_id': '1.16.121', 'relevant_datasize': 35, 'fees': [{'asset_id': '1.3.0', 'amount': 20732}], 'existed_pv': False, 'real_running_time': 216}], [1, {'fees': [{'asset_id': '1.3.1', 'amount': 10000}], 'real_running_time': 36}]], 'extensions': [], 'ref_block_num': 59057, 'operations': [[0, {'to': '1.2.5', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}, 'from': '1.2.16', 'extensions': []}], [35, {'caller': '1.2.16', 'value_list': [], 'contract_id': '1.16.121', 'extensions': [], 'function_name': 'test_helloworld'}], [35, {'caller': '1.2.6', 'value_list': [], 'contract_id': '1.16.121', 'extensions': [], 'function_name': 'test_helloworld'}], [0, {'to': '1.2.6', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}, 'from': '1.2.16', 'extensions': []}]]}]], 'witness_signature': '207fcc6450dc99c8b15fa2ea63d6b89619ec07ff48f8c6bc499881d1094ba8cced699a691a80aa174906bcea090715791c253c6f433814b6f2a4cd030baa390a54', 'witness': '1.6.3', 'transaction_merkle_root': '01028c82a6a3045c26981d856073c93d37d234a3'}}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['c1016237f089108830f48007a7cd5d4c083001aaccefe42424c098877f5987e7', {'expiration': '2020-07-10T02:39:42', 'signatures': ['1f11b0cc87870d0a063ca2cdec878c86a2c4d4cf02314da4eab7f050ad3e82c7a5681cedd15ce563db5ba3d123b3eaba22e6726b8514593e9501862b81ccae46b8'], 'ref_block_prefix': 387154614, 'extensions': [], 'ref_block_num': 59057, 'operations': [[35, {'caller': '1.2.16', 'value_list': [], 'contract_id': '1.16.121', 'extensions': [], 'function_name': 'test_helloworld'}]]}]}

>> get_transaction_in_block_info ['c1016237f089108830f48007a7cd5d4c083001aaccefe42424c098877f5987e7']
{'jsonrpc': '2.0', 'id': 1, 'result': {'trx_hash': 'c1016237f089108830f48007a7cd5d4c083001aaccefe42424c098877f5987e7', 'block_num': 7464636, 'id': '3.1.824860', 'trx_in_block': 0}}

>> get_transaction_in_block_info c1016237f089108830f48007a7cd5d4c083001aaccefe42424c098877f5987e7
 {'trx_hash': 'c1016237f089108830f48007a7cd5d4c083001aaccefe42424c098877f5987e7', 'block_num': 7464636, 'id': '3.1.824860', 'trx_in_block': 0}

>> get_block [7464636]
{'jsonrpc': '2.0', 'id': 1, 'result': {'timestamp': '2020-07-10T02:19:14', 'block_id': '0071e6bc7929807051a708a25f39009d20b3e5a1', 'previous': '0071e6bba9b08edc0f9d2c853b2ce75356fdeb32', 'transactions': [['c1016237f089108830f48007a7cd5d4c083001aaccefe42424c098877f5987e7', {'expiration': '2020-07-10T02:39:42', 'signatures': ['1f11b0cc87870d0a063ca2cdec878c86a2c4d4cf02314da4eab7f050ad3e82c7a5681cedd15ce563db5ba3d123b3eaba22e6726b8514593e9501862b81ccae46b8'], 'ref_block_prefix': 387154614, 'operation_results': [[4, {'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'Hi, Cocos-BCX contract'}], [5, {'affected_account': '1.2.16', 'fees': [{'asset_id': '1.3.0', 'amount': 20823}], 'message': '100%'}]], 'process_value': '', 'contract_id': '1.16.121', 'relevant_datasize': 35, 'fees': [{'asset_id': '1.3.0', 'amount': 20823}], 'existed_pv': False, 'real_running_time': 307}]], 'extensions': [], 'ref_block_num': 59057, 'operations': [[35, {'caller': '1.2.16', 'value_list': [], 'contract_id': '1.16.121', 'extensions': [], 'function_name': 'test_helloworld'}]]}]], 'witness_signature': '1f79df8a740a0798d500ec2135e6fbe1914cc2b11f58e71dfa81a2eae0741e7c60265ec29f8ca2011e76fd65c4d500bf47d89c163d93b58f63c24e07b6cbe722e6', 'witness': '1.6.6', 'transaction_merkle_root': 'd009898108d78c3b5cc68f10b9f80a0214bfe8bb'}}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['b9d79accbfd4ec21c9da74fa2d6c7f506521ed05d139fc06e4614224e8fab28f', {'expiration': '2020-07-10T02:39:44', 'signatures': ['2060d7ba5493143a3d27643bef9d77d3863888aed07ed255615bd9f589ece655295b38bd05e38d266ece4c1b035ccd32224ce5c89229bfe442cb15065c7ce3cefa'], 'ref_block_prefix': 2593921570, 'extensions': [], 'ref_block_num': 59058, 'operations': [[35, {'caller': '1.2.6', 'value_list': [], 'contract_id': '1.16.121', 'extensions': [], 'function_name': 'test_helloworld'}]]}]}

>> get_transaction_in_block_info ['b9d79accbfd4ec21c9da74fa2d6c7f506521ed05d139fc06e4614224e8fab28f']
{'jsonrpc': '2.0', 'id': 1, 'result': {'trx_hash': 'b9d79accbfd4ec21c9da74fa2d6c7f506521ed05d139fc06e4614224e8fab28f', 'block_num': 7464637, 'id': '3.1.824861', 'trx_in_block': 0}}

>> get_transaction_in_block_info b9d79accbfd4ec21c9da74fa2d6c7f506521ed05d139fc06e4614224e8fab28f
 {'trx_hash': 'b9d79accbfd4ec21c9da74fa2d6c7f506521ed05d139fc06e4614224e8fab28f', 'block_num': 7464637, 'id': '3.1.824861', 'trx_in_block': 0}

>> get_block [7464637]
{'jsonrpc': '2.0', 'id': 1, 'result': {'timestamp': '2020-07-10T02:19:16', 'block_id': '0071e6bd3f28b3635082c92d5fffa47896ba46a6', 'previous': '0071e6bc7929807051a708a25f39009d20b3e5a1', 'transactions': [['b9d79accbfd4ec21c9da74fa2d6c7f506521ed05d139fc06e4614224e8fab28f', {'expiration': '2020-07-10T02:39:44', 'signatures': ['2060d7ba5493143a3d27643bef9d77d3863888aed07ed255615bd9f589ece655295b38bd05e38d266ece4c1b035ccd32224ce5c89229bfe442cb15065c7ce3cefa'], 'ref_block_prefix': 2593921570, 'operation_results': [[4, {'contract_affecteds': [[3, {'affected_account': '1.2.6', 'message': 'Hi, Cocos-BCX contract'}], [5, {'affected_account': '1.2.6', 'fees': [{'asset_id': '1.3.0', 'amount': 6288}], 'message': '30%'}], [5, {'affected_account': '1.2.16', 'fees': [{'asset_id': '1.3.0', 'amount': 14671}], 'message': '70%'}]], 'process_value': '', 'contract_id': '1.16.121', 'relevant_datasize': 35, 'fees': [{'asset_id': '1.3.0', 'amount': 20959}], 'existed_pv': False, 'real_running_time': 443}]], 'extensions': [], 'ref_block_num': 59058, 'operations': [[35, {'caller': '1.2.6', 'value_list': [], 'contract_id': '1.16.121', 'extensions': [], 'function_name': 'test_helloworld'}]]}]], 'witness_signature': '1f5503cb125ecfa4be62809943ce28ccbf5983b8c42d097a12444219fafd0bc35f7b1d4b67ce08b6b6c855b7507568258948295cc7a45dab7cd9d269a4fb3480c0', 'witness': '1.6.4', 'transaction_merkle_root': '6273743f85fc47b6cbe551e40e62bddd63ac2ad4'}}

ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```  
合约调用成功，合约调用费用在block中有记录。比如：  
``` text  
  "operation_results": [[
      4,{
        "fees": [{
            "amount": 20959,
            "asset_id": "1.3.0"
          }
        ],
        "contract_id": "1.16.121",
        "contract_affecteds": [[
            3,{
              "affected_account": "1.2.6",
              "message": "Hi, Cocos-BCX contract"
            }
          ],[
            5,{
              "fees": [{
                  "amount": 6288,
                  "asset_id": "1.3.0"
                }
              ],
              "affected_account": "1.2.6",
              "message": "30%"
            }
          ],[
            5,{
              "fees": [{
                  "amount": 14671,
                  "asset_id": "1.3.0"
                }
              ],
              "affected_account": "1.2.16",
              "message": "70%"
            }
          ]
        ],
        "real_running_time": 443,
        "existed_pv": false,
        "process_value": "",
        "relevant_datasize": 35
      }
    ]
  ]
```

## 3.3 设置百分比为0  
**设置过程和结果：**  
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 contract_call_fee.py 
>> unlock ['123456']
{'id': 1, 'jsonrpc': '2.0', 'result': None}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_set_percent', [[1, {'v': 0}]], True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['eb66f710924bc09a459a30788af58a1d6c130f19351c9f7525e098fa1288e18e', {'ref_block_num': 3542, 'operations': [[35, {'extensions': [], 'value_list': [[1, {'v': '0.00000000000000000'}]], 'caller': '1.2.16', 'function_name': 'test_set_percent', 'contract_id': '1.16.121'}]], 'signatures': ['1f221466444c24242b8d4dd0cea6fde83ab6297395a8d8daf16bf87588b3631ae2479fd95d6fa9f72b5773529bedf6c41f89c6496671247ae87ded170b302a2838'], 'extensions': [], 'expiration': '2020-07-10T09:27:02', 'ref_block_prefix': 2995161666}]}

>> get_transaction_in_block_info ['eb66f710924bc09a459a30788af58a1d6c130f19351c9f7525e098fa1288e18e']
{'id': 1, 'jsonrpc': '2.0', 'result': {'id': '3.1.824879', 'block_num': 7474656, 'trx_hash': 'eb66f710924bc09a459a30788af58a1d6c130f19351c9f7525e098fa1288e18e', 'trx_in_block': 0}}

>> get_transaction_in_block_info eb66f710924bc09a459a30788af58a1d6c130f19351c9f7525e098fa1288e18e
 {'id': '3.1.824879', 'block_num': 7474656, 'trx_hash': 'eb66f710924bc09a459a30788af58a1d6c130f19351c9f7525e098fa1288e18e', 'trx_in_block': 0}

>> get_block [7474656]
{'id': 1, 'jsonrpc': '2.0', 'result': {'timestamp': '2020-07-10T09:06:34', 'witness_signature': '202765cfc2eaec37e84598a5ad066fea3cc11875a462a4fe6b683a5e01ddefe03f54c32680bb202b6a26186c48c4323438b24e520f43835d008c434c346ffbab50', 'previous': '00720ddfbcbbdc5f96eb4928e87f59c63bb68df0', 'block_id': '00720de0f88dae248a2757c0d478b19d3c44d735', 'transactions': [['eb66f710924bc09a459a30788af58a1d6c130f19351c9f7525e098fa1288e18e', {'ref_block_num': 3542, 'operations': [[35, {'extensions': [], 'value_list': [[1, {'v': '0.00000000000000000'}]], 'caller': '1.2.16', 'function_name': 'test_set_percent', 'contract_id': '1.16.121'}]], 'signatures': ['1f221466444c24242b8d4dd0cea6fde83ab6297395a8d8daf16bf87588b3631ae2479fd95d6fa9f72b5773529bedf6c41f89c6496671247ae87ded170b302a2838'], 'extensions': [], 'expiration': '2020-07-10T09:27:02', 'operation_results': [[4, {'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'set_invoke_share_percent'}], [5, {'affected_account': '1.2.16', 'message': '100%', 'fees': [{'asset_id': '1.3.0', 'amount': 21074}]}]], 'contract_id': '1.16.121', 'real_running_time': 440, 'process_value': '', 'relevant_datasize': 37, 'existed_pv': False, 'fees': [{'asset_id': '1.3.0', 'amount': 21074}]}]], 'ref_block_prefix': 2995161666}]], 'witness': '1.6.8', 'transaction_merkle_root': '1273b20a3ba72d3d5fc582e4391228f83686438e'}}
```  

**通过cli_wallet查看结果：**  
``` text  
locked >>> get_object 1.16.121
get_object 1.16.121
[{
    "id": "1.16.121",
    "creation_date": "2020-07-09T03:22:16",
    "owner": "1.2.16",
    "name": "contract.testapi.contractfeeshare",
    "user_invoke_share_percent": 0,
    "current_version": "7feed5235f0e1338d33775109673e80aa6d27618f6f4e1d460e64ad6cdb206a1",
    "contract_authority": "COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx",
    "is_release": false,
    "check_contract_authority": false,
    "contract_data": [],
    "contract_ABI": [[{
          "key": [
            2,{
              "v": "test_contract_fee_share"
            }
          ]
        },[
          5,{
            "is_var_arg": false,
            "arglist": []
          }
        ]
      ],[{
          "key": [
            2,{
              "v": "test_helloworld"
            }
          ]
        },[
          5,{
            "is_var_arg": false,
            "arglist": []
          }
        ]
      ],[{
          "key": [
            2,{
              "v": "test_set_percent"
            }
          ]
        },[
          5,{
            "is_var_arg": false,
            "arglist": [
              "percent"
            ]
          }
        ]
      ]
    ],
    "lua_code_b_id": "2.2.121"
  }
]

locked >>> 
```  
显示以及设置成功  

**合约调用过程和结果测试：**  
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 builder_tx.py 
>> unlock ['123456']
{'result': None, 'jsonrpc': '2.0', 'id': 1}

>> begin_builder_transaction []
{'result': 0, 'jsonrpc': '2.0', 'id': 1}

>> transfer ['nicotest', 'init0', 23, 'COCOS', ['', False], False]
{'result': ['5b9c3ff95111dc0dc0582d6a6a41c9e0bccbd8583e0e815d86033d9d94626442', {'expiration': '2020-07-10T09:35:24', 'operations': [[0, {'from': '1.2.16', 'amount': {'amount': 2300000, 'asset_id': '1.3.0'}, 'to': '1.2.5', 'extensions': []}]], 'signatures': ['201d8696b28821ce754521c97794704a01dcb0e644b2e2a83a9a1ae71cdefa27f97aee19529cc43ef9607d8c1b3741766d786387999ee70083dd91a1b7cfa34e4b'], 'ref_block_prefix': 796512999, 'ref_block_num': 3748, 'extensions': []}], 'jsonrpc': '2.0', 'id': 1}

>> add_operation_to_builder_transaction [0, [0, {'from': '1.2.16', 'amount': {'amount': 2300000, 'asset_id': '1.3.0'}, 'to': '1.2.5', 'extensions': []}]]
{'result': None, 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], False]
{'result': ['da51a4c5fc0de843c06f2a395dc9d80321e153aa02b68cc28aa7fc0c792b8b36', {'expiration': '2020-07-10T09:35:24', 'operations': [[35, {'extensions': [], 'value_list': [], 'contract_id': '1.16.121', 'caller': '1.2.16', 'function_name': 'test_helloworld'}]], 'signatures': ['200856c9639b6118a1228491e1b2cd3883cff16ef2a77174f049595f314b899e485e45e2f7bcdd8d5312561bf723fe8fc2a3d1704c3a745f0fe60f74ce4e143236'], 'ref_block_prefix': 796512999, 'ref_block_num': 3748, 'extensions': []}], 'jsonrpc': '2.0', 'id': 1}

>> add_operation_to_builder_transaction [0, [35, {'extensions': [], 'value_list': [], 'contract_id': '1.16.121', 'caller': '1.2.16', 'function_name': 'test_helloworld'}]]
{'result': None, 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], False]
{'result': ['2c76368384dcb6cb9033fb684ac42929aa61f46ea570b784db39e1d6d0048063', {'expiration': '2020-07-10T09:35:24', 'operations': [[35, {'extensions': [], 'value_list': [], 'contract_id': '1.16.121', 'caller': '1.2.6', 'function_name': 'test_helloworld'}]], 'signatures': ['2075413ee78f367e1e22176f93b80635c96a45c59553ccb97c75c0c075189d1bd1748e230b51c863e87cbcab31fcaa13c728fb2fd45cbd5c3adc78208f352be2e0'], 'ref_block_prefix': 796512999, 'ref_block_num': 3748, 'extensions': []}], 'jsonrpc': '2.0', 'id': 1}

>> add_operation_to_builder_transaction [0, [35, {'extensions': [], 'value_list': [], 'contract_id': '1.16.121', 'caller': '1.2.6', 'function_name': 'test_helloworld'}]]
{'result': None, 'jsonrpc': '2.0', 'id': 1}

>> transfer ['nicotest', 'init1', 78, 'COCOS', ['', False], False]
{'result': ['a650eebd93a15f5e5ab4c0f83ee10e7270307155892870e69afd355d7a586dd0', {'expiration': '2020-07-10T09:35:24', 'operations': [[0, {'from': '1.2.16', 'amount': {'amount': 7800000, 'asset_id': '1.3.0'}, 'to': '1.2.6', 'extensions': []}]], 'signatures': ['200fdc05be909e558245b1cfd13560e624e2487e361c45c49e2749e855db4a23961ccf7f8e2022043e7f9325e9ae578942a3ee47d464d63017006e2b5deade02db'], 'ref_block_prefix': 796512999, 'ref_block_num': 3748, 'extensions': []}], 'jsonrpc': '2.0', 'id': 1}

>> add_operation_to_builder_transaction [0, [0, {'from': '1.2.16', 'amount': {'amount': 7800000, 'asset_id': '1.3.0'}, 'to': '1.2.6', 'extensions': []}]]
{'result': None, 'jsonrpc': '2.0', 'id': 1}

>> preview_builder_transaction [0]
{'result': {'expiration': '1970-01-01T00:00:00', 'operations': [[0, {'from': '1.2.16', 'amount': {'amount': 2300000, 'asset_id': '1.3.0'}, 'to': '1.2.5', 'extensions': []}], [35, {'extensions': [], 'value_list': [], 'contract_id': '1.16.121', 'caller': '1.2.16', 'function_name': 'test_helloworld'}], [35, {'extensions': [], 'value_list': [], 'contract_id': '1.16.121', 'caller': '1.2.6', 'function_name': 'test_helloworld'}], [0, {'from': '1.2.16', 'amount': {'amount': 7800000, 'asset_id': '1.3.0'}, 'to': '1.2.6', 'extensions': []}]], 'ref_block_num': 0, 'ref_block_prefix': 0, 'extensions': []}, 'jsonrpc': '2.0', 'id': 1}

>> sign_builder_transaction [0, True]
{'result': ['110d018853472fb3be8067a4d81237e3aa1bd230a444125838af932f2ebb17bc', {'expiration': '2020-07-10T09:35:24', 'operations': [[0, {'from': '1.2.16', 'amount': {'amount': 2300000, 'asset_id': '1.3.0'}, 'to': '1.2.5', 'extensions': []}], [35, {'extensions': [], 'value_list': [], 'contract_id': '1.16.121', 'caller': '1.2.16', 'function_name': 'test_helloworld'}], [35, {'extensions': [], 'value_list': [], 'contract_id': '1.16.121', 'caller': '1.2.6', 'function_name': 'test_helloworld'}], [0, {'from': '1.2.16', 'amount': {'amount': 7800000, 'asset_id': '1.3.0'}, 'to': '1.2.6', 'extensions': []}]], 'signatures': ['1f7eaacc5f7fe224e6e09a7827c770c6408a021d778aba0ec6dfc3699feed0682d1314f9a46e3fed88c02f48c2691fe3d556793f8bc0889929e546b26e993c40e9', '1f6fc31b8fddac78357a84c38763db2201f1f05a1e17175ff52d831d98c73ec90718f042c582c84be6e23d784f7780ad9536276ea55bd09cadce9487b19559b278'], 'ref_block_prefix': 796512999, 'ref_block_num': 3748, 'extensions': []}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['110d018853472fb3be8067a4d81237e3aa1bd230a444125838af932f2ebb17bc']
{'result': {'trx_hash': '110d018853472fb3be8067a4d81237e3aa1bd230a444125838af932f2ebb17bc', 'block_num': 7474861, 'id': '3.1.824880', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info 110d018853472fb3be8067a4d81237e3aa1bd230a444125838af932f2ebb17bc
 {'trx_hash': '110d018853472fb3be8067a4d81237e3aa1bd230a444125838af932f2ebb17bc', 'block_num': 7474861, 'id': '3.1.824880', 'trx_in_block': 0}

>> get_block [7474861]
{'result': {'previous': '00720eacbb0293c9af9256339bc4bdfdfff42324', 'block_id': '00720eade563035407ed07b0eaf945b18fa62226', 'transaction_merkle_root': 'aaa399ad0dd5777c4734eabd76bf538d0970e8e3', 'witness': '1.6.5', 'witness_signature': '1f5332d771a5b3982226d5566d573efc5d87916f72f4a70f92ced787d0d9a75b8b10697a8b8e145e255d2cc72852e007b09226e2b4d1a4fe752509610deef2f920', 'transactions': [['110d018853472fb3be8067a4d81237e3aa1bd230a444125838af932f2ebb17bc', {'expiration': '2020-07-10T09:35:24', 'operations': [[0, {'from': '1.2.16', 'amount': {'amount': 2300000, 'asset_id': '1.3.0'}, 'to': '1.2.5', 'extensions': []}], [35, {'extensions': [], 'value_list': [], 'contract_id': '1.16.121', 'caller': '1.2.16', 'function_name': 'test_helloworld'}], [35, {'extensions': [], 'value_list': [], 'contract_id': '1.16.121', 'caller': '1.2.6', 'function_name': 'test_helloworld'}], [0, {'from': '1.2.16', 'amount': {'amount': 7800000, 'asset_id': '1.3.0'}, 'to': '1.2.6', 'extensions': []}]], 'signatures': ['1f7eaacc5f7fe224e6e09a7827c770c6408a021d778aba0ec6dfc3699feed0682d1314f9a46e3fed88c02f48c2691fe3d556793f8bc0889929e546b26e993c40e9', '1f6fc31b8fddac78357a84c38763db2201f1f05a1e17175ff52d831d98c73ec90718f042c582c84be6e23d784f7780ad9536276ea55bd09cadce9487b19559b278'], 'operation_results': [[1, {'real_running_time': 81, 'fees': [{'amount': 10000, 'asset_id': '1.3.0'}]}], [4, {'real_running_time': 349, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20865, 'asset_id': '1.3.0'}]}]], 'contract_id': '1.16.121', 'relevant_datasize': 35, 'existed_pv': False, 'fees': [{'amount': 20865, 'asset_id': '1.3.0'}], 'process_value': ''}], [4, {'real_running_time': 315, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}], [5, {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20831, 'asset_id': '1.3.0'}]}]], 'contract_id': '1.16.121', 'relevant_datasize': 35, 'existed_pv': False, 'fees': [{'amount': 20831, 'asset_id': '1.3.0'}], 'process_value': ''}], [1, {'real_running_time': 95, 'fees': [{'amount': 10000, 'asset_id': '1.3.0'}]}]], 'ref_block_prefix': 796512999, 'ref_block_num': 3748, 'extensions': []}]], 'timestamp': '2020-07-10T09:14:58'}, 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['a60c88d179caaae529b7abb9ede524458817525a73f66dfc365acdc580561734', {'expiration': '2020-07-10T09:35:28', 'operations': [[35, {'extensions': [], 'value_list': [], 'contract_id': '1.16.121', 'caller': '1.2.16', 'function_name': 'test_helloworld'}]], 'signatures': ['1f4afb4b60adc86340e1dd4696b49b148e8ef50519951ad0de1ef0a1051ddae28f010029e74530af61025378a30e05af4ea4f845d9c90be8c0253f2fc34cd1f312'], 'ref_block_prefix': 1334964234, 'ref_block_num': 3749, 'extensions': []}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['a60c88d179caaae529b7abb9ede524458817525a73f66dfc365acdc580561734']
{'result': {'trx_hash': 'a60c88d179caaae529b7abb9ede524458817525a73f66dfc365acdc580561734', 'block_num': 7474862, 'id': '3.1.824881', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info a60c88d179caaae529b7abb9ede524458817525a73f66dfc365acdc580561734
 {'trx_hash': 'a60c88d179caaae529b7abb9ede524458817525a73f66dfc365acdc580561734', 'block_num': 7474862, 'id': '3.1.824881', 'trx_in_block': 0}

>> get_block [7474862]
{'result': {'previous': '00720eade563035407ed07b0eaf945b18fa62226', 'block_id': '00720eaeec30903527c255b54f717071e8b0ecca', 'transaction_merkle_root': 'a13856f55129f8226691a86c33e04ebe384b781c', 'witness': '1.6.7', 'witness_signature': '20096f4d2ed9a96caf2744dd175783e9ab0bb399a57d7bdd2ad3cb14494c2a2e1431711c0a2d6efff4e04b7a9e969b4f0d10fdfd5c53e27ce903bb29818ea9a7c4', 'transactions': [['a60c88d179caaae529b7abb9ede524458817525a73f66dfc365acdc580561734', {'expiration': '2020-07-10T09:35:28', 'operations': [[35, {'extensions': [], 'value_list': [], 'contract_id': '1.16.121', 'caller': '1.2.16', 'function_name': 'test_helloworld'}]], 'signatures': ['1f4afb4b60adc86340e1dd4696b49b148e8ef50519951ad0de1ef0a1051ddae28f010029e74530af61025378a30e05af4ea4f845d9c90be8c0253f2fc34cd1f312'], 'operation_results': [[4, {'real_running_time': 454, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20970, 'asset_id': '1.3.0'}]}]], 'contract_id': '1.16.121', 'relevant_datasize': 35, 'existed_pv': False, 'fees': [{'amount': 20970, 'asset_id': '1.3.0'}], 'process_value': ''}]], 'ref_block_prefix': 1334964234, 'ref_block_num': 3749, 'extensions': []}]], 'timestamp': '2020-07-10T09:15:00'}, 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['81dd604d1f7f74a5bc4c22424ded2d2757ff14a663ff3d8a6a8a9d9212c33bf6', {'expiration': '2020-07-10T09:35:30', 'operations': [[35, {'extensions': [], 'value_list': [], 'contract_id': '1.16.121', 'caller': '1.2.6', 'function_name': 'test_helloworld'}]], 'signatures': ['20703061003c0f6d12db967dea4de0f4d1fb1ae3e061c744d7f1786ee3a8271fa755ea0b36bde3b71fdba0870f5c5dc504d7af88f658fb98277f0e559c82d7e0a3'], 'ref_block_prefix': 370746716, 'ref_block_num': 3750, 'extensions': []}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['81dd604d1f7f74a5bc4c22424ded2d2757ff14a663ff3d8a6a8a9d9212c33bf6']
{'result': {'trx_hash': '81dd604d1f7f74a5bc4c22424ded2d2757ff14a663ff3d8a6a8a9d9212c33bf6', 'block_num': 7474863, 'id': '3.1.824882', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info 81dd604d1f7f74a5bc4c22424ded2d2757ff14a663ff3d8a6a8a9d9212c33bf6
 {'trx_hash': '81dd604d1f7f74a5bc4c22424ded2d2757ff14a663ff3d8a6a8a9d9212c33bf6', 'block_num': 7474863, 'id': '3.1.824882', 'trx_in_block': 0}

>> get_block [7474863]
{'result': {'previous': '00720eaeec30903527c255b54f717071e8b0ecca', 'block_id': '00720eaf6d72a3b0a200ef44b514615ed596fafa', 'transaction_merkle_root': 'd7af9926d550966a917cfd4fb28c4d20c383c2b2', 'witness': '1.6.2', 'witness_signature': '1f2f153e32e2c31aa856a6cc84695dde089e205176b3805251a96436d144168d1705734199c55bb0f3515443d7bb8d8585a967e340cd5b26013092731894226636', 'transactions': [['81dd604d1f7f74a5bc4c22424ded2d2757ff14a663ff3d8a6a8a9d9212c33bf6', {'expiration': '2020-07-10T09:35:30', 'operations': [[35, {'extensions': [], 'value_list': [], 'contract_id': '1.16.121', 'caller': '1.2.6', 'function_name': 'test_helloworld'}]], 'signatures': ['20703061003c0f6d12db967dea4de0f4d1fb1ae3e061c744d7f1786ee3a8271fa755ea0b36bde3b71fdba0870f5c5dc504d7af88f658fb98277f0e559c82d7e0a3'], 'operation_results': [[4, {'real_running_time': 354, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}], [5, {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20870, 'asset_id': '1.3.0'}]}]], 'contract_id': '1.16.121', 'relevant_datasize': 35, 'existed_pv': False, 'fees': [{'amount': 20870, 'asset_id': '1.3.0'}], 'process_value': ''}]], 'ref_block_prefix': 370746716, 'ref_block_num': 3750, 'extensions': []}]], 'timestamp': '2020-07-10T09:15:02'}, 'jsonrpc': '2.0', 'id': 1}

ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```  
合约验证功能均测试成功    

---------------------
# 4. 合约费用计算测试  
**只对硬分叉后的合约调用费用进行计算**  

[测试代码](https://github.com/gkany/CocosBCX/blob/master/feature_test/contract_fee_share/contract_call_fee.py)  

## 4.1 合约费用分摊比例100%  
**设置分摊比例为100，也即合约调用费用完全从调用者扣除**  
**设置过程和结果如下：**  
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 contract_call_fee.py 
>> unlock ['123456']
{'id': 1, 'jsonrpc': '2.0', 'result': None}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_set_percent', [[1, {'v': 100}]], True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['aeafa7952b7f55803bdae5bde151073e9e3fb1f8da5708a6f0ee01dffd1efd8e', {'ref_block_num': 5919, 'ref_block_prefix': 1182087351, 'operations': [[35, {'contract_id': '1.16.121', 'extensions': [], 'caller': '1.2.16', 'value_list': [[1, {'v': '100.00000000000000000'}]], 'function_name': 'test_set_percent'}]], 'signatures': ['1f36564a8f48248e1c7c3ca4280feb04f71743cc7550bc55b37e10305a82d95cb4414a2938bd2b1a57efdb1ecfbae76898ffa27fa4903f6229a453d6d89e187e65'], 'expiration': '2020-07-10T11:03:56', 'extensions': []}]}

>> get_transaction_in_block_info ['aeafa7952b7f55803bdae5bde151073e9e3fb1f8da5708a6f0ee01dffd1efd8e']
{'id': 1, 'jsonrpc': '2.0', 'result': None}

>> get_transaction_in_block_info aeafa7952b7f55803bdae5bde151073e9e3fb1f8da5708a6f0ee01dffd1efd8e
 None

>> get_transaction_in_block_info ['aeafa7952b7f55803bdae5bde151073e9e3fb1f8da5708a6f0ee01dffd1efd8e']
{'id': 1, 'jsonrpc': '2.0', 'result': {'id': '3.1.824902', 'block_num': 7477034, 'trx_hash': 'aeafa7952b7f55803bdae5bde151073e9e3fb1f8da5708a6f0ee01dffd1efd8e', 'trx_in_block': 0}}

>> get_transaction_in_block_info aeafa7952b7f55803bdae5bde151073e9e3fb1f8da5708a6f0ee01dffd1efd8e
 {'id': '3.1.824902', 'block_num': 7477034, 'trx_hash': 'aeafa7952b7f55803bdae5bde151073e9e3fb1f8da5708a6f0ee01dffd1efd8e', 'trx_in_block': 0}

>> get_block [7477034]
{'id': 1, 'jsonrpc': '2.0', 'result': {'previous': '00721729debc7bbb6c139af7624e547e3d0b86a6', 'witness': '1.6.1', 'timestamp': '2020-07-10T10:43:30', 'transactions': [['aeafa7952b7f55803bdae5bde151073e9e3fb1f8da5708a6f0ee01dffd1efd8e', {'ref_block_num': 5919, 'ref_block_prefix': 1182087351, 'operations': [[35, {'contract_id': '1.16.121', 'extensions': [], 'caller': '1.2.16', 'value_list': [[1, {'v': '100.00000000000000000'}]], 'function_name': 'test_set_percent'}]], 'operation_results': [[4, {'contract_id': '1.16.121', 'real_running_time': 410, 'process_value': '', 'existed_pv': False, 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'set_invoke_share_percent'}], [5, {'affected_account': '1.2.16', 'fees': [{'asset_id': '1.3.0', 'amount': 21044}], 'message': '100%'}]], 'relevant_datasize': 37, 'fees': [{'asset_id': '1.3.0', 'amount': 21044}]}]], 'signatures': ['1f36564a8f48248e1c7c3ca4280feb04f71743cc7550bc55b37e10305a82d95cb4414a2938bd2b1a57efdb1ecfbae76898ffa27fa4903f6229a453d6d89e187e65'], 'expiration': '2020-07-10T11:03:56', 'extensions': []}]], 'transaction_merkle_root': '08cbbca6c02c7a3519e253e447d10afe36559018', 'witness_signature': '207a6a4125acaa95396a78f14d37b6354e48ab17731de1bcc648f09787cd2efb8b538752f252de9da3610753ea06efe208683bb28890c30a21bdecaa38499bdd05', 'block_id': '0072172ab048d44671093ef6e752f2c9e6f5e1ff'}}

ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```  

**cli_wallet再次查看合约百分比设置结果**  
``` text  
unlocked >>> 
get_object 1.16.121
unlocked >>> get_object 1.16.121
[{
    "id": "1.16.121",
    "creation_date": "2020-07-09T03:22:16",
    "owner": "1.2.16",
    "name": "contract.testapi.contractfeeshare",
    "user_invoke_share_percent": 100,
    "current_version": "7feed5235f0e1338d33775109673e80aa6d27618f6f4e1d460e64ad6cdb206a1",
    "contract_authority": "COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx",
    "is_release": false,
    "check_contract_authority": false,
    "contract_data": [],
    "contract_ABI": [[{
          "key": [
            2,{
              "v": "test_contract_fee_share"
            }
          ]
        },[
          5,{
            "is_var_arg": false,
            "arglist": []
          }
        ]
      ],[{
          "key": [
            2,{
              "v": "test_helloworld"
            }
          ]
        },[
          5,{
            "is_var_arg": false,
            "arglist": []
          }
        ]
      ],[{
          "key": [
            2,{
              "v": "test_set_percent"
            }
          ]
        },[
          5,{
            "is_var_arg": false,
            "arglist": [
              "percent"
            ]
          }
        ]
      ]
    ],
    "lua_code_b_id": "2.2.121"
  }
]

unlocked >>> 
```  
> "user_invoke_share_percent": 100, 已设置成功  


### 4.1.1 合约所有者调用  
#### 4.1.1.1 只有COCOS，无GAS测试  
**a. COCOS充足**  
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 contract_call_fee.py 
>> unlock ['123456']
{'id': 1, 'result': None, 'jsonrpc': '2.0'}

>> list_account_balances ['nicotest']
{'id': 1, 'result': [{'amount': '2999999959850201', 'asset_id': '1.3.0'}, {'amount': -5316016, 'asset_id': '1.3.1'}], 'jsonrpc': '2.0'}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'id': 1, 'result': ['5efe4e4e92005057ef86bd51f6169e51911d3b4408517f3cbaabaeab713a2b6c', {'extensions': [], 'signatures': ['20148da20de724a154c24b770d7de09173a90233b8a19d9bb5290c6930c441b27a3b5b12c99f0df31a0e0ca9284b4e3408163c3279de1c58fa0606a92deabe1935'], 'expiration': '2020-07-10T11:31:28', 'ref_block_num': 6600, 'ref_block_prefix': 4293013357, 'operations': [[35, {'function_name': 'test_helloworld', 'extensions': [], 'value_list': [], 'caller': '1.2.16', 'contract_id': '1.16.121'}]]}], 'jsonrpc': '2.0'}

>> get_transaction_in_block_info ['5efe4e4e92005057ef86bd51f6169e51911d3b4408517f3cbaabaeab713a2b6c']
{'id': 1, 'result': None, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info 5efe4e4e92005057ef86bd51f6169e51911d3b4408517f3cbaabaeab713a2b6c
 None

>> get_transaction_in_block_info ['5efe4e4e92005057ef86bd51f6169e51911d3b4408517f3cbaabaeab713a2b6c']
{'id': 1, 'result': {'id': '3.1.824916', 'trx_hash': '5efe4e4e92005057ef86bd51f6169e51911d3b4408517f3cbaabaeab713a2b6c', 'block_num': 7477714, 'trx_in_block': 0}, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info 5efe4e4e92005057ef86bd51f6169e51911d3b4408517f3cbaabaeab713a2b6c
 {'id': '3.1.824916', 'trx_hash': '5efe4e4e92005057ef86bd51f6169e51911d3b4408517f3cbaabaeab713a2b6c', 'block_num': 7477714, 'trx_in_block': 0}

>> get_block [7477714]
{'id': 1, 'result': {'timestamp': '2020-07-10T11:11:02', 'previous': '007219d15554fa72b807840d1ec21dee795d6459', 'transactions': [['5efe4e4e92005057ef86bd51f6169e51911d3b4408517f3cbaabaeab713a2b6c', {'extensions': [], 'operation_results': [[4, {'relevant_datasize': 35, 'existed_pv': False, 'real_running_time': 522, 'fees': [{'amount': 21038, 'asset_id': '1.3.0'}], 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'Hi, Cocos-BCX contract'}], [5, {'fees': [{'amount': 21038, 'asset_id': '1.3.0'}], 'affected_account': '1.2.16', 'message': '100%'}]], 'process_value': '', 'contract_id': '1.16.121'}]], 'signatures': ['20148da20de724a154c24b770d7de09173a90233b8a19d9bb5290c6930c441b27a3b5b12c99f0df31a0e0ca9284b4e3408163c3279de1c58fa0606a92deabe1935'], 'expiration': '2020-07-10T11:31:28', 'ref_block_num': 6600, 'ref_block_prefix': 4293013357, 'operations': [[35, {'function_name': 'test_helloworld', 'extensions': [], 'value_list': [], 'caller': '1.2.16', 'contract_id': '1.16.121'}]]}]], 'witness_signature': '20497fb8044ba8a78a7a5c89e10f5e818a140983037131a535096f2b74e4b9bbaa5780eaf1eb3b30557605f51802eb6d0ea8d9d4a34eb80f99afa5d37fba54a2b7', 'witness': '1.6.1', 'transaction_merkle_root': 'b9001b1f938768c869209e4522a8a2b076368c92', 'block_id': '007219d2786395e8f5fe47b6489349f28c7a91d5'}, 'jsonrpc': '2.0'}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 21038, 'asset_id': '1.3.0'}]
### {'fees': [{'amount': 21038, 'asset_id': '1.3.0'}], 'affected_account': '1.2.16', 'message': '100%'}
-----------------------------------------------------------------------
>> list_account_balances ['nicotest']
{'id': 1, 'result': [{'amount': '2999999959829163', 'asset_id': '1.3.0'}, {'amount': -5316016, 'asset_id': '1.3.1'}], 'jsonrpc': '2.0'}

op before balances: {'nicotest': [{'amount': '2999999959850201', 'asset_id': '1.3.0'}, {'amount': -5316016, 'asset_id': '1.3.1'}]}
op after  balances: {'nicotest': [{'amount': '2999999959829163', 'asset_id': '1.3.0'}, {'amount': -5316016, 'asset_id': '1.3.1'}]}
balances delta: {'nicotest': {'1.3.0': 21038, '1.3.1': 0}}
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```  

**b. COCOS不足**  

#### 4.1.1.2 有GAS测试  
**a. GAS充足**
**测试过程和结果：**  
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 contract_call_fee.py 
>> unlock ['123456']
{'jsonrpc': '2.0', 'result': None, 'id': 1}

>> list_account_balances ['nicotest']
{'jsonrpc': '2.0', 'result': [{'amount': '3000000002495945', 'asset_id': '1.3.0'}, {'amount': '413593220945477', 'asset_id': '1.3.1'}], 'id': 1}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'jsonrpc': '2.0', 'result': ['86f06d5668c84d073c0f65115552586689d41bbc0a6d8cdf54771e9364e9eac9', {'signatures': ['1f1a051072d8b40c2012aa09f9d5788694db6aad7a3db57419ccb6ae875be00f601422a64cb0c5814ff28cd53192e64c52d8955626e4e3a5a7706e00fc886606e9'], 'extensions': [], 'ref_block_num': 6074, 'ref_block_prefix': 828116448, 'expiration': '2020-07-10T11:10:18', 'operations': [[35, {'extensions': [], 'contract_id': '1.16.121', 'value_list': [], 'caller': '1.2.16', 'function_name': 'test_helloworld'}]]}], 'id': 1}

>> get_transaction_in_block_info ['86f06d5668c84d073c0f65115552586689d41bbc0a6d8cdf54771e9364e9eac9']
{'jsonrpc': '2.0', 'result': {'trx_hash': '86f06d5668c84d073c0f65115552586689d41bbc0a6d8cdf54771e9364e9eac9', 'trx_in_block': 0, 'block_num': 7477191, 'id': '3.1.824903'}, 'id': 1}

>> get_transaction_in_block_info 86f06d5668c84d073c0f65115552586689d41bbc0a6d8cdf54771e9364e9eac9
 {'trx_hash': '86f06d5668c84d073c0f65115552586689d41bbc0a6d8cdf54771e9364e9eac9', 'trx_in_block': 0, 'block_num': 7477191, 'id': '3.1.824903'}

>> get_block [7477191]
{'jsonrpc': '2.0', 'result': {'timestamp': '2020-07-10T10:49:50', 'block_id': '007217c7717afbd2ed2fe34838776ab67f7b162e', 'witness_signature': '204040c1a2ac987fdb31f73b1c56c766ee315b41339aa6d26302a2b7b3899d180f0689d2e58e224d6c0162b57809788a3791a6a395366e7549e129cceebf5fb8f3', 'witness': '1.6.3', 'transaction_merkle_root': '88e96279259e6649a02e2871d31b0eed9d6c5763', 'transactions': [['86f06d5668c84d073c0f65115552586689d41bbc0a6d8cdf54771e9364e9eac9', {'signatures': ['1f1a051072d8b40c2012aa09f9d5788694db6aad7a3db57419ccb6ae875be00f601422a64cb0c5814ff28cd53192e64c52d8955626e4e3a5a7706e00fc886606e9'], 'extensions': [], 'ref_block_num': 6074, 'ref_block_prefix': 828116448, 'expiration': '2020-07-10T11:10:18', 'operations': [[35, {'extensions': [], 'contract_id': '1.16.121', 'value_list': [], 'caller': '1.2.16', 'function_name': 'test_helloworld'}]], 'operation_results': [[4, {'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'fees': [{'amount': 20888, 'asset_id': '1.3.0'}], 'message': '100%', 'affected_account': '1.2.16'}]], 'process_value': '', 'relevant_datasize': 35, 'fees': [{'amount': 20888, 'asset_id': '1.3.0'}], 'contract_id': '1.16.121', 'existed_pv': False, 'real_running_time': 372}]]}]], 'previous': '007217c6c9acd35bea00ec53fd9ae674c9976707'}, 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 20888, 'asset_id': '1.3.0'}]
### {'fees': [{'amount': 20888, 'asset_id': '1.3.0'}], 'message': '100%', 'affected_account': '1.2.16'}
-----------------------------------------------------------------------
>> list_account_balances ['nicotest']
{'jsonrpc': '2.0', 'result': [{'amount': '3000000002495945', 'asset_id': '1.3.0'}, {'amount': '413593220924589', 'asset_id': '1.3.1'}], 'id': 1}

op before balances: {'nicotest': [{'amount': '3000000002495945', 'asset_id': '1.3.0'}, {'amount': '413593220945477', 'asset_id': '1.3.1'}]}
op after  balances: {'nicotest': [{'amount': '3000000002495945', 'asset_id': '1.3.0'}, {'amount': '413593220924589', 'asset_id': '1.3.1'}]}
balances delta: {'nicotest': {'1.3.1': 20888, '1.3.0': 0}}
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```  

**b. GAS不足**
``` text  

```  


### 4.1.2 非合约所有者调用  
#### 4.1.2.1 只有COCOS，无GAS测试  
**a. COCOS充足**  

**b. COCOS不足**  

#### 4.1.2.2 有GAS测试  
**a. GAS充足**

**b. GAS不足**


## 4.2 合约费用分摊比例介于0%和100%之间  
**合约费用分摊比例：30%**  
### 4.2.1 合约所有者调用  
**测试main代码：**    
``` python  
if __name__ == '__main__':
    # print('>> {}'.format(sys.argv))
    unlock("123456")

    # main_build_tx()
    # get_contract_function_call_op_test()

    # test_helloworld(log_result=True)
    # test_helloworld(caller="init1", log_result=True)

    # test_set_percent()

    # result = list_account_balances("init1")
    # print("result: {}".format(result))

    # result = accounts_balances(["init1", "nicotest"])
    # print("balances: {}".format(result))
    # print("============================================")
    # calc_contract_call_operation_fee(test_helloworld, ["nicotest"])
    calc_contract_call_operation_fee(test_helloworld_owner, ["nicotest"])
```

#### 4.2.1.1 有GAS测试  
**a. GAS充足**  
**测试过程和结果：**
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 contract_call_fee.py 
>> unlock ['123456']
{'result': None, 'id': 1, 'jsonrpc': '2.0'}

>> list_account_balances ['nicotest']
{'result': [{'asset_id': '1.3.0', 'amount': '5596616713538030'}, {'asset_id': '1.3.1', 'amount': '14271295257'}], 'id': 1, 'jsonrpc': '2.0'}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['3f378d4b61fde082bb2c8ec1e136bdc8e88f80867b19c42708c277fcb7bad03d', {'expiration': '2020-07-10T07:53:42', 'operations': [[35, {'caller': '1.2.16', 'contract_id': '1.16.121', 'extensions': [], 'value_list': [], 'function_name': 'test_helloworld'}]], 'ref_block_num': 1252, 'signatures': ['2065d700bf500b67a53dfd156286f39cd436bf72c768c395de8c8edf696544cd1e25e45d7d78fe1c9426ea9ee3513220ab99ed03a796b1c7b091a90318e4d829d7'], 'ref_block_prefix': 3732037736, 'extensions': []}], 'id': 1, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info ['3f378d4b61fde082bb2c8ec1e136bdc8e88f80867b19c42708c277fcb7bad03d']
{'result': {'trx_in_block': 0, 'id': '3.1.824865', 'trx_hash': '3f378d4b61fde082bb2c8ec1e136bdc8e88f80867b19c42708c277fcb7bad03d', 'block_num': 7472365}, 'id': 1, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info 3f378d4b61fde082bb2c8ec1e136bdc8e88f80867b19c42708c277fcb7bad03d
 {'trx_in_block': 0, 'id': '3.1.824865', 'trx_hash': '3f378d4b61fde082bb2c8ec1e136bdc8e88f80867b19c42708c277fcb7bad03d', 'block_num': 7472365}

>> get_block [7472365]
{'result': {'timestamp': '2020-07-10T07:33:14', 'transactions': [['3f378d4b61fde082bb2c8ec1e136bdc8e88f80867b19c42708c277fcb7bad03d', {'operation_results': [[4, {'existed_pv': False, 'contract_id': '1.16.121', 'relevant_datasize': 35, 'process_value': '', 'real_running_time': 217, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'message': '100%', 'fees': [{'asset_id': '1.3.0', 'amount': 20733}], 'affected_account': '1.2.16'}]], 'fees': [{'asset_id': '1.3.0', 'amount': 20733}]}]], 'expiration': '2020-07-10T07:53:42', 'operations': [[35, {'caller': '1.2.16', 'contract_id': '1.16.121', 'extensions': [], 'value_list': [], 'function_name': 'test_helloworld'}]], 'ref_block_num': 1252, 'signatures': ['2065d700bf500b67a53dfd156286f39cd436bf72c768c395de8c8edf696544cd1e25e45d7d78fe1c9426ea9ee3513220ab99ed03a796b1c7b091a90318e4d829d7'], 'ref_block_prefix': 3732037736, 'extensions': []}]], 'witness_signature': '2076cd892f89ad8d6b98e1dfb18879d871aac36a87b8b5339f22c2cc3373dfb8322aa48dd11c56856960fddbe4ddfd084653271f09f63228ef1458038f5842f678', 'witness': '1.6.6', 'block_id': '007204ed9994b16f5d329e954407a1f22d831848', 'transaction_merkle_root': '60899b0b8f716bd28e92fe993b497979e4928c6d', 'previous': '007204ecdc5fd6317b9ac2a6ebfa6b3c5133580d'}, 'id': 1, 'jsonrpc': '2.0'}

-------------------- contract call fee result ------------------------
## total_fee: [{'asset_id': '1.3.0', 'amount': 20733}]
### {'message': '100%', 'fees': [{'asset_id': '1.3.0', 'amount': 20733}], 'affected_account': '1.2.16'}
-----------------------------------------------------------------------
>> list_account_balances ['nicotest']
{'result': [{'asset_id': '1.3.0', 'amount': '5596616713538030'}, {'asset_id': '1.3.1', 'amount': '14271274524'}], 'id': 1, 'jsonrpc': '2.0'}

op before balances: {'nicotest': [{'asset_id': '1.3.0', 'amount': '5596616713538030'}, {'asset_id': '1.3.1', 'amount': '14271295257'}]}
op after  balances: {'nicotest': [{'asset_id': '1.3.0', 'amount': '5596616713538030'}, {'asset_id': '1.3.1', 'amount': '14271274524'}]}
balances delta: {'nicotest': {'1.3.0': 0, '1.3.1': 20733}}
```  
**b. GAS不足** 
**抵押gas，使账户GAS不够一次合约调用的手续费**  
操作过程和结果如下：  
``` text  
unlocked >>> 
list_account_balances nicotest 
unlocked >>> list_account_balances nicotest 
55966124422.73030 COCOS
-108.88112 GAS

update_collateral_for_gas nicotest nicotest 15218 true
unlocked >>> update_collateral_for_gas nicotest nicotest 15218 true
[
  "a97469410f89f9d7b0c4d2dda684b6b0f8da5cfba11eccb991bda41b3846b234",{
    "ref_block_num": 2355,
    "ref_block_prefix": 3795370144,
    "expiration": "2020-07-10T08:38:36",
    "operations": [[
        54,{
          "mortgager": "1.2.16",
          "beneficiary": "1.2.16",
          "collateral": 15218
        }
      ]
    ],
    "extensions": [],
    "signatures": [
      "20053cad18f063e30a120c4750586f8dc518153e9a5e50e16cb113e8944c24325f7a54caaef5a1ee9784ce3740fc6d44122f203c5311a6ced4218805986ea4fecc"
    ]
  }
]

unlocked >>> 
list_account_balances nicotest 
unlocked >>> list_account_balances nicotest 
55966124422.63030 COCOS
-108.88204 GAS
```  

**合约调用过程和结果：**  
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 contract_call_fee.py 
>> unlock ['123456']
{'result': None, 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['nicotest']
{'result': [{'asset_id': '1.3.0', 'amount': '5596612442263030'}, {'asset_id': '1.3.1', 'amount': -10888204}], 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['4648eb7eb00bfd9384ca719e84d5f6f420428ad3959fb3820e2517257e3f8da9', {'operations': [[35, {'function_name': 'test_helloworld', 'value_list': [], 'caller': '1.2.16', 'extensions': [], 'contract_id': '1.16.121'}]], 'ref_block_prefix': 2073901621, 'signatures': ['205d4211f596d4bbf776a5619ae5bd91dfa100077ebc5bb51f6f41774bdd0e3c786abdfe68566e9a59686ccdd1c2f73e51a66bb65ae60bf400d04244f547efcaae'], 'ref_block_num': 2442, 'extensions': [], 'expiration': '2020-07-10T08:42:06'}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['4648eb7eb00bfd9384ca719e84d5f6f420428ad3959fb3820e2517257e3f8da9']
{'result': {'block_num': 7473558, 'id': '3.1.824870', 'trx_hash': '4648eb7eb00bfd9384ca719e84d5f6f420428ad3959fb3820e2517257e3f8da9', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info 4648eb7eb00bfd9384ca719e84d5f6f420428ad3959fb3820e2517257e3f8da9
 {'block_num': 7473558, 'id': '3.1.824870', 'trx_hash': '4648eb7eb00bfd9384ca719e84d5f6f420428ad3959fb3820e2517257e3f8da9', 'trx_in_block': 0}

>> get_block [7473558]
{'result': {'witness_signature': '1f3c102385fcd9d068a67312d88ee9a237350bd8c1b4a38f940c1ce8460c2f2cbf466736715ba95d18b6f39930e80b5a89e9ebaa5fb9ab231e0225bd2f9b1fe9de', 'block_id': '007209962b0e849984d892fe85fdd1a3d19bae0c', 'transaction_merkle_root': 'fdfd32d1370d95b3343a6cae2b18da447c60c32b', 'timestamp': '2020-07-10T08:21:38', 'witness': '1.6.10', 'previous': '007209951bff6ae985a0209efa561404c4771039', 'transactions': [['4648eb7eb00bfd9384ca719e84d5f6f420428ad3959fb3820e2517257e3f8da9', {'operations': [[35, {'function_name': 'test_helloworld', 'value_list': [], 'caller': '1.2.16', 'extensions': [], 'contract_id': '1.16.121'}]], 'ref_block_prefix': 2073901621, 'signatures': ['205d4211f596d4bbf776a5619ae5bd91dfa100077ebc5bb51f6f41774bdd0e3c786abdfe68566e9a59686ccdd1c2f73e51a66bb65ae60bf400d04244f547efcaae'], 'ref_block_num': 2442, 'extensions': [], 'expiration': '2020-07-10T08:42:06', 'operation_results': [[4, {'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'Hi, Cocos-BCX contract'}], [5, {'affected_account': '1.2.16', 'fees': [{'asset_id': '1.3.0', 'amount': 20971}], 'message': '100%'}]], 'relevant_datasize': 35, 'existed_pv': False, 'real_running_time': 455, 'process_value': '', 'fees': [{'asset_id': '1.3.0', 'amount': 20971}], 'contract_id': '1.16.121'}]]}]]}, 'jsonrpc': '2.0', 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'asset_id': '1.3.0', 'amount': 20971}]
### {'affected_account': '1.2.16', 'fees': [{'asset_id': '1.3.0', 'amount': 20971}], 'message': '100%'}
-----------------------------------------------------------------------
>> list_account_balances ['nicotest']
{'result': [{'asset_id': '1.3.0', 'amount': '5596612442242059'}, {'asset_id': '1.3.1', 'amount': -10888204}], 'jsonrpc': '2.0', 'id': 1}

op before balances: {'nicotest': [{'asset_id': '1.3.0', 'amount': '5596612442263030'}, {'asset_id': '1.3.1', 'amount': -10888204}]}
op after  balances: {'nicotest': [{'asset_id': '1.3.0', 'amount': '5596612442242059'}, {'asset_id': '1.3.1', 'amount': -10888204}]}
balances delta: {'nicotest': {'1.3.1': 0, '1.3.0': 20971}}
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```  



### 4.2.2 非合约所有者调用  
**测试main代码：**    
``` python  
if __name__ == '__main__':
    # print('>> {}'.format(sys.argv))
    unlock("123456")

    # main_build_tx()
    # get_contract_function_call_op_test()

    # test_helloworld(log_result=True)
    # test_helloworld(caller="init1", log_result=True)

    # test_set_percent()

    # result = list_account_balances("init1")
    # print("result: {}".format(result))

    # result = accounts_balances(["init1", "nicotest"])
    # print("balances: {}".format(result))
    # print("============================================")
    # calc_contract_call_operation_fee(test_helloworld, ["nicotest"])
    # calc_contract_call_operation_fee(test_helloworld_owner, ["nicotest"])
    calc_contract_call_operation_fee(test_helloworld_not_owner, ["nicotest", "init1"])
```

**a. GAS不足**  
**账户抵押gas，使其不够一次合约调用的费用**  
``` text  
unlocked >>> 
list_account_balances init1
unlocked >>> list_account_balances init1
136261393.08010 COCOS
0 GAS


unlocked >>> 
update_collateral_for_gas init1 init1 10276 true 
unlocked >>> update_collateral_for_gas init1 init1 10276 true 
[
  "570a77210fc905c6bbde37a3ed4cf077b709241179ded1af92724b9634fbbb10",{
    "ref_block_num": 2906,
    "ref_block_prefix": 3132529633,
    "expiration": "2020-07-10T09:01:16",
    "operations": [[
        54,{
          "mortgager": "1.2.6",
          "beneficiary": "1.2.6",
          "collateral": 10276
        }
      ]
    ],
    "extensions": [],
    "signatures": [
      "204bde1f921991ae706c7790782835397f9c404e34528376ab98d18c085682041e77e664c0ebf1864da067570aa253954e55ff9288c1c863a09811f4df447a9f9b"
    ]
  }
]

unlocked >>> 
list_account_balances init1 
unlocked >>> list_account_balances init1 
136261392.98970 COCOS
0.02686 GAS
```  

**测试过程和结果：**
``` text 
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 contract_call_fee.py 
>> unlock ['123456']
{'result': None, 'id': 1, 'jsonrpc': '2.0'}

>> list_account_balances ['nicotest']
{'result': [{'asset_id': '1.3.0', 'amount': '5596612442242059'}, {'asset_id': '1.3.1', 'amount': -10888204}], 'id': 1, 'jsonrpc': '2.0'}

>> list_account_balances ['init1']
{'result': [{'asset_id': '1.3.0', 'amount': '13626139298970'}, {'asset_id': '1.3.1', 'amount': 2686}], 'id': 1, 'jsonrpc': '2.0'}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['6cfd1c0b161888bb4a365d0faf40598f06c601171c9365931c13450ad1fe8f80', {'ref_block_num': 2950, 'operations': [[35, {'value_list': [], 'contract_id': '1.16.121', 'caller': '1.2.6', 'function_name': 'test_helloworld', 'extensions': []}]], 'extensions': [], 'ref_block_prefix': 4241624039, 'expiration': '2020-07-10T09:02:54', 'signatures': ['201dd5ffb805a85a0eae3131536afc36a4658271f865b6139b152fad57976e0b9b55ae3f7bf58948608b5cdea42625b1a13b0e1045c4c51d9763fec932982c0459']}], 'id': 1, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info ['6cfd1c0b161888bb4a365d0faf40598f06c601171c9365931c13450ad1fe8f80']
{'result': {'block_num': 7474065, 'id': '3.1.824874', 'trx_hash': '6cfd1c0b161888bb4a365d0faf40598f06c601171c9365931c13450ad1fe8f80', 'trx_in_block': 0}, 'id': 1, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info 6cfd1c0b161888bb4a365d0faf40598f06c601171c9365931c13450ad1fe8f80
 {'block_num': 7474065, 'id': '3.1.824874', 'trx_hash': '6cfd1c0b161888bb4a365d0faf40598f06c601171c9365931c13450ad1fe8f80', 'trx_in_block': 0}

>> get_block [7474065]
{'result': {'transactions': [['6cfd1c0b161888bb4a365d0faf40598f06c601171c9365931c13450ad1fe8f80', {'operation_results': [[4, {'real_running_time': 203, 'contract_id': '1.16.121', 'contract_affecteds': [[3, {'affected_account': '1.2.6', 'message': 'Hi, Cocos-BCX contract'}], [5, {'affected_account': '1.2.6', 'fees': [{'asset_id': '1.3.0', 'amount': 6216}], 'message': '30%'}], [5, {'affected_account': '1.2.16', 'fees': [{'asset_id': '1.3.0', 'amount': 14503}], 'message': '70%'}]], 'relevant_datasize': 35, 'existed_pv': False, 'process_value': '', 'fees': [{'asset_id': '1.3.0', 'amount': 20719}]}]], 'ref_block_num': 2950, 'operations': [[35, {'value_list': [], 'contract_id': '1.16.121', 'caller': '1.2.6', 'function_name': 'test_helloworld', 'extensions': []}]], 'extensions': [], 'ref_block_prefix': 4241624039, 'expiration': '2020-07-10T09:02:54', 'signatures': ['201dd5ffb805a85a0eae3131536afc36a4658271f865b6139b152fad57976e0b9b55ae3f7bf58948608b5cdea42625b1a13b0e1045c4c51d9763fec932982c0459']}]], 'witness_signature': '1f4b188f353d02a01af1b5cb7a6a3dea627d1ffc668fb859da66160174c8eadc9447b9f3940444880775ea4c96f38ef33d89af739a91a71506e62ea8cd04a8cd06', 'witness': '1.6.4', 'transaction_merkle_root': 'f2e105df5a7fb5367d593bd883a1cae258842fd0', 'previous': '00720b90e1931c21b800eff28f1ab700f08741ea', 'timestamp': '2020-07-10T08:42:26', 'block_id': '00720b915b669dfaa00b30e89157fe55dec71f96'}, 'id': 1, 'jsonrpc': '2.0'}

-------------------- contract call fee result ------------------------
## total_fee: [{'asset_id': '1.3.0', 'amount': 20719}]
### {'affected_account': '1.2.6', 'fees': [{'asset_id': '1.3.0', 'amount': 6216}], 'message': '30%'}
### {'affected_account': '1.2.16', 'fees': [{'asset_id': '1.3.0', 'amount': 14503}], 'message': '70%'}
-----------------------------------------------------------------------
>> list_account_balances ['nicotest']
{'result': [{'asset_id': '1.3.0', 'amount': '5596612442227556'}, {'asset_id': '1.3.1', 'amount': -10888204}], 'id': 1, 'jsonrpc': '2.0'}

>> list_account_balances ['init1']
{'result': [{'asset_id': '1.3.0', 'amount': '13626139295440'}, {'asset_id': '1.3.1', 'amount': 0}], 'id': 1, 'jsonrpc': '2.0'}

op before balances: {'init1': [{'asset_id': '1.3.0', 'amount': '13626139298970'}, {'asset_id': '1.3.1', 'amount': 2686}], 'nicotest': [{'asset_id': '1.3.0', 'amount': '5596612442242059'}, {'asset_id': '1.3.1', 'amount': -10888204}]}
op after  balances: {'init1': [{'asset_id': '1.3.0', 'amount': '13626139295440'}, {'asset_id': '1.3.1', 'amount': 0}], 'nicotest': [{'asset_id': '1.3.0', 'amount': '5596612442227556'}, {'asset_id': '1.3.1', 'amount': -10888204}]}
balances delta: {'init1': {'1.3.1': 2686, '1.3.0': 3530}, 'nicotest': {'1.3.1': 0, '1.3.0': 14503}}
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```  
合约调用者和合约所有者合约调用的手续费和账户资产的变化一致。  

**b. GAS充足**  
**给合约调用者抵押足够的GAS**  
抵押后的结果：  
``` text  
unlocked >>> 
list_account_balances init1 
unlocked >>> list_account_balances init1
136254607.95440 COCOS
9521.01587 GAS
```  

**测试过程和结果：**  
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 contract_call_fee.py 
>> unlock ['123456']
{'jsonrpc': '2.0', 'result': None, 'id': 1}

>> list_account_balances ['nicotest']
{'jsonrpc': '2.0', 'result': [{'asset_id': '1.3.0', 'amount': '5596612439742990'}, {'asset_id': '1.3.1', 'amount': -7415710}], 'id': 1}

>> list_account_balances ['init1']
{'jsonrpc': '2.0', 'result': [{'asset_id': '1.3.0', 'amount': '13625460795440'}, {'asset_id': '1.3.1', 'amount': 952101587}], 'id': 1}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'jsonrpc': '2.0', 'result': ['2195d4787995f427910ff7a3e58a10cb881c44ad78a9ffb0ba8499284d3149a6', {'operations': [[35, {'extensions': [], 'function_name': 'test_helloworld', 'value_list': [], 'caller': '1.2.6', 'contract_id': '1.16.121'}]], 'extensions': [], 'ref_block_num': 3212, 'ref_block_prefix': 150057028, 'expiration': '2020-07-10T09:13:38', 'signatures': ['1f7587248e3ffd0d0a7b1ef57df79a2000eeafdf5608c008cb123a2c5c7613d15b155581411ae77795a6d52e3f16006bd8203d82cdb55cd192b4d16d2652d35d28']}], 'id': 1}

>> get_transaction_in_block_info ['2195d4787995f427910ff7a3e58a10cb881c44ad78a9ffb0ba8499284d3149a6']
{'jsonrpc': '2.0', 'result': {'trx_hash': '2195d4787995f427910ff7a3e58a10cb881c44ad78a9ffb0ba8499284d3149a6', 'block_num': 7474326, 'trx_in_block': 0, 'id': '3.1.824878'}, 'id': 1}

>> get_transaction_in_block_info 2195d4787995f427910ff7a3e58a10cb881c44ad78a9ffb0ba8499284d3149a6
 {'trx_hash': '2195d4787995f427910ff7a3e58a10cb881c44ad78a9ffb0ba8499284d3149a6', 'block_num': 7474326, 'trx_in_block': 0, 'id': '3.1.824878'}

>> get_block [7474326]
{'jsonrpc': '2.0', 'result': {'previous': '00720c950c3ac9ecb1bdd6278cc999d0b967352e', 'witness_signature': '2016599c0b3817b05f91e931aeef503d7b83fef2e5169ad1b3ee3d4101e0fe4ddc6a693807cd8609bce15fe6ff22296c1d9a006876112e3f80d695a3eae7ecaeb6', 'transaction_merkle_root': '4cad1ba8ad0aee4448307e46661f7d98262a9078', 'transactions': [['2195d4787995f427910ff7a3e58a10cb881c44ad78a9ffb0ba8499284d3149a6', {'operations': [[35, {'extensions': [], 'function_name': 'test_helloworld', 'value_list': [], 'caller': '1.2.6', 'contract_id': '1.16.121'}]], 'extensions': [], 'ref_block_num': 3212, 'ref_block_prefix': 150057028, 'operation_results': [[4, {'process_value': '', 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}], [5, {'message': '30%', 'affected_account': '1.2.6', 'fees': [{'asset_id': '1.3.0', 'amount': 6221}]}], [5, {'message': '70%', 'affected_account': '1.2.16', 'fees': [{'asset_id': '1.3.0', 'amount': 14514}]}]], 'fees': [{'asset_id': '1.3.0', 'amount': 20735}], 'existed_pv': False, 'real_running_time': 219, 'relevant_datasize': 35, 'contract_id': '1.16.121'}]], 'expiration': '2020-07-10T09:13:38', 'signatures': ['1f7587248e3ffd0d0a7b1ef57df79a2000eeafdf5608c008cb123a2c5c7613d15b155581411ae77795a6d52e3f16006bd8203d82cdb55cd192b4d16d2652d35d28']}]], 'witness': '1.6.4', 'block_id': '00720c96225baa3510ac5b800ec1276e2aab5553', 'timestamp': '2020-07-10T08:53:10'}, 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'asset_id': '1.3.0', 'amount': 20735}]
### {'message': '30%', 'affected_account': '1.2.6', 'fees': [{'asset_id': '1.3.0', 'amount': 6221}]}
### {'message': '70%', 'affected_account': '1.2.16', 'fees': [{'asset_id': '1.3.0', 'amount': 14514}]}
-----------------------------------------------------------------------
>> list_account_balances ['nicotest']
{'jsonrpc': '2.0', 'result': [{'asset_id': '1.3.0', 'amount': '5596612439728476'}, {'asset_id': '1.3.1', 'amount': -7415710}], 'id': 1}

>> list_account_balances ['init1']
{'jsonrpc': '2.0', 'result': [{'asset_id': '1.3.0', 'amount': '13625460795440'}, {'asset_id': '1.3.1', 'amount': 952095366}], 'id': 1}

op before balances: {'nicotest': [{'asset_id': '1.3.0', 'amount': '5596612439742990'}, {'asset_id': '1.3.1', 'amount': -7415710}], 'init1': [{'asset_id': '1.3.0', 'amount': '13625460795440'}, {'asset_id': '1.3.1', 'amount': 952101587}]}
op after  balances: {'nicotest': [{'asset_id': '1.3.0', 'amount': '5596612439728476'}, {'asset_id': '1.3.1', 'amount': -7415710}], 'init1': [{'asset_id': '1.3.0', 'amount': '13625460795440'}, {'asset_id': '1.3.1', 'amount': 952095366}]}
balances delta: {'nicotest': {'1.3.1': 0, '1.3.0': 14514}, 'init1': {'1.3.1': 6221, '1.3.0': 0}}
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$  
```  

**c. 只有COCOS**  
**测试过程和结果：**  
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 contract_call_fee.py 
>> unlock ['123456']
{'result': None, 'id': 1, 'jsonrpc': '2.0'}

>> list_account_balances ['nicotest']
{'result': [{'asset_id': '1.3.0', 'amount': '5596616713538030'}, {'asset_id': '1.3.1', 'amount': '14271274524'}], 'id': 1, 'jsonrpc': '2.0'}

>> list_account_balances ['init1']
{'result': [{'asset_id': '1.3.0', 'amount': '13626139333745'}], 'id': 1, 'jsonrpc': '2.0'}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['b64cb464d5d755ace3222240f37f0cbbfa6b65b9781b42728df3b9ef141e59e2', {'ref_block_num': 1359, 'extensions': [], 'operations': [[35, {'value_list': [], 'caller': '1.2.6', 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld'}]], 'expiration': '2020-07-10T07:58:06', 'signatures': ['20636c7d10cd2b6a86915d7316bbf3aa90539d4c1b1ee85bb956b7192205fa48496bddfcf55ff701e6f901194e9061742a2a16b625e76561342d640eb0a420f564'], 'ref_block_prefix': 2789100178}], 'id': 1, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info ['b64cb464d5d755ace3222240f37f0cbbfa6b65b9781b42728df3b9ef141e59e2']
{'result': {'trx_hash': 'b64cb464d5d755ace3222240f37f0cbbfa6b65b9781b42728df3b9ef141e59e2', 'id': '3.1.824866', 'block_num': 7472473, 'trx_in_block': 0}, 'id': 1, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info b64cb464d5d755ace3222240f37f0cbbfa6b65b9781b42728df3b9ef141e59e2
 {'trx_hash': 'b64cb464d5d755ace3222240f37f0cbbfa6b65b9781b42728df3b9ef141e59e2', 'id': '3.1.824866', 'block_num': 7472473, 'trx_in_block': 0}

>> get_block [7472473]
{'result': {'timestamp': '2020-07-10T07:37:38', 'transaction_merkle_root': 'e974dd1219d2b138cd0c3f7f773d2ad1d85dfb7d', 'witness': '1.6.8', 'previous': '007205585da3d75c0c5c1b50fb4aad0b24f72f97', 'block_id': '007205592816b8c5181248a4feb640f271e92415', 'transactions': [['b64cb464d5d755ace3222240f37f0cbbfa6b65b9781b42728df3b9ef141e59e2', {'ref_block_num': 1359, 'extensions': [], 'operations': [[35, {'value_list': [], 'caller': '1.2.6', 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld'}]], 'expiration': '2020-07-10T07:58:06', 'signatures': ['20636c7d10cd2b6a86915d7316bbf3aa90539d4c1b1ee85bb956b7192205fa48496bddfcf55ff701e6f901194e9061742a2a16b625e76561342d640eb0a420f564'], 'ref_block_prefix': 2789100178, 'operation_results': [[4, {'existed_pv': False, 'contract_affecteds': [[3, {'affected_account': '1.2.6', 'message': 'Hi, Cocos-BCX contract'}], [5, {'fees': [{'asset_id': '1.3.0', 'amount': 6233}], 'affected_account': '1.2.6', 'message': '30%'}], [5, {'fees': [{'asset_id': '1.3.0', 'amount': 14543}], 'affected_account': '1.2.16', 'message': '70%'}]], 'contract_id': '1.16.121', 'process_value': '', 'fees': [{'asset_id': '1.3.0', 'amount': 20776}], 'real_running_time': 260, 'relevant_datasize': 35}]]}]], 'witness_signature': '1f21b46e07fd3625764a5d10c6312df31e456cfdc584caaf1b47f285e1316bc214141d60a0d9568549d4e99412749b4d5ac3162a1e85006139e8194c11343b9be7'}, 'id': 1, 'jsonrpc': '2.0'}

-------------------- contract call fee result ------------------------
## total_fee: [{'asset_id': '1.3.0', 'amount': 20776}]
### {'fees': [{'asset_id': '1.3.0', 'amount': 6233}], 'affected_account': '1.2.6', 'message': '30%'}
### {'fees': [{'asset_id': '1.3.0', 'amount': 14543}], 'affected_account': '1.2.16', 'message': '70%'}
-----------------------------------------------------------------------
>> list_account_balances ['nicotest']
{'result': [{'asset_id': '1.3.0', 'amount': '5596616713538030'}, {'asset_id': '1.3.1', 'amount': '14271259981'}], 'id': 1, 'jsonrpc': '2.0'}

>> list_account_balances ['init1']
{'result': [{'asset_id': '1.3.0', 'amount': '13626139327512'}], 'id': 1, 'jsonrpc': '2.0'}

op before balances: {'nicotest': [{'asset_id': '1.3.0', 'amount': '5596616713538030'}, {'asset_id': '1.3.1', 'amount': '14271274524'}], 'init1': [{'asset_id': '1.3.0', 'amount': '13626139333745'}]}
op after  balances: {'nicotest': [{'asset_id': '1.3.0', 'amount': '5596616713538030'}, {'asset_id': '1.3.1', 'amount': '14271259981'}], 'init1': [{'asset_id': '1.3.0', 'amount': '13626139327512'}]}
balances delta: {'nicotest': {'1.3.1': 14543, '1.3.0': 0}, 'init1': {'1.3.1': 0, '1.3.0': 6233}}
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```  
合约调用者和合约所有者合约调用的手续费和账户资产的变化一致。  

## 4.3 合约费用分摊比例0%  
**查看合约费用分摊比例：**    
``` text  
locked >>> get_object 1.16.121
get_object 1.16.121
[{
    "id": "1.16.121",
    "creation_date": "2020-07-09T03:22:16",
    "owner": "1.2.16",
    "name": "contract.testapi.contractfeeshare",
    "user_invoke_share_percent": 0,
    "current_version": "7feed5235f0e1338d33775109673e80aa6d27618f6f4e1d460e64ad6cdb206a1",
    "contract_authority": "COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx",
    "is_release": false,
    "check_contract_authority": false,
    "contract_data": [],
    "contract_ABI": [[{
          "key": [
            2,{
              "v": "test_contract_fee_share"
            }
          ]
        },[
          5,{
            "is_var_arg": false,
            "arglist": []
          }
        ]
      ],[{
          "key": [
            2,{
              "v": "test_helloworld"
            }
          ]
        },[
          5,{
            "is_var_arg": false,
            "arglist": []
          }
        ]
      ],[{
          "key": [
            2,{
              "v": "test_set_percent"
            }
          ]
        },[
          5,{
            "is_var_arg": false,
            "arglist": [
              "percent"
            ]
          }
        ]
      ]
    ],
    "lua_code_b_id": "2.2.121"
  }
]

locked >>> 
```  
> "user_invoke_share_percent": 0,  
 

### 4.3.1 合约所有者调用  
**测试main代码：**    
``` python  
if __name__ == '__main__':
    # print('>> {}'.format(sys.argv))
    unlock("123456")

    # main_build_tx()
    # get_contract_function_call_op_test()

    # test_helloworld(log_result=True)
    # test_helloworld(caller="init1", log_result=True)

    # test_set_percent()

    # result = list_account_balances("init1")
    # print("result: {}".format(result))

    # result = accounts_balances(["init1", "nicotest"])
    # print("balances: {}".format(result))
    # print("============================================")
    calc_contract_call_operation_fee(test_helloworld, ["nicotest"])
    # calc_contract_call_operation_fee(test_helloworld_owner, ["nicotest"])
```  

**a. 无GAS，COCOS充足**  
**测试过程和结果：**  
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 contract_call_fee.py 
>> unlock ['123456']
{'jsonrpc': '2.0', 'result': None, 'id': 1}

>> list_account_balances ['nicotest']
{'jsonrpc': '2.0', 'result': [{'asset_id': '1.3.0', 'amount': '5596612429503866'}, {'asset_id': '1.3.1', 'amount': -7415710}], 'id': 1}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'jsonrpc': '2.0', 'result': ['18046da3c9db8b3b3fd344a91b94c000a64a8161e3ed8197d30092b7cb536237', {'signatures': ['1f540d73320bce0174347628a3f81dabf0c7bdd4b73378a2579851d9aecd18c8be7bade3873779102b82c8b622e0a20f16624a2dd3a4ce8e756b0bdee227eba0f0'], 'extensions': [], 'expiration': '2020-07-10T10:16:48', 'operations': [[35, {'caller': '1.2.16', 'extensions': [], 'value_list': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld'}]], 'ref_block_num': 4763, 'ref_block_prefix': 2748631969}], 'id': 1}

>> get_transaction_in_block_info ['18046da3c9db8b3b3fd344a91b94c000a64a8161e3ed8197d30092b7cb536237']
{'jsonrpc': '2.0', 'result': None, 'id': 1}

>> get_transaction_in_block_info 18046da3c9db8b3b3fd344a91b94c000a64a8161e3ed8197d30092b7cb536237
 None

>> get_transaction_in_block_info ['18046da3c9db8b3b3fd344a91b94c000a64a8161e3ed8197d30092b7cb536237']
{'jsonrpc': '2.0', 'result': {'trx_in_block': 0, 'id': '3.1.824883', 'trx_hash': '18046da3c9db8b3b3fd344a91b94c000a64a8161e3ed8197d30092b7cb536237', 'block_num': 7475876}, 'id': 1}

>> get_transaction_in_block_info 18046da3c9db8b3b3fd344a91b94c000a64a8161e3ed8197d30092b7cb536237
 {'trx_in_block': 0, 'id': '3.1.824883', 'trx_hash': '18046da3c9db8b3b3fd344a91b94c000a64a8161e3ed8197d30092b7cb536237', 'block_num': 7475876}

>> get_block [7475876]
{'jsonrpc': '2.0', 'result': {'transaction_merkle_root': '696d7563fd2b42534d080ca640939949d772464a', 'previous': '007212a37e4d11eb0d640ae18537955dd476e249', 'timestamp': '2020-07-10T09:56:22', 'transactions': [['18046da3c9db8b3b3fd344a91b94c000a64a8161e3ed8197d30092b7cb536237', {'signatures': ['1f540d73320bce0174347628a3f81dabf0c7bdd4b73378a2579851d9aecd18c8be7bade3873779102b82c8b622e0a20f16624a2dd3a4ce8e756b0bdee227eba0f0'], 'extensions': [], 'expiration': '2020-07-10T10:16:48', 'operations': [[35, {'caller': '1.2.16', 'extensions': [], 'value_list': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld'}]], 'ref_block_num': 4763, 'ref_block_prefix': 2748631969, 'operation_results': [[4, {'process_value': '', 'contract_id': '1.16.121', 'existed_pv': False, 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'Hi, Cocos-BCX contract'}], [5, {'fees': [{'asset_id': '1.3.0', 'amount': 20730}], 'affected_account': '1.2.16', 'message': '100%'}]], 'fees': [{'asset_id': '1.3.0', 'amount': 20730}], 'real_running_time': 214, 'relevant_datasize': 35}]]}]], 'witness': '1.6.6', 'block_id': '007212a4ef52a408d88a1c58e670de38568b25fb', 'witness_signature': '1f717ab735434ae570021158f96df076b8b05c1f4160b4c4839708e35675a5441a117629c74fefe8ecb8dfefe2d9fe9052f6c109bb4d2d7cdd950a24d1093f4ac8'}, 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'asset_id': '1.3.0', 'amount': 20730}]
### {'fees': [{'asset_id': '1.3.0', 'amount': 20730}], 'affected_account': '1.2.16', 'message': '100%'}
-----------------------------------------------------------------------
>> list_account_balances ['nicotest']
{'jsonrpc': '2.0', 'result': [{'asset_id': '1.3.0', 'amount': '5596612429483136'}, {'asset_id': '1.3.1', 'amount': -7415710}], 'id': 1}

op before balances: {'nicotest': [{'asset_id': '1.3.0', 'amount': '5596612429503866'}, {'asset_id': '1.3.1', 'amount': -7415710}]}
op after  balances: {'nicotest': [{'asset_id': '1.3.0', 'amount': '5596612429483136'}, {'asset_id': '1.3.1', 'amount': -7415710}]}
balances delta: {'nicotest': {'1.3.0': 20730, '1.3.1': 0}}
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```  

**b. 无GAS，COCOS不足**  
合约所有者账户资产：  
``` text  
unlocked >>> 
list_account_balances nicotest
transfer nicotest init1 17.4 COCOS ["", false] true
unlocked >>> list_account_balances nicotest
50000037.40000 COCOS
-74.15710 GAS


unlocked >>> transfer nicotest init1 17.4 COCOS ["", false] true
[
  "825da911ac5c81622c3c8495d09588fd12a4ccff04e272314e3690fd49c28fa1",{
    "ref_block_num": 5235,
    "ref_block_prefix": 2307462562,
    "expiration": "2020-07-10T10:36:02",
    "operations": [[
        0,{
          "from": "1.2.16",
          "to": "1.2.6",
          "amount": {
            "amount": 1740000,
            "asset_id": "1.3.0"
          },
          "extensions": []
        }
      ]
    ],
    "extensions": [],
    "signatures": [
      "1f0955d1ca8bc5ef1bc06ab24fccc4f57c7c1356d5943ab605f50d6c35f3fe55932802cad13f82189861983ecd7fc4d874f97a383a20ced6710fc9f5c211fcb4f5"
    ]
  }
]

unlocked >>> 
list_account_balances nicotest
transfer nicotest init1 17.4 COCOS ["", false] trueunlocked >>> list_account_balances nicotest
50000019.90000 COCOS
-74.15710 GAS


unlocked >>> transfer nicotest init1 17.4 COCOS ["", false] true
939946ms th_a       wallet.cpp:1788               sign_transaction     ] Caught exception while broadcasting tx ed821cee3cbbecddddb7e477eb288931be40d055:  0 exception: unspecified
Assert Exception: locked->value >= 0 && itr->get_balance() + delta >= asset(locked->value, delta.asset_id): Some assets are locked and cannot be transferred.asset_id:1.3.0,lock_amount:5000001900000,request_amount:-1740000
    {"error":"Assert Exception: locked->value >= 0 && itr->get_balance() + delta >= asset(locked->value, delta.asset_id): Some assets are locked and cannot be transferred.asset_id:1.3.0,lock_amount:5000001900000,request_amount:-1740000","data":{"id":306,"jsonrpc":"2.0","error":{"code":306,"message":"Assert Exception: locked->value >= 0 && itr->get_balance() + delta >= asset(locked->value, delta.asset_id): Some assets are locked and cannot be transferred.asset_id:1.3.0,lock_amount:5000001900000,request_amount:-1740000"}}}
    th_a  state.cpp:38 handle_reply
0 exception: unspecified
Assert Exception: locked->value >= 0 && itr->get_balance() + delta >= asset(locked->value, delta.asset_id): Some assets are locked and cannot be transferred.asset_id:1.3.0,lock_amount:5000001900000,request_amount:-1740000
    {"error":"Assert Exception: locked->value >= 0 && itr->get_balance() + delta >= asset(locked->value, delta.asset_id): Some assets are locked and cannot be transferred.asset_id:1.3.0,lock_amount:5000001900000,request_amount:-1740000","data":{"id":306,"jsonrpc":"2.0","error":{"code":306,"message":"Assert Exception: locked->value >= 0 && itr->get_balance() + delta >= asset(locked->value, delta.asset_id): Some assets are locked and cannot be transferred.asset_id:1.3.0,lock_amount:5000001900000,request_amount:-1740000"}}}
    th_a  state.cpp:38 handle_reply

    {"from":"nicotest","to":"init1","amount":"17.4","asset_symbol":"COCOS","memo":["",false],"broadcast":true}
    th_a  wallet.cpp:1966 transfer

unlocked >>> 

......

unlocked >>> 
list_account_balances nicotest
transfer nicotest init1 0.4 COCOS ["", false] trueunlocked >>> list_account_balances nicotest
50000019.06161 COCOS
-74.15710 GAS


unlocked >>> transfer nicotest init1 0.4 COCOS ["", false] true
1168978ms th_a       wallet.cpp:1788               sign_transaction     ] Caught exception while broadcasting tx f7d05b02870f39fe7fdd7cceb351f04a1a42611a:  0 exception: unspecified
Assert Exception: locked->value >= 0 && itr->get_balance() + delta >= asset(locked->value, delta.asset_id): Some assets are locked and cannot be transferred.asset_id:1.3.0,lock_amount:5000001900000,request_amount:-40000
    {"error":"Assert Exception: locked->value >= 0 && itr->get_balance() + delta >= asset(locked->value, delta.asset_id): Some assets are locked and cannot be transferred.asset_id:1.3.0,lock_amount:5000001900000,request_amount:-40000","data":{"id":388,"jsonrpc":"2.0","error":{"code":388,"message":"Assert Exception: locked->value >= 0 && itr->get_balance() + delta >= asset(locked->value, delta.asset_id): Some assets are locked and cannot be transferred.asset_id:1.3.0,lock_amount:5000001900000,request_amount:-40000"}}}
    th_a  state.cpp:38 handle_reply
0 exception: unspecified
Assert Exception: locked->value >= 0 && itr->get_balance() + delta >= asset(locked->value, delta.asset_id): Some assets are locked and cannot be transferred.asset_id:1.3.0,lock_amount:5000001900000,request_amount:-40000
    {"error":"Assert Exception: locked->value >= 0 && itr->get_balance() + delta >= asset(locked->value, delta.asset_id): Some assets are locked and cannot be transferred.asset_id:1.3.0,lock_amount:5000001900000,request_amount:-40000","data":{"id":388,"jsonrpc":"2.0","error":{"code":388,"message":"Assert Exception: locked->value >= 0 && itr->get_balance() + delta >= asset(locked->value, delta.asset_id): Some assets are locked and cannot be transferred.asset_id:1.3.0,lock_amount:5000001900000,request_amount:-40000"}}}
    th_a  state.cpp:38 handle_reply

    {"from":"nicotest","to":"init1","amount":"0.4","asset_symbol":"COCOS","memo":["",false],"broadcast":true}
    th_a  wallet.cpp:1966 transfer

unlocked >>> 
```  

**合约调用过程和结果：**  
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 contract_call_fee.py 
>> unlock ['123456']
{'id': 1, 'result': None, 'jsonrpc': '2.0'}

>> list_account_balances ['nicotest']
{'id': 1, 'result': [{'asset_id': '1.3.0', 'amount': '5000001906161'}, {'asset_id': '1.3.1', 'amount': -7415710}], 'jsonrpc': '2.0'}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'id': 1, 'jsonrpc': '2.0', 'error': {'message': 'unspecified: Assert Exception: locked->value >= 0 && itr->get_balance() + delta >= asset(locked->value, delta.asset_id): Some assets are locked and cannot be transferred.asset_id:1.3.0,lock_amount:5000001900000,request_amount:-20732', 'code': 1}}

KeyError('result',)
Traceback (most recent call last):
  File "contract_call_fee.py", line 383, in <module>
    calc_contract_call_operation_fee(test_helloworld_owner, ["nicotest"])
  File "contract_call_fee.py", line 99, in calc_contract_call_operation_fee
    func()
  File "contract_call_fee.py", line 352, in test_helloworld_owner
    test_helloworld(log_result=True)
  File "contract_call_fee.py", line 332, in test_helloworld
    block = get_block_by_transaction_id(call_result[0])
TypeError: 'NoneType' object is not subscriptable
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```  

**cli_wallet异常**  
``` text  
unlocked >>> 
1202145ms th_a       wallet.cpp:1788               sign_transaction     ] Caught exception while broadcasting tx 904d7795574518c7c08910e95dc04d6668d795d9:  0 exception: unspecified
Assert Exception: locked->value >= 0 && itr->get_balance() + delta >= asset(locked->value, delta.asset_id): Some assets are locked and cannot be transferred.asset_id:1.3.0,lock_amount:5000001900000,request_amount:-20732
    {"error":"Assert Exception: locked->value >= 0 && itr->get_balance() + delta >= asset(locked->value, delta.asset_id): Some assets are locked and cannot be transferred.asset_id:1.3.0,lock_amount:5000001900000,request_amount:-20732","data":{"id":397,"jsonrpc":"2.0","error":{"code":397,"message":"Assert Exception: locked->value >= 0 && itr->get_balance() + delta >= asset(locked->value, delta.asset_id): Some assets are locked and cannot be transferred.asset_id:1.3.0,lock_amount:5000001900000,request_amount:-20732"}}}
    th_a  state.cpp:38 handle_reply
1202146ms th_a       websocket_api.cpp:158         on_message           ] websocket api exception :{"code":0,"name":"exception","message":"unspecified","stack":[{"context":{"level":"error","file":"state.cpp","line":38,"method":"handle_reply","hostname":"","thread_name":"th_a","timestamp":"2020-07-10T10:20:02"},"format":"${error}","data":{"error":"Assert Exception: locked->value >= 0 && itr->get_balance() + delta >= asset(locked->value, delta.asset_id): Some assets are locked and cannot be transferred.asset_id:1.3.0,lock_amount:5000001900000,request_amount:-20732","data":{"id":397,"jsonrpc":"2.0","error":{"code":397,"message":"Assert Exception: locked->value >= 0 && itr->get_balance() + delta >= asset(locked->value, delta.asset_id): Some assets are locked and cannot be transferred.asset_id:1.3.0,lock_amount:5000001900000,request_amount:-20732"}}}},{"context":{"level":"warn","file":"wallet.cpp","line":2090,"method":"call_contract_function","hostname":"","thread_name":"th_a","timestamp":"2020-07-10T10:20:02"},"format":"","data":{"account_id_or_name":"nicotest","contract_id_or_name":"contract.testapi.contractfeeshare","function_name":"test_helloworld","value_list":[],"broadcast":true}},{"context":{"level":"warn","file":"websocket_api.cpp","line":154,"method":"on_message","hostname":"","thread_name":"th_a","timestamp":"2020-07-10T10:20:02"},"format":"","data":{"call.method":"call_contract_function","call.params":["nicotest","contract.testapi.contractfeeshare","test_helloworld",[],true]}}]}

unlocked >>> 
```  
账户资金不足，合约调用失败    

**c. 合约所有者有足够的GAS**  
**给账户抵押足够的GAS：**  
``` text  
unlocked >>> 
list_account_balances nicotest 
unlocked >>> list_account_balances nicotest 
32947344242.06161 COCOS
-74.15710 GAS

unlocked >>> 
update_collateral_for_gas nicotest nicotest 294734424200000 true 
unlocked >>> update_collateral_for_gas nicotest nicotest 294734424200000 true 
[
  "b5ae257cbe8a8c899aa3fdf1b8aa2b3ba8e8a7f484a7c764468715dc28bf22ab",{
    "ref_block_num": 5464,
    "ref_block_prefix": 1154662183,
    "expiration": "2020-07-10T10:45:26",
    "operations": [[
        54,{
          "mortgager": "1.2.16",
          "beneficiary": "1.2.16",
          "collateral": "294734424200000"
        }
      ]
    ],
    "extensions": [],
    "signatures": [
      "204a28ba1ec95a77aeaa864c8db840f257eb8e641f1a6d59296ae19d1fc00b176341bdd2206797af3d72e0c25685a73f4b2adf8677585125b25ff2f7b1fbccde4b"
    ]
  }
]

unlocked >>> 
list_account_balances nicotest 
unlocked >>> list_account_balances nicotest 
30000000024.95945 COCOS
4135932210.08476 GAS

```   

**合约调用过程和结果：**  
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 contract_call_fee.py 
>> unlock ['123456']
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> list_account_balances ['nicotest']
{'jsonrpc': '2.0', 'id': 1, 'result': [{'amount': '3000000002495945', 'asset_id': '1.3.0'}, {'amount': '413593221008476', 'asset_id': '1.3.1'}]}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['d99699d6fc04d24b2d586262162b7f97a143fffa19cadeedbcfb39cfd2703070', {'ref_block_num': 5516, 'signatures': ['1f0bddab58208609543910e1fc9c4850d7729ee39dd66dc300655510c33b3d39737f1209cd45e7d90038a32469f6035a1042d32b872f0c31e33be1327c88aca0b4'], 'expiration': '2020-07-10T10:47:32', 'operations': [[35, {'value_list': [], 'caller': '1.2.16', 'contract_id': '1.16.121', 'extensions': [], 'function_name': 'test_helloworld'}]], 'ref_block_prefix': 2699420632, 'extensions': []}]}

>> get_transaction_in_block_info ['d99699d6fc04d24b2d586262162b7f97a143fffa19cadeedbcfb39cfd2703070']
{'jsonrpc': '2.0', 'id': 1, 'result': {'trx_hash': 'd99699d6fc04d24b2d586262162b7f97a143fffa19cadeedbcfb39cfd2703070', 'id': '3.1.824900', 'trx_in_block': 0, 'block_num': 7476630}}

>> get_transaction_in_block_info d99699d6fc04d24b2d586262162b7f97a143fffa19cadeedbcfb39cfd2703070
 {'trx_hash': 'd99699d6fc04d24b2d586262162b7f97a143fffa19cadeedbcfb39cfd2703070', 'id': '3.1.824900', 'trx_in_block': 0, 'block_num': 7476630}

>> get_block [7476630]
{'jsonrpc': '2.0', 'id': 1, 'result': {'previous': '007215959ecfcd809bb27b8b53fbb8babdc48d6c', 'timestamp': '2020-07-10T10:27:04', 'witness_signature': '200bd37276d0403dde383fdcd60f98ee2ca2802796084a780c3f3388615ef3eccb45066802b5e1d2a310da1ad0dcb54c9e99dcc3055ca8349ddfa924f75becd538', 'witness': '1.6.7', 'transactions': [['d99699d6fc04d24b2d586262162b7f97a143fffa19cadeedbcfb39cfd2703070', {'ref_block_num': 5516, 'signatures': ['1f0bddab58208609543910e1fc9c4850d7729ee39dd66dc300655510c33b3d39737f1209cd45e7d90038a32469f6035a1042d32b872f0c31e33be1327c88aca0b4'], 'expiration': '2020-07-10T10:47:32', 'operations': [[35, {'value_list': [], 'caller': '1.2.16', 'contract_id': '1.16.121', 'extensions': [], 'function_name': 'test_helloworld'}]], 'ref_block_prefix': 2699420632, 'extensions': [], 'operation_results': [[4, {'existed_pv': False, 'relevant_datasize': 35, 'real_running_time': 424, 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'Hi, Cocos-BCX contract'}], [5, {'affected_account': '1.2.16', 'fees': [{'amount': 20940, 'asset_id': '1.3.0'}], 'message': '100%'}]], 'contract_id': '1.16.121', 'process_value': '', 'fees': [{'amount': 20940, 'asset_id': '1.3.0'}]}]]}]], 'transaction_merkle_root': 'c7865bacaa32fae040263d9ecfdb69cc2f7c3c0b', 'block_id': '00721596150a5ba74dc02c5ffd9502f36cbd7cb9'}}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 20940, 'asset_id': '1.3.0'}]
### {'affected_account': '1.2.16', 'fees': [{'amount': 20940, 'asset_id': '1.3.0'}], 'message': '100%'}
-----------------------------------------------------------------------
>> list_account_balances ['nicotest']
{'jsonrpc': '2.0', 'id': 1, 'result': [{'amount': '3000000002495945', 'asset_id': '1.3.0'}, {'amount': '413593220987536', 'asset_id': '1.3.1'}]}

op before balances: {'nicotest': [{'amount': '3000000002495945', 'asset_id': '1.3.0'}, {'amount': '413593221008476', 'asset_id': '1.3.1'}]}
op after  balances: {'nicotest': [{'amount': '3000000002495945', 'asset_id': '1.3.0'}, {'amount': '413593220987536', 'asset_id': '1.3.1'}]}
balances delta: {'nicotest': {'1.3.0': 0, '1.3.1': 20940}}
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```  
合约调用成功，手续费和账户调用前后资产变化相同。  


### 4.3.2 非合约所有者调用  
**测试main代码：**    
``` python  
if __name__ == '__main__':
    # print('>> {}'.format(sys.argv))
    unlock("123456")

    # main_build_tx()
    # get_contract_function_call_op_test()

    # test_helloworld(log_result=True)
    # test_helloworld(caller="init1", log_result=True)

    # test_set_percent()

    # result = list_account_balances("init1")
    # print("result: {}".format(result))

    # result = accounts_balances(["init1", "nicotest"])
    # print("balances: {}".format(result))
    # print("============================================")
    # calc_contract_call_operation_fee(test_helloworld, ["nicotest"])
    calc_contract_call_operation_fee(test_helloworld_owner, ["nicotest"])
```  

> **说明：**此种情况，合约调用手续费全部从合约所有者账户中扣除，和合约调用者账户资产无关  

**测试过程和结果如下：**  
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 contract_call_fee.py 
>> unlock ['123456']
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> list_account_balances ['nicotest']
{'jsonrpc': '2.0', 'id': 1, 'result': [{'amount': '3000000002495945', 'asset_id': '1.3.0'}, {'amount': '413593220987536', 'asset_id': '1.3.1'}]}

>> list_account_balances ['init1']
{'jsonrpc': '2.0', 'id': 1, 'result': [{'amount': '2315503473688576', 'asset_id': '1.3.0'}, {'amount': 952085366, 'asset_id': '1.3.1'}]}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['7cce1c16a254f9d25f6f23caf315d349aec3ff8e23067671ba8233da83b04314', {'signatures': ['2005234bb04ee7610d72cbb0ad76e948bbf6879894d68672a4ab432c3138aecc636d42002d8d2edd6c7ff9b25c513aa2f9c1a53bf340476377507532336bd0a028'], 'ref_block_num': 5570, 'operations': [[35, {'function_name': 'test_helloworld', 'extensions': [], 'contract_id': '1.16.121', 'value_list': [], 'caller': '1.2.6'}]], 'ref_block_prefix': 161740626, 'expiration': '2020-07-10T10:49:48', 'extensions': []}]}

>> get_transaction_in_block_info ['7cce1c16a254f9d25f6f23caf315d349aec3ff8e23067671ba8233da83b04314']
{'jsonrpc': '2.0', 'id': 1, 'result': {'block_num': 7476685, 'id': '3.1.824901', 'trx_in_block': 0, 'trx_hash': '7cce1c16a254f9d25f6f23caf315d349aec3ff8e23067671ba8233da83b04314'}}

>> get_transaction_in_block_info 7cce1c16a254f9d25f6f23caf315d349aec3ff8e23067671ba8233da83b04314
 {'block_num': 7476685, 'id': '3.1.824901', 'trx_in_block': 0, 'trx_hash': '7cce1c16a254f9d25f6f23caf315d349aec3ff8e23067671ba8233da83b04314'}

>> get_block [7476685]
{'jsonrpc': '2.0', 'id': 1, 'result': {'block_id': '007215cdb2c279afac87d179f020145215486ffe', 'previous': '007215ccad914136127f33682ffe820b9a7d1b3b', 'timestamp': '2020-07-10T10:29:20', 'transactions': [['7cce1c16a254f9d25f6f23caf315d349aec3ff8e23067671ba8233da83b04314', {'signatures': ['2005234bb04ee7610d72cbb0ad76e948bbf6879894d68672a4ab432c3138aecc636d42002d8d2edd6c7ff9b25c513aa2f9c1a53bf340476377507532336bd0a028'], 'ref_block_num': 5570, 'operations': [[35, {'function_name': 'test_helloworld', 'extensions': [], 'contract_id': '1.16.121', 'value_list': [], 'caller': '1.2.6'}]], 'operation_results': [[4, {'relevant_datasize': 35, 'fees': [{'amount': 21015, 'asset_id': '1.3.0'}], 'contract_id': '1.16.121', 'existed_pv': False, 'process_value': '', 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}], [5, {'fees': [{'amount': 21015, 'asset_id': '1.3.0'}], 'message': '100%', 'affected_account': '1.2.16'}]], 'real_running_time': 499}]], 'ref_block_prefix': 161740626, 'expiration': '2020-07-10T10:49:48', 'extensions': []}]], 'transaction_merkle_root': '985bdee36b02da456d81e46c1fd683e4d80e39c2', 'witness': '1.6.8', 'witness_signature': '1f17000db0fedd30e4e195cd62c3e15f1046dd2981fd77b36a1fee22d800a4e1081a6c071f3574ff5f5e680eda0368fffd4470c369789295fb8b576458dac7a356'}}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 21015, 'asset_id': '1.3.0'}]
### {'fees': [{'amount': 21015, 'asset_id': '1.3.0'}], 'message': '100%', 'affected_account': '1.2.16'}
-----------------------------------------------------------------------
>> list_account_balances ['nicotest']
{'jsonrpc': '2.0', 'id': 1, 'result': [{'amount': '3000000002495945', 'asset_id': '1.3.0'}, {'amount': '413593220966521', 'asset_id': '1.3.1'}]}

>> list_account_balances ['init1']
{'jsonrpc': '2.0', 'id': 1, 'result': [{'amount': '2315503473688576', 'asset_id': '1.3.0'}, {'amount': 952085366, 'asset_id': '1.3.1'}]}

op before balances: {'nicotest': [{'amount': '3000000002495945', 'asset_id': '1.3.0'}, {'amount': '413593220987536', 'asset_id': '1.3.1'}], 'init1': [{'amount': '2315503473688576', 'asset_id': '1.3.0'}, {'amount': 952085366, 'asset_id': '1.3.1'}]}
op after  balances: {'nicotest': [{'amount': '3000000002495945', 'asset_id': '1.3.0'}, {'amount': '413593220966521', 'asset_id': '1.3.1'}], 'init1': [{'amount': '2315503473688576', 'asset_id': '1.3.0'}, {'amount': 952085366, 'asset_id': '1.3.1'}]}
balances delta: {'nicotest': {'1.3.0': 0, '1.3.1': 21015}, 'init1': {'1.3.0': 0, '1.3.1': 0}}
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```  


## 4.4 合约费用分摊比例为负数测试  
**测试过程和结果：**  
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 contract_call_fee.py 
>> unlock ['123456']
{'jsonrpc': '2.0', 'result': None, 'id': 1}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_set_percent', [[1, {'v': -20}]], True]
{'jsonrpc': '2.0', 'error': {'code': 1, 'message': 'unspecified: unspecified: Try the contract resolution execution failure,[2,{"v":"Assert Exception: not_in_range: percent should be in range 0-100 "}]'}, 'id': 1}

KeyError('result',)
Traceback (most recent call last):
  File "contract_call_fee.py", line 374, in <module>
    test_set_percent(percent=-20)
  File "contract_call_fee.py", line 320, in test_set_percent
    block = get_block_by_transaction_id(call_result[0])
TypeError: 'NoneType' object is not subscriptable
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```  

**cli_wallet异常结果：**  
``` text  
unlocked >>> 
277682ms th_a       wallet.cpp:1788               sign_transaction     ] Caught exception while broadcasting tx 8c7ac6d9f3818050513df8106877ee90fd040bd2:  0 exception: unspecified
unspecified: Try the contract resolution execution failure,[2,{"v":"Assert Exception: not_in_range: percent should be in range 0-100 "}]
    {"error":"unspecified: Try the contract resolution execution failure,[2,{\"v\":\"Assert Exception: not_in_range: percent should be in range 0-100 \"}]","data":{"id":152,"jsonrpc":"2.0","error":{"code":152,"message":"unspecified: Try the contract resolution execution failure,[2,{\"v\":\"Assert Exception: not_in_range: percent should be in range 0-100 \"}]"}}}
    th_a  state.cpp:38 handle_reply
277682ms th_a       websocket_api.cpp:158         on_message           ] websocket api exception :{"code":0,"name":"exception","message":"unspecified","stack":[{"context":{"level":"error","file":"state.cpp","line":38,"method":"handle_reply","hostname":"","thread_name":"th_a","timestamp":"2020-07-10T09:04:37"},"format":"${error}","data":{"error":"unspecified: Try the contract resolution execution failure,[2,{\"v\":\"Assert Exception: not_in_range: percent should be in range 0-100 \"}]","data":{"id":152,"jsonrpc":"2.0","error":{"code":152,"message":"unspecified: Try the contract resolution execution failure,[2,{\"v\":\"Assert Exception: not_in_range: percent should be in range 0-100 \"}]"}}}},{"context":{"level":"warn","file":"wallet.cpp","line":2090,"method":"call_contract_function","hostname":"","thread_name":"th_a","timestamp":"2020-07-10T09:04:37"},"format":"","data":{"account_id_or_name":"nicotest","contract_id_or_name":"contract.testapi.contractfeeshare","function_name":"test_set_percent","value_list":[[1,{"v":"-20.00000000000000000"}]],"broadcast":true}},{"context":{"level":"warn","file":"websocket_api.cpp","line":154,"method":"on_message","hostname":"","thread_name":"th_a","timestamp":"2020-07-10T09:04:37"},"format":"","data":{"call.method":"call_contract_function","call.params":["nicotest","contract.testapi.contractfeeshare","test_set_percent",[[1,{"v":-20}]],true]}}]}
```  

比例范围为0~100，所以操作失败。  


