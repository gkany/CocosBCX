
## 启动节点  
**单节点本地测试**  
单节点部署参考[CocosBCX/chain_init](https://github.com/gkany/CocosBCX/tree/master/chain_init)

## 测试合约  
[contract_34_contract_fee_share_test.lua](https://github.com/gkany/Cocos-Contracts-API/blob/master/contract_34_contract_fee_share_test.lua)
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
    chainhelper:contract_fee_share_test()
end

```

## 合约部署  
``` text
dev@ubuntu:~/data/mrepo/Cocos-Contracts-API$ python3 contract_test.py 
>> unlock ['123456']

{'jsonrpc': '2.0', 'id': 1, 'result': None}


>> list_my_accounts []

{'jsonrpc': '2.0', 'id': 1, 'result': [{'membership_expiration_date': '1969-12-31T23:59:59', 'id': '1.2.5', 'statistics': '2.6.5', 'owner': {'key_auths': [['COCOS8hxjGaAwkNHewgQqg6ERLA7L4J6wkzuhhLRVbKKuJZUYM3dfuS', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'active': {'key_auths': [['COCOS8hxjGaAwkNHewgQqg6ERLA7L4J6wkzuhhLRVbKKuJZUYM3dfuS', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'registrar': '1.2.4', 'committee_status': ['1.5.0', True], 'name': 'init0', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}, 'contract_lock_details': [], 'committee_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}}, 'witness_status': ['1.6.1', True], 'options': {'votes': [], 'memo_key': 'COCOS8hxjGaAwkNHewgQqg6ERLA7L4J6wkzuhhLRVbKKuJZUYM3dfuS', 'extensions': []}}, {'membership_expiration_date': '1969-12-31T23:59:59', 'id': '1.2.6', 'statistics': '2.6.6', 'owner': {'key_auths': [['COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'active': {'key_auths': [['COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'registrar': '1.2.4', 'committee_status': ['1.5.1', True], 'name': 'init1', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}, 'contract_lock_details': [], 'committee_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}}, 'witness_status': ['1.6.2', True], 'options': {'votes': [], 'memo_key': 'COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7', 'extensions': []}}, {'membership_expiration_date': '1969-12-31T23:59:59', 'id': '1.2.7', 'statistics': '2.6.7', 'owner': {'key_auths': [['COCOS8hjpaYLn6RxfQEg61en7fEMy9beYsaWZ4Vm6jnqujQjJ5PQSGo', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'active': {'key_auths': [['COCOS8hjpaYLn6RxfQEg61en7fEMy9beYsaWZ4Vm6jnqujQjJ5PQSGo', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'registrar': '1.2.4', 'committee_status': ['1.5.2', True], 'name': 'init2', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}, 'contract_lock_details': [], 'committee_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}}, 'witness_status': ['1.6.3', True], 'options': {'votes': [], 'memo_key': 'COCOS8hjpaYLn6RxfQEg61en7fEMy9beYsaWZ4Vm6jnqujQjJ5PQSGo', 'extensions': []}}, {'membership_expiration_date': '1969-12-31T23:59:59', 'id': '1.2.8', 'statistics': '2.6.8', 'owner': {'key_auths': [['COCOS5dLtguN6A12QBuV3dmh3YCLg3adkKmY3m2gV7hm9Cw9jtyGd3Y', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'active': {'key_auths': [['COCOS5dLtguN6A12QBuV3dmh3YCLg3adkKmY3m2gV7hm9Cw9jtyGd3Y', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'registrar': '1.2.4', 'committee_status': ['1.5.3', True], 'name': 'init3', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}, 'contract_lock_details': [], 'committee_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}}, 'witness_status': ['1.6.4', True], 'options': {'votes': [], 'memo_key': 'COCOS5dLtguN6A12QBuV3dmh3YCLg3adkKmY3m2gV7hm9Cw9jtyGd3Y', 'extensions': []}}, {'membership_expiration_date': '1969-12-31T23:59:59', 'id': '1.2.9', 'statistics': '2.6.9', 'owner': {'key_auths': [['COCOS7nEYNaXP9P84LQA2kHArvDBTfQ8RizhYd8em3T5zfXBZj29h4i', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'active': {'key_auths': [['COCOS7nEYNaXP9P84LQA2kHArvDBTfQ8RizhYd8em3T5zfXBZj29h4i', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'registrar': '1.2.4', 'committee_status': ['1.5.4', True], 'name': 'init4', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}, 'contract_lock_details': [], 'committee_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}}, 'witness_status': ['1.6.5', True], 'options': {'votes': [], 'memo_key': 'COCOS7nEYNaXP9P84LQA2kHArvDBTfQ8RizhYd8em3T5zfXBZj29h4i', 'extensions': []}}, {'membership_expiration_date': '1969-12-31T23:59:59', 'id': '1.2.10', 'statistics': '2.6.10', 'owner': {'key_auths': [['COCOS8LQSvCgZvwW44iJuCBkVmpR3uUh6J2VFkBJScA3vJq3gXTLCLr', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'active': {'key_auths': [['COCOS8LQSvCgZvwW44iJuCBkVmpR3uUh6J2VFkBJScA3vJq3gXTLCLr', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'registrar': '1.2.4', 'committee_status': ['1.5.5', True], 'name': 'init5', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}, 'contract_lock_details': [], 'committee_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}}, 'witness_status': ['1.6.6', True], 'options': {'votes': [], 'memo_key': 'COCOS8LQSvCgZvwW44iJuCBkVmpR3uUh6J2VFkBJScA3vJq3gXTLCLr', 'extensions': []}}, {'membership_expiration_date': '1969-12-31T23:59:59', 'id': '1.2.11', 'statistics': '2.6.11', 'owner': {'key_auths': [['COCOS6Y5gjJG6YageUeVeoHMMLpESXFi3LdhHWB7dZsKfWQ8giEWN1z', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'active': {'key_auths': [['COCOS6Y5gjJG6YageUeVeoHMMLpESXFi3LdhHWB7dZsKfWQ8giEWN1z', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'registrar': '1.2.4', 'committee_status': ['1.5.6', True], 'name': 'init6', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}, 'contract_lock_details': [], 'committee_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}}, 'witness_status': ['1.6.7', True], 'options': {'votes': [], 'memo_key': 'COCOS6Y5gjJG6YageUeVeoHMMLpESXFi3LdhHWB7dZsKfWQ8giEWN1z', 'extensions': []}}, {'membership_expiration_date': '1969-12-31T23:59:59', 'id': '1.2.12', 'statistics': '2.6.12', 'owner': {'key_auths': [['COCOS8aJKupmQ4XjWyAbsn58wLb2oLHfEDGMFtd7dDbFtxFpBzMGUda', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'active': {'key_auths': [['COCOS8aJKupmQ4XjWyAbsn58wLb2oLHfEDGMFtd7dDbFtxFpBzMGUda', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'registrar': '1.2.4', 'committee_status': ['1.5.7', True], 'name': 'init7', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}, 'contract_lock_details': [], 'committee_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}}, 'witness_status': ['1.6.8', True], 'options': {'votes': [], 'memo_key': 'COCOS8aJKupmQ4XjWyAbsn58wLb2oLHfEDGMFtd7dDbFtxFpBzMGUda', 'extensions': []}}, {'membership_expiration_date': '1969-12-31T23:59:59', 'id': '1.2.13', 'statistics': '2.6.13', 'owner': {'key_auths': [['COCOS5fW5NuvGjaVQTGwcJLwogxheq2KMjm3y5ccAShJqQnB3gNkGbL', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'active': {'key_auths': [['COCOS5fW5NuvGjaVQTGwcJLwogxheq2KMjm3y5ccAShJqQnB3gNkGbL', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'registrar': '1.2.4', 'committee_status': ['1.5.8', True], 'name': 'init8', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}, 'contract_lock_details': [], 'committee_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}}, 'witness_status': ['1.6.9', True], 'options': {'votes': [], 'memo_key': 'COCOS5fW5NuvGjaVQTGwcJLwogxheq2KMjm3y5ccAShJqQnB3gNkGbL', 'extensions': []}}, {'membership_expiration_date': '1969-12-31T23:59:59', 'id': '1.2.14', 'statistics': '2.6.14', 'owner': {'key_auths': [['COCOS5rYpiyVtxuX5PDbxHrPEsjVd6Ucz5fWJTdhvAxoPtZGSxvkE82', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'active': {'key_auths': [['COCOS5rYpiyVtxuX5PDbxHrPEsjVd6Ucz5fWJTdhvAxoPtZGSxvkE82', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'registrar': '1.2.4', 'committee_status': ['1.5.9', True], 'name': 'init9', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}, 'contract_lock_details': [], 'committee_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}}, 'witness_status': ['1.6.10', True], 'options': {'votes': [], 'memo_key': 'COCOS5rYpiyVtxuX5PDbxHrPEsjVd6Ucz5fWJTdhvAxoPtZGSxvkE82', 'extensions': []}}, {'membership_expiration_date': '1969-12-31T23:59:59', 'id': '1.2.15', 'statistics': '2.6.15', 'owner': {'key_auths': [['COCOS6e4j3DaruANMUNsK8PMit8Sp3kA1Dw3EhJb3mpCHeZb7nTgUnP', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'active': {'key_auths': [['COCOS6e4j3DaruANMUNsK8PMit8Sp3kA1Dw3EhJb3mpCHeZb7nTgUnP', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'registrar': '1.2.4', 'committee_status': ['1.5.10', True], 'name': 'init10', 'asset_locked': {'locked_total': [['1.3.0', '10000000000000']], 'witness_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}, 'contract_lock_details': [], 'committee_freeze': {'asset_id': '1.3.0', 'amount': '5000000000000'}}, 'witness_status': ['1.6.11', True], 'options': {'votes': [], 'memo_key': 'COCOS6e4j3DaruANMUNsK8PMit8Sp3kA1Dw3EhJb3mpCHeZb7nTgUnP', 'extensions': []}}, {'membership_expiration_date': '1970-01-01T00:00:00', 'id': '1.2.16', 'statistics': '2.6.16', 'owner': {'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'registrar': '1.2.4', 'active': {'key_auths': [['COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]], 'weight_threshold': 1, 'address_auths': [], 'account_auths': []}, 'name': 'nicotest', 'asset_locked': {'locked_total': [], 'contract_lock_details': []}, 'options': {'votes': [], 'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': []}}]}


setUpClass done

ssssssssssssssssssssssssssssssss>> get_contract ['contract.testapi.contractfeeshare']

{'jsonrpc': '2.0', 'id': 1, 'error': {'code': 1, 'message': 'unspecified: Assert Exception: contract_itr != con_index.end(): The contract (contract.testapi.contractfeeshare) does not exist'}}


>> create_contract_from_file ['nicotest', 'contract.testapi.contractfeeshare', 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', '/home/dev/data/mrepo/Cocos-Contracts-API/contract_34_contract_fee_share_test.lua', 'true']

{'jsonrpc': '2.0', 'id': 1, 'result': ['f100308c0245afeb04516cebd67bac71b383c9d2085dc9c37cfd9065647c9270', {'expiration': '2020-07-01T05:35:16', 'operations': [[34, {'contract_authority': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'name': 'contract.testapi.contractfeeshare', 'data': "function test_set_percent(percent)     chainhelper:log('set_invoke_share_percent')     chainhelper:set_invoke_share_percent(percent) end  function test_helloworld()     chainhelper:log('Hi, Cocos-BCX contract') end  function test_contract_fee_share()     chainhelper:log('contract_fee_share_test')     chainhelper:contract_fee_share_test() end ", 'owner': '1.2.16', 'extensions': []}]], 'ref_block_prefix': 810369034, 'signatures': ['1f2cdcd23c871ec75fbd9e6ce20a170cdd32d91db2e375cb69c6c40999d52c59ce31166a6b071e27742348f504f55bdafdce94301c7eb647871d4e17845ca8f109'], 'ref_block_num': 3377, 'extensions': []}]}


test_contract_34_contract_fee_share done

.ss>> lock []

{'jsonrpc': '2.0', 'id': 1, 'result': None}


tearDownClass done


----------------------------------------------------------------------
Ran 35 tests in 2.072s

OK (skipped=34)
```


## 测试

### 一个transaction中多operation测试
``` text
dev@ubuntu:~/data/mrepo/CocosBCX/feature_test/contract_fee_share$ python3 builder_tx.py 
>> unlock ['123456']
{'id': 1, 'result': None, 'jsonrpc': '2.0'}

>> begin_builder_transaction []
{'id': 1, 'result': 10, 'jsonrpc': '2.0'}

>> transfer ['nicotest', 'init0', 23, 'COCOS', ['', False], False]
{'id': 1, 'result': ['3663d5bddb04af690b5641471fbd9da678aa59fee25f3fa7d5b33af0c5008114', {'operations': [[0, {'to': '1.2.5', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}}]], 'extensions': [], 'ref_block_num': 6152, 'signatures': ['20531217fd4e9e5a4f819948b18d587bee14249f1bd0d11c33b699dae03b95e6fb0f99c272a5ce323bf32860cd7059f14442c47216d96a88b0ba4502cf891b8060'], 'expiration': '2020-07-01T07:17:44', 'ref_block_prefix': 1788441776}], 'jsonrpc': '2.0'}

>> add_operation_to_builder_transaction [10, [0, {'to': '1.2.5', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}}]]
{'id': 1, 'result': None, 'jsonrpc': '2.0'}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], False]
{'id': 1, 'result': ['916842928b3335ec26e7e1f51310e43be5db5152fc72ce7cd0eb79aab489ffa9', {'operations': [[35, {'function_name': 'test_helloworld', 'caller': '1.2.16', 'value_list': [], 'extensions': [], 'contract_id': '1.16.1'}]], 'extensions': [], 'ref_block_num': 6152, 'signatures': ['1f157accacdea241ce8a7f2ddf7c95938884f07609f392a55a62430fc9a1fb439d7a5f5fb5b122a3cc97aa458d35f55602dabd946d8cfdcc18e7e144fa2ab6b022'], 'expiration': '2020-07-01T07:17:44', 'ref_block_prefix': 1788441776}], 'jsonrpc': '2.0'}

>> add_operation_to_builder_transaction [10, [35, {'function_name': 'test_helloworld', 'caller': '1.2.16', 'value_list': [], 'extensions': [], 'contract_id': '1.16.1'}]]
{'id': 1, 'result': None, 'jsonrpc': '2.0'}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], False]
{'id': 1, 'result': ['60fb30374db9481c7682b810b650c1e31c8ae513e361f55e11ac3d521f0c10c0', {'operations': [[35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'value_list': [], 'extensions': [], 'contract_id': '1.16.1'}]], 'extensions': [], 'ref_block_num': 6152, 'signatures': ['1f358c7cf8e49350b07ec61022ae1e79a83c8c287e09b8ba162598ff79fc8fede423b8bd332b457adfcfc453d59c5caf8eee02952180adb87e2789486262a2cbb2'], 'expiration': '2020-07-01T07:17:44', 'ref_block_prefix': 1788441776}], 'jsonrpc': '2.0'}

>> add_operation_to_builder_transaction [10, [35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'value_list': [], 'extensions': [], 'contract_id': '1.16.1'}]]
{'id': 1, 'result': None, 'jsonrpc': '2.0'}

>> transfer ['nicotest', 'init1', 78, 'COCOS', ['', False], False]
{'id': 1, 'result': ['e3eec8209cd70c76c7a756ba8589bf45a1e6fd2f3d1604a773d7f9ba6500a161', {'operations': [[0, {'to': '1.2.6', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}}]], 'extensions': [], 'ref_block_num': 6152, 'signatures': ['202cf9962fc8fec687fb0129048b7ce338f41fa15e82faea19bf0c1ea8dcfe58ce062261b413f428b001dc152213cff1cd1721b798c628135e9c58b6385b425517'], 'expiration': '2020-07-01T07:17:44', 'ref_block_prefix': 1788441776}], 'jsonrpc': '2.0'}

>> add_operation_to_builder_transaction [10, [0, {'to': '1.2.6', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}}]]
{'id': 1, 'result': None, 'jsonrpc': '2.0'}

>> preview_builder_transaction [10]
{'id': 1, 'result': {'extensions': [], 'operations': [[0, {'to': '1.2.5', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}}], [35, {'function_name': 'test_helloworld', 'caller': '1.2.16', 'value_list': [], 'extensions': [], 'contract_id': '1.16.1'}], [35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'value_list': [], 'extensions': [], 'contract_id': '1.16.1'}], [0, {'to': '1.2.6', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}}]], 'expiration': '1970-01-01T00:00:00', 'ref_block_num': 0, 'ref_block_prefix': 0}, 'jsonrpc': '2.0'}

>> sign_builder_transaction [10, True]
{'id': 1, 'result': ['213096dff39e86fd37241cc943b67845eae588c9513e49021ec1fe9b85d1d8ab', {'operations': [[0, {'to': '1.2.5', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}}], [35, {'function_name': 'test_helloworld', 'caller': '1.2.16', 'value_list': [], 'extensions': [], 'contract_id': '1.16.1'}], [35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'value_list': [], 'extensions': [], 'contract_id': '1.16.1'}], [0, {'to': '1.2.6', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}}]], 'extensions': [], 'ref_block_num': 6152, 'signatures': ['1f65584ef7de5df9348d1849b36a0f3fb6ec28126962ad98af4221a9f440850e5160e12fe81548116c1cf66079a1cce0835324a8976ed694c837819a0c626c2940', '2057714cacb4f47c82ead43ba1f62760d1633c8fa98f0c5bf84cbfdb881c2bd4001de75de355b2b13567fb76734d3222b2675ee01af4764097f84296e5f8132579'], 'expiration': '2020-07-01T07:17:44', 'ref_block_prefix': 1788441776}], 'jsonrpc': '2.0'}

sign result: ['213096dff39e86fd37241cc943b67845eae588c9513e49021ec1fe9b85d1d8ab', {'operations': [[0, {'to': '1.2.5', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}}], [35, {'function_name': 'test_helloworld', 'caller': '1.2.16', 'value_list': [], 'extensions': [], 'contract_id': '1.16.1'}], [35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'value_list': [], 'extensions': [], 'contract_id': '1.16.1'}], [0, {'to': '1.2.6', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}}]], 'extensions': [], 'ref_block_num': 6152, 'signatures': ['1f65584ef7de5df9348d1849b36a0f3fb6ec28126962ad98af4221a9f440850e5160e12fe81548116c1cf66079a1cce0835324a8976ed694c837819a0c626c2940', '2057714cacb4f47c82ead43ba1f62760d1633c8fa98f0c5bf84cbfdb881c2bd4001de75de355b2b13567fb76734d3222b2675ee01af4764097f84296e5f8132579'], 'expiration': '2020-07-01T07:17:44', 'ref_block_prefix': 1788441776}]
>> get_transaction_in_block_info ['213096dff39e86fd37241cc943b67845eae588c9513e49021ec1fe9b85d1d8ab']
{'id': 1, 'result': {'id': '3.1.9', 'trx_in_block': 0, 'block_num': 6163, 'trx_hash': '213096dff39e86fd37241cc943b67845eae588c9513e49021ec1fe9b85d1d8ab'}, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info 213096dff39e86fd37241cc943b67845eae588c9513e49021ec1fe9b85d1d8ab
 {'id': '3.1.9', 'trx_in_block': 0, 'block_num': 6163, 'trx_hash': '213096dff39e86fd37241cc943b67845eae588c9513e49021ec1fe9b85d1d8ab'}

>> get_block [6163]
{'id': 1, 'result': {'block_id': '000018131f5dfecb296f476ac0a5e8e9b65ece8e', 'transaction_merkle_root': '95b0802a8f029921122a0029f9b77d36900acf7a', 'witness': '1.6.7', 'witness_signature': '1f02a0b8d25e63cf97f9f4e7d4b6c549726f2ba2a59bbac63c81c8b27e3226fbe77c547d00fb7236aaa547c0a06d78fe7d0ac1eb206a94be2074c75dbbd596fbd8', 'previous': '00001812a1e074ebe96bd6fa109f58fa38c0050e', 'timestamp': '2020-07-01T06:57:16', 'transactions': [['213096dff39e86fd37241cc943b67845eae588c9513e49021ec1fe9b85d1d8ab', {'operations': [[0, {'to': '1.2.5', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}}], [35, {'function_name': 'test_helloworld', 'caller': '1.2.16', 'value_list': [], 'extensions': [], 'contract_id': '1.16.1'}], [35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'value_list': [], 'extensions': [], 'contract_id': '1.16.1'}], [0, {'to': '1.2.6', 'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}}]], 'extensions': [], 'ref_block_num': 6152, 'signatures': ['1f65584ef7de5df9348d1849b36a0f3fb6ec28126962ad98af4221a9f440850e5160e12fe81548116c1cf66079a1cce0835324a8976ed694c837819a0c626c2940', '2057714cacb4f47c82ead43ba1f62760d1633c8fa98f0c5bf84cbfdb881c2bd4001de75de355b2b13567fb76734d3222b2675ee01af4764097f84296e5f8132579'], 'expiration': '2020-07-01T07:17:44', 'ref_block_prefix': 1788441776, 'operation_results': [[1, {'real_running_time': 178, 'fees': [{'asset_id': '1.3.0', 'amount': 2000000}]}], [4, {'process_value': '', 'relevant_datasize': 35, 'real_running_time': 335, 'fees': [{'asset_id': '1.3.0', 'amount': 2386757}], 'existed_pv': False, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'asset_id': '1.3.0', 'amount': 2386757}]}]], 'contract_id': '1.16.1'}], [4, {'process_value': '', 'relevant_datasize': 35, 'real_running_time': 336, 'fees': [{'asset_id': '1.3.0', 'amount': 2387757}], 'existed_pv': False, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}], [5, {'message': '20%', 'affected_account': '1.2.6', 'fees': [{'asset_id': '1.3.0', 'amount': 477552}]}], [5, {'message': '80%', 'affected_account': '1.2.16', 'fees': [{'asset_id': '1.3.0', 'amount': 1910205}]}]], 'contract_id': '1.16.1'}], [1, {'real_running_time': 146, 'fees': [{'asset_id': '1.3.0', 'amount': 2000000}]}]]}]]}, 'jsonrpc': '2.0'}

```

#### cli_wallet 查看区块6163  

``` shell
unlocked >>> get_block 6163  
```  
执行结果  
``` json
{
  "previous": "00001812a1e074ebe96bd6fa109f58fa38c0050e",
  "timestamp": "2020-07-01T06:57:16",
  "witness": "1.6.7",
  "transaction_merkle_root": "95b0802a8f029921122a0029f9b77d36900acf7a",
  "witness_signature": "1f02a0b8d25e63cf97f9f4e7d4b6c549726f2ba2a59bbac63c81c8b27e3226fbe77c547d00fb7236aaa547c0a06d78fe7d0ac1eb206a94be2074c75dbbd596fbd8",
  "block_id": "000018131f5dfecb296f476ac0a5e8e9b65ece8e",
  "transactions": [[
      "213096dff39e86fd37241cc943b67845eae588c9513e49021ec1fe9b85d1d8ab",{
        "ref_block_num": 6152,
        "ref_block_prefix": 1788441776,
        "expiration": "2020-07-01T07:17:44",
        "operations": [[
            0,{
              "from": "1.2.16",
              "to": "1.2.5",
              "amount": {
                "amount": 2300000,
                "asset_id": "1.3.0"
              },
              "extensions": []
            }
          ],[
            35,{
              "caller": "1.2.16",
              "contract_id": "1.16.1",
              "function_name": "test_helloworld",
              "value_list": [],
              "extensions": []
            }
          ],[
            35,{
              "caller": "1.2.6",
              "contract_id": "1.16.1",
              "function_name": "test_helloworld",
              "value_list": [],
              "extensions": []
            }
          ],[
            0,{
              "from": "1.2.16",
              "to": "1.2.6",
              "amount": {
                "amount": 7800000,
                "asset_id": "1.3.0"
              },
              "extensions": []
            }
          ]
        ],
        "extensions": [],
        "signatures": [
          "1f65584ef7de5df9348d1849b36a0f3fb6ec28126962ad98af4221a9f440850e5160e12fe81548116c1cf66079a1cce0835324a8976ed694c837819a0c626c2940",
          "2057714cacb4f47c82ead43ba1f62760d1633c8fa98f0c5bf84cbfdb881c2bd4001de75de355b2b13567fb76734d3222b2675ee01af4764097f84296e5f8132579"
        ],
        "operation_results": [[
            1,{
              "fees": [{
                  "amount": 2000000,
                  "asset_id": "1.3.0"
                }
              ],
              "real_running_time": 178
            }
          ],[
            4,{
              "fees": [{
                  "amount": 2386757,
                  "asset_id": "1.3.0"
                }
              ],
              "contract_id": "1.16.1",
              "contract_affecteds": [[
                  3,{
                    "affected_account": "1.2.16",
                    "message": "Hi, Cocos-BCX contract"
                  }
                ],[
                  5,{
                    "fees": [{
                        "amount": 2386757,
                        "asset_id": "1.3.0"
                      }
                    ],
                    "affected_account": "1.2.16",
                    "message": "100%"
                  }
                ]
              ],
              "real_running_time": 335,
              "existed_pv": false,
              "process_value": "",
              "relevant_datasize": 35
            }
          ],[
            4,{
              "fees": [{
                  "amount": 2387757,
                  "asset_id": "1.3.0"
                }
              ],
              "contract_id": "1.16.1",
              "contract_affecteds": [[
                  3,{
                    "affected_account": "1.2.6",
                    "message": "Hi, Cocos-BCX contract"
                  }
                ],[
                  5,{
                    "fees": [{
                        "amount": 477552,
                        "asset_id": "1.3.0"
                      }
                    ],
                    "affected_account": "1.2.6",
                    "message": "20%"
                  }
                ],[
                  5,{
                    "fees": [{
                        "amount": 1910205,
                        "asset_id": "1.3.0"
                      }
                    ],
                    "affected_account": "1.2.16",
                    "message": "80%"
                  }
                ]
              ],
              "real_running_time": 336,
              "existed_pv": false,
              "process_value": "",
              "relevant_datasize": 35
            }
          ],[
            1,{
              "fees": [{
                  "amount": 2000000,
                  "asset_id": "1.3.0"
                }
              ],
              "real_running_time": 146
            }
          ]
        ]
      }
    ]
  ]
}

```

**说明：**  
* block中的operations和operation_results是按照索引顺序一一对应的  


