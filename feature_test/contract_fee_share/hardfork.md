
# 硬分叉功能测试
-----------------------
## 设置  
### 设置说明
设置的硬分叉时间节点：
head_block_time: 2020-07-07T07:02:28, hard_fork time: 2020-07-07T00:30:00
说明：
* hf 的时间其实设置的是不合理的，正常应该设置为比head_block time 大；    
* hf时间设置不合理，运行后发现，代码逻辑判断上写反了    
  写错的逻辑    
  ``` c++
    if(db.head_block_time() > hard_fork_time) {
        // old 逻辑
    } else {
        // 新的逻辑
    }
  ```
  正确的逻辑    
  ``` c++
    if(db.head_block_time() < hard_fork_time) {
        // old 逻辑
    } else {
        // 新的逻辑
    }
  ```
* 合理利用了这个bug，避免又要修改代码，又要重新设置 hardfork time
节点启动后，运行的是old 逻辑。
由于正好需要去测试旧的逻辑，所以没有修改代码，直接调用合约测试旧的逻辑。
测试完成后，修改代码逻辑为正确的逻辑，此时运行的是新的逻辑。

### 测试环境  
本地，单节点  
路径：
``` text
/home/ck/xukang/local/contract_fee_share2
```  

## 1. old的逻辑流程测试
``` json
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 builder_tx.py 
>> unlock ['123456']
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> begin_builder_transaction []
{'jsonrpc': '2.0', 'id': 1, 'result': 0}

>> transfer ['nicotest', 'init0', 23, 'COCOS', ['', False], False]
{'jsonrpc': '2.0', 'id': 1, 'result': ['f31b7ccb98562371b09e296c280b8eacade49150418323e108909a062512e9bf', {'signatures': ['1f07abb4c320df8e01472cd10df6551d582bfd1e3f13a0d6ee248470ffd9b9b0ba4d13b0c6e77de5b3dfcb429b5830e7a1f05b3c61e34f9781062bf53710f0a152'], 'expiration': '2020-07-07T07:29:48', 'ref_block_num': 267, 'operations': [[0, {'from': '1.2.16', 'to': '1.2.5', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}, 'extensions': []}]], 'extensions': [], 'ref_block_prefix': 2913680693}]}

>> add_operation_to_builder_transaction [0, [0, {'from': '1.2.16', 'to': '1.2.5', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}, 'extensions': []}]]
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], False]
{'jsonrpc': '2.0', 'id': 1, 'result': ['5e6ee91280a9dd3653f98ef78fe62c19b7511a42cb5ceb98859c09625cd1d704', {'signatures': ['1f13112b5bb92aa5e0313f4bdcfc12dba35d2ba1be286c01b65493aa96ad14e3bc0705073f2da0bdb12e30c1e1b99c5267ff5c6a2ef65018ec0476cf04a972474e'], 'expiration': '2020-07-07T07:29:48', 'ref_block_num': 267, 'operations': [[35, {'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.1', 'value_list': [], 'extensions': []}]], 'extensions': [], 'ref_block_prefix': 2913680693}]}

>> add_operation_to_builder_transaction [0, [35, {'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.1', 'value_list': [], 'extensions': []}]]
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], False]
{'jsonrpc': '2.0', 'id': 1, 'result': ['402f6d85a012dcaee94a51febbff176d61a75d1b893bf6b75ae21431eff1024e', {'signatures': ['1f625e74d59e45a7db7d3429b30437e98e4cf08f412d36818d2537a2fbca1a4e6742840d4faa2ef7a6662a1df8ecb3df9c488fe0ebb5f3e45dfab65b53c566fca7'], 'expiration': '2020-07-07T07:29:48', 'ref_block_num': 267, 'operations': [[35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.1', 'value_list': [], 'extensions': []}]], 'extensions': [], 'ref_block_prefix': 2913680693}]}

>> add_operation_to_builder_transaction [0, [35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.1', 'value_list': [], 'extensions': []}]]
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> transfer ['nicotest', 'init1', 78, 'COCOS', ['', False], False]
{'jsonrpc': '2.0', 'id': 1, 'result': ['8705da5973984a4c237bcd671b24d76e109bb12eae90b61811b80bb99020700f', {'signatures': ['206335b9864cd80c792b615f6c7bc8f454a6a1fd20c553406fdd829469879b92a94d37b0a914894069f0b23da537143d015dbdb2cfb690cdadae67b02758abac76'], 'expiration': '2020-07-07T07:29:48', 'ref_block_num': 267, 'operations': [[0, {'from': '1.2.16', 'to': '1.2.6', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}, 'extensions': []}]], 'extensions': [], 'ref_block_prefix': 2913680693}]}

>> add_operation_to_builder_transaction [0, [0, {'from': '1.2.16', 'to': '1.2.6', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}, 'extensions': []}]]
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> preview_builder_transaction [0]
{'jsonrpc': '2.0', 'id': 1, 'result': {'operations': [[0, {'from': '1.2.16', 'to': '1.2.5', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}, 'extensions': []}], [35, {'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.1', 'value_list': [], 'extensions': []}], [35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.1', 'value_list': [], 'extensions': []}], [0, {'from': '1.2.16', 'to': '1.2.6', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}, 'extensions': []}]], 'extensions': [], 'expiration': '1970-01-01T00:00:00', 'ref_block_prefix': 0, 'ref_block_num': 0}}

>> sign_builder_transaction [0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['fc1c2bb9c932536ed1184171934f8a53f2058688a3ba83419672332b11cd3f84', {'signatures': ['1f1d26503ba8371d7be6f02972b6b28755dcfe75f06e3ed5f34c68852a30d6ba617ce95f4bbd1ad07a4204554234474089e891b3694b08039e095a8b0251ca2320', '1f2bf779fd162544b2a9d41c5826f3234020ca61311ab9a755a1dd34b1f48cf74a77be2ac8cc347def4b8268c9551cf62ad58ddcb8a0852f540902317d8587faca'], 'expiration': '2020-07-07T07:29:48', 'ref_block_num': 267, 'operations': [[0, {'from': '1.2.16', 'to': '1.2.5', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}, 'extensions': []}], [35, {'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.1', 'value_list': [], 'extensions': []}], [35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.1', 'value_list': [], 'extensions': []}], [0, {'from': '1.2.16', 'to': '1.2.6', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}, 'extensions': []}]], 'extensions': [], 'ref_block_prefix': 2913680693}]}

>> get_transaction_in_block_info ['fc1c2bb9c932536ed1184171934f8a53f2058688a3ba83419672332b11cd3f84']
{'jsonrpc': '2.0', 'id': 1, 'result': {'block_num': 276, 'id': '3.1.4', 'trx_hash': 'fc1c2bb9c932536ed1184171934f8a53f2058688a3ba83419672332b11cd3f84', 'trx_in_block': 0}}

>> get_transaction_in_block_info fc1c2bb9c932536ed1184171934f8a53f2058688a3ba83419672332b11cd3f84
 {'block_num': 276, 'id': '3.1.4', 'trx_hash': 'fc1c2bb9c932536ed1184171934f8a53f2058688a3ba83419672332b11cd3f84', 'trx_in_block': 0}

>> get_block [276]
{'jsonrpc': '2.0', 'id': 1, 'result': {'transaction_merkle_root': '2ef7e280ab92b66b8a37f0577a585659f790f5a3', 'block_id': '000001144cd2e5c2ad7cdbfbb548586004aa28fc', 'witness': '1.6.10', 'timestamp': '2020-07-07T07:09:20', 'previous': '000001136af7281fbc9f0c6e61da93eb3dd65d56', 'witness_signature': '2027a994b8c13de86f7d98210ba17351b2f65f0cb62ef23e9fa03c03b0d59975b4712d1edb784973e61140c0819afffc248c3fcd404099098a272ee1c73fe920c1', 'transactions': [['fc1c2bb9c932536ed1184171934f8a53f2058688a3ba83419672332b11cd3f84', {'signatures': ['1f1d26503ba8371d7be6f02972b6b28755dcfe75f06e3ed5f34c68852a30d6ba617ce95f4bbd1ad07a4204554234474089e891b3694b08039e095a8b0251ca2320', '1f2bf779fd162544b2a9d41c5826f3234020ca61311ab9a755a1dd34b1f48cf74a77be2ac8cc347def4b8268c9551cf62ad58ddcb8a0852f540902317d8587faca'], 'expiration': '2020-07-07T07:29:48', 'ref_block_num': 267, 'operation_results': [[1, {'real_running_time': 86, 'fees': [{'asset_id': '1.3.0', 'amount': 2000000}]}], [4, {'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'Hi, Cocos-BCX contract'}]], 'existed_pv': False, 'relevant_datasize': 35, 'fees': [{'asset_id': '1.3.0', 'amount': 2435757}], 'process_value': '', 'contract_id': '1.16.1', 'real_running_time': 384}], [4, {'contract_affecteds': [[3, {'affected_account': '1.2.6', 'message': 'Hi, Cocos-BCX contract'}]], 'existed_pv': False, 'relevant_datasize': 35, 'fees': [{'asset_id': '1.3.0', 'amount': 2363757}], 'process_value': '', 'contract_id': '1.16.1', 'real_running_time': 312}], [1, {'real_running_time': 102, 'fees': [{'asset_id': '1.3.0', 'amount': 2000000}]}]], 'operations': [[0, {'from': '1.2.16', 'to': '1.2.5', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}, 'extensions': []}], [35, {'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.1', 'value_list': [], 'extensions': []}], [35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.1', 'value_list': [], 'extensions': []}], [0, {'from': '1.2.16', 'to': '1.2.6', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}, 'extensions': []}]], 'extensions': [], 'ref_block_prefix': 2913680693}]]}}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['be5c9de986e2efe3402bce4ed1154053141be689e5957c6af827c82ad02c8f9b', {'signatures': ['1f338de868ed511fd78627e7305bee2efeb58ad9f3fd76bb85f78f57050043cf7c0abc206aa86ac6692fa2bb8f355aceefe7af5804e703560732bff57b051d9170'], 'expiration': '2020-07-07T07:29:50', 'ref_block_num': 268, 'operations': [[35, {'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.1', 'value_list': [], 'extensions': []}]], 'extensions': [], 'ref_block_prefix': 1394505510}]}

>> get_transaction_in_block_info ['be5c9de986e2efe3402bce4ed1154053141be689e5957c6af827c82ad02c8f9b']
{'jsonrpc': '2.0', 'id': 1, 'result': {'block_num': 277, 'id': '3.1.5', 'trx_hash': 'be5c9de986e2efe3402bce4ed1154053141be689e5957c6af827c82ad02c8f9b', 'trx_in_block': 0}}

>> get_transaction_in_block_info be5c9de986e2efe3402bce4ed1154053141be689e5957c6af827c82ad02c8f9b
 {'block_num': 277, 'id': '3.1.5', 'trx_hash': 'be5c9de986e2efe3402bce4ed1154053141be689e5957c6af827c82ad02c8f9b', 'trx_in_block': 0}

>> get_block [277]
{'jsonrpc': '2.0', 'id': 1, 'result': {'transaction_merkle_root': '547e35ecc0d0a74c719e3d2b62194f2f252b54a9', 'block_id': '00000115f09955c36a11ca2807d194c38a973d49', 'witness': '1.6.4', 'timestamp': '2020-07-07T07:09:22', 'previous': '000001144cd2e5c2ad7cdbfbb548586004aa28fc', 'witness_signature': '20398d8aebdc2d1ef96c9184c80f5cc9f4e8fdae807868f25399482d83b22d024c2d7e4e6dec40370df51717cc4ecac3871d61a1c9aa232d495221839833b1375c', 'transactions': [['be5c9de986e2efe3402bce4ed1154053141be689e5957c6af827c82ad02c8f9b', {'signatures': ['1f338de868ed511fd78627e7305bee2efeb58ad9f3fd76bb85f78f57050043cf7c0abc206aa86ac6692fa2bb8f355aceefe7af5804e703560732bff57b051d9170'], 'expiration': '2020-07-07T07:29:50', 'ref_block_num': 268, 'operation_results': [[4, {'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'Hi, Cocos-BCX contract'}]], 'existed_pv': False, 'relevant_datasize': 35, 'fees': [{'asset_id': '1.3.0', 'amount': 2545757}], 'process_value': '', 'contract_id': '1.16.1', 'real_running_time': 494}]], 'operations': [[35, {'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.1', 'value_list': [], 'extensions': []}]], 'extensions': [], 'ref_block_prefix': 1394505510}]]}}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['b415d1e18a98b7ded3e3d10b8f1fb2ae06cc2fa11c5de599a154ca685abc7fe4', {'signatures': ['1f4c0c55f2c8550635db3caffa7880bb593a29d22c860831753697910c494d46543d9c8921b3bc27b89661a0a935567973a3af9cc608f0b61d7059c13ef390e11f'], 'expiration': '2020-07-07T07:29:52', 'ref_block_num': 269, 'operations': [[35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.1', 'value_list': [], 'extensions': []}]], 'extensions': [], 'ref_block_prefix': 2104020942}]}

>> get_transaction_in_block_info ['b415d1e18a98b7ded3e3d10b8f1fb2ae06cc2fa11c5de599a154ca685abc7fe4']
{'jsonrpc': '2.0', 'id': 1, 'result': {'block_num': 278, 'id': '3.1.6', 'trx_hash': 'b415d1e18a98b7ded3e3d10b8f1fb2ae06cc2fa11c5de599a154ca685abc7fe4', 'trx_in_block': 0}}

>> get_transaction_in_block_info b415d1e18a98b7ded3e3d10b8f1fb2ae06cc2fa11c5de599a154ca685abc7fe4
 {'block_num': 278, 'id': '3.1.6', 'trx_hash': 'b415d1e18a98b7ded3e3d10b8f1fb2ae06cc2fa11c5de599a154ca685abc7fe4', 'trx_in_block': 0}

>> get_block [278]
{'jsonrpc': '2.0', 'id': 1, 'result': {'transaction_merkle_root': '2adb3891800e3f2020de320d3bb7541a371104f2', 'block_id': '00000116d5fe3dc0c6bd1a27e6d5880b0f955097', 'witness': '1.6.1', 'timestamp': '2020-07-07T07:09:24', 'previous': '00000115f09955c36a11ca2807d194c38a973d49', 'witness_signature': '20340bf0b92047a9d450296f875fe190a340c552fdc4881a286a2bdce55e632099202c645d473c6ff343149e4a63570f887da44e6dec1971bc3b559733150bb457', 'transactions': [['b415d1e18a98b7ded3e3d10b8f1fb2ae06cc2fa11c5de599a154ca685abc7fe4', {'signatures': ['1f4c0c55f2c8550635db3caffa7880bb593a29d22c860831753697910c494d46543d9c8921b3bc27b89661a0a935567973a3af9cc608f0b61d7059c13ef390e11f'], 'expiration': '2020-07-07T07:29:52', 'ref_block_num': 269, 'operation_results': [[4, {'contract_affecteds': [[3, {'affected_account': '1.2.6', 'message': 'Hi, Cocos-BCX contract'}]], 'existed_pv': False, 'relevant_datasize': 35, 'fees': [{'asset_id': '1.3.0', 'amount': 2423757}], 'process_value': '', 'contract_id': '1.16.1', 'real_running_time': 372}]], 'operations': [[35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.1', 'value_list': [], 'extensions': []}]], 'extensions': [], 'ref_block_prefix': 2104020942}]]}}
```

为了拥有更多测试数据，上面的流程执行了多次。

## 2. 新的流程  
### 2.1 未修改费用比例之前  
** a.单个合约调用测试**  
``` json
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 builder_tx.py 
>> unlock ['123456']
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['aac73fd2a099df9be3a4312f81318703421741fd6bc5b621f37636dc312a124d', {'expiration': '2020-07-07T08:10:26', 'ref_block_num': 1367, 'signatures': ['2040b3e6216e544b3e3995c5682d97f039fa140373fad27cb0380906f39c7a676002f04e475f402279dad492bb918ea688febdc22052cd4d84f8dc9c388509d1b7'], 'operations': [[35, {'caller': '1.2.16', 'extensions': [], 'value_list': [], 'function_name': 'test_helloworld', 'contract_id': '1.16.1'}]], 'extensions': [], 'ref_block_prefix': 3053158061}]}

>> get_transaction_in_block_info ['aac73fd2a099df9be3a4312f81318703421741fd6bc5b621f37636dc312a124d']
{'jsonrpc': '2.0', 'id': 1, 'result': {'trx_in_block': 0, 'id': '3.1.30', 'block_num': 1378, 'trx_hash': 'aac73fd2a099df9be3a4312f81318703421741fd6bc5b621f37636dc312a124d'}}

>> get_transaction_in_block_info aac73fd2a099df9be3a4312f81318703421741fd6bc5b621f37636dc312a124d
 {'trx_in_block': 0, 'id': '3.1.30', 'block_num': 1378, 'trx_hash': 'aac73fd2a099df9be3a4312f81318703421741fd6bc5b621f37636dc312a124d'}

>> get_block [1378]
{'jsonrpc': '2.0', 'id': 1, 'result': {'previous': '00000561e7b01d065067a83e40fd7e160b2a809e', 'witness': '1.6.6', 'witness_signature': '20423dcb1566275ef79efc207d5742d7a52b6880af61c4e22af55fa2c2f3623d6d035dcd2df31373099c40d7a3af181f10b2a98f7f729d203e2a823fd9949157ba', 'transaction_merkle_root': '7cd1332b1f5cf17a43c4ec41778c4c8a75dda4d7', 'transactions': [['aac73fd2a099df9be3a4312f81318703421741fd6bc5b621f37636dc312a124d', {'expiration': '2020-07-07T08:10:26', 'ref_block_num': 1367, 'signatures': ['2040b3e6216e544b3e3995c5682d97f039fa140373fad27cb0380906f39c7a676002f04e475f402279dad492bb918ea688febdc22052cd4d84f8dc9c388509d1b7'], 'operations': [[35, {'caller': '1.2.16', 'extensions': [], 'value_list': [], 'function_name': 'test_helloworld', 'contract_id': '1.16.1'}]], 'extensions': [], 'ref_block_prefix': 3053158061, 'operation_results': [[4, {'contract_id': '1.16.1', 'relevant_datasize': 35, 'real_running_time': 610, 'fees': [{'asset_id': '1.3.0', 'amount': 2661757}], 'process_value': '', 'existed_pv': False, 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'Hi, Cocos-BCX contract'}], [5, {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'asset_id': '1.3.0', 'amount': 2661757}]}]]}], [1, {'real_running_time': 109, 'fees': [{'asset_id': '1.3.1', 'amount': 100000}]}]]}]], 'timestamp': '2020-07-07T07:49:58', 'block_id': '00000562f1891dd3575d8a2ea668a322380bbab1'}}
```

b. 多个调用
``` json
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 builder_tx.py 
>> unlock ['123456']
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> begin_builder_transaction []
{'jsonrpc': '2.0', 'id': 1, 'result': 0}

>> transfer ['nicotest', 'init0', 23, 'COCOS', ['', False], False]
{'jsonrpc': '2.0', 'id': 1, 'result': ['25d5f84bda29f9e2d09ca5d4e94851900fd005f3e93bd888be60de0fce4b3552', {'signatures': ['207ceb98ad669217ece7317c89066fd0508ea2a8bf1f26aa42ed6d76a1fbd5839773ec4fec05c262404262b20516fb055135f2623112aca085be1873b087e780a3'], 'ref_block_num': 1522, 'operations': [[0, {'amount': {'amount': 2300000, 'asset_id': '1.3.0'}, 'extensions': [], 'to': '1.2.5', 'from': '1.2.16'}]], 'expiration': '2020-07-07T08:15:58', 'extensions': [], 'ref_block_prefix': 1848249812}]}

>> add_operation_to_builder_transaction [0, [0, {'amount': {'amount': 2300000, 'asset_id': '1.3.0'}, 'extensions': [], 'to': '1.2.5', 'from': '1.2.16'}]]
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], False]
{'jsonrpc': '2.0', 'id': 1, 'result': ['6aceceb7490a8df7b8c5c14107a6df5661c348b6e2f8a3935fc2d482b3c2acda', {'signatures': ['2059b2758417387a08832199217f19fa84c906a495d988ea3ee294d5b204bdebd36465a09b6b203037e3625521b5b14d3bdc30218a5325a736fbc184105703300c'], 'ref_block_num': 1522, 'operations': [[35, {'value_list': [], 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.1'}]], 'expiration': '2020-07-07T08:15:58', 'extensions': [], 'ref_block_prefix': 1848249812}]}

>> add_operation_to_builder_transaction [0, [35, {'value_list': [], 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.1'}]]
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], False]
{'jsonrpc': '2.0', 'id': 1, 'result': ['60795960d4f5a1e7916da9f7279768e2f83b92e0f00fda3d8f8bab14d30fec00', {'signatures': ['2050585e32d74a63e6f03282f96705576fa0f2f0b6e4379f262cf527807b3ce06b025c7a215a99f8c2458956616c698455a9164ecc4cd810f63abb9e28aca3cda0'], 'ref_block_num': 1522, 'operations': [[35, {'value_list': [], 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.1'}]], 'expiration': '2020-07-07T08:15:58', 'extensions': [], 'ref_block_prefix': 1848249812}]}

>> add_operation_to_builder_transaction [0, [35, {'value_list': [], 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.1'}]]
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> transfer ['nicotest', 'init1', 78, 'COCOS', ['', False], False]
{'jsonrpc': '2.0', 'id': 1, 'result': ['9a96d5db631de34362ea44b9d1d62f9afb72c8373b565c04bff901f14278933e', {'signatures': ['1f64f3852f99706c83a058e7d9050ed0b139046045399b11c0f8a9b78a2b71b8024f2d585d4308ce2797ad097ba9e9ca4116a510ce53dac791092c94024b6e60ab'], 'ref_block_num': 1522, 'operations': [[0, {'amount': {'amount': 7800000, 'asset_id': '1.3.0'}, 'extensions': [], 'to': '1.2.6', 'from': '1.2.16'}]], 'expiration': '2020-07-07T08:15:58', 'extensions': [], 'ref_block_prefix': 1848249812}]}

>> add_operation_to_builder_transaction [0, [0, {'amount': {'amount': 7800000, 'asset_id': '1.3.0'}, 'extensions': [], 'to': '1.2.6', 'from': '1.2.16'}]]
{'jsonrpc': '2.0', 'id': 1, 'result': None}

>> preview_builder_transaction [0]
{'jsonrpc': '2.0', 'id': 1, 'result': {'operations': [[0, {'amount': {'amount': 2300000, 'asset_id': '1.3.0'}, 'extensions': [], 'to': '1.2.5', 'from': '1.2.16'}], [35, {'value_list': [], 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.1'}], [35, {'value_list': [], 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.1'}], [0, {'amount': {'amount': 7800000, 'asset_id': '1.3.0'}, 'extensions': [], 'to': '1.2.6', 'from': '1.2.16'}]], 'ref_block_num': 0, 'expiration': '1970-01-01T00:00:00', 'extensions': [], 'ref_block_prefix': 0}}

>> sign_builder_transaction [0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['5859d4c669f400fc2bb91b0a381480e522483d5e4a79c1c78333662ef6eb9e22', {'signatures': ['202755f280fc53956d0270710a4d2a13127e901d4cf79754043544c2f0f4bb4baa418c116badf09b9df5a1b680f50de1600be4f1bc6d363328b38f69d690656a0a', '1f4aafa547d4f634435b51da69f4bca3a5eac0998ee44503d716a9cef9cc57746956fd1235adfd8f30fe28fa3f43f2715a440e4472748eda44304cd29331a677ed'], 'ref_block_num': 1522, 'operations': [[0, {'amount': {'amount': 2300000, 'asset_id': '1.3.0'}, 'extensions': [], 'to': '1.2.5', 'from': '1.2.16'}], [35, {'value_list': [], 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.1'}], [35, {'value_list': [], 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.1'}], [0, {'amount': {'amount': 7800000, 'asset_id': '1.3.0'}, 'extensions': [], 'to': '1.2.6', 'from': '1.2.16'}]], 'expiration': '2020-07-07T08:15:58', 'extensions': [], 'ref_block_prefix': 1848249812}]}

>> get_transaction_in_block_info ['5859d4c669f400fc2bb91b0a381480e522483d5e4a79c1c78333662ef6eb9e22']
{'jsonrpc': '2.0', 'id': 1, 'result': {'id': '3.1.31', 'trx_hash': '5859d4c669f400fc2bb91b0a381480e522483d5e4a79c1c78333662ef6eb9e22', 'trx_in_block': 0, 'block_num': 1531}}

>> get_transaction_in_block_info 5859d4c669f400fc2bb91b0a381480e522483d5e4a79c1c78333662ef6eb9e22
 {'id': '3.1.31', 'trx_hash': '5859d4c669f400fc2bb91b0a381480e522483d5e4a79c1c78333662ef6eb9e22', 'trx_in_block': 0, 'block_num': 1531}

>> get_block [1531]
{'jsonrpc': '2.0', 'id': 1, 'result': {'witness_signature': '202c4366ea965ee88267aa992864e03010772002f2f13671af33d003d00091e78453a91ad34a422b8093f3234f18da3fba53575ef701ad4dcc3e0496d9614251d1', 'witness': '1.6.3', 'transactions': [['5859d4c669f400fc2bb91b0a381480e522483d5e4a79c1c78333662ef6eb9e22', {'signatures': ['202755f280fc53956d0270710a4d2a13127e901d4cf79754043544c2f0f4bb4baa418c116badf09b9df5a1b680f50de1600be4f1bc6d363328b38f69d690656a0a', '1f4aafa547d4f634435b51da69f4bca3a5eac0998ee44503d716a9cef9cc57746956fd1235adfd8f30fe28fa3f43f2715a440e4472748eda44304cd29331a677ed'], 'ref_block_num': 1522, 'operations': [[0, {'amount': {'amount': 2300000, 'asset_id': '1.3.0'}, 'extensions': [], 'to': '1.2.5', 'from': '1.2.16'}], [35, {'value_list': [], 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.1'}], [35, {'value_list': [], 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.1'}], [0, {'amount': {'amount': 7800000, 'asset_id': '1.3.0'}, 'extensions': [], 'to': '1.2.6', 'from': '1.2.16'}]], 'operation_results': [[1, {'real_running_time': 33, 'fees': [{'amount': 2000000, 'asset_id': '1.3.1'}]}], [4, {'existed_pv': False, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 2247757, 'asset_id': '1.3.0'}]}]], 'real_running_time': 196, 'contract_id': '1.16.1', 'relevant_datasize': 35, 'process_value': '', 'fees': [{'amount': 2247757, 'asset_id': '1.3.0'}]}], [4, {'existed_pv': False, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}], [5, {'message': '100%', 'affected_account': '1.2.6', 'fees': [{'amount': 2184757, 'asset_id': '1.3.0'}]}]], 'real_running_time': 133, 'contract_id': '1.16.1', 'relevant_datasize': 35, 'process_value': '', 'fees': [{'amount': 2184757, 'asset_id': '1.3.0'}]}], [1, {'real_running_time': 21, 'fees': [{'amount': 2000000, 'asset_id': '1.3.1'}]}]], 'expiration': '2020-07-07T08:15:58', 'extensions': [], 'ref_block_prefix': 1848249812}]], 'block_id': '000005fb66efa9b562578d04dfa33fbe44ea6c1a', 'previous': '000005faa2af2f1996705861217f5db994ce4a19', 'transaction_merkle_root': 'f9b50a0506c10ff5473c0e0d9364409f8b8ad9bc', 'timestamp': '2020-07-07T07:55:30'}}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['35cef78ea8cf4aeee22a0d72c046abd41d60799987671ca3f930e03ea4264d77', {'signatures': ['1f51acb2a353f685c3744b3c294fdab417ef4c77cbdd91f1d0c46eb60e43316bc21c9c90dd50facf24a010286e9adbbf9d74d54664dd705d288b4c71ca3cc912b4'], 'ref_block_num': 1522, 'operations': [[35, {'value_list': [], 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.1'}]], 'expiration': '2020-07-07T08:16:00', 'extensions': [], 'ref_block_prefix': 1848249812}]}

>> get_transaction_in_block_info ['35cef78ea8cf4aeee22a0d72c046abd41d60799987671ca3f930e03ea4264d77']
{'jsonrpc': '2.0', 'id': 1, 'result': {'id': '3.1.32', 'trx_hash': '35cef78ea8cf4aeee22a0d72c046abd41d60799987671ca3f930e03ea4264d77', 'trx_in_block': 0, 'block_num': 1532}}

>> get_transaction_in_block_info 35cef78ea8cf4aeee22a0d72c046abd41d60799987671ca3f930e03ea4264d77
 {'id': '3.1.32', 'trx_hash': '35cef78ea8cf4aeee22a0d72c046abd41d60799987671ca3f930e03ea4264d77', 'trx_in_block': 0, 'block_num': 1532}

>> get_block [1532]
{'jsonrpc': '2.0', 'id': 1, 'result': {'witness_signature': '1f26d198a5072c59f2825e0752350fa589a1d1604c34a9d016e64b2f2361b2322f1095b8f135570e9ec01b041eb45d30ab066d4aac3b2de806ae127d584eb1f28c', 'witness': '1.6.8', 'transactions': [['35cef78ea8cf4aeee22a0d72c046abd41d60799987671ca3f930e03ea4264d77', {'signatures': ['1f51acb2a353f685c3744b3c294fdab417ef4c77cbdd91f1d0c46eb60e43316bc21c9c90dd50facf24a010286e9adbbf9d74d54664dd705d288b4c71ca3cc912b4'], 'ref_block_num': 1522, 'operations': [[35, {'value_list': [], 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.16', 'contract_id': '1.16.1'}]], 'operation_results': [[4, {'existed_pv': False, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'message': '100%', 'affected_account': '1.2.16', 'fees': [{'amount': 2260757, 'asset_id': '1.3.0'}]}]], 'real_running_time': 209, 'contract_id': '1.16.1', 'relevant_datasize': 35, 'process_value': '', 'fees': [{'amount': 2260757, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-07T08:16:00', 'extensions': [], 'ref_block_prefix': 1848249812}]], 'block_id': '000005fc3cee8cd6df4ed42f3d77f2722e955481', 'previous': '000005fb66efa9b562578d04dfa33fbe44ea6c1a', 'transaction_merkle_root': '411bbd14f9406867215b868be34e0168bb521d1f', 'timestamp': '2020-07-07T07:55:32'}}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['d6fc90d8063826e5a16f0b4864e009f8dc74a0a89a2970c8bbf848022139ca8d', {'signatures': ['202cf583c29b724ad9dd2ec7205e179984652f92b0a595b4715714a9a86aea1451368be9774d8ccd7767d179c257f9ac77d7f1e53429c37b1c291c00e58764da09'], 'ref_block_num': 1524, 'operations': [[35, {'value_list': [], 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.1'}]], 'expiration': '2020-07-07T08:16:02', 'extensions': [], 'ref_block_prefix': 2136419760}]}

>> get_transaction_in_block_info ['d6fc90d8063826e5a16f0b4864e009f8dc74a0a89a2970c8bbf848022139ca8d']
{'jsonrpc': '2.0', 'id': 1, 'result': {'id': '3.1.33', 'trx_hash': 'd6fc90d8063826e5a16f0b4864e009f8dc74a0a89a2970c8bbf848022139ca8d', 'trx_in_block': 0, 'block_num': 1533}}

>> get_transaction_in_block_info d6fc90d8063826e5a16f0b4864e009f8dc74a0a89a2970c8bbf848022139ca8d
 {'id': '3.1.33', 'trx_hash': 'd6fc90d8063826e5a16f0b4864e009f8dc74a0a89a2970c8bbf848022139ca8d', 'trx_in_block': 0, 'block_num': 1533}

>> get_block [1533]
{'jsonrpc': '2.0', 'id': 1, 'result': {'witness_signature': '1f33992f4d68e10fc8c88c14c8634285325fa4a6ec5cca1a1fdb3da3e343a846d174e3c3721b64425953849dbfb1218aba53105431c9b42c42afbd8d9fa8f50c1d', 'witness': '1.6.7', 'transactions': [['d6fc90d8063826e5a16f0b4864e009f8dc74a0a89a2970c8bbf848022139ca8d', {'signatures': ['202cf583c29b724ad9dd2ec7205e179984652f92b0a595b4715714a9a86aea1451368be9774d8ccd7767d179c257f9ac77d7f1e53429c37b1c291c00e58764da09'], 'ref_block_num': 1524, 'operations': [[35, {'value_list': [], 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.6', 'contract_id': '1.16.1'}]], 'operation_results': [[4, {'existed_pv': False, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}], [5, {'message': '100%', 'affected_account': '1.2.6', 'fees': [{'amount': 2316757, 'asset_id': '1.3.0'}]}]], 'real_running_time': 265, 'contract_id': '1.16.1', 'relevant_datasize': 35, 'process_value': '', 'fees': [{'amount': 2316757, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-07T08:16:02', 'extensions': [], 'ref_block_prefix': 2136419760}]], 'block_id': '000005fd8363d8e2b18de7a32160d25adff5598c', 'previous': '000005fc3cee8cd6df4ed42f3d77f2722e955481', 'transaction_merkle_root': 'b4b451665bdc0d8b5afe687da32910a1e8bcba0f', 'timestamp': '2020-07-07T07:55:34'}}
```

### 2.2 修改费用分摊比例    
修改为30%
``` json
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 builder_tx.py 
>> unlock ['123456']
{'result': None, 'id': 1, 'jsonrpc': '2.0'}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_set_percent', [[1, {'v': 30}]], True]
{'result': ['c33ac28e8d4cde8397bc37fddf8b93055b344468f32d5ce61f0956654bdb92b4', {'operations': [[35, {'value_list': [[1, {'v': '30.00000000000000000'}]], 'contract_id': '1.16.1', 'extensions': [], 'caller': '1.2.16', 'function_name': 'test_set_percent'}]], 'expiration': '2020-07-07T08:17:36', 'ref_block_num': 1566, 'extensions': [], 'ref_block_prefix': 1249293485, 'signatures': ['2058538fac98df67b90f718fedcd993222998fa7f2b65ec3ceac4e3be8f89c093e2e33851dda0f3abc03f59c894445ebe0106eb9bf0ee8b9c509470e53d4a111fa']}], 'id': 1, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info ['c33ac28e8d4cde8397bc37fddf8b93055b344468f32d5ce61f0956654bdb92b4']
{'result': {'trx_in_block': 0, 'id': '3.1.34', 'block_num': 1576, 'trx_hash': 'c33ac28e8d4cde8397bc37fddf8b93055b344468f32d5ce61f0956654bdb92b4'}, 'id': 1, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info c33ac28e8d4cde8397bc37fddf8b93055b344468f32d5ce61f0956654bdb92b4
 {'trx_in_block': 0, 'id': '3.1.34', 'block_num': 1576, 'trx_hash': 'c33ac28e8d4cde8397bc37fddf8b93055b344468f32d5ce61f0956654bdb92b4'}

>> get_block [1576]
{'result': {'block_id': '0000062896d51f18e29ecb815bb20424ad05ede1', 'previous': '00000627c6ec4d550b2809acae8ce41ed6cc7856', 'witness': '1.6.6', 'transaction_merkle_root': '13cecb989876d7379c6b8d0fba608c46521abf69', 'witness_signature': '1f574bb30cd3bc959f9eb9d4030b63b614cbb9fa4a4a13d817382dba0d683a244e56c5d25c34a26e2edf11e914f39d7376e43de51799a94b18036f9c8e3d6e4fa5', 'timestamp': '2020-07-07T07:57:08', 'transactions': [['c33ac28e8d4cde8397bc37fddf8b93055b344468f32d5ce61f0956654bdb92b4', {'operations': [[35, {'value_list': [[1, {'v': '30.00000000000000000'}]], 'contract_id': '1.16.1', 'extensions': [], 'caller': '1.2.16', 'function_name': 'test_set_percent'}]], 'expiration': '2020-07-07T08:17:36', 'ref_block_num': 1566, 'extensions': [], 'operation_results': [[4, {'real_running_time': 255, 'contract_id': '1.16.1', 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'set_invoke_share_percent'}], [5, {'affected_account': '1.2.16', 'message': '100%', 'fees': [{'asset_id': '1.3.0', 'amount': 2318475}]}]], 'process_value': '', 'existed_pv': False, 'fees': [{'asset_id': '1.3.0', 'amount': 2318475}], 'relevant_datasize': 37}], [1, {'real_running_time': 57, 'fees': [{'asset_id': '1.3.1', 'amount': 100000}]}]], 'ref_block_prefix': 1249293485, 'signatures': ['2058538fac98df67b90f718fedcd993222998fa7f2b65ec3ceac4e3be8f89c093e2e33851dda0f3abc03f59c894445ebe0106eb9bf0ee8b9c509470e53d4a111fa']}]]}, 'id': 1, 'jsonrpc': '2.0'}
```

 ** 执行成功后，查看合约数据 **    
 ``` json
locked >>> get_object 1.16.1
[{
    "id": "1.16.1",
    "creation_date": "2020-07-07T07:01:20",
    "owner": "1.2.16",
    "name": "contract.testapi.contractfeeshare",
    "user_invoke_share_percent": 30,
    "current_version": "1bb846d2ada923348799655e072ee91f6e892ae90f1f2779c1a330e7ddb6b00c",
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
    "lua_code_b_id": "2.2.1"
  }
]

 ```

### 2.3 修改后合约调用测试
``` json
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 builder_tx.py 
>> unlock ['123456']
{'id': 1, 'jsonrpc': '2.0', 'result': None}

>> begin_builder_transaction []
{'id': 1, 'jsonrpc': '2.0', 'result': 1}

>> transfer ['nicotest', 'init0', 23, 'COCOS', ['', False], False]
{'id': 1, 'jsonrpc': '2.0', 'result': ['e98e532c4f143cb981d3b0ed7487a4dffe0ede888983033b8ddcfd9108488fe5', {'extensions': [], 'expiration': '2020-07-07T08:21:28', 'signatures': ['1f57971c621f4cb0326df6c8c488de9a2748f9305dea1e1a5f7bc1608a1ff69db935cb5caaa090827daae2b679e6bd272c985fc4ddc37ae2973b5ca2e6b97246f4'], 'ref_block_num': 1673, 'operations': [[0, {'from': '1.2.16', 'extensions': [], 'to': '1.2.5', 'amount': {'amount': 2300000, 'asset_id': '1.3.0'}}]], 'ref_block_prefix': 2720007022}]}

>> add_operation_to_builder_transaction [1, [0, {'from': '1.2.16', 'extensions': [], 'to': '1.2.5', 'amount': {'amount': 2300000, 'asset_id': '1.3.0'}}]]
{'id': 1, 'jsonrpc': '2.0', 'result': None}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], False]
{'id': 1, 'jsonrpc': '2.0', 'result': ['ae9f3ebad328a01b9767855b4a265578606a681a25f5303fd709ea53e38d0ec8', {'extensions': [], 'expiration': '2020-07-07T08:21:28', 'signatures': ['1f0b172922daa10b8b5fa9a01c31de0bbc96be73fc76fede04068478d77331818660c132cae6f1502b20a6eef82f168aece3baa469d98c4ad8f14396110da6c59b'], 'ref_block_num': 1673, 'operations': [[35, {'value_list': [], 'contract_id': '1.16.1', 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.16'}]], 'ref_block_prefix': 2720007022}]}

>> add_operation_to_builder_transaction [1, [35, {'value_list': [], 'contract_id': '1.16.1', 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.16'}]]
{'id': 1, 'jsonrpc': '2.0', 'result': None}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], False]
{'id': 1, 'jsonrpc': '2.0', 'result': ['308a0f8632405a0ac20e4600db9a89ef1d7c64a2898e20d1bc53df66e8a75be1', {'extensions': [], 'expiration': '2020-07-07T08:21:28', 'signatures': ['200f636a9f13637bc7fbf782e31baeabfd057565faf93b97f75add788e7a79ac3574683efcb2664b0509ce94d04b8304e69a61af2df5fbe9eee14b162c1e8d5a83'], 'ref_block_num': 1673, 'operations': [[35, {'value_list': [], 'contract_id': '1.16.1', 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.6'}]], 'ref_block_prefix': 2720007022}]}

>> add_operation_to_builder_transaction [1, [35, {'value_list': [], 'contract_id': '1.16.1', 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.6'}]]
{'id': 1, 'jsonrpc': '2.0', 'result': None}

>> transfer ['nicotest', 'init1', 78, 'COCOS', ['', False], False]
{'id': 1, 'jsonrpc': '2.0', 'result': ['cc600ce7f36a3ee0e60c18b3ec6e9d68322b81f403695be220b960a97e48f2b6', {'extensions': [], 'expiration': '2020-07-07T08:21:28', 'signatures': ['20033c7e0f1d61db73e7d97f2efa54db42b93f897d42682833cd2d0cc17c0260d655d4751a9edd300403aaf93fd22bd1baa10e16ce5f5ba9e23406f61e4620ce2d'], 'ref_block_num': 1673, 'operations': [[0, {'from': '1.2.16', 'extensions': [], 'to': '1.2.6', 'amount': {'amount': 7800000, 'asset_id': '1.3.0'}}]], 'ref_block_prefix': 2720007022}]}

>> add_operation_to_builder_transaction [1, [0, {'from': '1.2.16', 'extensions': [], 'to': '1.2.6', 'amount': {'amount': 7800000, 'asset_id': '1.3.0'}}]]
{'id': 1, 'jsonrpc': '2.0', 'result': None}

>> preview_builder_transaction [1]
{'id': 1, 'jsonrpc': '2.0', 'result': {'ref_block_num': 0, 'operations': [[0, {'from': '1.2.16', 'extensions': [], 'to': '1.2.5', 'amount': {'amount': 2300000, 'asset_id': '1.3.0'}}], [35, {'value_list': [], 'contract_id': '1.16.1', 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.16'}], [35, {'value_list': [], 'contract_id': '1.16.1', 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.6'}], [0, {'from': '1.2.16', 'extensions': [], 'to': '1.2.6', 'amount': {'amount': 7800000, 'asset_id': '1.3.0'}}]], 'extensions': [], 'expiration': '1970-01-01T00:00:00', 'ref_block_prefix': 0}}

>> sign_builder_transaction [1, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['88b34b0da65deeb517be77f40a9a5498a7f251a2f1b8ded72c77c25650f12d47', {'extensions': [], 'expiration': '2020-07-07T08:21:28', 'signatures': ['2023f4ceb86f2dea40daf126a8f9ee75877e6dba96180d1b1710771a63d30d9b606e7a07a79c8a11babcb748d005b3c9ea693db13dfcc01fd292660b4e80740917', '1f384f128144c0c8fc548a5cf128d9649ca3da4e31561f4071239a9388aabc90000c5b5f481c6e2cba5574abdd47bfd58928f3b30c4b141e163cc29a0fcfd6cd3d'], 'ref_block_num': 1673, 'operations': [[0, {'from': '1.2.16', 'extensions': [], 'to': '1.2.5', 'amount': {'amount': 2300000, 'asset_id': '1.3.0'}}], [35, {'value_list': [], 'contract_id': '1.16.1', 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.16'}], [35, {'value_list': [], 'contract_id': '1.16.1', 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.6'}], [0, {'from': '1.2.16', 'extensions': [], 'to': '1.2.6', 'amount': {'amount': 7800000, 'asset_id': '1.3.0'}}]], 'ref_block_prefix': 2720007022}]}

>> get_transaction_in_block_info ['88b34b0da65deeb517be77f40a9a5498a7f251a2f1b8ded72c77c25650f12d47']
{'id': 1, 'jsonrpc': '2.0', 'result': {'id': '3.1.35', 'block_num': 1682, 'trx_in_block': 0, 'trx_hash': '88b34b0da65deeb517be77f40a9a5498a7f251a2f1b8ded72c77c25650f12d47'}}

>> get_transaction_in_block_info 88b34b0da65deeb517be77f40a9a5498a7f251a2f1b8ded72c77c25650f12d47
 {'id': '3.1.35', 'block_num': 1682, 'trx_in_block': 0, 'trx_hash': '88b34b0da65deeb517be77f40a9a5498a7f251a2f1b8ded72c77c25650f12d47'}

>> get_block [1682]
{'id': 1, 'jsonrpc': '2.0', 'result': {'witness': '1.6.1', 'timestamp': '2020-07-07T08:01:00', 'witness_signature': '207421494bb30e69d5502c588e8976d1c6352022a8de6560e98446f882a01e658d50024c06ac5f03eaf8e4138f5dbfbce8f2dd618959a1d2afd458a150a359b3d2', 'transaction_merkle_root': '0dfd92c1757136e161598c0c953e8186101e77bf', 'previous': '0000069158bb099789c7cb22feb985a56bf0bb79', 'block_id': '000006929272a8b18c9cb8b7875db5aa8019881a', 'transactions': [['88b34b0da65deeb517be77f40a9a5498a7f251a2f1b8ded72c77c25650f12d47', {'operation_results': [[1, {'fees': [{'amount': 2000000, 'asset_id': '1.3.1'}], 'real_running_time': 521}], [4, {'contract_id': '1.16.1', 'real_running_time': 237, 'existed_pv': False, 'process_value': '', 'fees': [{'amount': 2288757, 'asset_id': '1.3.0'}], 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'message': '100%', 'fees': [{'amount': 2288757, 'asset_id': '1.3.0'}], 'affected_account': '1.2.16'}]], 'relevant_datasize': 35}], [4, {'contract_id': '1.16.1', 'real_running_time': 139, 'existed_pv': False, 'process_value': '', 'fees': [{'amount': 2190757, 'asset_id': '1.3.0'}], 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}], [5, {'message': '30%', 'fees': [{'amount': 657228, 'asset_id': '1.3.0'}], 'affected_account': '1.2.6'}], [5, {'message': '70%', 'fees': [{'amount': 1533529, 'asset_id': '1.3.0'}], 'affected_account': '1.2.16'}]], 'relevant_datasize': 35}], [1, {'fees': [{'amount': 2000000, 'asset_id': '1.3.1'}], 'real_running_time': 24}]], 'extensions': [], 'expiration': '2020-07-07T08:21:28', 'signatures': ['2023f4ceb86f2dea40daf126a8f9ee75877e6dba96180d1b1710771a63d30d9b606e7a07a79c8a11babcb748d005b3c9ea693db13dfcc01fd292660b4e80740917', '1f384f128144c0c8fc548a5cf128d9649ca3da4e31561f4071239a9388aabc90000c5b5f481c6e2cba5574abdd47bfd58928f3b30c4b141e163cc29a0fcfd6cd3d'], 'ref_block_num': 1673, 'operations': [[0, {'from': '1.2.16', 'extensions': [], 'to': '1.2.5', 'amount': {'amount': 2300000, 'asset_id': '1.3.0'}}], [35, {'value_list': [], 'contract_id': '1.16.1', 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.16'}], [35, {'value_list': [], 'contract_id': '1.16.1', 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.6'}], [0, {'from': '1.2.16', 'extensions': [], 'to': '1.2.6', 'amount': {'amount': 7800000, 'asset_id': '1.3.0'}}]], 'ref_block_prefix': 2720007022}]]}}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['a3ada5ac1540d00a81d92a524ea59a9a69d5f89c00ab147613a22fbb1f11c5ab', {'extensions': [], 'expiration': '2020-07-07T08:21:30', 'signatures': ['1f2d55e882e5d514ccdfdf7e9bb7e467ad412cce5faf7a6fe798d93dd736d9dcc73eedc772fb255b0d51bfd3ca0196b4f01fcae49a8418689e902f35bd4ea2270a'], 'ref_block_num': 1674, 'operations': [[35, {'value_list': [], 'contract_id': '1.16.1', 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.16'}]], 'ref_block_prefix': 3300345972}]}

>> get_transaction_in_block_info ['a3ada5ac1540d00a81d92a524ea59a9a69d5f89c00ab147613a22fbb1f11c5ab']
{'id': 1, 'jsonrpc': '2.0', 'result': {'id': '3.1.36', 'block_num': 1683, 'trx_in_block': 0, 'trx_hash': 'a3ada5ac1540d00a81d92a524ea59a9a69d5f89c00ab147613a22fbb1f11c5ab'}}

>> get_transaction_in_block_info a3ada5ac1540d00a81d92a524ea59a9a69d5f89c00ab147613a22fbb1f11c5ab
 {'id': '3.1.36', 'block_num': 1683, 'trx_in_block': 0, 'trx_hash': 'a3ada5ac1540d00a81d92a524ea59a9a69d5f89c00ab147613a22fbb1f11c5ab'}

>> get_block [1683]
{'id': 1, 'jsonrpc': '2.0', 'result': {'witness': '1.6.10', 'timestamp': '2020-07-07T08:01:02', 'witness_signature': '1f29e15dfa70b7940767a7e2ce6f39ccf1986fa8042b76fc1c96f9a0136e6676ee4ad6d825f1de703c2c35c3a4f02b12fa0215472eeb04987f26e1180b365d82f6', 'transaction_merkle_root': '21a0f6397271dc1e70d090833882920fa78aed22', 'previous': '000006929272a8b18c9cb8b7875db5aa8019881a', 'block_id': '00000693817be9477cae585d9ee8309852ff1c20', 'transactions': [['a3ada5ac1540d00a81d92a524ea59a9a69d5f89c00ab147613a22fbb1f11c5ab', {'operation_results': [[4, {'contract_id': '1.16.1', 'real_running_time': 261, 'existed_pv': False, 'process_value': '', 'fees': [{'amount': 2312757, 'asset_id': '1.3.0'}], 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'message': '100%', 'fees': [{'amount': 2312757, 'asset_id': '1.3.0'}], 'affected_account': '1.2.16'}]], 'relevant_datasize': 35}]], 'extensions': [], 'expiration': '2020-07-07T08:21:30', 'signatures': ['1f2d55e882e5d514ccdfdf7e9bb7e467ad412cce5faf7a6fe798d93dd736d9dcc73eedc772fb255b0d51bfd3ca0196b4f01fcae49a8418689e902f35bd4ea2270a'], 'ref_block_num': 1674, 'operations': [[35, {'value_list': [], 'contract_id': '1.16.1', 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.16'}]], 'ref_block_prefix': 3300345972}]]}}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['8a83ae8cfd089fc91eeb1d6618d477e48e132f0f8a4222b2eaf972a6307f34c8', {'extensions': [], 'expiration': '2020-07-07T08:21:32', 'signatures': ['1f566642057746a233f03d083545e3527e3e44e2180362225ee2ebd677a4804d374d041df3ae7c533aaf7426ed1015541a85f6de0e725571b4f3c7ea6830a53d14'], 'ref_block_num': 1675, 'operations': [[35, {'value_list': [], 'contract_id': '1.16.1', 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.6'}]], 'ref_block_prefix': 2719754898}]}

>> get_transaction_in_block_info ['8a83ae8cfd089fc91eeb1d6618d477e48e132f0f8a4222b2eaf972a6307f34c8']
{'id': 1, 'jsonrpc': '2.0', 'result': {'id': '3.1.37', 'block_num': 1684, 'trx_in_block': 0, 'trx_hash': '8a83ae8cfd089fc91eeb1d6618d477e48e132f0f8a4222b2eaf972a6307f34c8'}}

>> get_transaction_in_block_info 8a83ae8cfd089fc91eeb1d6618d477e48e132f0f8a4222b2eaf972a6307f34c8
 {'id': '3.1.37', 'block_num': 1684, 'trx_in_block': 0, 'trx_hash': '8a83ae8cfd089fc91eeb1d6618d477e48e132f0f8a4222b2eaf972a6307f34c8'}

>> get_block [1684]
{'id': 1, 'jsonrpc': '2.0', 'result': {'witness': '1.6.6', 'timestamp': '2020-07-07T08:01:04', 'witness_signature': '1f37e2f2593bd7009850add70dd76906909d7240456d703902b90d79e2b6a921e828b4675d39ff3ca63c2e971602cdfa35e60a83d68af4ea12c34a6eb67b70de27', 'transaction_merkle_root': '0d42451e45cad0db636af83a2e616d13406c8c26', 'previous': '00000693817be9477cae585d9ee8309852ff1c20', 'block_id': '000006943d0f7f1af42e238e56572de8e785889f', 'transactions': [['8a83ae8cfd089fc91eeb1d6618d477e48e132f0f8a4222b2eaf972a6307f34c8', {'operation_results': [[4, {'contract_id': '1.16.1', 'real_running_time': 216, 'existed_pv': False, 'process_value': '', 'fees': [{'amount': 2267757, 'asset_id': '1.3.0'}], 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}], [5, {'message': '30%', 'fees': [{'amount': 680328, 'asset_id': '1.3.0'}], 'affected_account': '1.2.6'}], [5, {'message': '70%', 'fees': [{'amount': 1587429, 'asset_id': '1.3.0'}], 'affected_account': '1.2.16'}]], 'relevant_datasize': 35}]], 'extensions': [], 'expiration': '2020-07-07T08:21:32', 'signatures': ['1f566642057746a233f03d083545e3527e3e44e2180362225ee2ebd677a4804d374d041df3ae7c533aaf7426ed1015541a85f6de0e725571b4f3c7ea6830a53d14'], 'ref_block_num': 1675, 'operations': [[35, {'value_list': [], 'contract_id': '1.16.1', 'extensions': [], 'function_name': 'test_helloworld', 'caller': '1.2.6'}]], 'ref_block_prefix': 2719754898}]]}}

ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ 
```