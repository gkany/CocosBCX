
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/contract_fee_share$ python3 builder_tx.py 
>> unlock ['123456']
{'result': None, 'id': 1, 'jsonrpc': '2.0'}

>> begin_builder_transaction []
{'result': 1, 'id': 1, 'jsonrpc': '2.0'}

>> transfer ['nicotest', 'init0', 23, 'COCOS', ['', False], False]
{'result': ['08e2a450b9ac52d12e6e55806dd9549984bf56f1e4870c86bd8d5df802f4c85c', {'expiration': '2020-07-09T10:57:04', 'signatures': ['1f04a99b78a06db5b4e6d084572066c30d1a9deba92b3236f1dc3add123ad8090b30bef19ca171cbb1ff98d4ddb81a4c43254b6cb39540bf392e1a20132e5ec3a9'], 'extensions': [], 'ref_block_num': 35815, 'operations': [[0, {'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}, 'to': '1.2.5'}]], 'ref_block_prefix': 2817312832}], 'id': 1, 'jsonrpc': '2.0'}

>> add_operation_to_builder_transaction [1, [0, {'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}, 'to': '1.2.5'}]]
{'result': None, 'id': 1, 'jsonrpc': '2.0'}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], False]
{'result': ['56964004bb5d904167c6820a808768f86a51c5b7481c29e2183ba3b9f761f129', {'expiration': '2020-07-09T10:57:04', 'signatures': ['1f2e6026934a35d6af4ced7c3d24165176300524fd15b14a2ae9c572013dcf24dc57016dd9906bbbaecbfe1fadb9d0afc5a35c934726192e846d3f8e27305a8abb'], 'extensions': [], 'ref_block_num': 35815, 'operations': [[35, {'function_name': 'test_helloworld', 'value_list': [], 'extensions': [], 'caller': '1.2.16', 'contract_id': '1.16.121'}]], 'ref_block_prefix': 2817312832}], 'id': 1, 'jsonrpc': '2.0'}

>> add_operation_to_builder_transaction [1, [35, {'function_name': 'test_helloworld', 'value_list': [], 'extensions': [], 'caller': '1.2.16', 'contract_id': '1.16.121'}]]
{'result': None, 'id': 1, 'jsonrpc': '2.0'}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], False]
{'result': ['c38c79fde07c35c134a34aadea9196e68684eb29b5591ae39c9fa5be77396fab', {'expiration': '2020-07-09T10:57:04', 'signatures': ['20405fe3f0cba35f88e400b8bf060ad16d507817743a5241e4894cd9e4dc4f256763d822cfa1164b87ade10cbedfe1c2b726f34ff5b3b75c37d0139d3766973928'], 'extensions': [], 'ref_block_num': 35815, 'operations': [[35, {'function_name': 'test_helloworld', 'value_list': [], 'extensions': [], 'caller': '1.2.6', 'contract_id': '1.16.121'}]], 'ref_block_prefix': 2817312832}], 'id': 1, 'jsonrpc': '2.0'}

>> add_operation_to_builder_transaction [1, [35, {'function_name': 'test_helloworld', 'value_list': [], 'extensions': [], 'caller': '1.2.6', 'contract_id': '1.16.121'}]]
{'result': None, 'id': 1, 'jsonrpc': '2.0'}

>> transfer ['nicotest', 'init1', 78, 'COCOS', ['', False], False]
{'result': ['8fe6cb75cd77614cb9e7255e8dab54ca79bbeb08a53e656325f5b83abaceb514', {'expiration': '2020-07-09T10:57:04', 'signatures': ['1f67ff6e1973e1ff3b0b79d4f8633d84d2c512c314469be615ff82da602072cf2a7a205f1044154fb6d3ea7edf95ae14dfbd838c8eab88bfcef595c51f59678937'], 'extensions': [], 'ref_block_num': 35815, 'operations': [[0, {'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}, 'to': '1.2.6'}]], 'ref_block_prefix': 2817312832}], 'id': 1, 'jsonrpc': '2.0'}

>> add_operation_to_builder_transaction [1, [0, {'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}, 'to': '1.2.6'}]]
{'result': None, 'id': 1, 'jsonrpc': '2.0'}

>> preview_builder_transaction [1]
{'result': {'operations': [[0, {'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}, 'to': '1.2.5'}], [35, {'function_name': 'test_helloworld', 'value_list': [], 'extensions': [], 'caller': '1.2.16', 'contract_id': '1.16.121'}], [35, {'function_name': 'test_helloworld', 'value_list': [], 'extensions': [], 'caller': '1.2.6', 'contract_id': '1.16.121'}], [0, {'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}, 'to': '1.2.6'}]], 'ref_block_num': 0, 'extensions': [], 'expiration': '1970-01-01T00:00:00', 'ref_block_prefix': 0}, 'id': 1, 'jsonrpc': '2.0'}

>> sign_builder_transaction [1, True]
{'result': ['dee7ce75adcefb4716a7c7f15020d137f814679d034d29543d91be3bd463d69f', {'expiration': '2020-07-09T10:57:04', 'signatures': ['2017cea4c0c5e44c49dd8da348196129c4d7a5589fc9a823657dc3e821af31f1ed70b8bab12e4114f7e1a695538be3e06298060570ae74e471df0b444af426766e', '1f4e1d9b8551c038fb678761b512481ca6cc5a23d24bd7a125a4f93cf42271b6ed1940af24cabefce22763e0c92b096cb4db7136fba2d20034d11741813fbc284b'], 'extensions': [], 'ref_block_num': 35815, 'operations': [[0, {'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}, 'to': '1.2.5'}], [35, {'function_name': 'test_helloworld', 'value_list': [], 'extensions': [], 'caller': '1.2.16', 'contract_id': '1.16.121'}], [35, {'function_name': 'test_helloworld', 'value_list': [], 'extensions': [], 'caller': '1.2.6', 'contract_id': '1.16.121'}], [0, {'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}, 'to': '1.2.6'}]], 'ref_block_prefix': 2817312832}], 'id': 1, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info ['dee7ce75adcefb4716a7c7f15020d137f814679d034d29543d91be3bd463d69f']
{'result': {'trx_in_block': 0, 'trx_hash': 'dee7ce75adcefb4716a7c7f15020d137f814679d034d29543d91be3bd463d69f', 'id': '3.1.824848', 'block_num': 7441392}, 'id': 1, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info dee7ce75adcefb4716a7c7f15020d137f814679d034d29543d91be3bd463d69f
 {'trx_in_block': 0, 'trx_hash': 'dee7ce75adcefb4716a7c7f15020d137f814679d034d29543d91be3bd463d69f', 'id': '3.1.824848', 'block_num': 7441392}

>> get_block [7441392]
{'result': {'witness': '1.6.3', 'witness_signature': '2006540ad3b361ec9e58bc64b9e4b9e814d46200b250f42371060718884662afc2081cff089770bc6a779593df57612a0e384504f9b70803ceae8835a59e078290', 'transactions': [['dee7ce75adcefb4716a7c7f15020d137f814679d034d29543d91be3bd463d69f', {'expiration': '2020-07-09T10:57:04', 'signatures': ['2017cea4c0c5e44c49dd8da348196129c4d7a5589fc9a823657dc3e821af31f1ed70b8bab12e4114f7e1a695538be3e06298060570ae74e471df0b444af426766e', '1f4e1d9b8551c038fb678761b512481ca6cc5a23d24bd7a125a4f93cf42271b6ed1940af24cabefce22763e0c92b096cb4db7136fba2d20034d11741813fbc284b'], 'operation_results': [[1, {'fees': [{'asset_id': '1.3.1', 'amount': 10000}], 'real_running_time': 43}], [4, {'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}]], 'relevant_datasize': 35, 'existed_pv': False, 'fees': [{'asset_id': '1.3.1', 'amount': 20711}], 'real_running_time': 195, 'process_value': '', 'contract_id': '1.16.121'}], [4, {'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}]], 'relevant_datasize': 35, 'existed_pv': False, 'fees': [{'asset_id': '1.3.0', 'amount': 20897}], 'real_running_time': 381, 'process_value': '', 'contract_id': '1.16.121'}], [1, {'fees': [{'asset_id': '1.3.1', 'amount': 10000}], 'real_running_time': 24}]], 'extensions': [], 'ref_block_num': 35815, 'operations': [[0, {'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 2300000}, 'to': '1.2.5'}], [35, {'function_name': 'test_helloworld', 'value_list': [], 'extensions': [], 'caller': '1.2.16', 'contract_id': '1.16.121'}], [35, {'function_name': 'test_helloworld', 'value_list': [], 'extensions': [], 'caller': '1.2.6', 'contract_id': '1.16.121'}], [0, {'extensions': [], 'from': '1.2.16', 'amount': {'asset_id': '1.3.0', 'amount': 7800000}, 'to': '1.2.6'}]], 'ref_block_prefix': 2817312832}]], 'timestamp': '2020-07-09T10:36:36', 'previous': '00718bef8bd969570bff3082ca4652e7155b06ed', 'block_id': '00718bf0a2244e7a0c03d9554c3f0513d64cc540', 'transaction_merkle_root': '1bd8b970f44939a594a462fddf4d8079e6b72e95'}, 'id': 1, 'jsonrpc': '2.0'}

>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['4e1221e23b0be1b4f47f4fda49ea65d8e2ac8b157b8936da8b095c1413f9a885', {'expiration': '2020-07-09T10:57:06', 'signatures': ['205aff1c4056972c02c819cda37f9f7f60e16c54599540d348bb8199e8573ed0fd5f750c224f8553dab7871cc95edca3168ef67a38f13573bb0ea89905598c39fb'], 'extensions': [], 'ref_block_num': 35815, 'operations': [[35, {'function_name': 'test_helloworld', 'value_list': [], 'extensions': [], 'caller': '1.2.16', 'contract_id': '1.16.121'}]], 'ref_block_prefix': 2817312832}], 'id': 1, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info ['4e1221e23b0be1b4f47f4fda49ea65d8e2ac8b157b8936da8b095c1413f9a885']
{'result': {'trx_in_block': 0, 'trx_hash': '4e1221e23b0be1b4f47f4fda49ea65d8e2ac8b157b8936da8b095c1413f9a885', 'id': '3.1.824849', 'block_num': 7441393}, 'id': 1, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info 4e1221e23b0be1b4f47f4fda49ea65d8e2ac8b157b8936da8b095c1413f9a885
 {'trx_in_block': 0, 'trx_hash': '4e1221e23b0be1b4f47f4fda49ea65d8e2ac8b157b8936da8b095c1413f9a885', 'id': '3.1.824849', 'block_num': 7441393}

>> get_block [7441393]
{'result': {'witness': '1.6.6', 'witness_signature': '1f7941b5504c8875b7e4e275680de8ba91b5fac3bd5627fc49b56d6e7f4a01dcdd7f7de4ca592f78c7630ade47400513ad4de78be4d677b56cc1f2ae109e5f9a28', 'transactions': [['4e1221e23b0be1b4f47f4fda49ea65d8e2ac8b157b8936da8b095c1413f9a885', {'expiration': '2020-07-09T10:57:06', 'signatures': ['205aff1c4056972c02c819cda37f9f7f60e16c54599540d348bb8199e8573ed0fd5f750c224f8553dab7871cc95edca3168ef67a38f13573bb0ea89905598c39fb'], 'operation_results': [[4, {'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}]], 'relevant_datasize': 35, 'existed_pv': False, 'fees': [{'asset_id': '1.3.1', 'amount': 20857}], 'real_running_time': 341, 'process_value': '', 'contract_id': '1.16.121'}]], 'extensions': [], 'ref_block_num': 35815, 'operations': [[35, {'function_name': 'test_helloworld', 'value_list': [], 'extensions': [], 'caller': '1.2.16', 'contract_id': '1.16.121'}]], 'ref_block_prefix': 2817312832}]], 'timestamp': '2020-07-09T10:36:38', 'previous': '00718bf0a2244e7a0c03d9554c3f0513d64cc540', 'block_id': '00718bf1654790b64766a9aa727a19181295c7fe', 'transaction_merkle_root': '2a8e8ef2d12d7228f391e680cf49438925534ab5'}, 'id': 1, 'jsonrpc': '2.0'}

>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['46b3257f1319e56b497e8cda94588399e6a437678121d2b2d6c76c7348038712', {'expiration': '2020-07-09T10:57:08', 'signatures': ['2060228cb874878664bf02dbfe56b6dd24459c2e7a7ee297600610ffec7f0cc7d768939df1438d5cbb67b87c1f50e76c76291e2e067a65f0825e2369cee68f2f7d'], 'extensions': [], 'ref_block_num': 35815, 'operations': [[35, {'function_name': 'test_helloworld', 'value_list': [], 'extensions': [], 'caller': '1.2.6', 'contract_id': '1.16.121'}]], 'ref_block_prefix': 2817312832}], 'id': 1, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info ['46b3257f1319e56b497e8cda94588399e6a437678121d2b2d6c76c7348038712']
{'result': {'trx_in_block': 0, 'trx_hash': '46b3257f1319e56b497e8cda94588399e6a437678121d2b2d6c76c7348038712', 'id': '3.1.824850', 'block_num': 7441394}, 'id': 1, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info 46b3257f1319e56b497e8cda94588399e6a437678121d2b2d6c76c7348038712
 {'trx_in_block': 0, 'trx_hash': '46b3257f1319e56b497e8cda94588399e6a437678121d2b2d6c76c7348038712', 'id': '3.1.824850', 'block_num': 7441394}

>> get_block [7441394]
{'result': {'witness': '1.6.8', 'witness_signature': '2063a123e1162f839b541deb3d974f403fe087bd2fd91c135a2de6a40623d95c3b35603e1dcc313018b7f9b353fe15c56bf6914f93ed801d4284a3d790a4cc6fe4', 'transactions': [['46b3257f1319e56b497e8cda94588399e6a437678121d2b2d6c76c7348038712', {'expiration': '2020-07-09T10:57:08', 'signatures': ['2060228cb874878664bf02dbfe56b6dd24459c2e7a7ee297600610ffec7f0cc7d768939df1438d5cbb67b87c1f50e76c76291e2e067a65f0825e2369cee68f2f7d'], 'operation_results': [[4, {'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.6'}]], 'relevant_datasize': 35, 'existed_pv': False, 'fees': [{'asset_id': '1.3.0', 'amount': 20740}], 'real_running_time': 224, 'process_value': '', 'contract_id': '1.16.121'}]], 'extensions': [], 'ref_block_num': 35815, 'operations': [[35, {'function_name': 'test_helloworld', 'value_list': [], 'extensions': [], 'caller': '1.2.6', 'contract_id': '1.16.121'}]], 'ref_block_prefix': 2817312832}]], 'timestamp': '2020-07-09T10:36:40', 'previous': '00718bf1654790b64766a9aa727a19181295c7fe', 'block_id': '00718bf2f3f4f9006061907f00a268360ec51338', 'transaction_merkle_root': '53a2bc0b2feda215889f164f9f6b9881675644cf'}, 'id': 1, 'jsonrpc': '2.0'}
```