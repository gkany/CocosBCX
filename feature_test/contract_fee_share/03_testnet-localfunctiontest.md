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

## 3.2 重新设置合约费用分摊百分比测试  


---------------------
# 4. 合约费用计算测试  
**只对硬分叉后的合约调用费用进行计算**  

## 4.1 合约费用分摊比例100%  
### 4.1.1 合约所有者调用  
#### 4.1.1.1 只有COCOS，无GAS测试  
**a. COCOS充足**  

**b. COCOS不足**  

#### 4.1.1.2 有GAS测试  
**a. GAS充足**

**b. GAS不足**

### 4.1.2 非合约所有者调用  
#### 4.1.2.1 只有COCOS，无GAS测试  
**a. COCOS充足**  

**b. COCOS不足**  

#### 4.1.2.2 有GAS测试  
**a. GAS充足**

**b. GAS不足**


## 4.2 合约费用分摊比例介于0%和100%之间  
### 4.2.1 合约所有者调用  

### 4.2.2 非合约所有者调用  


## 4.3 合约费用分摊比例0%  
### 4.3.1 合约所有者调用  

### 4.3.2 非合约所有者调用  

