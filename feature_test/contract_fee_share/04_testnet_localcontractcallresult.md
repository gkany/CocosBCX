# 1.测试准备  
> 基于测试网数据  

fn节点同步测试网数据到最新后，停止该节点，修改该节点的config.ini配置：  
* 添加见证人和对应的区块签名秘钥对  
* 移除现有测试网的p2p节点配置  
使其成为独立的bp节点  

# 2. 合约部署和重置测试  
[测试代码和合约](https://github.com/gkany/Cocos-Contracts-API)  

**测试过程和结果：**  
``` text  
ck@ubuntu:~/xukang/Cocos-Contracts-API$ python3 contract_test.py 
>> unlock ['123456']

{'id': 1, 'jsonrpc': '2.0', 'result': None}


>> list_my_accounts []

{'id': 1, 'jsonrpc': '2.0', 'result': [{'committee_status': ['1.5.0', True], 'cashback_vote': '1.13.777', 'name': 'init0', 'membership_expiration_date': '1969-12-31T23:59:59', 'statistics': '2.6.5', 'options': {'memo_key': 'COCOS8hxjGaAwkNHewgQqg6ERLA7L4J6wkzuhhLRVbKKuJZUYM3dfuS', 'extensions': [], 'votes': ['1:10', '0:19']}, 'active': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS8hxjGaAwkNHewgQqg6ERLA7L4J6wkzuhhLRVbKKuJZUYM3dfuS', 1]], 'account_auths': []}, 'owner': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS8hxjGaAwkNHewgQqg6ERLA7L4J6wkzuhhLRVbKKuJZUYM3dfuS', 1]], 'account_auths': []}, 'registrar': '1.2.4', 'id': '1.2.5', 'asset_locked': {'locked_total': [['1.3.0', '10000000000389']], 'vote_for_witness': {'amount': 299, 'asset_id': '1.3.0'}, 'committee_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'vote_for_committee': {'amount': 90, 'asset_id': '1.3.0'}, 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'contract_lock_details': []}, 'witness_status': ['1.6.1', True]}, {'statistics': '2.6.6', 'registrar': '1.2.4', 'id': '1.2.6', 'committee_status': ['1.5.1', True], 'name': 'init1', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'committee_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'contract_lock_details': []}, 'options': {'memo_key': 'COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7', 'extensions': [], 'votes': []}, 'active': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7', 1]], 'account_auths': []}, 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.2', True], 'owner': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7', 1]], 'account_auths': []}}, {'statistics': '2.6.7', 'registrar': '1.2.4', 'id': '1.2.7', 'committee_status': ['1.5.2', True], 'name': 'init2', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'committee_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'contract_lock_details': []}, 'options': {'memo_key': 'COCOS8hjpaYLn6RxfQEg61en7fEMy9beYsaWZ4Vm6jnqujQjJ5PQSGo', 'extensions': [], 'votes': []}, 'active': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS8hjpaYLn6RxfQEg61en7fEMy9beYsaWZ4Vm6jnqujQjJ5PQSGo', 1]], 'account_auths': []}, 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.3', True], 'owner': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS8hjpaYLn6RxfQEg61en7fEMy9beYsaWZ4Vm6jnqujQjJ5PQSGo', 1]], 'account_auths': []}}, {'statistics': '2.6.8', 'registrar': '1.2.4', 'id': '1.2.8', 'committee_status': ['1.5.3', True], 'name': 'init3', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'committee_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'contract_lock_details': []}, 'options': {'memo_key': 'COCOS5dLtguN6A12QBuV3dmh3YCLg3adkKmY3m2gV7hm9Cw9jtyGd3Y', 'extensions': [], 'votes': []}, 'active': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS5dLtguN6A12QBuV3dmh3YCLg3adkKmY3m2gV7hm9Cw9jtyGd3Y', 1]], 'account_auths': []}, 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.4', True], 'owner': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS5dLtguN6A12QBuV3dmh3YCLg3adkKmY3m2gV7hm9Cw9jtyGd3Y', 1]], 'account_auths': []}}, {'statistics': '2.6.9', 'registrar': '1.2.4', 'id': '1.2.9', 'committee_status': ['1.5.4', True], 'name': 'init4', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'committee_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'contract_lock_details': []}, 'options': {'memo_key': 'COCOS7nEYNaXP9P84LQA2kHArvDBTfQ8RizhYd8em3T5zfXBZj29h4i', 'extensions': [], 'votes': []}, 'active': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS7nEYNaXP9P84LQA2kHArvDBTfQ8RizhYd8em3T5zfXBZj29h4i', 1]], 'account_auths': []}, 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.5', True], 'owner': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS7nEYNaXP9P84LQA2kHArvDBTfQ8RizhYd8em3T5zfXBZj29h4i', 1]], 'account_auths': []}}, {'statistics': '2.6.10', 'registrar': '1.2.4', 'id': '1.2.10', 'committee_status': ['1.5.5', True], 'name': 'init5', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'committee_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'contract_lock_details': []}, 'options': {'memo_key': 'COCOS8LQSvCgZvwW44iJuCBkVmpR3uUh6J2VFkBJScA3vJq3gXTLCLr', 'extensions': [], 'votes': []}, 'active': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS8LQSvCgZvwW44iJuCBkVmpR3uUh6J2VFkBJScA3vJq3gXTLCLr', 1]], 'account_auths': []}, 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.6', True], 'owner': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS8LQSvCgZvwW44iJuCBkVmpR3uUh6J2VFkBJScA3vJq3gXTLCLr', 1]], 'account_auths': []}}, {'statistics': '2.6.11', 'registrar': '1.2.4', 'id': '1.2.11', 'committee_status': ['1.5.6', True], 'name': 'init6', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'committee_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'contract_lock_details': []}, 'options': {'memo_key': 'COCOS6Y5gjJG6YageUeVeoHMMLpESXFi3LdhHWB7dZsKfWQ8giEWN1z', 'extensions': [], 'votes': []}, 'active': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS6Y5gjJG6YageUeVeoHMMLpESXFi3LdhHWB7dZsKfWQ8giEWN1z', 1]], 'account_auths': []}, 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.7', True], 'owner': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS6Y5gjJG6YageUeVeoHMMLpESXFi3LdhHWB7dZsKfWQ8giEWN1z', 1]], 'account_auths': []}}, {'statistics': '2.6.12', 'registrar': '1.2.4', 'id': '1.2.12', 'committee_status': ['1.5.7', True], 'name': 'init7', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'committee_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'contract_lock_details': []}, 'options': {'memo_key': 'COCOS8aJKupmQ4XjWyAbsn58wLb2oLHfEDGMFtd7dDbFtxFpBzMGUda', 'extensions': [], 'votes': []}, 'active': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS8aJKupmQ4XjWyAbsn58wLb2oLHfEDGMFtd7dDbFtxFpBzMGUda', 1]], 'account_auths': []}, 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.8', True], 'owner': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS8aJKupmQ4XjWyAbsn58wLb2oLHfEDGMFtd7dDbFtxFpBzMGUda', 1]], 'account_auths': []}}, {'statistics': '2.6.13', 'registrar': '1.2.4', 'id': '1.2.13', 'committee_status': ['1.5.8', True], 'name': 'init8', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'committee_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'contract_lock_details': []}, 'options': {'memo_key': 'COCOS5fW5NuvGjaVQTGwcJLwogxheq2KMjm3y5ccAShJqQnB3gNkGbL', 'extensions': [], 'votes': []}, 'active': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS5fW5NuvGjaVQTGwcJLwogxheq2KMjm3y5ccAShJqQnB3gNkGbL', 1]], 'account_auths': []}, 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.9', True], 'owner': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS5fW5NuvGjaVQTGwcJLwogxheq2KMjm3y5ccAShJqQnB3gNkGbL', 1]], 'account_auths': []}}, {'statistics': '2.6.14', 'registrar': '1.2.4', 'id': '1.2.14', 'committee_status': ['1.5.9', True], 'name': 'init9', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'committee_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'contract_lock_details': []}, 'options': {'memo_key': 'COCOS5rYpiyVtxuX5PDbxHrPEsjVd6Ucz5fWJTdhvAxoPtZGSxvkE82', 'extensions': [], 'votes': []}, 'active': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS5rYpiyVtxuX5PDbxHrPEsjVd6Ucz5fWJTdhvAxoPtZGSxvkE82', 1]], 'account_auths': []}, 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.10', True], 'owner': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS5rYpiyVtxuX5PDbxHrPEsjVd6Ucz5fWJTdhvAxoPtZGSxvkE82', 1]], 'account_auths': []}}, {'statistics': '2.6.15', 'registrar': '1.2.4', 'id': '1.2.15', 'committee_status': ['1.5.10', True], 'name': 'init10', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'committee_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'contract_lock_details': []}, 'options': {'memo_key': 'COCOS6e4j3DaruANMUNsK8PMit8Sp3kA1Dw3EhJb3mpCHeZb7nTgUnP', 'extensions': [], 'votes': []}, 'active': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS6e4j3DaruANMUNsK8PMit8Sp3kA1Dw3EhJb3mpCHeZb7nTgUnP', 1]], 'account_auths': []}, 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.11', True], 'owner': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS6e4j3DaruANMUNsK8PMit8Sp3kA1Dw3EhJb3mpCHeZb7nTgUnP', 1]], 'account_auths': []}}, {'cashback_vote': '1.13.385', 'name': 'nicotest', 'membership_expiration_date': '1969-12-31T23:59:59', 'statistics': '2.6.16', 'options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': ['1:0', '1:9', '1:10', '0:11', '0:13', '0:14', '0:21']}, 'active': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]], 'account_auths': []}, 'owner': {'weight_threshold': 1, 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]], 'account_auths': []}, 'registrar': '1.2.4', 'id': '1.2.16', 'cashback_vb': '1.13.262', 'cashback_gas': '1.13.30', 'asset_locked': {'locked_total': [['1.3.0', '5000001900000']], 'vote_for_witness': {'amount': 1000000, 'asset_id': '1.3.0'}, 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'vote_for_committee': {'amount': 900000, 'asset_id': '1.3.0'}, 'contract_lock_details': []}, 'witness_status': ['1.6.13', True]}]}


setUpClass done

ssssssssssssssssssssssssssssssss>> get_contract ['contract.testapi.contractfeeshare']

{'error': {'code': 1, 'message': 'unspecified: Assert Exception: contract_itr != con_index.end(): The contract (contract.testapi.contractfeeshare) does not exist'}, 'id': 1, 'jsonrpc': '2.0'}


>> create_contract_from_file ['nicotest', 'contract.testapi.contractfeeshare', 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', '/home/ck/xukang/Cocos-Contracts-API/contract_34_contract_fee_share_test.lua', 'true']

{'id': 1, 'jsonrpc': '2.0', 'result': ['c2880c179052dfc6703ad1cf4bc493464edfde0c077e5996fcc4d515b6c18d2a', {'expiration': '2020-07-13T10:41:14', 'operations': [[34, {'data': "function test_set_percent(percent)     chainhelper:log('set_invoke_share_percent')     chainhelper:set_invoke_share_percent(percent) end  function test_helloworld()     chainhelper:log('Hi, Cocos-BCX contract') end  function test_contract_fee_share()     chainhelper:log('contract_fee_share_test') end ", 'name': 'contract.testapi.contractfeeshare', 'extensions': [], 'contract_authority': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'owner': '1.2.16'}]], 'ref_block_num': 53700, 'extensions': [], 'ref_block_prefix': 1197580326, 'signatures': ['2059c1dbbd157d93fd1a5f16ec6beda72c0fa0dd560ae3e7176a40aff222ef1520106c5cbf2761672df02dd7af47049cd7c25a68783873fef83074c2634dce3d0c']}]}


>> get_contract ['contract.testapi.contractfeeshare']

{'id': 1, 'jsonrpc': '2.0', 'result': {'is_release': False, 'contract_data': [], 'name': 'contract.testapi.contractfeeshare', 'id': '1.16.121', 'creation_date': '2020-07-13T10:20:44', 'contract_authority': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'owner': '1.2.16', 'contract_ABI': [[{'key': [2, {'v': 'test_contract_fee_share'}]}, [5, {'is_var_arg': False, 'arglist': []}]], [{'key': [2, {'v': 'test_helloworld'}]}, [5, {'is_var_arg': False, 'arglist': []}]], [{'key': [2, {'v': 'test_set_percent'}]}, [5, {'is_var_arg': False, 'arglist': ['percent']}]]], 'lua_code_b_id': '2.2.121', 'check_contract_authority': False, 'current_version': 'c2880c179052dfc6703ad1cf4bc493464edfde0c077e5996fcc4d515b6c18d2a', 'user_invoke_share_percent': 100}}


>> revise_contract_from_file ['nicotest', 'contract.testapi.contractfeeshare', '/home/ck/xukang/Cocos-Contracts-API/contract_34_contract_fee_share_test.lua', 'true']

{'id': 1, 'jsonrpc': '2.0', 'result': ['86159fd499638c55a4d5aa07fb06f55e8230aebca30658b932c239052acd6185', {'expiration': '2020-07-13T10:41:18', 'operations': [[50, {'contract_id': '1.16.121', 'data': "function test_set_percent(percent)     chainhelper:log('set_invoke_share_percent')     chainhelper:set_invoke_share_percent(percent) end  function test_helloworld()     chainhelper:log('Hi, Cocos-BCX contract') end  function test_contract_fee_share()     chainhelper:log('contract_fee_share_test') end ", 'extensions': [], 'reviser': '1.2.16'}]], 'ref_block_num': 53707, 'extensions': [], 'ref_block_prefix': 312866864, 'signatures': ['1f1dbc702dd6892d878c6475e177af9f5abc6089f3ae95098b466a394ba09093981b21c1e7ba4852aefbe2513a76d33f70ea5050db82f9d64f99453d5ffc489892']}]}


test_contract_34_contract_fee_share done

.sss>> lock []

{'id': 1, 'jsonrpc': '2.0', 'result': None}


tearDownClass done


----------------------------------------------------------------------
Ran 36 tests in 4.042s

OK (skipped=35)
ck@ubuntu:~/xukang/Cocos-Contracts-API$ 
```  

**cli_wallet查看已部署合约：**
``` text  
unlocked >>> 
get_transaction_in_block_info 86159fd499638c55a4d5aa07fb06f55e8230aebca30658b932c239052acd6185 
locked >>> get_transaction_in_block_info 86159fd499638c55a4d5aa07fb06f55e8230aebca30658b932c239052acd6185 
{
  "id": "3.1.824836",
  "block_num": 7459284,
  "trx_in_block": 0,
  "trx_hash": "86159fd499638c55a4d5aa07fb06f55e8230aebca30658b932c239052acd6185"
}

locked >>> 
get_block 7459284 
locked >>> get_block 7459284 
{
  "previous": "0071d1d33f82cdd31c68f650c571a8db6b738b68",
  "timestamp": "2020-07-13T10:20:50",
  "witness": "1.6.7",
  "transaction_merkle_root": "4cf035a07333c2228363683832a398a71990db43",
  "witness_signature": "1f02de0c6e6040d46b049098077a775388112a6328eb37662bd2eaf322ebf1101413db4e8011308dc3292b654a4282fe0f3514b3344f30c53a0a4dc71206bf6b23",
  "block_id": "0071d1d4b68cd2bf15167c33aa50c2fa5ca09df3",
  "transactions": [[
      "86159fd499638c55a4d5aa07fb06f55e8230aebca30658b932c239052acd6185",{
        "ref_block_num": 53707,
        "ref_block_prefix": 312866864,
        "expiration": "2020-07-13T10:41:18",
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
          "1f1dbc702dd6892d878c6475e177af9f5abc6089f3ae95098b466a394ba09093981b21c1e7ba4852aefbe2513a76d33f70ea5050db82f9d64f99453d5ffc489892"
        ],
        "operation_results": [[
            5,{
              "fees": [{
                  "amount": 129687,
                  "asset_id": "1.3.1"
                }
              ],
              "message": "c2880c179052dfc6703ad1cf4bc493464edfde0c077e5996fcc4d515b6c18d2a",
              "real_running_time": 364
            }
          ]
        ]
      }
    ]
  ]
}

locked >>> 
get_object 1.16.121
locked >>> get_object 1.16.121
[{
    "id": "1.16.121",
    "creation_date": "2020-07-13T10:20:44",
    "owner": "1.2.16",
    "name": "contract.testapi.contractfeeshare",
    "user_invoke_share_percent": 100,
    "current_version": "86159fd499638c55a4d5aa07fb06f55e8230aebca30658b932c239052acd6185",
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
> ("user_invoke_share_percent": 100,)  
**合约部署后，合约调用费用分摊比例：100%，也即合约调用者手续非占比100%。**  

# 3. 合约修改分摊百分比测试  
[测试代码](https://github.com/gkany/CocosBCX/blob/master/feature_test/contract_fee_share/contract_call_fee.py)  

**测试主要代码：**  
``` python  
def set_percent_test(percents):
    # percents = [48, -19, 100, 125, 0, 37]
    for percent in percents:
        try:
            print("########. set_percent {}%".format(percent))
            test_set_percent(percent=percent)
        except Exception as e:
            print("test set_percent: {} failed. exception: {}".format(percent, repr(e)))
        print("--------------- END -----------------\n")

if __name__ == '__main__':
    # print('>> {}'.format(sys.argv))
    unlock("123456")

    # main_build_tx()
    # get_contract_function_call_op_test()

    # test_helloworld(log_result=True)
    # test_helloworld(caller="init1", log_result=True)

    #test_set_percent(percent=76)
    percents = [48, -19, 100, 125, 0, 37] 
    set_percent_test(percents)

    # result = list_account_balances("init1")
    # print("result: {}".format(result))

    # result = accounts_balances(["init1", "nicotest"])
    # print("balances: {}".format(result))
    # print("============================================")
    # calc_contract_call_operation_fee(test_helloworld, ["nicotest"])
    #calc_contract_call_operation_fee(test_helloworld_owner, ["nicotest"])
    # batch_calc_contract_call_operation_fee(test_helloworld_owner, ["nicotest"], count=10)
    # calc_contract_call_operation_fee(test_helloworld_not_owner, ["nicotest", "init1"])
    #batch_calc_contract_call_operation_fee(test_helloworld_not_owner, ["nicotest", "init1"])
```  

**测试过程和结果：**  
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 contract_call_fee.py 
>> unlock ['123456']
{'id': 1, 'jsonrpc': '2.0', 'result': None}

########. set_percent 48%
>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_set_percent', [[1, {'v': 48}]], True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['011701a9e501c2092dbb2a8fc4176f826ac42be8e4488e06c5ad0ba29bd82e43', {'operations': [[35, {'function_name': 'test_set_percent', 'contract_id': '1.16.121', 'value_list': [[1, {'v': '48.00000000000000000'}]], 'caller': '1.2.16', 'extensions': []}]], 'ref_block_num': 54681, 'signatures': ['1f72e62b0ad43fa9afbb5e22761bcce751f7d5ace6249550b2042aad7fab6828ac101ddb9d28300f753bb408d62465f93c95d13af487975c1643c8b0f1bfc99213'], 'expiration': '2020-07-13T11:21:02', 'extensions': [], 'ref_block_prefix': 2894824110}]}

>> get_transaction_in_block_info ['011701a9e501c2092dbb2a8fc4176f826ac42be8e4488e06c5ad0ba29bd82e43']
{'id': 1, 'jsonrpc': '2.0', 'result': {'block_num': 7460260, 'id': '3.1.824839', 'trx_in_block': 0, 'trx_hash': '011701a9e501c2092dbb2a8fc4176f826ac42be8e4488e06c5ad0ba29bd82e43'}}

>> get_transaction_in_block_info 011701a9e501c2092dbb2a8fc4176f826ac42be8e4488e06c5ad0ba29bd82e43
 {'block_num': 7460260, 'id': '3.1.824839', 'trx_in_block': 0, 'trx_hash': '011701a9e501c2092dbb2a8fc4176f826ac42be8e4488e06c5ad0ba29bd82e43'}

>> get_block [7460260]
{'id': 1, 'jsonrpc': '2.0', 'result': {'timestamp': '2020-07-13T11:00:34', 'previous': '0071d5a3b1e6b93513f498702cc4e3dac98d6f8f', 'witness': '1.6.5', 'transactions': [['011701a9e501c2092dbb2a8fc4176f826ac42be8e4488e06c5ad0ba29bd82e43', {'operations': [[35, {'function_name': 'test_set_percent', 'contract_id': '1.16.121', 'value_list': [[1, {'v': '48.00000000000000000'}]], 'caller': '1.2.16', 'extensions': []}]], 'ref_block_num': 54681, 'signatures': ['1f72e62b0ad43fa9afbb5e22761bcce751f7d5ace6249550b2042aad7fab6828ac101ddb9d28300f753bb408d62465f93c95d13af487975c1643c8b0f1bfc99213'], 'operation_results': [[4, {'contract_id': '1.16.121', 'process_value': '', 'relevant_datasize': 37, 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'set_invoke_share_percent'}], [5, {'affected_account': '1.2.16', 'message': '100%', 'fees': [{'asset_id': '1.3.1', 'amount': 20893}]}]], 'existed_pv': False, 'fees': [{'asset_id': '1.3.0', 'amount': 20893}], 'real_running_time': 259}]], 'expiration': '2020-07-13T11:21:02', 'extensions': [], 'ref_block_prefix': 2894824110}]], 'transaction_merkle_root': '9dc1d9414864cc5ad62c8e73df10f6942ba2e0fb', 'witness_signature': '1f77fdfbde8d8d5e6c0b5a284da5ab9b6e88e96a36bb4f50de23fc6b19b32a71ef43d8f0f4a7f19323340f03da3637f60f177791e17567a536495c82eb4eb3124b', 'block_id': '0071d5a4cc0edb9dfc4ffcca5ab98831367744f8'}}

--------------- END -----------------

########. set_percent -19%
>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_set_percent', [[1, {'v': -19}]], True]
{'id': 1, 'error': {'code': 1, 'message': 'unspecified: unspecified: Try the contract resolution execution failure,[2,{"v":"Assert Exception: not_in_range: percent should be in range 0-100 "}]'}, 'jsonrpc': '2.0'}

KeyError('result',)
test set_percent: -19 failed. exception: TypeError("'NoneType' object is not subscriptable",)
--------------- END -----------------

########. set_percent 100%
>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_set_percent', [[1, {'v': 100}]], True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['7f880502fe8e239cb2f36746f00d6940df0d001bff83a040892e472486009814', {'operations': [[35, {'function_name': 'test_set_percent', 'contract_id': '1.16.121', 'value_list': [[1, {'v': '100.00000000000000000'}]], 'caller': '1.2.16', 'extensions': []}]], 'ref_block_num': 54683, 'signatures': ['205af6f69c70e89627d2497958170dded484f850d27cf10b2ea629d958f0584f3628d2352203ef4fe0a6f8a13c0592d0d428052f3d05c538c6b5e398ae0c52ed84'], 'expiration': '2020-07-13T11:21:04', 'extensions': [], 'ref_block_prefix': 1925274831}]}

>> get_transaction_in_block_info ['7f880502fe8e239cb2f36746f00d6940df0d001bff83a040892e472486009814']
{'id': 1, 'jsonrpc': '2.0', 'result': {'block_num': 7460261, 'id': '3.1.824840', 'trx_in_block': 0, 'trx_hash': '7f880502fe8e239cb2f36746f00d6940df0d001bff83a040892e472486009814'}}

>> get_transaction_in_block_info 7f880502fe8e239cb2f36746f00d6940df0d001bff83a040892e472486009814
 {'block_num': 7460261, 'id': '3.1.824840', 'trx_in_block': 0, 'trx_hash': '7f880502fe8e239cb2f36746f00d6940df0d001bff83a040892e472486009814'}

>> get_block [7460261]
{'id': 1, 'jsonrpc': '2.0', 'result': {'timestamp': '2020-07-13T11:00:36', 'previous': '0071d5a4cc0edb9dfc4ffcca5ab98831367744f8', 'witness': '1.6.1', 'transactions': [['7f880502fe8e239cb2f36746f00d6940df0d001bff83a040892e472486009814', {'operations': [[35, {'function_name': 'test_set_percent', 'contract_id': '1.16.121', 'value_list': [[1, {'v': '100.00000000000000000'}]], 'caller': '1.2.16', 'extensions': []}]], 'ref_block_num': 54683, 'signatures': ['205af6f69c70e89627d2497958170dded484f850d27cf10b2ea629d958f0584f3628d2352203ef4fe0a6f8a13c0592d0d428052f3d05c538c6b5e398ae0c52ed84'], 'operation_results': [[4, {'contract_id': '1.16.121', 'process_value': '', 'relevant_datasize': 37, 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'set_invoke_share_percent'}], [5, {'affected_account': '1.2.16', 'message': '100%', 'fees': [{'asset_id': '1.3.1', 'amount': 20922}]}]], 'existed_pv': False, 'fees': [{'asset_id': '1.3.0', 'amount': 20922}], 'real_running_time': 288}]], 'expiration': '2020-07-13T11:21:04', 'extensions': [], 'ref_block_prefix': 1925274831}]], 'transaction_merkle_root': 'c5b689bf20667d77df6e4a73cf0f39d5a7767350', 'witness_signature': '1f608545f11c4fee6c190952095cf14005d0db3a33049b63b38bc8cf5407ee09100d6d2b1418f79ea5a92a024940d9f48b48ad63643b972323af08e649ebaa9fe5', 'block_id': '0071d5a5af459949a9aed59b5f8f0b7a4459fd89'}}

--------------- END -----------------

########. set_percent 125%
>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_set_percent', [[1, {'v': 125}]], True]
{'id': 1, 'error': {'code': 1, 'message': 'unspecified: unspecified: Try the contract resolution execution failure,[2,{"v":"Assert Exception: not_in_range: percent should be in range 0-100 "}]'}, 'jsonrpc': '2.0'}

KeyError('result',)
test set_percent: 125 failed. exception: TypeError("'NoneType' object is not subscriptable",)
--------------- END -----------------

########. set_percent 0%
>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_set_percent', [[1, {'v': 0}]], True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['84848236b6caa855039b5113e39b440765f8d7a9f328b4956f6f9fa179bea91f', {'operations': [[35, {'function_name': 'test_set_percent', 'contract_id': '1.16.121', 'value_list': [[1, {'v': '0.00000000000000000'}]], 'caller': '1.2.16', 'extensions': []}]], 'ref_block_num': 54683, 'signatures': ['1f366f639502a9375eb5e2ca26fd2476049904bcb2cc07fd95398be9f4778e5f77127f0c6507eef21f3da710f543948159b1efc7fd1d434fc6969a0883204bcd5b'], 'expiration': '2020-07-13T11:21:06', 'extensions': [], 'ref_block_prefix': 1925274831}]}

>> get_transaction_in_block_info ['84848236b6caa855039b5113e39b440765f8d7a9f328b4956f6f9fa179bea91f']
{'id': 1, 'jsonrpc': '2.0', 'result': {'block_num': 7460262, 'id': '3.1.824841', 'trx_in_block': 0, 'trx_hash': '84848236b6caa855039b5113e39b440765f8d7a9f328b4956f6f9fa179bea91f'}}

>> get_transaction_in_block_info 84848236b6caa855039b5113e39b440765f8d7a9f328b4956f6f9fa179bea91f
 {'block_num': 7460262, 'id': '3.1.824841', 'trx_in_block': 0, 'trx_hash': '84848236b6caa855039b5113e39b440765f8d7a9f328b4956f6f9fa179bea91f'}

>> get_block [7460262]
{'id': 1, 'jsonrpc': '2.0', 'result': {'timestamp': '2020-07-13T11:00:38', 'previous': '0071d5a5af459949a9aed59b5f8f0b7a4459fd89', 'witness': '1.6.7', 'transactions': [['84848236b6caa855039b5113e39b440765f8d7a9f328b4956f6f9fa179bea91f', {'operations': [[35, {'function_name': 'test_set_percent', 'contract_id': '1.16.121', 'value_list': [[1, {'v': '0.00000000000000000'}]], 'caller': '1.2.16', 'extensions': []}]], 'ref_block_num': 54683, 'signatures': ['1f366f639502a9375eb5e2ca26fd2476049904bcb2cc07fd95398be9f4778e5f77127f0c6507eef21f3da710f543948159b1efc7fd1d434fc6969a0883204bcd5b'], 'operation_results': [[4, {'contract_id': '1.16.121', 'process_value': '', 'relevant_datasize': 37, 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'set_invoke_share_percent'}], [5, {'affected_account': '1.2.16', 'message': '100%', 'fees': [{'asset_id': '1.3.1', 'amount': 20965}]}]], 'existed_pv': False, 'fees': [{'asset_id': '1.3.0', 'amount': 20965}], 'real_running_time': 331}]], 'expiration': '2020-07-13T11:21:06', 'extensions': [], 'ref_block_prefix': 1925274831}]], 'transaction_merkle_root': 'a75cfb199216f0a8e90f81d47ec31ccbd505f5ec', 'witness_signature': '1f145b336a783348a500f8b3c6ef09074480e1886693faa7f56f6c888dadecb37070d7ce5babdddfcb427134f036ecac03d06a70e21c930ee9a2274895dde9bce9', 'block_id': '0071d5a61906027e12db1aa489aa6462c8ea52ba'}}

--------------- END -----------------

########. set_percent 37%
>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_set_percent', [[1, {'v': 37}]], True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['75098db29b390a7877f4d0ead3bb60ceac0ae9f93e188fb0de753b68e1158ce8', {'operations': [[35, {'function_name': 'test_set_percent', 'contract_id': '1.16.121', 'value_list': [[1, {'v': '37.00000000000000000'}]], 'caller': '1.2.16', 'extensions': []}]], 'ref_block_num': 54685, 'signatures': ['2038502042296a91065991de00f5f03f296033c0aef8b41df118854832f50fa5ef678fb822948c26c72ee0f0addc2aa52980e98cf8a37bb2070edfe1e0847870d7'], 'expiration': '2020-07-13T11:21:08', 'extensions': [], 'ref_block_prefix': 4253298050}]}

>> get_transaction_in_block_info ['75098db29b390a7877f4d0ead3bb60ceac0ae9f93e188fb0de753b68e1158ce8']
{'id': 1, 'jsonrpc': '2.0', 'result': None}

>> get_transaction_in_block_info 75098db29b390a7877f4d0ead3bb60ceac0ae9f93e188fb0de753b68e1158ce8
 None

>> get_transaction_in_block_info ['75098db29b390a7877f4d0ead3bb60ceac0ae9f93e188fb0de753b68e1158ce8']
{'id': 1, 'jsonrpc': '2.0', 'result': {'block_num': 7460263, 'id': '3.1.824842', 'trx_in_block': 0, 'trx_hash': '75098db29b390a7877f4d0ead3bb60ceac0ae9f93e188fb0de753b68e1158ce8'}}

>> get_transaction_in_block_info 75098db29b390a7877f4d0ead3bb60ceac0ae9f93e188fb0de753b68e1158ce8
 {'block_num': 7460263, 'id': '3.1.824842', 'trx_in_block': 0, 'trx_hash': '75098db29b390a7877f4d0ead3bb60ceac0ae9f93e188fb0de753b68e1158ce8'}

>> get_block [7460263]
{'id': 1, 'jsonrpc': '2.0', 'result': {'timestamp': '2020-07-13T11:00:42', 'previous': '0071d5a61906027e12db1aa489aa6462c8ea52ba', 'witness': '1.6.4', 'transactions': [['75098db29b390a7877f4d0ead3bb60ceac0ae9f93e188fb0de753b68e1158ce8', {'operations': [[35, {'function_name': 'test_set_percent', 'contract_id': '1.16.121', 'value_list': [[1, {'v': '37.00000000000000000'}]], 'caller': '1.2.16', 'extensions': []}]], 'ref_block_num': 54685, 'signatures': ['2038502042296a91065991de00f5f03f296033c0aef8b41df118854832f50fa5ef678fb822948c26c72ee0f0addc2aa52980e98cf8a37bb2070edfe1e0847870d7'], 'operation_results': [[4, {'contract_id': '1.16.121', 'process_value': '', 'relevant_datasize': 37, 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'set_invoke_share_percent'}], [5, {'affected_account': '1.2.16', 'message': '100%', 'fees': [{'asset_id': '1.3.1', 'amount': 21037}]}]], 'existed_pv': False, 'fees': [{'asset_id': '1.3.0', 'amount': 21037}], 'real_running_time': 403}]], 'expiration': '2020-07-13T11:21:08', 'extensions': [], 'ref_block_prefix': 4253298050}]], 'transaction_merkle_root': '86f524c439f51329a74c4d210cfb3ff37f12b508', 'witness_signature': '1f6b20ccb37ac182df3e4bef4a942bf0e4130bf5da0744afea3af6ebd5d310f1b5062b522d182831b07ded904630b84d3ff96813f4e93d16248634cdb1b2a72ed8', 'block_id': '0071d5a75912fb23516bf064556443e025a234a0'}}

--------------- END -----------------

ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```  

# 4. 合约调用测试  
[测试代码](https://github.com/gkany/CocosBCX/blob/master/feature_test/contract_fee_share/builder_tx.py)  

**main 部分：**  
``` python  
if __name__ == '__main__':
    # print('>> {}'.format(sys.argv))
    unlock("123456")

    print("############ 1. multi operation in transaction")
    main_build_tx()
    # get_contract_function_call_op_test()

    print("############ 2. contract owner call contranct")
    test_helloworld()
        
    print("############ 3. contract not owner call contranct")
    test_helloworld(caller="init1")

    # test_set_percent()
```  

**合约测试过程和结果：**  
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 builder_tx.py 
>> unlock ['123456']
{'jsonrpc': '2.0', 'id': 1, 'result': None}

############ 1. multi operation in transaction
>> begin_builder_transaction []
{'jsonrpc': '2.0', 'id': 1, 'result': 0}

>> transfer ['nicotest', 'init0', 23, 'COCOS', ['', False], False]
{'jsonrpc': '2.0', 'id': 1, 'result': ['50b3f09021639ef0354cde6fdc938ee1c42c7788cc0614f364cfabf65abac6da', {'expiration': '2020-07-13T11:30:28', 'ref_block_prefix': 2677801849, 'extensions': [], 'ref_block_num': 54913, 'operations': [[0, {'amount': {'amount': 2300000, 'asset_id': '1.3.0'}, 'from': '1.2.16', 'to': '1.2.5', 'extensions': []}]], 'signatures': ['203be7277230a4f3f80483a092c2b2a7075184c00ac521ddbcf0a45a7d830ea3044422d0b35776fe98d17b180f208aa3bc61f3643bc76684f2b6f4c78d15e07479']}]}

>> add_operation_to_builder_transaction [0, [0, {'amount': {'amount': 2300000, 'asset_id': '1.3.0'}, 'from': '1.2.16', 'to': '1.2.5', 'extensions': []}]]
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], False]
{'jsonrpc': '2.0', 'id': 1, 'result': ['334604362bd65c7f2aa8179e5ef79adc437d76c3ff5c8811456ca47b0602231c', {'expiration': '2020-07-13T11:30:28', 'ref_block_prefix': 2677801849, 'extensions': [], 'ref_block_num': 54913, 'operations': [[35, {'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.121', 'extensions': [], 'value_list': []}]], 'signatures': ['1f1ec1c2798da312ceee0cdadbdbccfced394a773fc738a383bc3eeb609a7b85f23ecc1f594f560d9c943d496aaca893c027fbcabe586761bbdb7ed0c610687738']}]}

>> add_operation_to_builder_transaction [0, [35, {'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.121', 'extensions': [], 'value_list': []}]]
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], False]
{'jsonrpc': '2.0', 'id': 1, 'result': ['e6348c9412165a8eaefb567472d5b4ee4bf1b4eb1622de5486ebd4645ef64f8c', {'expiration': '2020-07-13T11:30:28', 'ref_block_prefix': 2677801849, 'extensions': [], 'ref_block_num': 54913, 'operations': [[35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.121', 'extensions': [], 'value_list': []}]], 'signatures': ['20230c7d5bc6e94ae1a097e211e3b0944e510952bd68487efbb60deaf736bfe56b0ebd90b30bbb7ad34b06386a3f3f028e4724d6e742a49e2d04364fd57aa48543']}]}

>> add_operation_to_builder_transaction [0, [35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.121', 'extensions': [], 'value_list': []}]]
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> transfer ['nicotest', 'init1', 78, 'COCOS', ['', False], False]
{'jsonrpc': '2.0', 'id': 1, 'result': ['223916412e802ab641eb54ecd3369ab6aee127d037fdc560ae95adf5345c80a9', {'expiration': '2020-07-13T11:30:28', 'ref_block_prefix': 2677801849, 'extensions': [], 'ref_block_num': 54913, 'operations': [[0, {'amount': {'amount': 7800000, 'asset_id': '1.3.0'}, 'from': '1.2.16', 'to': '1.2.6', 'extensions': []}]], 'signatures': ['1f7e60343e3acb014e7972d530aa88b96bdd8c01a522531e68b068f5c101336aa81e54113eb8837850454260d74237a3ab1fff043412c65b81a4aa5eaef2176826']}]}

>> add_operation_to_builder_transaction [0, [0, {'amount': {'amount': 7800000, 'asset_id': '1.3.0'}, 'from': '1.2.16', 'to': '1.2.6', 'extensions': []}]]
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> preview_builder_transaction [0]
{'jsonrpc': '2.0', 'id': 1, 'result': {'extensions': [], 'operations': [[0, {'amount': {'amount': 2300000, 'asset_id': '1.3.0'}, 'from': '1.2.16', 'to': '1.2.5', 'extensions': []}], [35, {'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.121', 'extensions': [], 'value_list': []}], [35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.121', 'extensions': [], 'value_list': []}], [0, {'amount': {'amount': 7800000, 'asset_id': '1.3.0'}, 'from': '1.2.16', 'to': '1.2.6', 'extensions': []}]], 'ref_block_prefix': 0, 'expiration': '1970-01-01T00:00:00', 'ref_block_num': 0}}

>> sign_builder_transaction [0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['971f1eea1c1eed22c66843bb732b875f2d6791faf47a3f43402791c613a1e2b4', {'expiration': '2020-07-13T11:30:28', 'ref_block_prefix': 2677801849, 'extensions': [], 'ref_block_num': 54913, 'operations': [[0, {'amount': {'amount': 2300000, 'asset_id': '1.3.0'}, 'from': '1.2.16', 'to': '1.2.5', 'extensions': []}], [35, {'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.121', 'extensions': [], 'value_list': []}], [35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.121', 'extensions': [], 'value_list': []}], [0, {'amount': {'amount': 7800000, 'asset_id': '1.3.0'}, 'from': '1.2.16', 'to': '1.2.6', 'extensions': []}]], 'signatures': ['206ccc9cfa2ebc30fc43f864f05a11bb7d670eba0694b6f60955d736a5d2e452e058815742a38287452c5bc41662ae9b5ed0b7f30fa905c69a7455b20ba5dfd547', '1f1e2ead44627d4125a2e3d7afeb8ad0d3b8360036b01accdf39939f3b1f5be940342dd782deb1377d0ec2df3d7b2be07c1d607171dd44c9ea79e8ae0e9c047093']}]}

>> get_transaction_in_block_info ['971f1eea1c1eed22c66843bb732b875f2d6791faf47a3f43402791c613a1e2b4']
{'jsonrpc': '2.0', 'id': 1, 'result': {'id': '3.1.824843', 'trx_in_block': 0, 'trx_hash': '971f1eea1c1eed22c66843bb732b875f2d6791faf47a3f43402791c613a1e2b4', 'block_num': 7460492}}

>> get_transaction_in_block_info 971f1eea1c1eed22c66843bb732b875f2d6791faf47a3f43402791c613a1e2b4
 {'id': '3.1.824843', 'trx_in_block': 0, 'trx_hash': '971f1eea1c1eed22c66843bb732b875f2d6791faf47a3f43402791c613a1e2b4', 'block_num': 7460492}

>> get_block [7460492]
{'jsonrpc': '2.0', 'id': 1, 'result': {'previous': '0071d68b33dbcb5c3048839c1ef315c136e188c1', 'witness_signature': '1f324e7b45123dc9f11864eebc396cc73feb795d3109f9a0c15fa0138b473f280b2c0142dc900bf503b3c0f74f74576fbddd9e2aae77e584e16f3efdfaed11289b', 'timestamp': '2020-07-13T11:10:00', 'witness': '1.6.10', 'block_id': '0071d68c4075da7960d358a627289976c940fb7e', 'transaction_merkle_root': '81a9ed0cbe7f04932a5c524391ebc9fb229e60b6', 'transactions': [['971f1eea1c1eed22c66843bb732b875f2d6791faf47a3f43402791c613a1e2b4', {'expiration': '2020-07-13T11:30:28', 'ref_block_prefix': 2677801849, 'extensions': [], 'ref_block_num': 54913, 'operations': [[0, {'amount': {'amount': 2300000, 'asset_id': '1.3.0'}, 'from': '1.2.16', 'to': '1.2.5', 'extensions': []}], [35, {'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.121', 'extensions': [], 'value_list': []}], [35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.121', 'extensions': [], 'value_list': []}], [0, {'amount': {'amount': 7800000, 'asset_id': '1.3.0'}, 'from': '1.2.16', 'to': '1.2.6', 'extensions': []}]], 'signatures': ['206ccc9cfa2ebc30fc43f864f05a11bb7d670eba0694b6f60955d736a5d2e452e058815742a38287452c5bc41662ae9b5ed0b7f30fa905c69a7455b20ba5dfd547', '1f1e2ead44627d4125a2e3d7afeb8ad0d3b8360036b01accdf39939f3b1f5be940342dd782deb1377d0ec2df3d7b2be07c1d607171dd44c9ea79e8ae0e9c047093'], 'operation_results': [[1, {'fees': [{'amount': 10000, 'asset_id': '1.3.1'}], 'real_running_time': 39}], [4, {'process_value': '', 'real_running_time': 219, 'fees': [{'amount': 20735, 'asset_id': '1.3.0'}], 'relevant_datasize': 35, 'contract_id': '1.16.121', 'existed_pv': False, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'fees': [{'amount': 20735, 'asset_id': '1.3.1'}], 'message': '100%', 'affected_account': '1.2.16'}]]}], [4, {'process_value': '', 'real_running_time': 135, 'fees': [{'amount': 20651, 'asset_id': '1.3.0'}], 'relevant_datasize': 35, 'contract_id': '1.16.121', 'existed_pv': False, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}], [5, {'fees': [{'amount': 7641, 'asset_id': '1.3.0'}], 'message': '37%', 'affected_account': '1.2.6'}], [5, {'fees': [{'amount': 13010, 'asset_id': '1.3.1'}], 'message': '63%', 'affected_account': '1.2.16'}]]}], [1, {'fees': [{'amount': 10000, 'asset_id': '1.3.1'}], 'real_running_time': 22}]]}]]}}

############ 2. contract owner call contranct
>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['fa77e2cfab612302915adacc3a7c44e8bab465d97a669bba025a0dff39e9575c', {'expiration': '2020-07-13T11:30:30', 'ref_block_prefix': 451646035, 'extensions': [], 'ref_block_num': 54914, 'operations': [[35, {'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.121', 'extensions': [], 'value_list': []}]], 'signatures': ['207a3c3d292b1fd4550227b67d7e24f6bd71f69b2336fda62a8680fb8f42f4bb3e1920f35c213d093433caaa9ae13dc095b58f1d73762964973f6620da0266415c']}]}

>> get_transaction_in_block_info ['fa77e2cfab612302915adacc3a7c44e8bab465d97a669bba025a0dff39e9575c']
{'jsonrpc': '2.0', 'id': 1, 'result': {'id': '3.1.824844', 'trx_in_block': 0, 'trx_hash': 'fa77e2cfab612302915adacc3a7c44e8bab465d97a669bba025a0dff39e9575c', 'block_num': 7460493}}

>> get_transaction_in_block_info fa77e2cfab612302915adacc3a7c44e8bab465d97a669bba025a0dff39e9575c
 {'id': '3.1.824844', 'trx_in_block': 0, 'trx_hash': 'fa77e2cfab612302915adacc3a7c44e8bab465d97a669bba025a0dff39e9575c', 'block_num': 7460493}

>> get_block [7460493]
{'jsonrpc': '2.0', 'id': 1, 'result': {'previous': '0071d68c4075da7960d358a627289976c940fb7e', 'witness_signature': '2052aff8b4ae9bde86fb6bf0ce66ffe2d62222e8c8439fdbd79ea5809f51147b0064b85e2de9b0e64b63f056c4cd28f118989d86f4fcf7577c12ee2eb8f149680a', 'timestamp': '2020-07-13T11:10:02', 'witness': '1.6.2', 'block_id': '0071d68db805a3f94d1b3982e62168c592620b36', 'transaction_merkle_root': 'c2fbb0bc144ceed52940c08b470e1a984b894c38', 'transactions': [['fa77e2cfab612302915adacc3a7c44e8bab465d97a669bba025a0dff39e9575c', {'expiration': '2020-07-13T11:30:30', 'ref_block_prefix': 451646035, 'extensions': [], 'ref_block_num': 54914, 'operations': [[35, {'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.121', 'extensions': [], 'value_list': []}]], 'signatures': ['207a3c3d292b1fd4550227b67d7e24f6bd71f69b2336fda62a8680fb8f42f4bb3e1920f35c213d093433caaa9ae13dc095b58f1d73762964973f6620da0266415c'], 'operation_results': [[4, {'process_value': '', 'real_running_time': 351, 'fees': [{'amount': 20867, 'asset_id': '1.3.0'}], 'relevant_datasize': 35, 'contract_id': '1.16.121', 'existed_pv': False, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'fees': [{'amount': 20867, 'asset_id': '1.3.1'}], 'message': '100%', 'affected_account': '1.2.16'}]]}]]}]]}}

############ 3. contract not owner call contranct
>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['beb01196e85191c956fb9abbed300cd15bac6201caade88cf0a6a6a879ac79ab', {'expiration': '2020-07-13T11:30:32', 'ref_block_prefix': 451646035, 'extensions': [], 'ref_block_num': 54914, 'operations': [[35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.121', 'extensions': [], 'value_list': []}]], 'signatures': ['2054d38df69d86e23b7047dd5e89fedffd9378375b0337f3a5607f74dba46319c504373b2174c9b42837bb988a345ae51b652bfbe5d86da52fa51e539d75901331']}]}

>> get_transaction_in_block_info ['beb01196e85191c956fb9abbed300cd15bac6201caade88cf0a6a6a879ac79ab']
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> get_transaction_in_block_info beb01196e85191c956fb9abbed300cd15bac6201caade88cf0a6a6a879ac79ab
 None

>> get_transaction_in_block_info ['beb01196e85191c956fb9abbed300cd15bac6201caade88cf0a6a6a879ac79ab']
{'jsonrpc': '2.0', 'id': 1, 'result': {'id': '3.1.824845', 'trx_in_block': 0, 'trx_hash': 'beb01196e85191c956fb9abbed300cd15bac6201caade88cf0a6a6a879ac79ab', 'block_num': 7460494}}

>> get_transaction_in_block_info beb01196e85191c956fb9abbed300cd15bac6201caade88cf0a6a6a879ac79ab
 {'id': '3.1.824845', 'trx_in_block': 0, 'trx_hash': 'beb01196e85191c956fb9abbed300cd15bac6201caade88cf0a6a6a879ac79ab', 'block_num': 7460494}

>> get_block [7460494]
{'jsonrpc': '2.0', 'id': 1, 'result': {'previous': '0071d68db805a3f94d1b3982e62168c592620b36', 'witness_signature': '205e21c12efe7d07d18ef975821a94199d39b46e4bf30cc6790166c0585cb33fe6772478911a7ed4a63e7e13cc8126dca674b1b8073e9e00510f025396357419d4', 'timestamp': '2020-07-13T11:10:06', 'witness': '1.6.1', 'block_id': '0071d68ef3a0025fd107c7fd0dfbc63437a1ddbd', 'transaction_merkle_root': 'ea648f5ea1c6a82c79c52c52a7b5fba3fbc4b4cb', 'transactions': [['beb01196e85191c956fb9abbed300cd15bac6201caade88cf0a6a6a879ac79ab', {'expiration': '2020-07-13T11:30:32', 'ref_block_prefix': 451646035, 'extensions': [], 'ref_block_num': 54914, 'operations': [[35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.121', 'extensions': [], 'value_list': []}]], 'signatures': ['2054d38df69d86e23b7047dd5e89fedffd9378375b0337f3a5607f74dba46319c504373b2174c9b42837bb988a345ae51b652bfbe5d86da52fa51e539d75901331'], 'operation_results': [[4, {'process_value': '', 'real_running_time': 399, 'fees': [{'amount': 20915, 'asset_id': '1.3.0'}], 'relevant_datasize': 35, 'contract_id': '1.16.121', 'existed_pv': False, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}], [5, {'fees': [{'amount': 7739, 'asset_id': '1.3.0'}], 'message': '37%', 'affected_account': '1.2.6'}], [5, {'fees': [{'amount': 13176, 'asset_id': '1.3.1'}], 'message': '63%', 'affected_account': '1.2.16'}]]}]]}]]}}

ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```  

# 5. 手续费测试  
[测试代码](https://github.com/gkany/CocosBCX/blob/master/feature_test/contract_fee_share/contract_call_fee.py)  

**main主要部分：**  
``` python  
if __name__ == '__main__':
    # print('>> {}'.format(sys.argv))
    unlock("123456")

    # main_build_tx()
    # get_contract_function_call_op_test()

    # test_helloworld(log_result=True)
    # test_helloworld(caller="init1", log_result=True)

    #test_set_percent(percent=76)
    #percents = [48, -19, 100, 125, 0, 37]
    #set_percent_test(percents)

    # result = list_account_balances("init1")
    # print("result: {}".format(result))

    # result = accounts_balances(["init1", "nicotest"])
    # print("balances: {}".format(result))
    # print("============================================")
    # calc_contract_call_operation_fee(test_helloworld, ["nicotest"])
    calc_contract_call_operation_fee(test_helloworld_owner, ["nicotest"])
    batch_calc_contract_call_operation_fee(test_helloworld_owner, ["nicotest"], count=10)
    calc_contract_call_operation_fee(test_helloworld_not_owner, ["nicotest", "init1"])
    batch_calc_contract_call_operation_fee(test_helloworld_not_owner, ["nicotest", "init1"])
```  

**测试过程和结果：**  
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 contract_call_fee.py 
>> unlock ['123456']
{'result': None, 'jsonrpc': '2.0', 'id': 1}

>> get_account ['nicotest']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'name': 'nicotest', 'id': '1.2.16', 'cashback_gas': '1.13.30', 'cashback_vote': '1.13.385', 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.13', True], 'asset_locked': {'locked_total': [['1.3.0', '5000001900000']], 'vote_for_witness': {'amount': 1000000, 'asset_id': '1.3.0'}, 'contract_lock_details': [], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'vote_for_committee': {'amount': 900000, 'asset_id': '1.3.0'}}, 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'registrar': '1.2.4', 'cashback_vb': '1.13.262', 'options': {'extensions': [], 'votes': ['1:0', '1:9', '1:10', '0:11', '0:13', '0:14', '0:21'], 'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx'}, 'statistics': '2.6.16'}, 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271338663', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['5179990587dd824f04178ba7ba070511131eafa53c5bd03b463a3bd963a9932a', {'extensions': [], 'signatures': ['204e231f386f15a0f231cd2433165529b44351d8d471cda1af7b24006f06d13d2075172909aef133b5086f4ffeb40b4a44048cb427c7e0ce78e0ef27678a2be431'], 'ref_block_prefix': 1059129019, 'expiration': '2020-07-13T11:36:18', 'ref_block_num': 55056, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['5179990587dd824f04178ba7ba070511131eafa53c5bd03b463a3bd963a9932a']
{'result': {'trx_hash': '5179990587dd824f04178ba7ba070511131eafa53c5bd03b463a3bd963a9932a', 'block_num': 7460636, 'id': '3.1.824846', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info 5179990587dd824f04178ba7ba070511131eafa53c5bd03b463a3bd963a9932a
 {'trx_hash': '5179990587dd824f04178ba7ba070511131eafa53c5bd03b463a3bd963a9932a', 'block_num': 7460636, 'id': '3.1.824846', 'trx_in_block': 0}

>> get_block [7460636]
{'result': {'block_id': '0071d71c91723a8ed886efd7c114fbab06d445bb', 'timestamp': '2020-07-13T11:15:50', 'transaction_merkle_root': 'a76e452a5901aa28fb86e113b3f1ed81fbacebd8', 'witness': '1.6.5', 'previous': '0071d71b9c12966158b925bed3cb5481b4390b84', 'witness_signature': '1f498d9e39dd915d01ca2fbdd9a13efc391c013ec85fceea73e4592cebe93ceaf915b4e1a0f3858c76279820d385f9a801e23971f4555b927e477c79332b01908f', 'transactions': [['5179990587dd824f04178ba7ba070511131eafa53c5bd03b463a3bd963a9932a', {'extensions': [], 'operation_results': [[4, {'fees': [{'amount': 20803, 'asset_id': '1.3.0'}], 'existed_pv': False, 'process_value': '', 'real_running_time': 287, 'contract_id': '1.16.121', 'relevant_datasize': 35, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20803, 'asset_id': '1.3.1'}]}]]}]], 'signatures': ['204e231f386f15a0f231cd2433165529b44351d8d471cda1af7b24006f06d13d2075172909aef133b5086f4ffeb40b4a44048cb427c7e0ce78e0ef27678a2be431'], 'ref_block_prefix': 1059129019, 'expiration': '2020-07-13T11:36:18', 'ref_block_num': 55056, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}]]}, 'jsonrpc': '2.0', 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 20803, 'asset_id': '1.3.0'}]
### {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20803, 'asset_id': '1.3.1'}]}, total_fee: 20803
### [COCOS] fee_total_in_block: 20803, fee_total_range_accounts: 20803
### account_balances delta in block: 
  {'1.2.16': {'1.3.1': 20803}}
-----------------------------------------------------------------------

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271317860', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

-------------------- contract owner and caller acccount_balances changed --------------------
>>> contract call op before account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271338663', 'asset_id': '1.3.1'}]}
>>> contract call op before         account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271317860', 'asset_id': '1.3.1'}]}
>>> account_balances delta: 
  {'1.2.16': {'1.3.1': 20803}}
---------------------------------------------------------------------------------------------

func_accounts_balances: {'1.2.16': {'1.3.1': 20803}}
calc_accounts_balances: {'1.2.16': {'1.3.1': 20803}}
******************* calc_contract_call_operation_fee END ************************************

accounts: ['nicotest'], count: 10
index = 0
>> get_account ['nicotest']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'name': 'nicotest', 'id': '1.2.16', 'cashback_gas': '1.13.30', 'cashback_vote': '1.13.385', 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.13', True], 'asset_locked': {'locked_total': [['1.3.0', '5000001900000']], 'vote_for_witness': {'amount': 1000000, 'asset_id': '1.3.0'}, 'contract_lock_details': [], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'vote_for_committee': {'amount': 900000, 'asset_id': '1.3.0'}}, 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'registrar': '1.2.4', 'cashback_vb': '1.13.262', 'options': {'extensions': [], 'votes': ['1:0', '1:9', '1:10', '0:11', '0:13', '0:14', '0:21'], 'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx'}, 'statistics': '2.6.16'}, 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271317860', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['ba336ac531012bf97e8df6e69dd70db4182965b04107c2282e1aa17df4bec289', {'extensions': [], 'signatures': ['1f43853b91401ffd6204588de725878ebbf04c85bf0a6ad31d4dc5d4a201b8b71d32eb5ce287fb1ccc41d4fcca028078270a451230b45894f5a11e5d9d652cfc79'], 'ref_block_prefix': 1059129019, 'expiration': '2020-07-13T11:36:20', 'ref_block_num': 55056, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['ba336ac531012bf97e8df6e69dd70db4182965b04107c2282e1aa17df4bec289']
{'result': {'trx_hash': 'ba336ac531012bf97e8df6e69dd70db4182965b04107c2282e1aa17df4bec289', 'block_num': 7460637, 'id': '3.1.824847', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ba336ac531012bf97e8df6e69dd70db4182965b04107c2282e1aa17df4bec289
 {'trx_hash': 'ba336ac531012bf97e8df6e69dd70db4182965b04107c2282e1aa17df4bec289', 'block_num': 7460637, 'id': '3.1.824847', 'trx_in_block': 0}

>> get_block [7460637]
{'result': {'block_id': '0071d71dd56189925a4c1e1198695e6d6e68621c', 'timestamp': '2020-07-13T11:15:52', 'transaction_merkle_root': 'fbc9ba6da86a873391757f9af539d234318bbfc4', 'witness': '1.6.1', 'previous': '0071d71c91723a8ed886efd7c114fbab06d445bb', 'witness_signature': '206bef27f3ae8f31e6eb46a67cebaed9264f7cc6007d93e93afc100607d47f0a8c5121ae1c4a8f932fdf1d3e9b230a995c3f1d1b71721ca6677eae54f909f55c15', 'transactions': [['ba336ac531012bf97e8df6e69dd70db4182965b04107c2282e1aa17df4bec289', {'extensions': [], 'operation_results': [[4, {'fees': [{'amount': 20872, 'asset_id': '1.3.0'}], 'existed_pv': False, 'process_value': '', 'real_running_time': 356, 'contract_id': '1.16.121', 'relevant_datasize': 35, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20872, 'asset_id': '1.3.1'}]}]]}]], 'signatures': ['1f43853b91401ffd6204588de725878ebbf04c85bf0a6ad31d4dc5d4a201b8b71d32eb5ce287fb1ccc41d4fcca028078270a451230b45894f5a11e5d9d652cfc79'], 'ref_block_prefix': 1059129019, 'expiration': '2020-07-13T11:36:20', 'ref_block_num': 55056, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}]]}, 'jsonrpc': '2.0', 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 20872, 'asset_id': '1.3.0'}]
### {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20872, 'asset_id': '1.3.1'}]}, total_fee: 20872
### [COCOS] fee_total_in_block: 20872, fee_total_range_accounts: 20872
### account_balances delta in block: 
  {'1.2.16': {'1.3.1': 20872}}
-----------------------------------------------------------------------

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271296988', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

-------------------- contract owner and caller acccount_balances changed --------------------
>>> contract call op before account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271317860', 'asset_id': '1.3.1'}]}
>>> contract call op before         account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271296988', 'asset_id': '1.3.1'}]}
>>> account_balances delta: 
  {'1.2.16': {'1.3.1': 20872}}
---------------------------------------------------------------------------------------------

func_accounts_balances: {'1.2.16': {'1.3.1': 20872}}
calc_accounts_balances: {'1.2.16': {'1.3.1': 20872}}
******************* calc_contract_call_operation_fee END ************************************

index = 1
>> get_account ['nicotest']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'name': 'nicotest', 'id': '1.2.16', 'cashback_gas': '1.13.30', 'cashback_vote': '1.13.385', 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.13', True], 'asset_locked': {'locked_total': [['1.3.0', '5000001900000']], 'vote_for_witness': {'amount': 1000000, 'asset_id': '1.3.0'}, 'contract_lock_details': [], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'vote_for_committee': {'amount': 900000, 'asset_id': '1.3.0'}}, 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'registrar': '1.2.4', 'cashback_vb': '1.13.262', 'options': {'extensions': [], 'votes': ['1:0', '1:9', '1:10', '0:11', '0:13', '0:14', '0:21'], 'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx'}, 'statistics': '2.6.16'}, 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271296988', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['1b54d313dea312641cee77a05c9b44f34330cf7f94cba755f3058f55f52b0e45', {'extensions': [], 'signatures': ['1f6a599184a50e7e247f77b1f6cb3a63f32fdccda6727a9affd111eddd1a64528f4f9b5305f011b9ffb0e585ac7ed350ca9dde9f61d73eeb9c4daa0f04970fb20e'], 'ref_block_prefix': 307887193, 'expiration': '2020-07-13T11:36:22', 'ref_block_num': 55061, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['1b54d313dea312641cee77a05c9b44f34330cf7f94cba755f3058f55f52b0e45']
{'result': {'trx_hash': '1b54d313dea312641cee77a05c9b44f34330cf7f94cba755f3058f55f52b0e45', 'block_num': 7460638, 'id': '3.1.824848', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info 1b54d313dea312641cee77a05c9b44f34330cf7f94cba755f3058f55f52b0e45
 {'trx_hash': '1b54d313dea312641cee77a05c9b44f34330cf7f94cba755f3058f55f52b0e45', 'block_num': 7460638, 'id': '3.1.824848', 'trx_in_block': 0}

>> get_block [7460638]
{'result': {'block_id': '0071d71e18e6dd3385596e71ce75c246811fb4eb', 'timestamp': '2020-07-13T11:15:54', 'transaction_merkle_root': '541a35bedc02fbf19ef3d0dff89b878c0916d8fa', 'witness': '1.6.2', 'previous': '0071d71dd56189925a4c1e1198695e6d6e68621c', 'witness_signature': '2050f0754dd5fe99005e24927c438165e19c31efe719bf9cb55d34f2e78961d5c7099c97c07a05cffdddc248671542466b8eb5584029ecf59a54ec9c784c1be1f1', 'transactions': [['1b54d313dea312641cee77a05c9b44f34330cf7f94cba755f3058f55f52b0e45', {'extensions': [], 'operation_results': [[4, {'fees': [{'amount': 20847, 'asset_id': '1.3.0'}], 'existed_pv': False, 'process_value': '', 'real_running_time': 331, 'contract_id': '1.16.121', 'relevant_datasize': 35, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20847, 'asset_id': '1.3.1'}]}]]}]], 'signatures': ['1f6a599184a50e7e247f77b1f6cb3a63f32fdccda6727a9affd111eddd1a64528f4f9b5305f011b9ffb0e585ac7ed350ca9dde9f61d73eeb9c4daa0f04970fb20e'], 'ref_block_prefix': 307887193, 'expiration': '2020-07-13T11:36:22', 'ref_block_num': 55061, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}]]}, 'jsonrpc': '2.0', 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 20847, 'asset_id': '1.3.0'}]
### {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20847, 'asset_id': '1.3.1'}]}, total_fee: 20847
### [COCOS] fee_total_in_block: 20847, fee_total_range_accounts: 20847
### account_balances delta in block: 
  {'1.2.16': {'1.3.1': 20847}}
-----------------------------------------------------------------------

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271276141', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

-------------------- contract owner and caller acccount_balances changed --------------------
>>> contract call op before account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271296988', 'asset_id': '1.3.1'}]}
>>> contract call op before         account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271276141', 'asset_id': '1.3.1'}]}
>>> account_balances delta: 
  {'1.2.16': {'1.3.1': 20847}}
---------------------------------------------------------------------------------------------

func_accounts_balances: {'1.2.16': {'1.3.1': 20847}}
calc_accounts_balances: {'1.2.16': {'1.3.1': 20847}}
******************* calc_contract_call_operation_fee END ************************************

index = 2
>> get_account ['nicotest']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'name': 'nicotest', 'id': '1.2.16', 'cashback_gas': '1.13.30', 'cashback_vote': '1.13.385', 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.13', True], 'asset_locked': {'locked_total': [['1.3.0', '5000001900000']], 'vote_for_witness': {'amount': 1000000, 'asset_id': '1.3.0'}, 'contract_lock_details': [], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'vote_for_committee': {'amount': 900000, 'asset_id': '1.3.0'}}, 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'registrar': '1.2.4', 'cashback_vb': '1.13.262', 'options': {'extensions': [], 'votes': ['1:0', '1:9', '1:10', '0:11', '0:13', '0:14', '0:21'], 'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx'}, 'statistics': '2.6.16'}, 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271276141', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['51695e93fe8e56d20de1a205e1d2501557dbd33598d25dba184d22c7dfe68ac1', {'extensions': [], 'signatures': ['207b1578762366d9758c582a2371c92710766e09f2673e50400e08798799287d8e5088c0f628986aeeb7eac006d9d5aaddf9873f60667b49a8039be595b83fca2e'], 'ref_block_prefix': 331538414, 'expiration': '2020-07-13T11:36:24', 'ref_block_num': 55062, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['51695e93fe8e56d20de1a205e1d2501557dbd33598d25dba184d22c7dfe68ac1']
{'result': {'trx_hash': '51695e93fe8e56d20de1a205e1d2501557dbd33598d25dba184d22c7dfe68ac1', 'block_num': 7460639, 'id': '3.1.824849', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info 51695e93fe8e56d20de1a205e1d2501557dbd33598d25dba184d22c7dfe68ac1
 {'trx_hash': '51695e93fe8e56d20de1a205e1d2501557dbd33598d25dba184d22c7dfe68ac1', 'block_num': 7460639, 'id': '3.1.824849', 'trx_in_block': 0}

>> get_block [7460639]
{'result': {'block_id': '0071d71fd32c2b9ec3fd25dca28cd8fcaf643b5f', 'timestamp': '2020-07-13T11:15:58', 'transaction_merkle_root': '7b4cbcb3aad80165ffdbec10cef316d5fd2b4cf9', 'witness': '1.6.6', 'previous': '0071d71e18e6dd3385596e71ce75c246811fb4eb', 'witness_signature': '2075109c5abe61100a4b54d094578cb5a45e9f2e4c6cc9d76c2d5d0e5803f3d21f19c07921703eb0201511c2b051efef29c2eeecf26c83a6ef4920820ff7c6c530', 'transactions': [['51695e93fe8e56d20de1a205e1d2501557dbd33598d25dba184d22c7dfe68ac1', {'extensions': [], 'operation_results': [[4, {'fees': [{'amount': 20994, 'asset_id': '1.3.0'}], 'existed_pv': False, 'process_value': '', 'real_running_time': 478, 'contract_id': '1.16.121', 'relevant_datasize': 35, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20994, 'asset_id': '1.3.1'}]}]]}]], 'signatures': ['207b1578762366d9758c582a2371c92710766e09f2673e50400e08798799287d8e5088c0f628986aeeb7eac006d9d5aaddf9873f60667b49a8039be595b83fca2e'], 'ref_block_prefix': 331538414, 'expiration': '2020-07-13T11:36:24', 'ref_block_num': 55062, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}]]}, 'jsonrpc': '2.0', 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 20994, 'asset_id': '1.3.0'}]
### {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20994, 'asset_id': '1.3.1'}]}, total_fee: 20994
### [COCOS] fee_total_in_block: 20994, fee_total_range_accounts: 20994
### account_balances delta in block: 
  {'1.2.16': {'1.3.1': 20994}}
-----------------------------------------------------------------------

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271255147', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

-------------------- contract owner and caller acccount_balances changed --------------------
>>> contract call op before account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271276141', 'asset_id': '1.3.1'}]}
>>> contract call op before         account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271255147', 'asset_id': '1.3.1'}]}
>>> account_balances delta: 
  {'1.2.16': {'1.3.1': 20994}}
---------------------------------------------------------------------------------------------

func_accounts_balances: {'1.2.16': {'1.3.1': 20994}}
calc_accounts_balances: {'1.2.16': {'1.3.1': 20994}}
******************* calc_contract_call_operation_fee END ************************************

index = 3
>> get_account ['nicotest']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'name': 'nicotest', 'id': '1.2.16', 'cashback_gas': '1.13.30', 'cashback_vote': '1.13.385', 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.13', True], 'asset_locked': {'locked_total': [['1.3.0', '5000001900000']], 'vote_for_witness': {'amount': 1000000, 'asset_id': '1.3.0'}, 'contract_lock_details': [], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'vote_for_committee': {'amount': 900000, 'asset_id': '1.3.0'}}, 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'registrar': '1.2.4', 'cashback_vb': '1.13.262', 'options': {'extensions': [], 'votes': ['1:0', '1:9', '1:10', '0:11', '0:13', '0:14', '0:21'], 'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx'}, 'statistics': '2.6.16'}, 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271255147', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['452060f095dd680df8749963b899e52fdb81fa112cbbd5b04ec14b032e587168', {'extensions': [], 'signatures': ['2038bacbcbadd5dbf5be48d2e87e63ff77a2a77bf94df52ebd9934ebdd1bbd0db234c3ae8f1e0d142f15cd8b8430a85fef27da1b8d09f1d855d2299a2f7903d9fb'], 'ref_block_prefix': 2355078845, 'expiration': '2020-07-13T11:36:28', 'ref_block_num': 55063, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['452060f095dd680df8749963b899e52fdb81fa112cbbd5b04ec14b032e587168']
{'result': {'trx_hash': '452060f095dd680df8749963b899e52fdb81fa112cbbd5b04ec14b032e587168', 'block_num': 7460640, 'id': '3.1.824850', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info 452060f095dd680df8749963b899e52fdb81fa112cbbd5b04ec14b032e587168
 {'trx_hash': '452060f095dd680df8749963b899e52fdb81fa112cbbd5b04ec14b032e587168', 'block_num': 7460640, 'id': '3.1.824850', 'trx_in_block': 0}

>> get_block [7460640]
{'result': {'block_id': '0071d720f833b1299132d707e99037646030cb05', 'timestamp': '2020-07-13T11:16:00', 'transaction_merkle_root': '5a126d7648df094d917cf30f87ed6442ceed1118', 'witness': '1.6.3', 'previous': '0071d71fd32c2b9ec3fd25dca28cd8fcaf643b5f', 'witness_signature': '207b9d2edf4a750c17d80e26cf7a87e6b9fbd8543e9891cca8dcdade3a4d29009b5600eebaffe1eddd332f8d6901cd16196f948398b795f4103bf0871f6db924b2', 'transactions': [['452060f095dd680df8749963b899e52fdb81fa112cbbd5b04ec14b032e587168', {'extensions': [], 'operation_results': [[4, {'fees': [{'amount': 20990, 'asset_id': '1.3.0'}], 'existed_pv': False, 'process_value': '', 'real_running_time': 474, 'contract_id': '1.16.121', 'relevant_datasize': 35, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20990, 'asset_id': '1.3.1'}]}]]}]], 'signatures': ['2038bacbcbadd5dbf5be48d2e87e63ff77a2a77bf94df52ebd9934ebdd1bbd0db234c3ae8f1e0d142f15cd8b8430a85fef27da1b8d09f1d855d2299a2f7903d9fb'], 'ref_block_prefix': 2355078845, 'expiration': '2020-07-13T11:36:28', 'ref_block_num': 55063, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}]]}, 'jsonrpc': '2.0', 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 20990, 'asset_id': '1.3.0'}]
### {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20990, 'asset_id': '1.3.1'}]}, total_fee: 20990
### [COCOS] fee_total_in_block: 20990, fee_total_range_accounts: 20990
### account_balances delta in block: 
  {'1.2.16': {'1.3.1': 20990}}
-----------------------------------------------------------------------

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271234157', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

-------------------- contract owner and caller acccount_balances changed --------------------
>>> contract call op before account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271255147', 'asset_id': '1.3.1'}]}
>>> contract call op before         account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271234157', 'asset_id': '1.3.1'}]}
>>> account_balances delta: 
  {'1.2.16': {'1.3.1': 20990}}
---------------------------------------------------------------------------------------------

func_accounts_balances: {'1.2.16': {'1.3.1': 20990}}
calc_accounts_balances: {'1.2.16': {'1.3.1': 20990}}
******************* calc_contract_call_operation_fee END ************************************

index = 4
>> get_account ['nicotest']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'name': 'nicotest', 'id': '1.2.16', 'cashback_gas': '1.13.30', 'cashback_vote': '1.13.385', 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.13', True], 'asset_locked': {'locked_total': [['1.3.0', '5000001900000']], 'vote_for_witness': {'amount': 1000000, 'asset_id': '1.3.0'}, 'contract_lock_details': [], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'vote_for_committee': {'amount': 900000, 'asset_id': '1.3.0'}}, 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'registrar': '1.2.4', 'cashback_vb': '1.13.262', 'options': {'extensions': [], 'votes': ['1:0', '1:9', '1:10', '0:11', '0:13', '0:14', '0:21'], 'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx'}, 'statistics': '2.6.16'}, 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271234157', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['e95c38313cf5d456d24cfbe38c6efbaba8261090005eef056a51ba6a172ec8bb', {'extensions': [], 'signatures': ['201dbb6c5fd8dbdcc312cb0d3b6c87473cfd76295e344e979bafaa59223b747e7a0e9f3980d8a1df7f006d80a74cc4ccf815c02154b2340884203fe6a61ae3514d'], 'ref_block_prefix': 3485438241, 'expiration': '2020-07-13T11:36:30', 'ref_block_num': 55064, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['e95c38313cf5d456d24cfbe38c6efbaba8261090005eef056a51ba6a172ec8bb']
{'result': None, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info e95c38313cf5d456d24cfbe38c6efbaba8261090005eef056a51ba6a172ec8bb
 None

>> get_transaction_in_block_info ['e95c38313cf5d456d24cfbe38c6efbaba8261090005eef056a51ba6a172ec8bb']
{'result': {'trx_hash': 'e95c38313cf5d456d24cfbe38c6efbaba8261090005eef056a51ba6a172ec8bb', 'block_num': 7460641, 'id': '3.1.824851', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info e95c38313cf5d456d24cfbe38c6efbaba8261090005eef056a51ba6a172ec8bb
 {'trx_hash': 'e95c38313cf5d456d24cfbe38c6efbaba8261090005eef056a51ba6a172ec8bb', 'block_num': 7460641, 'id': '3.1.824851', 'trx_in_block': 0}

>> get_block [7460641]
{'result': {'block_id': '0071d721d0c7072d19af6c3367cd2896cef7cba5', 'timestamp': '2020-07-13T11:16:04', 'transaction_merkle_root': '0aabae2e29f2c05f344131ce20ddb12771021d67', 'witness': '1.6.10', 'previous': '0071d720f833b1299132d707e99037646030cb05', 'witness_signature': '205712be0ecf4eaf2c82959a10438fdf13d25a804db492702d6ff52d67a0844ce84e4fd39e62e67ccdb5ad942f7d012e6f1a89c371963a7a25c314c4788c7dd4e4', 'transactions': [['e95c38313cf5d456d24cfbe38c6efbaba8261090005eef056a51ba6a172ec8bb', {'extensions': [], 'operation_results': [[4, {'fees': [{'amount': 20957, 'asset_id': '1.3.0'}], 'existed_pv': False, 'process_value': '', 'real_running_time': 441, 'contract_id': '1.16.121', 'relevant_datasize': 35, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20957, 'asset_id': '1.3.1'}]}]]}]], 'signatures': ['201dbb6c5fd8dbdcc312cb0d3b6c87473cfd76295e344e979bafaa59223b747e7a0e9f3980d8a1df7f006d80a74cc4ccf815c02154b2340884203fe6a61ae3514d'], 'ref_block_prefix': 3485438241, 'expiration': '2020-07-13T11:36:30', 'ref_block_num': 55064, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}]]}, 'jsonrpc': '2.0', 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 20957, 'asset_id': '1.3.0'}]
### {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20957, 'asset_id': '1.3.1'}]}, total_fee: 20957
### [COCOS] fee_total_in_block: 20957, fee_total_range_accounts: 20957
### account_balances delta in block: 
  {'1.2.16': {'1.3.1': 20957}}
-----------------------------------------------------------------------

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271213200', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

-------------------- contract owner and caller acccount_balances changed --------------------
>>> contract call op before account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271234157', 'asset_id': '1.3.1'}]}
>>> contract call op before         account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271213200', 'asset_id': '1.3.1'}]}
>>> account_balances delta: 
  {'1.2.16': {'1.3.1': 20957}}
---------------------------------------------------------------------------------------------

func_accounts_balances: {'1.2.16': {'1.3.1': 20957}}
calc_accounts_balances: {'1.2.16': {'1.3.1': 20957}}
******************* calc_contract_call_operation_fee END ************************************

index = 5
>> get_account ['nicotest']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'name': 'nicotest', 'id': '1.2.16', 'cashback_gas': '1.13.30', 'cashback_vote': '1.13.385', 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.13', True], 'asset_locked': {'locked_total': [['1.3.0', '5000001900000']], 'vote_for_witness': {'amount': 1000000, 'asset_id': '1.3.0'}, 'contract_lock_details': [], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'vote_for_committee': {'amount': 900000, 'asset_id': '1.3.0'}}, 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'registrar': '1.2.4', 'cashback_vb': '1.13.262', 'options': {'extensions': [], 'votes': ['1:0', '1:9', '1:10', '0:11', '0:13', '0:14', '0:21'], 'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx'}, 'statistics': '2.6.16'}, 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271213200', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['e406bfc6c9dd3e8577c8f3932919cd738306121c7604be1621fe1c61713b734f', {'extensions': [], 'signatures': ['1f0b20d893ac4bad7a9a83b13b9c2dc9b64177d13a8f07a66e45a76b679079d99610e1e1f26dc5439481c2936b80051c114429e941affa3a8758438d55907a0279'], 'ref_block_prefix': 889511940, 'expiration': '2020-07-13T11:36:34', 'ref_block_num': 55065, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['e406bfc6c9dd3e8577c8f3932919cd738306121c7604be1621fe1c61713b734f']
{'result': {'trx_hash': 'e406bfc6c9dd3e8577c8f3932919cd738306121c7604be1621fe1c61713b734f', 'block_num': 7460642, 'id': '3.1.824852', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info e406bfc6c9dd3e8577c8f3932919cd738306121c7604be1621fe1c61713b734f
 {'trx_hash': 'e406bfc6c9dd3e8577c8f3932919cd738306121c7604be1621fe1c61713b734f', 'block_num': 7460642, 'id': '3.1.824852', 'trx_in_block': 0}

>> get_block [7460642]
{'result': {'block_id': '0071d72275ffc9b8a2c5f8ce42072adee9ab63d6', 'timestamp': '2020-07-13T11:16:06', 'transaction_merkle_root': '1226d3a2d5bc06bdf29a64f3563d6b359995fb50', 'witness': '1.6.7', 'previous': '0071d721d0c7072d19af6c3367cd2896cef7cba5', 'witness_signature': '2068381d68acea1742ab0b2c9287f71b35a6fd7eb47088acbb139bd0e7a93dbf6f50135175a7db30c00e996b6673f43b9c7f0f5b0ec1b090bc7be6695956193f52', 'transactions': [['e406bfc6c9dd3e8577c8f3932919cd738306121c7604be1621fe1c61713b734f', {'extensions': [], 'operation_results': [[4, {'fees': [{'amount': 20932, 'asset_id': '1.3.0'}], 'existed_pv': False, 'process_value': '', 'real_running_time': 416, 'contract_id': '1.16.121', 'relevant_datasize': 35, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20932, 'asset_id': '1.3.1'}]}]]}]], 'signatures': ['1f0b20d893ac4bad7a9a83b13b9c2dc9b64177d13a8f07a66e45a76b679079d99610e1e1f26dc5439481c2936b80051c114429e941affa3a8758438d55907a0279'], 'ref_block_prefix': 889511940, 'expiration': '2020-07-13T11:36:34', 'ref_block_num': 55065, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}]]}, 'jsonrpc': '2.0', 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 20932, 'asset_id': '1.3.0'}]
### {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20932, 'asset_id': '1.3.1'}]}, total_fee: 20932
### [COCOS] fee_total_in_block: 20932, fee_total_range_accounts: 20932
### account_balances delta in block: 
  {'1.2.16': {'1.3.1': 20932}}
-----------------------------------------------------------------------

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271192268', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

-------------------- contract owner and caller acccount_balances changed --------------------
>>> contract call op before account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271213200', 'asset_id': '1.3.1'}]}
>>> contract call op before         account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271192268', 'asset_id': '1.3.1'}]}
>>> account_balances delta: 
  {'1.2.16': {'1.3.1': 20932}}
---------------------------------------------------------------------------------------------

func_accounts_balances: {'1.2.16': {'1.3.1': 20932}}
calc_accounts_balances: {'1.2.16': {'1.3.1': 20932}}
******************* calc_contract_call_operation_fee END ************************************

index = 6
>> get_account ['nicotest']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'name': 'nicotest', 'id': '1.2.16', 'cashback_gas': '1.13.30', 'cashback_vote': '1.13.385', 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.13', True], 'asset_locked': {'locked_total': [['1.3.0', '5000001900000']], 'vote_for_witness': {'amount': 1000000, 'asset_id': '1.3.0'}, 'contract_lock_details': [], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'vote_for_committee': {'amount': 900000, 'asset_id': '1.3.0'}}, 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'registrar': '1.2.4', 'cashback_vb': '1.13.262', 'options': {'extensions': [], 'votes': ['1:0', '1:9', '1:10', '0:11', '0:13', '0:14', '0:21'], 'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx'}, 'statistics': '2.6.16'}, 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271192268', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['56fefbfb3b169b6ce63e9c8d0fa537557d770e470982931f899fa31f514d9de9', {'extensions': [], 'signatures': ['2032f7e0e36990cfb25733424ee2a898a98e46203ea2e1041cab2f26e83c03390314b919e285ee77e0c9490b5510af351e705d03f74cb8e8480ae63ffbc7bd1e9f'], 'ref_block_prefix': 3820981358, 'expiration': '2020-07-13T11:36:36', 'ref_block_num': 55066, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['56fefbfb3b169b6ce63e9c8d0fa537557d770e470982931f899fa31f514d9de9']
{'result': None, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info 56fefbfb3b169b6ce63e9c8d0fa537557d770e470982931f899fa31f514d9de9
 None

>> get_transaction_in_block_info ['56fefbfb3b169b6ce63e9c8d0fa537557d770e470982931f899fa31f514d9de9']
{'result': {'trx_hash': '56fefbfb3b169b6ce63e9c8d0fa537557d770e470982931f899fa31f514d9de9', 'block_num': 7460643, 'id': '3.1.824853', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info 56fefbfb3b169b6ce63e9c8d0fa537557d770e470982931f899fa31f514d9de9
 {'trx_hash': '56fefbfb3b169b6ce63e9c8d0fa537557d770e470982931f899fa31f514d9de9', 'block_num': 7460643, 'id': '3.1.824853', 'trx_in_block': 0}

>> get_block [7460643]
{'result': {'block_id': '0071d7230c5e634a2c4cae48027e56c210bc9949', 'timestamp': '2020-07-13T11:16:10', 'transaction_merkle_root': '2b27e0b70be811504d1c3ba59e92288eaa1429be', 'witness': '1.6.5', 'previous': '0071d72275ffc9b8a2c5f8ce42072adee9ab63d6', 'witness_signature': '2060d02295382383691ea93842da7fb46cd11ef032c03fb4375e2347b3601147015260c21fcc28077f9e4ad14ea16de5416b53c43726f349a0243df5bd6d7d1b70', 'transactions': [['56fefbfb3b169b6ce63e9c8d0fa537557d770e470982931f899fa31f514d9de9', {'extensions': [], 'operation_results': [[4, {'fees': [{'amount': 20933, 'asset_id': '1.3.0'}], 'existed_pv': False, 'process_value': '', 'real_running_time': 417, 'contract_id': '1.16.121', 'relevant_datasize': 35, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20933, 'asset_id': '1.3.1'}]}]]}]], 'signatures': ['2032f7e0e36990cfb25733424ee2a898a98e46203ea2e1041cab2f26e83c03390314b919e285ee77e0c9490b5510af351e705d03f74cb8e8480ae63ffbc7bd1e9f'], 'ref_block_prefix': 3820981358, 'expiration': '2020-07-13T11:36:36', 'ref_block_num': 55066, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}]]}, 'jsonrpc': '2.0', 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 20933, 'asset_id': '1.3.0'}]
### {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20933, 'asset_id': '1.3.1'}]}, total_fee: 20933
### [COCOS] fee_total_in_block: 20933, fee_total_range_accounts: 20933
### account_balances delta in block: 
  {'1.2.16': {'1.3.1': 20933}}
-----------------------------------------------------------------------

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271171335', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

-------------------- contract owner and caller acccount_balances changed --------------------
>>> contract call op before account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271192268', 'asset_id': '1.3.1'}]}
>>> contract call op before         account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271171335', 'asset_id': '1.3.1'}]}
>>> account_balances delta: 
  {'1.2.16': {'1.3.1': 20933}}
---------------------------------------------------------------------------------------------

func_accounts_balances: {'1.2.16': {'1.3.1': 20933}}
calc_accounts_balances: {'1.2.16': {'1.3.1': 20933}}
******************* calc_contract_call_operation_fee END ************************************

index = 7
>> get_account ['nicotest']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'name': 'nicotest', 'id': '1.2.16', 'cashback_gas': '1.13.30', 'cashback_vote': '1.13.385', 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.13', True], 'asset_locked': {'locked_total': [['1.3.0', '5000001900000']], 'vote_for_witness': {'amount': 1000000, 'asset_id': '1.3.0'}, 'contract_lock_details': [], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'vote_for_committee': {'amount': 900000, 'asset_id': '1.3.0'}}, 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'registrar': '1.2.4', 'cashback_vb': '1.13.262', 'options': {'extensions': [], 'votes': ['1:0', '1:9', '1:10', '0:11', '0:13', '0:14', '0:21'], 'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx'}, 'statistics': '2.6.16'}, 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271171335', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['148f244bd9b238d054e9b04f44e2581f30b0cc1066d81ad9be34bb85a2e81002', {'extensions': [], 'signatures': ['1f0c9da149b0d909d37ce7ad3346b6af6c92fb3ab4647a3dbf17cb49281a591f9f1c153ae0ec1d5b446deb2d7b38fb60d1f2a157c31af2829e424fce8539d44683'], 'ref_block_prefix': 3820981358, 'expiration': '2020-07-13T11:36:40', 'ref_block_num': 55066, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['148f244bd9b238d054e9b04f44e2581f30b0cc1066d81ad9be34bb85a2e81002']
{'result': {'trx_hash': '148f244bd9b238d054e9b04f44e2581f30b0cc1066d81ad9be34bb85a2e81002', 'block_num': 7460644, 'id': '3.1.824854', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info 148f244bd9b238d054e9b04f44e2581f30b0cc1066d81ad9be34bb85a2e81002
 {'trx_hash': '148f244bd9b238d054e9b04f44e2581f30b0cc1066d81ad9be34bb85a2e81002', 'block_num': 7460644, 'id': '3.1.824854', 'trx_in_block': 0}

>> get_block [7460644]
{'result': {'block_id': '0071d724f9bf9bbee7fd183b1eeb0fa9a1d6deac', 'timestamp': '2020-07-13T11:16:12', 'transaction_merkle_root': '85f16634248cb55dc34e82f5eb8316885c2d9c36', 'witness': '1.6.4', 'previous': '0071d7230c5e634a2c4cae48027e56c210bc9949', 'witness_signature': '2042fc13cdd1f0b2633ea76a8d87e36b3b786094da899dafa10a0b6e9aab352cba059d4dd2e4fcf3501d6ec2e297f518c37105eabb70067b01e81530430a213522', 'transactions': [['148f244bd9b238d054e9b04f44e2581f30b0cc1066d81ad9be34bb85a2e81002', {'extensions': [], 'operation_results': [[4, {'fees': [{'amount': 20961, 'asset_id': '1.3.0'}], 'existed_pv': False, 'process_value': '', 'real_running_time': 445, 'contract_id': '1.16.121', 'relevant_datasize': 35, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20961, 'asset_id': '1.3.1'}]}]]}]], 'signatures': ['1f0c9da149b0d909d37ce7ad3346b6af6c92fb3ab4647a3dbf17cb49281a591f9f1c153ae0ec1d5b446deb2d7b38fb60d1f2a157c31af2829e424fce8539d44683'], 'ref_block_prefix': 3820981358, 'expiration': '2020-07-13T11:36:40', 'ref_block_num': 55066, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}]]}, 'jsonrpc': '2.0', 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 20961, 'asset_id': '1.3.0'}]
### {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20961, 'asset_id': '1.3.1'}]}, total_fee: 20961
### [COCOS] fee_total_in_block: 20961, fee_total_range_accounts: 20961
### account_balances delta in block: 
  {'1.2.16': {'1.3.1': 20961}}
-----------------------------------------------------------------------

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271150374', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

-------------------- contract owner and caller acccount_balances changed --------------------
>>> contract call op before account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271171335', 'asset_id': '1.3.1'}]}
>>> contract call op before         account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271150374', 'asset_id': '1.3.1'}]}
>>> account_balances delta: 
  {'1.2.16': {'1.3.1': 20961}}
---------------------------------------------------------------------------------------------

func_accounts_balances: {'1.2.16': {'1.3.1': 20961}}
calc_accounts_balances: {'1.2.16': {'1.3.1': 20961}}
******************* calc_contract_call_operation_fee END ************************************

index = 8
>> get_account ['nicotest']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'name': 'nicotest', 'id': '1.2.16', 'cashback_gas': '1.13.30', 'cashback_vote': '1.13.385', 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.13', True], 'asset_locked': {'locked_total': [['1.3.0', '5000001900000']], 'vote_for_witness': {'amount': 1000000, 'asset_id': '1.3.0'}, 'contract_lock_details': [], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'vote_for_committee': {'amount': 900000, 'asset_id': '1.3.0'}}, 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'registrar': '1.2.4', 'cashback_vb': '1.13.262', 'options': {'extensions': [], 'votes': ['1:0', '1:9', '1:10', '0:11', '0:13', '0:14', '0:21'], 'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx'}, 'statistics': '2.6.16'}, 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271150374', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['6c5d50bf994e65509f0d0df3e42850b559b07d4d36563ad93606fb12ea59b612', {'extensions': [], 'signatures': ['1f5dda48523f4241ea92bfa6ffc89811cddee91bcd9509fa24243fc4d7ffde684a7bf7bd5ad4b7700dbb1e1d98e73008e2acf873763094ac1fbf9d0f5d8502a142'], 'ref_block_prefix': 2386195089, 'expiration': '2020-07-13T11:36:42', 'ref_block_num': 55068, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['6c5d50bf994e65509f0d0df3e42850b559b07d4d36563ad93606fb12ea59b612']
{'result': {'trx_hash': '6c5d50bf994e65509f0d0df3e42850b559b07d4d36563ad93606fb12ea59b612', 'block_num': 7460645, 'id': '3.1.824855', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info 6c5d50bf994e65509f0d0df3e42850b559b07d4d36563ad93606fb12ea59b612
 {'trx_hash': '6c5d50bf994e65509f0d0df3e42850b559b07d4d36563ad93606fb12ea59b612', 'block_num': 7460645, 'id': '3.1.824855', 'trx_in_block': 0}

>> get_block [7460645]
{'result': {'block_id': '0071d7257be4134a094ce66af944f6f25ab16288', 'timestamp': '2020-07-13T11:16:14', 'transaction_merkle_root': '3e4dc5ecabfb857b6a98d1cb31a021d7e7166105', 'witness': '1.6.8', 'previous': '0071d724f9bf9bbee7fd183b1eeb0fa9a1d6deac', 'witness_signature': '1f233e85b7d9277d4abbe2de833f8c4bc8d1abef9a3eedc56212b8cf04967a7d416a3a233b827e0fe50ba00683b11e571fa52dd451516809dc9bbac64a72991f8e', 'transactions': [['6c5d50bf994e65509f0d0df3e42850b559b07d4d36563ad93606fb12ea59b612', {'extensions': [], 'operation_results': [[4, {'fees': [{'amount': 21028, 'asset_id': '1.3.0'}], 'existed_pv': False, 'process_value': '', 'real_running_time': 512, 'contract_id': '1.16.121', 'relevant_datasize': 35, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 21028, 'asset_id': '1.3.1'}]}]]}]], 'signatures': ['1f5dda48523f4241ea92bfa6ffc89811cddee91bcd9509fa24243fc4d7ffde684a7bf7bd5ad4b7700dbb1e1d98e73008e2acf873763094ac1fbf9d0f5d8502a142'], 'ref_block_prefix': 2386195089, 'expiration': '2020-07-13T11:36:42', 'ref_block_num': 55068, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}]]}, 'jsonrpc': '2.0', 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 21028, 'asset_id': '1.3.0'}]
### {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 21028, 'asset_id': '1.3.1'}]}, total_fee: 21028
### [COCOS] fee_total_in_block: 21028, fee_total_range_accounts: 21028
### account_balances delta in block: 
  {'1.2.16': {'1.3.1': 21028}}
-----------------------------------------------------------------------

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271129346', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

-------------------- contract owner and caller acccount_balances changed --------------------
>>> contract call op before account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271150374', 'asset_id': '1.3.1'}]}
>>> contract call op before         account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271129346', 'asset_id': '1.3.1'}]}
>>> account_balances delta: 
  {'1.2.16': {'1.3.1': 21028}}
---------------------------------------------------------------------------------------------

func_accounts_balances: {'1.2.16': {'1.3.1': 21028}}
calc_accounts_balances: {'1.2.16': {'1.3.1': 21028}}
******************* calc_contract_call_operation_fee END ************************************

index = 9
>> get_account ['nicotest']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'name': 'nicotest', 'id': '1.2.16', 'cashback_gas': '1.13.30', 'cashback_vote': '1.13.385', 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.13', True], 'asset_locked': {'locked_total': [['1.3.0', '5000001900000']], 'vote_for_witness': {'amount': 1000000, 'asset_id': '1.3.0'}, 'contract_lock_details': [], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'vote_for_committee': {'amount': 900000, 'asset_id': '1.3.0'}}, 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'registrar': '1.2.4', 'cashback_vb': '1.13.262', 'options': {'extensions': [], 'votes': ['1:0', '1:9', '1:10', '0:11', '0:13', '0:14', '0:21'], 'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx'}, 'statistics': '2.6.16'}, 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271129346', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['83904e8a7b692298c2cea0bd7f95862a74b872a106c4fe959e811e8106c17f59', {'extensions': [], 'signatures': ['2029ff2079c97c60d8ddd8b31daaa3d1c46b4aee4167e0f194cac20d23213ce25b4f185b44508c06d7793313a81351607ec6f471513b72dd05e10916cd72de86a2'], 'ref_block_prefix': 2458477013, 'expiration': '2020-07-13T11:36:44', 'ref_block_num': 55069, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['83904e8a7b692298c2cea0bd7f95862a74b872a106c4fe959e811e8106c17f59']
{'result': {'trx_hash': '83904e8a7b692298c2cea0bd7f95862a74b872a106c4fe959e811e8106c17f59', 'block_num': 7460646, 'id': '3.1.824856', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info 83904e8a7b692298c2cea0bd7f95862a74b872a106c4fe959e811e8106c17f59
 {'trx_hash': '83904e8a7b692298c2cea0bd7f95862a74b872a106c4fe959e811e8106c17f59', 'block_num': 7460646, 'id': '3.1.824856', 'trx_in_block': 0}

>> get_block [7460646]
{'result': {'block_id': '0071d726b571258e89fd62c52a8d1cae61f6b2fb', 'timestamp': '2020-07-13T11:16:16', 'transaction_merkle_root': 'b15c9b5614e825fe674e5d1e03e936f7b4387bbe', 'witness': '1.6.1', 'previous': '0071d7257be4134a094ce66af944f6f25ab16288', 'witness_signature': '20152f2d191a2d70db4f0f12ebf06c6b013134c2df7dc3c156623da79a131bc2fe27cdf35680cc4a671dfa6ea74b61a333525649557794b71b6bf865c1e09bbca6', 'transactions': [['83904e8a7b692298c2cea0bd7f95862a74b872a106c4fe959e811e8106c17f59', {'extensions': [], 'operation_results': [[4, {'fees': [{'amount': 20919, 'asset_id': '1.3.0'}], 'existed_pv': False, 'process_value': '', 'real_running_time': 403, 'contract_id': '1.16.121', 'relevant_datasize': 35, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20919, 'asset_id': '1.3.1'}]}]]}]], 'signatures': ['2029ff2079c97c60d8ddd8b31daaa3d1c46b4aee4167e0f194cac20d23213ce25b4f185b44508c06d7793313a81351607ec6f471513b72dd05e10916cd72de86a2'], 'ref_block_prefix': 2458477013, 'expiration': '2020-07-13T11:36:44', 'ref_block_num': 55069, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]}]]}, 'jsonrpc': '2.0', 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 20919, 'asset_id': '1.3.0'}]
### {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 20919, 'asset_id': '1.3.1'}]}, total_fee: 20919
### [COCOS] fee_total_in_block: 20919, fee_total_range_accounts: 20919
### account_balances delta in block: 
  {'1.2.16': {'1.3.1': 20919}}
-----------------------------------------------------------------------

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271108427', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

-------------------- contract owner and caller acccount_balances changed --------------------
>>> contract call op before account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271129346', 'asset_id': '1.3.1'}]}
>>> contract call op before         account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271108427', 'asset_id': '1.3.1'}]}
>>> account_balances delta: 
  {'1.2.16': {'1.3.1': 20919}}
---------------------------------------------------------------------------------------------

func_accounts_balances: {'1.2.16': {'1.3.1': 20919}}
calc_accounts_balances: {'1.2.16': {'1.3.1': 20919}}
******************* calc_contract_call_operation_fee END ************************************

>> get_account ['nicotest']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'name': 'nicotest', 'id': '1.2.16', 'cashback_gas': '1.13.30', 'cashback_vote': '1.13.385', 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.13', True], 'asset_locked': {'locked_total': [['1.3.0', '5000001900000']], 'vote_for_witness': {'amount': 1000000, 'asset_id': '1.3.0'}, 'contract_lock_details': [], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'vote_for_committee': {'amount': 900000, 'asset_id': '1.3.0'}}, 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'registrar': '1.2.4', 'cashback_vb': '1.13.262', 'options': {'extensions': [], 'votes': ['1:0', '1:9', '1:10', '0:11', '0:13', '0:14', '0:21'], 'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx'}, 'statistics': '2.6.16'}, 'jsonrpc': '2.0', 'id': 1}

>> get_account ['init1']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7', 1]]}, 'name': 'init1', 'id': '1.2.6', 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7', 1]]}, 'registrar': '1.2.4', 'membership_expiration_date': '1969-12-31T23:59:59', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'contract_lock_details': [], 'committee_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}}, 'options': {'extensions': [], 'votes': [], 'memo_key': 'COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7'}, 'witness_status': ['1.6.2', True], 'statistics': '2.6.6', 'committee_status': ['1.5.1', True]}, 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271108427', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.6']
{'result': [{'amount': '13626092814673', 'asset_id': '1.3.0'}], 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['f3bc5e918001b4a9cbd325196e65aa8dbe0c54921132eeab03fbf71cb225b030', {'extensions': [], 'signatures': ['206c333f842a45162af5df6f0886ba85817b13204f228d3ecb9a7d55cdc5dbe15c7db18704d9f9b416d290559c4fda5aa097484fbc42ff63d22ea52cdb5439beda'], 'ref_block_prefix': 870180376, 'expiration': '2020-07-13T11:36:46', 'ref_block_num': 55070, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.6'}]]}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['f3bc5e918001b4a9cbd325196e65aa8dbe0c54921132eeab03fbf71cb225b030']
{'result': {'trx_hash': 'f3bc5e918001b4a9cbd325196e65aa8dbe0c54921132eeab03fbf71cb225b030', 'block_num': 7460647, 'id': '3.1.824857', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info f3bc5e918001b4a9cbd325196e65aa8dbe0c54921132eeab03fbf71cb225b030
 {'trx_hash': 'f3bc5e918001b4a9cbd325196e65aa8dbe0c54921132eeab03fbf71cb225b030', 'block_num': 7460647, 'id': '3.1.824857', 'trx_in_block': 0}

>> get_block [7460647]
{'result': {'block_id': '0071d727cbb24cdc441be81ae4badfdc4a5e9e41', 'timestamp': '2020-07-13T11:16:18', 'transaction_merkle_root': 'dd31de873788b05e2a7cc5d0680ca33f6bc8c438', 'witness': '1.6.3', 'previous': '0071d726b571258e89fd62c52a8d1cae61f6b2fb', 'witness_signature': '205f5a5560c4d1881742a4be85f417fea729dbda650e2d2c220f476483fe10db207faec217f48d30be1e1ad525f6e903a1adf2d4c909296f4828b0d7d9048e5125', 'transactions': [['f3bc5e918001b4a9cbd325196e65aa8dbe0c54921132eeab03fbf71cb225b030', {'extensions': [], 'operation_results': [[4, {'fees': [{'amount': 20968, 'asset_id': '1.3.0'}], 'existed_pv': False, 'process_value': '', 'real_running_time': 452, 'contract_id': '1.16.121', 'relevant_datasize': 35, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}], [5, {'message': '37%', 'affected_account': '1.2.6', 'fees': [{'amount': 7759, 'asset_id': '1.3.0'}]}], [5, {'message': '63%', 'affected_account': '1.2.16', 'fees': [{'amount': 13209, 'asset_id': '1.3.1'}]}]]}]], 'signatures': ['206c333f842a45162af5df6f0886ba85817b13204f228d3ecb9a7d55cdc5dbe15c7db18704d9f9b416d290559c4fda5aa097484fbc42ff63d22ea52cdb5439beda'], 'ref_block_prefix': 870180376, 'expiration': '2020-07-13T11:36:46', 'ref_block_num': 55070, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.6'}]]}]]}, 'jsonrpc': '2.0', 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 20968, 'asset_id': '1.3.0'}]
### {'message': '37%', 'affected_account': '1.2.6', 'fees': [{'amount': 7759, 'asset_id': '1.3.0'}]}, total_fee: 7759
### {'message': '63%', 'affected_account': '1.2.16', 'fees': [{'amount': 13209, 'asset_id': '1.3.1'}]}, total_fee: 13209
### [COCOS] fee_total_in_block: 20968, fee_total_range_accounts: 20968
### account_balances delta in block: 
  {'1.2.6': {'1.3.0': 7759}, '1.2.16': {'1.3.1': 13209}}
-----------------------------------------------------------------------

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271095218', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.6']
{'result': [{'amount': '13626092806914', 'asset_id': '1.3.0'}], 'jsonrpc': '2.0', 'id': 1}

-------------------- contract owner and caller acccount_balances changed --------------------
>>> contract call op before account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271108427', 'asset_id': '1.3.1'}], '1.2.6': [{'amount': '13626092814673', 'asset_id': '1.3.0'}]}
>>> contract call op before         account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271095218', 'asset_id': '1.3.1'}], '1.2.6': [{'amount': '13626092806914', 'asset_id': '1.3.0'}]}
>>> account_balances delta: 
  {'1.2.16': {'1.3.1': 13209}, '1.2.6': {'1.3.0': 7759}}
---------------------------------------------------------------------------------------------

func_accounts_balances: {'1.2.6': {'1.3.0': 7759}, '1.2.16': {'1.3.1': 13209}}
calc_accounts_balances: {'1.2.16': {'1.3.1': 13209}, '1.2.6': {'1.3.0': 7759}}
******************* calc_contract_call_operation_fee END ************************************

accounts: ['nicotest', 'init1'], count: 5
index = 0
>> get_account ['nicotest']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'name': 'nicotest', 'id': '1.2.16', 'cashback_gas': '1.13.30', 'cashback_vote': '1.13.385', 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.13', True], 'asset_locked': {'locked_total': [['1.3.0', '5000001900000']], 'vote_for_witness': {'amount': 1000000, 'asset_id': '1.3.0'}, 'contract_lock_details': [], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'vote_for_committee': {'amount': 900000, 'asset_id': '1.3.0'}}, 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'registrar': '1.2.4', 'cashback_vb': '1.13.262', 'options': {'extensions': [], 'votes': ['1:0', '1:9', '1:10', '0:11', '0:13', '0:14', '0:21'], 'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx'}, 'statistics': '2.6.16'}, 'jsonrpc': '2.0', 'id': 1}

>> get_account ['init1']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7', 1]]}, 'name': 'init1', 'id': '1.2.6', 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7', 1]]}, 'registrar': '1.2.4', 'membership_expiration_date': '1969-12-31T23:59:59', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'contract_lock_details': [], 'committee_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}}, 'options': {'extensions': [], 'votes': [], 'memo_key': 'COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7'}, 'witness_status': ['1.6.2', True], 'statistics': '2.6.6', 'committee_status': ['1.5.1', True]}, 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271095218', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.6']
{'result': [{'amount': '13626092806914', 'asset_id': '1.3.0'}], 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['29d0dbeb3bd25cbc7a8b0504666514471f44f5c2e0c2f4623f03c9aa35f88d70', {'extensions': [], 'signatures': ['201e281a3d4b24036ebb097ad5ed09c65ff3d4ecde94758bc3ea6ec992b23ce1135999a4f10fbe1416b3daef171e5d3dab25ecfaf38fca1bcd34e280402c0fa1b9'], 'ref_block_prefix': 870180376, 'expiration': '2020-07-13T11:36:48', 'ref_block_num': 55070, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.6'}]]}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['29d0dbeb3bd25cbc7a8b0504666514471f44f5c2e0c2f4623f03c9aa35f88d70']
{'result': {'trx_hash': '29d0dbeb3bd25cbc7a8b0504666514471f44f5c2e0c2f4623f03c9aa35f88d70', 'block_num': 7460648, 'id': '3.1.824858', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info 29d0dbeb3bd25cbc7a8b0504666514471f44f5c2e0c2f4623f03c9aa35f88d70
 {'trx_hash': '29d0dbeb3bd25cbc7a8b0504666514471f44f5c2e0c2f4623f03c9aa35f88d70', 'block_num': 7460648, 'id': '3.1.824858', 'trx_in_block': 0}

>> get_block [7460648]
{'result': {'block_id': '0071d728691ab32830685e7598c1409ee6a90173', 'timestamp': '2020-07-13T11:16:20', 'transaction_merkle_root': 'cf6d25ef3e478c05262e26ca87e178b368c5b88b', 'witness': '1.6.2', 'previous': '0071d727cbb24cdc441be81ae4badfdc4a5e9e41', 'witness_signature': '20024a1584f640ddb6242d9682a14c7043e0fc5e3a4bf248514c6ba9510f2fca00075dd40831c0e955f95d53983aa75f8ed93a376746c7a648e8d70720a1fa2af2', 'transactions': [['29d0dbeb3bd25cbc7a8b0504666514471f44f5c2e0c2f4623f03c9aa35f88d70', {'extensions': [], 'operation_results': [[4, {'fees': [{'amount': 20756, 'asset_id': '1.3.0'}], 'existed_pv': False, 'process_value': '', 'real_running_time': 240, 'contract_id': '1.16.121', 'relevant_datasize': 35, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}], [5, {'message': '37%', 'affected_account': '1.2.6', 'fees': [{'amount': 7680, 'asset_id': '1.3.0'}]}], [5, {'message': '63%', 'affected_account': '1.2.16', 'fees': [{'amount': 13076, 'asset_id': '1.3.1'}]}]]}]], 'signatures': ['201e281a3d4b24036ebb097ad5ed09c65ff3d4ecde94758bc3ea6ec992b23ce1135999a4f10fbe1416b3daef171e5d3dab25ecfaf38fca1bcd34e280402c0fa1b9'], 'ref_block_prefix': 870180376, 'expiration': '2020-07-13T11:36:48', 'ref_block_num': 55070, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.6'}]]}]]}, 'jsonrpc': '2.0', 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 20756, 'asset_id': '1.3.0'}]
### {'message': '37%', 'affected_account': '1.2.6', 'fees': [{'amount': 7680, 'asset_id': '1.3.0'}]}, total_fee: 7680
### {'message': '63%', 'affected_account': '1.2.16', 'fees': [{'amount': 13076, 'asset_id': '1.3.1'}]}, total_fee: 13076
### [COCOS] fee_total_in_block: 20756, fee_total_range_accounts: 20756
### account_balances delta in block: 
  {'1.2.6': {'1.3.0': 7680}, '1.2.16': {'1.3.1': 13076}}
-----------------------------------------------------------------------

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271082142', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.6']
{'result': [{'amount': '13626092799234', 'asset_id': '1.3.0'}], 'jsonrpc': '2.0', 'id': 1}

-------------------- contract owner and caller acccount_balances changed --------------------
>>> contract call op before account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271095218', 'asset_id': '1.3.1'}], '1.2.6': [{'amount': '13626092806914', 'asset_id': '1.3.0'}]}
>>> contract call op before         account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271082142', 'asset_id': '1.3.1'}], '1.2.6': [{'amount': '13626092799234', 'asset_id': '1.3.0'}]}
>>> account_balances delta: 
  {'1.2.16': {'1.3.1': 13076}, '1.2.6': {'1.3.0': 7680}}
---------------------------------------------------------------------------------------------

func_accounts_balances: {'1.2.6': {'1.3.0': 7680}, '1.2.16': {'1.3.1': 13076}}
calc_accounts_balances: {'1.2.16': {'1.3.1': 13076}, '1.2.6': {'1.3.0': 7680}}
******************* calc_contract_call_operation_fee END ************************************

index = 1
>> get_account ['nicotest']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'name': 'nicotest', 'id': '1.2.16', 'cashback_gas': '1.13.30', 'cashback_vote': '1.13.385', 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.13', True], 'asset_locked': {'locked_total': [['1.3.0', '5000001900000']], 'vote_for_witness': {'amount': 1000000, 'asset_id': '1.3.0'}, 'contract_lock_details': [], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'vote_for_committee': {'amount': 900000, 'asset_id': '1.3.0'}}, 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'registrar': '1.2.4', 'cashback_vb': '1.13.262', 'options': {'extensions': [], 'votes': ['1:0', '1:9', '1:10', '0:11', '0:13', '0:14', '0:21'], 'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx'}, 'statistics': '2.6.16'}, 'jsonrpc': '2.0', 'id': 1}

>> get_account ['init1']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7', 1]]}, 'name': 'init1', 'id': '1.2.6', 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7', 1]]}, 'registrar': '1.2.4', 'membership_expiration_date': '1969-12-31T23:59:59', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'contract_lock_details': [], 'committee_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}}, 'options': {'extensions': [], 'votes': [], 'memo_key': 'COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7'}, 'witness_status': ['1.6.2', True], 'statistics': '2.6.6', 'committee_status': ['1.5.1', True]}, 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271082142', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.6']
{'result': [{'amount': '13626092799234', 'asset_id': '1.3.0'}], 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['3f8a31ea5815386f205d1e92d2b4b212f6867142c79b7fbcaf57b5df357b3292', {'extensions': [], 'signatures': ['2020cac62b52306c471f25538d55ba32c4cdc52623c4262967c45802c7c63972962c2fd601fd37b6d5b47052cc678db157f93de988f66e4227dbdb5a045b9ec6cc'], 'ref_block_prefix': 699479032, 'expiration': '2020-07-13T11:36:50', 'ref_block_num': 55072, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.6'}]]}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['3f8a31ea5815386f205d1e92d2b4b212f6867142c79b7fbcaf57b5df357b3292']
{'result': {'trx_hash': '3f8a31ea5815386f205d1e92d2b4b212f6867142c79b7fbcaf57b5df357b3292', 'block_num': 7460649, 'id': '3.1.824859', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info 3f8a31ea5815386f205d1e92d2b4b212f6867142c79b7fbcaf57b5df357b3292
 {'trx_hash': '3f8a31ea5815386f205d1e92d2b4b212f6867142c79b7fbcaf57b5df357b3292', 'block_num': 7460649, 'id': '3.1.824859', 'trx_in_block': 0}

>> get_block [7460649]
{'result': {'block_id': '0071d729da7d02144bda42d2b0127a2ac8063e4d', 'timestamp': '2020-07-13T11:16:22', 'transaction_merkle_root': '23a92f0d64ed30dfd76416061e801da7d6dee810', 'witness': '1.6.6', 'previous': '0071d728691ab32830685e7598c1409ee6a90173', 'witness_signature': '20777676625340f09fba009b938487e0ce5bb3cd9edf591bf77ed88362204926f426868c16e755301b48bbaae5aa4d3e17de21aab60de30a565eab47d26c44dc4f', 'transactions': [['3f8a31ea5815386f205d1e92d2b4b212f6867142c79b7fbcaf57b5df357b3292', {'extensions': [], 'operation_results': [[4, {'fees': [{'amount': 20908, 'asset_id': '1.3.0'}], 'existed_pv': False, 'process_value': '', 'real_running_time': 392, 'contract_id': '1.16.121', 'relevant_datasize': 35, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}], [5, {'message': '37%', 'affected_account': '1.2.6', 'fees': [{'amount': 7736, 'asset_id': '1.3.0'}]}], [5, {'message': '63%', 'affected_account': '1.2.16', 'fees': [{'amount': 13172, 'asset_id': '1.3.1'}]}]]}]], 'signatures': ['2020cac62b52306c471f25538d55ba32c4cdc52623c4262967c45802c7c63972962c2fd601fd37b6d5b47052cc678db157f93de988f66e4227dbdb5a045b9ec6cc'], 'ref_block_prefix': 699479032, 'expiration': '2020-07-13T11:36:50', 'ref_block_num': 55072, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.6'}]]}]]}, 'jsonrpc': '2.0', 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 20908, 'asset_id': '1.3.0'}]
### {'message': '37%', 'affected_account': '1.2.6', 'fees': [{'amount': 7736, 'asset_id': '1.3.0'}]}, total_fee: 7736
### {'message': '63%', 'affected_account': '1.2.16', 'fees': [{'amount': 13172, 'asset_id': '1.3.1'}]}, total_fee: 13172
### [COCOS] fee_total_in_block: 20908, fee_total_range_accounts: 20908
### account_balances delta in block: 
  {'1.2.6': {'1.3.0': 7736}, '1.2.16': {'1.3.1': 13172}}
-----------------------------------------------------------------------

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271068970', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.6']
{'result': [{'amount': '13626092791498', 'asset_id': '1.3.0'}], 'jsonrpc': '2.0', 'id': 1}

-------------------- contract owner and caller acccount_balances changed --------------------
>>> contract call op before account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271082142', 'asset_id': '1.3.1'}], '1.2.6': [{'amount': '13626092799234', 'asset_id': '1.3.0'}]}
>>> contract call op before         account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271068970', 'asset_id': '1.3.1'}], '1.2.6': [{'amount': '13626092791498', 'asset_id': '1.3.0'}]}
>>> account_balances delta: 
  {'1.2.16': {'1.3.1': 13172}, '1.2.6': {'1.3.0': 7736}}
---------------------------------------------------------------------------------------------

func_accounts_balances: {'1.2.6': {'1.3.0': 7736}, '1.2.16': {'1.3.1': 13172}}
calc_accounts_balances: {'1.2.16': {'1.3.1': 13172}, '1.2.6': {'1.3.0': 7736}}
******************* calc_contract_call_operation_fee END ************************************

index = 2
>> get_account ['nicotest']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'name': 'nicotest', 'id': '1.2.16', 'cashback_gas': '1.13.30', 'cashback_vote': '1.13.385', 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.13', True], 'asset_locked': {'locked_total': [['1.3.0', '5000001900000']], 'vote_for_witness': {'amount': 1000000, 'asset_id': '1.3.0'}, 'contract_lock_details': [], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'vote_for_committee': {'amount': 900000, 'asset_id': '1.3.0'}}, 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'registrar': '1.2.4', 'cashback_vb': '1.13.262', 'options': {'extensions': [], 'votes': ['1:0', '1:9', '1:10', '0:11', '0:13', '0:14', '0:21'], 'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx'}, 'statistics': '2.6.16'}, 'jsonrpc': '2.0', 'id': 1}

>> get_account ['init1']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7', 1]]}, 'name': 'init1', 'id': '1.2.6', 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7', 1]]}, 'registrar': '1.2.4', 'membership_expiration_date': '1969-12-31T23:59:59', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'contract_lock_details': [], 'committee_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}}, 'options': {'extensions': [], 'votes': [], 'memo_key': 'COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7'}, 'witness_status': ['1.6.2', True], 'statistics': '2.6.6', 'committee_status': ['1.5.1', True]}, 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271068970', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.6']
{'result': [{'amount': '13626092791498', 'asset_id': '1.3.0'}], 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['c7da41ef017e00a7740175d3d1c0f07d5936d23b7c82a6e61d8ae55903641395', {'extensions': [], 'signatures': ['1f5a8068a3f7d15b637628a634a3f23a634054010111dd0a92c5ab0e1911f8afe34fb3a0a8b860a59ff385c2fce5ddf3d21c3540e13bbb558572f89d3a570d1614'], 'ref_block_prefix': 755484624, 'expiration': '2020-07-13T11:36:52', 'ref_block_num': 55073, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.6'}]]}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['c7da41ef017e00a7740175d3d1c0f07d5936d23b7c82a6e61d8ae55903641395']
{'result': None, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info c7da41ef017e00a7740175d3d1c0f07d5936d23b7c82a6e61d8ae55903641395
 None

>> get_transaction_in_block_info ['c7da41ef017e00a7740175d3d1c0f07d5936d23b7c82a6e61d8ae55903641395']
{'result': {'trx_hash': 'c7da41ef017e00a7740175d3d1c0f07d5936d23b7c82a6e61d8ae55903641395', 'block_num': 7460650, 'id': '3.1.824860', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info c7da41ef017e00a7740175d3d1c0f07d5936d23b7c82a6e61d8ae55903641395
 {'trx_hash': 'c7da41ef017e00a7740175d3d1c0f07d5936d23b7c82a6e61d8ae55903641395', 'block_num': 7460650, 'id': '3.1.824860', 'trx_in_block': 0}

>> get_block [7460650]
{'result': {'block_id': '0071d72a30c1c827659fa2653b7f087368226651', 'timestamp': '2020-07-13T11:16:26', 'transaction_merkle_root': '08b694cf77316fb37e9e2b12c2d194fd970711db', 'witness': '1.6.10', 'previous': '0071d729da7d02144bda42d2b0127a2ac8063e4d', 'witness_signature': '207c835303b04cf74592c2bcfd8a2faae3385668471075abb0a34c5b1a7f0e61f65b8e05c1ae323038ba3c99515200943aef29056a01cc4da31f607f24ca6aee04', 'transactions': [['c7da41ef017e00a7740175d3d1c0f07d5936d23b7c82a6e61d8ae55903641395', {'extensions': [], 'operation_results': [[4, {'fees': [{'amount': 20996, 'asset_id': '1.3.0'}], 'existed_pv': False, 'process_value': '', 'real_running_time': 480, 'contract_id': '1.16.121', 'relevant_datasize': 35, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}], [5, {'message': '37%', 'affected_account': '1.2.6', 'fees': [{'amount': 7769, 'asset_id': '1.3.0'}]}], [5, {'message': '63%', 'affected_account': '1.2.16', 'fees': [{'amount': 13227, 'asset_id': '1.3.1'}]}]]}]], 'signatures': ['1f5a8068a3f7d15b637628a634a3f23a634054010111dd0a92c5ab0e1911f8afe34fb3a0a8b860a59ff385c2fce5ddf3d21c3540e13bbb558572f89d3a570d1614'], 'ref_block_prefix': 755484624, 'expiration': '2020-07-13T11:36:52', 'ref_block_num': 55073, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.6'}]]}]]}, 'jsonrpc': '2.0', 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 20996, 'asset_id': '1.3.0'}]
### {'message': '37%', 'affected_account': '1.2.6', 'fees': [{'amount': 7769, 'asset_id': '1.3.0'}]}, total_fee: 7769
### {'message': '63%', 'affected_account': '1.2.16', 'fees': [{'amount': 13227, 'asset_id': '1.3.1'}]}, total_fee: 13227
### [COCOS] fee_total_in_block: 20996, fee_total_range_accounts: 20996
### account_balances delta in block: 
  {'1.2.6': {'1.3.0': 7769}, '1.2.16': {'1.3.1': 13227}}
-----------------------------------------------------------------------

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271055743', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.6']
{'result': [{'amount': '13626092783729', 'asset_id': '1.3.0'}], 'jsonrpc': '2.0', 'id': 1}

-------------------- contract owner and caller acccount_balances changed --------------------
>>> contract call op before account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271068970', 'asset_id': '1.3.1'}], '1.2.6': [{'amount': '13626092791498', 'asset_id': '1.3.0'}]}
>>> contract call op before         account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271055743', 'asset_id': '1.3.1'}], '1.2.6': [{'amount': '13626092783729', 'asset_id': '1.3.0'}]}
>>> account_balances delta: 
  {'1.2.16': {'1.3.1': 13227}, '1.2.6': {'1.3.0': 7769}}
---------------------------------------------------------------------------------------------

func_accounts_balances: {'1.2.6': {'1.3.0': 7769}, '1.2.16': {'1.3.1': 13227}}
calc_accounts_balances: {'1.2.16': {'1.3.1': 13227}, '1.2.6': {'1.3.0': 7769}}
******************* calc_contract_call_operation_fee END ************************************

index = 3
>> get_account ['nicotest']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'name': 'nicotest', 'id': '1.2.16', 'cashback_gas': '1.13.30', 'cashback_vote': '1.13.385', 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.13', True], 'asset_locked': {'locked_total': [['1.3.0', '5000001900000']], 'vote_for_witness': {'amount': 1000000, 'asset_id': '1.3.0'}, 'contract_lock_details': [], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'vote_for_committee': {'amount': 900000, 'asset_id': '1.3.0'}}, 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'registrar': '1.2.4', 'cashback_vb': '1.13.262', 'options': {'extensions': [], 'votes': ['1:0', '1:9', '1:10', '0:11', '0:13', '0:14', '0:21'], 'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx'}, 'statistics': '2.6.16'}, 'jsonrpc': '2.0', 'id': 1}

>> get_account ['init1']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7', 1]]}, 'name': 'init1', 'id': '1.2.6', 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7', 1]]}, 'registrar': '1.2.4', 'membership_expiration_date': '1969-12-31T23:59:59', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'contract_lock_details': [], 'committee_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}}, 'options': {'extensions': [], 'votes': [], 'memo_key': 'COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7'}, 'witness_status': ['1.6.2', True], 'statistics': '2.6.6', 'committee_status': ['1.5.1', True]}, 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271055743', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.6']
{'result': [{'amount': '13626092783729', 'asset_id': '1.3.0'}], 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['fe3779a4cbae137392da428f0222e2697311188d0a8889af7ce0a54df70c8047', {'extensions': [], 'signatures': ['20611941b73a0283b3885ea609ceb306232c40b67af3d6b0e5d6adb5fa526796ba513a9499dbe338276a29efb991a021f8428c79116b4f955718355e4cffc347f3'], 'ref_block_prefix': 3100245877, 'expiration': '2020-07-13T11:36:56', 'ref_block_num': 55074, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.6'}]]}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['fe3779a4cbae137392da428f0222e2697311188d0a8889af7ce0a54df70c8047']
{'result': {'trx_hash': 'fe3779a4cbae137392da428f0222e2697311188d0a8889af7ce0a54df70c8047', 'block_num': 7460651, 'id': '3.1.824861', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info fe3779a4cbae137392da428f0222e2697311188d0a8889af7ce0a54df70c8047
 {'trx_hash': 'fe3779a4cbae137392da428f0222e2697311188d0a8889af7ce0a54df70c8047', 'block_num': 7460651, 'id': '3.1.824861', 'trx_in_block': 0}

>> get_block [7460651]
{'result': {'block_id': '0071d72b567bb1d2a8e61d2025e7808adea22aa3', 'timestamp': '2020-07-13T11:16:28', 'transaction_merkle_root': '7ee9d329a67489bc6b24dd1ca598390765f7e429', 'witness': '1.6.7', 'previous': '0071d72a30c1c827659fa2653b7f087368226651', 'witness_signature': '1f42901b955b3a6a177e947cd1f97edbae5cde1e9ed3f41fa9ae6d3bd578d9f16028053f04d6bda729375aab2f9115577ff33ea5df12fd9c5751ba8d1193bc9d42', 'transactions': [['fe3779a4cbae137392da428f0222e2697311188d0a8889af7ce0a54df70c8047', {'extensions': [], 'operation_results': [[4, {'fees': [{'amount': 20997, 'asset_id': '1.3.0'}], 'existed_pv': False, 'process_value': '', 'real_running_time': 481, 'contract_id': '1.16.121', 'relevant_datasize': 35, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}], [5, {'message': '37%', 'affected_account': '1.2.6', 'fees': [{'amount': 7769, 'asset_id': '1.3.0'}]}], [5, {'message': '63%', 'affected_account': '1.2.16', 'fees': [{'amount': 13228, 'asset_id': '1.3.1'}]}]]}]], 'signatures': ['20611941b73a0283b3885ea609ceb306232c40b67af3d6b0e5d6adb5fa526796ba513a9499dbe338276a29efb991a021f8428c79116b4f955718355e4cffc347f3'], 'ref_block_prefix': 3100245877, 'expiration': '2020-07-13T11:36:56', 'ref_block_num': 55074, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.6'}]]}]]}, 'jsonrpc': '2.0', 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 20997, 'asset_id': '1.3.0'}]
### {'message': '37%', 'affected_account': '1.2.6', 'fees': [{'amount': 7769, 'asset_id': '1.3.0'}]}, total_fee: 7769
### {'message': '63%', 'affected_account': '1.2.16', 'fees': [{'amount': 13228, 'asset_id': '1.3.1'}]}, total_fee: 13228
### [COCOS] fee_total_in_block: 20997, fee_total_range_accounts: 20997
### account_balances delta in block: 
  {'1.2.6': {'1.3.0': 7769}, '1.2.16': {'1.3.1': 13228}}
-----------------------------------------------------------------------

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271042515', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.6']
{'result': [{'amount': '13626092775960', 'asset_id': '1.3.0'}], 'jsonrpc': '2.0', 'id': 1}

-------------------- contract owner and caller acccount_balances changed --------------------
>>> contract call op before account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271055743', 'asset_id': '1.3.1'}], '1.2.6': [{'amount': '13626092783729', 'asset_id': '1.3.0'}]}
>>> contract call op before         account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271042515', 'asset_id': '1.3.1'}], '1.2.6': [{'amount': '13626092775960', 'asset_id': '1.3.0'}]}
>>> account_balances delta: 
  {'1.2.16': {'1.3.1': 13228}, '1.2.6': {'1.3.0': 7769}}
---------------------------------------------------------------------------------------------

func_accounts_balances: {'1.2.6': {'1.3.0': 7769}, '1.2.16': {'1.3.1': 13228}}
calc_accounts_balances: {'1.2.16': {'1.3.1': 13228}, '1.2.6': {'1.3.0': 7769}}
******************* calc_contract_call_operation_fee END ************************************

index = 4
>> get_account ['nicotest']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'name': 'nicotest', 'id': '1.2.16', 'cashback_gas': '1.13.30', 'cashback_vote': '1.13.385', 'membership_expiration_date': '1969-12-31T23:59:59', 'witness_status': ['1.6.13', True], 'asset_locked': {'locked_total': [['1.3.0', '5000001900000']], 'vote_for_witness': {'amount': 1000000, 'asset_id': '1.3.0'}, 'contract_lock_details': [], 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'vote_for_committee': {'amount': 900000, 'asset_id': '1.3.0'}}, 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]]}, 'registrar': '1.2.4', 'cashback_vb': '1.13.262', 'options': {'extensions': [], 'votes': ['1:0', '1:9', '1:10', '0:11', '0:13', '0:14', '0:21'], 'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx'}, 'statistics': '2.6.16'}, 'jsonrpc': '2.0', 'id': 1}

>> get_account ['init1']
{'result': {'owner': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7', 1]]}, 'name': 'init1', 'id': '1.2.6', 'active': {'weight_threshold': 1, 'account_auths': [], 'address_auths': [], 'key_auths': [['COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7', 1]]}, 'registrar': '1.2.4', 'membership_expiration_date': '1969-12-31T23:59:59', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'contract_lock_details': [], 'committee_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}, 'witness_freeze': {'amount': '5000000000000', 'asset_id': '1.3.0'}}, 'options': {'extensions': [], 'votes': [], 'memo_key': 'COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7'}, 'witness_status': ['1.6.2', True], 'statistics': '2.6.6', 'committee_status': ['1.5.1', True]}, 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271042515', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.6']
{'result': [{'amount': '13626092775960', 'asset_id': '1.3.0'}], 'jsonrpc': '2.0', 'id': 1}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['3cd73ebe41a707b8cd5bd70e9fc097dfc842474c2d9f6228fff5d91f063fe1c8', {'extensions': [], 'signatures': ['205d3e0d393646bc109c2cc7adcd347eb92ba4147038c519a3b1e0c13a257c743a2348cb645578b104e75f05ff7e313b51f634220decd695d1add698eccf1c388b'], 'ref_block_prefix': 1248026124, 'expiration': '2020-07-13T11:36:58', 'ref_block_num': 55075, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.6'}]]}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['3cd73ebe41a707b8cd5bd70e9fc097dfc842474c2d9f6228fff5d91f063fe1c8']
{'result': {'trx_hash': '3cd73ebe41a707b8cd5bd70e9fc097dfc842474c2d9f6228fff5d91f063fe1c8', 'block_num': 7460652, 'id': '3.1.824862', 'trx_in_block': 0}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info 3cd73ebe41a707b8cd5bd70e9fc097dfc842474c2d9f6228fff5d91f063fe1c8
 {'trx_hash': '3cd73ebe41a707b8cd5bd70e9fc097dfc842474c2d9f6228fff5d91f063fe1c8', 'block_num': 7460652, 'id': '3.1.824862', 'trx_in_block': 0}

>> get_block [7460652]
{'result': {'block_id': '0071d72cee45f9cce451ee3e92165a48100ae2eb', 'timestamp': '2020-07-13T11:16:30', 'transaction_merkle_root': '691bbc9fd1a6e133b7142b6d3c59608067561e77', 'witness': '1.6.8', 'previous': '0071d72b567bb1d2a8e61d2025e7808adea22aa3', 'witness_signature': '2063934c619b9ae66ed3c930c23ebcb18ceb86a3c31dbe47901e6eb905a88c925e3cd1ad0e30b4f89695f14a64fbf7566c819cfd32e45e797c1de0e1b2b0c04878', 'transactions': [['3cd73ebe41a707b8cd5bd70e9fc097dfc842474c2d9f6228fff5d91f063fe1c8', {'extensions': [], 'operation_results': [[4, {'fees': [{'amount': 20939, 'asset_id': '1.3.0'}], 'existed_pv': False, 'process_value': '', 'real_running_time': 423, 'contract_id': '1.16.121', 'relevant_datasize': 35, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}], [5, {'message': '37%', 'affected_account': '1.2.6', 'fees': [{'amount': 7748, 'asset_id': '1.3.0'}]}], [5, {'message': '63%', 'affected_account': '1.2.16', 'fees': [{'amount': 13191, 'asset_id': '1.3.1'}]}]]}]], 'signatures': ['205d3e0d393646bc109c2cc7adcd347eb92ba4147038c519a3b1e0c13a257c743a2348cb645578b104e75f05ff7e313b51f634220decd695d1add698eccf1c388b'], 'ref_block_prefix': 1248026124, 'expiration': '2020-07-13T11:36:58', 'ref_block_num': 55075, 'operations': [[35, {'value_list': [], 'extensions': [], 'contract_id': '1.16.121', 'function_name': 'test_helloworld', 'caller': '1.2.6'}]]}]]}, 'jsonrpc': '2.0', 'id': 1}

-------------------- contract call fee result ------------------------
## total_fee: [{'amount': 20939, 'asset_id': '1.3.0'}]
### {'message': '37%', 'affected_account': '1.2.6', 'fees': [{'amount': 7748, 'asset_id': '1.3.0'}]}, total_fee: 7748
### {'message': '63%', 'affected_account': '1.2.16', 'fees': [{'amount': 13191, 'asset_id': '1.3.1'}]}, total_fee: 13191
### [COCOS] fee_total_in_block: 20939, fee_total_range_accounts: 20939
### account_balances delta in block: 
  {'1.2.6': {'1.3.0': 7748}, '1.2.16': {'1.3.1': 13191}}
-----------------------------------------------------------------------

>> list_account_balances ['1.2.16']
{'result': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271029324', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}

>> list_account_balances ['1.2.6']
{'result': [{'amount': '13626092768212', 'asset_id': '1.3.0'}], 'jsonrpc': '2.0', 'id': 1}

-------------------- contract owner and caller acccount_balances changed --------------------
>>> contract call op before account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271042515', 'asset_id': '1.3.1'}], '1.2.6': [{'amount': '13626092775960', 'asset_id': '1.3.0'}]}
>>> contract call op before         account_balances: 
  {'1.2.16': [{'amount': '5596616774138030', 'asset_id': '1.3.0'}, {'amount': '14271029324', 'asset_id': '1.3.1'}], '1.2.6': [{'amount': '13626092768212', 'asset_id': '1.3.0'}]}
>>> account_balances delta: 
  {'1.2.16': {'1.3.1': 13191}, '1.2.6': {'1.3.0': 7748}}
---------------------------------------------------------------------------------------------

func_accounts_balances: {'1.2.6': {'1.3.0': 7748}, '1.2.16': {'1.3.1': 13191}}
calc_accounts_balances: {'1.2.16': {'1.3.1': 13191}, '1.2.6': {'1.3.0': 7748}}
******************* calc_contract_call_operation_fee END ************************************

ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```  