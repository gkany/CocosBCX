
# 1. 功能测试：(不包括提案修改最大投票数)    
**测试过程和结果：**  
``` text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/release1.1.5$ python3 release.py 
>> unlock ['123456']

{'id': 1, 'jsonrpc': '2.0', 'result': None}


# cli_wallet api test
contract_name: contract.release115rxz, test account: nicotest
1. create contract from file and call test
>> get_contract ['contract.release115rxz']

{'id': 1, 'jsonrpc': '2.0', 'error': {'message': 'unspecified: Assert Exception: contract_itr != con_index.end(): The contract (contract.release115rxz) does not exist', 'code': 1}}


>> create_contract_from_file ['nicotest', 'contract.release115rxz', 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz', '/home/ck/xukang/CocosBCX/feature_test/release1.1.5/contract_create.lua', 'true']

{'id': 1, 'jsonrpc': '2.0', 'result': ['bf6b63d129c149dce816cda6adfe6e045289d4d7dc7a01b39cbd05f04c972838', {'expiration': '2020-07-23T05:55:02', 'ref_block_num': 1312, 'ref_block_prefix': 2490275048, 'operations': [[34, {'name': 'contract.release115rxz', 'owner': '1.2.16', 'extensions': [], 'contract_authority': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz', 'data': 'function contract_test() \tchainhelper:log("Hi, create contract from file")  end'}]], 'extensions': [], 'signatures': ['1f2a1c703caad81a6d5ceea16cd68a4409cbb123a08f1086588516d18ddde42291184b8e49c96a4973e57de8436b9d9492914733755bfd55d13227715c055b61af']}]}


>> call_contract_function ['nicotest', 'contract.release115rxz', 'contract_test', [], 'true']

{'id': 1, 'jsonrpc': '2.0', 'result': ['174af78634c525ebaa01c47344b55be422e79d0db132735842e7ea88c1707f50', {'expiration': '2020-07-23T05:55:06', 'ref_block_num': 1313, 'ref_block_prefix': 676961893, 'operations': [[35, {'extensions': [], 'contract_id': '1.16.7', 'function_name': 'contract_test', 'value_list': [], 'caller': '1.2.16'}]], 'extensions': [], 'signatures': ['1f08895b799e4cc41b1a6a70b36a4019c4889d81511c1e1b946b399c7228e5c3b73cb1691659dc64e1d2980115737760e99a1fec6d7a5fc9743a7e903b26ae0ac9']}]}


>> get_transaction_by_id ['174af78634c525ebaa01c47344b55be422e79d0db132735842e7ea88c1707f50']

{'id': 1, 'jsonrpc': '2.0', 'result': {'expiration': '2020-07-23T05:55:06', 'ref_block_num': 1313, 'ref_block_prefix': 676961893, 'operations': [[35, {'extensions': [], 'contract_id': '1.16.7', 'function_name': 'contract_test', 'value_list': [], 'caller': '1.2.16'}]], 'extensions': [], 'signatures': ['1f08895b799e4cc41b1a6a70b36a4019c4889d81511c1e1b946b399c7228e5c3b73cb1691659dc64e1d2980115737760e99a1fec6d7a5fc9743a7e903b26ae0ac9'], 'operation_results': [[4, {'contract_id': '1.16.7', 'relevant_datasize': 42, 'existed_pv': False, 'contract_affecteds': [[3, {'message': 'Hi, create contract from file', 'affected_account': '1.2.16'}]], 'fees': [{'asset_id': '1.3.0', 'amount': 2248640}], 'real_running_time': 192, 'process_value': ''}]]}}


tx_id: 174af78634c525ebaa01c47344b55be422e79d0db132735842e7ea88c1707f50, result: [[4, {'contract_id': '1.16.7', 'relevant_datasize': 42, 'existed_pv': False, 'contract_affecteds': [[3, {'message': 'Hi, create contract from file', 'affected_account': '1.2.16'}]], 'fees': [{'asset_id': '1.3.0', 'amount': 2248640}], 'real_running_time': 192, 'process_value': ''}]]
2. contract revise from file and call test
>> get_contract ['contract.release115rxz']

{'id': 1, 'jsonrpc': '2.0', 'result': {'name': 'contract.release115rxz', 'owner': '1.2.16', 'contract_authority': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz', 'current_version': 'bf6b63d129c149dce816cda6adfe6e045289d4d7dc7a01b39cbd05f04c972838', 'lua_code_b_id': '2.2.7', 'contract_data': [], 'user_invoke_share_percent': 100, 'id': '1.16.7', 'creation_date': '2020-07-23T05:34:32', 'check_contract_authority': False, 'is_release': False, 'contract_ABI': [[{'key': [2, {'v': 'contract_test'}]}, [5, {'arglist': [], 'is_var_arg': False}]]]}}


>> revise_contract_from_file ['nicotest', 'contract.release115rxz', '/home/ck/xukang/CocosBCX/feature_test/release1.1.5/contract_revise.lua', 'true']

{'id': 1, 'jsonrpc': '2.0', 'result': ['a0715b0d84b5a1821e5a76e5d3790ef4c67291e36ffc5a4ff7c91b423377085b', {'expiration': '2020-07-23T05:55:10', 'ref_block_num': 1315, 'ref_block_prefix': 986722887, 'operations': [[50, {'contract_id': '1.16.7', 'extensions': [], 'reviser': '1.2.16', 'data': 'function contract_test() \tchainhelper:log("Hi, revise contract from file")  end'}]], 'extensions': [], 'signatures': ['1f4b48246e31b4a0be002f764e003ede7bd930c99760198d6305da1a9889fa3caf05d5f3da028cf676f2eb6f17a1c6f6a96a3884b54c6b9b80285b0304f56415d5']}]}


>> call_contract_function ['nicotest', 'contract.release115rxz', 'contract_test', [], 'true']

{'id': 1, 'jsonrpc': '2.0', 'result': ['626d040d20804ee0a249e533935a753f953a0d982d7371a9847b6cd921c8d921', {'expiration': '2020-07-23T05:55:14', 'ref_block_num': 1319, 'ref_block_prefix': 1026938970, 'operations': [[35, {'extensions': [], 'contract_id': '1.16.7', 'function_name': 'contract_test', 'value_list': [], 'caller': '1.2.16'}]], 'extensions': [], 'signatures': ['1f46ed96bd48e31c473a72c358495ede9cb60e794eec7775b21537bbbdf07a11dd730ae853ff69e1a46403dd1a970fb49e18d7cc5bc6c8d0a35a58d7f8668c15f9']}]}


>> get_transaction_by_id ['626d040d20804ee0a249e533935a753f953a0d982d7371a9847b6cd921c8d921']

{'id': 1, 'jsonrpc': '2.0', 'result': {'expiration': '2020-07-23T05:55:14', 'ref_block_num': 1319, 'ref_block_prefix': 1026938970, 'operations': [[35, {'extensions': [], 'contract_id': '1.16.7', 'function_name': 'contract_test', 'value_list': [], 'caller': '1.2.16'}]], 'extensions': [], 'signatures': ['1f46ed96bd48e31c473a72c358495ede9cb60e794eec7775b21537bbbdf07a11dd730ae853ff69e1a46403dd1a970fb49e18d7cc5bc6c8d0a35a58d7f8668c15f9'], 'operation_results': [[4, {'contract_id': '1.16.7', 'relevant_datasize': 42, 'existed_pv': False, 'contract_affecteds': [[3, {'message': 'Hi, revise contract from file', 'affected_account': '1.2.16'}]], 'fees': [{'asset_id': '1.3.0', 'amount': 2268640}], 'real_running_time': 212, 'process_value': ''}]]}}


tx_id: 626d040d20804ee0a249e533935a753f953a0d982d7371a9847b6cd921c8d921, result: [[4, {'contract_id': '1.16.7', 'relevant_datasize': 42, 'existed_pv': False, 'contract_affecteds': [[3, {'message': 'Hi, revise contract from file', 'affected_account': '1.2.16'}]], 'fees': [{'asset_id': '1.3.0', 'amount': 2268640}], 'real_running_time': 212, 'process_value': ''}]]
release_cli_wallet_api done

=============================================

# vote function test
# 1. test cli_wallet api: get_global_extensions_properties
>> get_global_extensions_properties []

{'id': 1, 'jsonrpc': '2.0', 'result': {'contract_private_data_size': 3072, 'committee_max_votes': 11, 'contract_total_data_size': 10485760, 'contract_max_data_size': 2147483648, 'id': '2.15.0', 'witness_max_votes': 11}}


# 2. test chain_api_get_global_property_extensions
>> call [0, 'get_global_property_extensions', [[]]]

{'id': 1, 'jsonrpc': '2.0', 'result': {'contract_private_data_size': 3072, 'committee_max_votes': 11, 'contract_total_data_size': 10485760, 'contract_max_data_size': 2147483648, 'id': '2.15.0', 'witness_max_votes': 11}}



# 3. test vote for witness
>> get_object ['2.15.0']

{'id': 1, 'jsonrpc': '2.0', 'result': [{'contract_private_data_size': 3072, 'committee_max_votes': 11, 'contract_total_data_size': 10485760, 'contract_max_data_size': 2147483648, 'id': '2.15.0', 'witness_max_votes': 11}]}


[{'contract_private_data_size': 3072, 'committee_max_votes': 11, 'contract_total_data_size': 10485760, 'contract_max_data_size': 2147483648, 'id': '2.15.0', 'witness_max_votes': 11}]
>> list_witnesses ['', 12]

{'id': 1, 'jsonrpc': '2.0', 'result': [['init0', '1.6.1'], ['init1', '1.6.2'], ['init10', '1.6.11'], ['init2', '1.6.3'], ['init3', '1.6.4'], ['init4', '1.6.5'], ['init5', '1.6.6'], ['init6', '1.6.7'], ['init7', '1.6.8'], ['init8', '1.6.9'], ['init9', '1.6.10']]}


witnesses: [['init0', '1.6.1'], ['init1', '1.6.2'], ['init10', '1.6.11'], ['init2', '1.6.3'], ['init3', '1.6.4'], ['init4', '1.6.5'], ['init5', '1.6.6'], ['init6', '1.6.7'], ['init7', '1.6.8'], ['init8', '1.6.9'], ['init9', '1.6.10']]
>> list_account_balances ['nicotest']

{'id': 1, 'jsonrpc': '2.0', 'result': [{'asset_id': '1.3.0', 'amount': '9780000166477989'}]}


[{'asset_id': '1.3.0', 'amount': '9780000166477989'}]
>> vote_for_witness ['nicotest', 'init0', 10, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['5ed71ab391438aa6115d37cea43ace96287fa3a15942c5198cbd6f996ffb3686', {'expiration': '2020-07-23T05:55:18', 'ref_block_num': 1320, 'ref_block_prefix': 243735362, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['1:0'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 10}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f3b64c9ec02b62b5cccdcf75367b48e1167192f1449cf098200c3b4db068b108d376ec04d3e5451a0ea91993779c6a5fdb51e5960e1c467152d30662250fade09']}]}


>> vote_for_witness ['nicotest', 'init1', 13, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['dd315c122a428f86318cdae177cce06f907590a0044081feac958b1d54b84c1f', {'expiration': '2020-07-23T05:55:18', 'ref_block_num': 1320, 'ref_block_prefix': 243735362, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['1:0', '1:1'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 13}], 'extensions': {}}]], 'extensions': [], 'signatures': ['207b6938f137a8c4ea4cc4d87eaa974f528ad2a0c3479f323c064602ebe0144d8206b0157cbff518dc7ce4a2921e874e5f1fffa459cad44b9b8bd52634101319a1']}]}


>> vote_for_witness ['nicotest', 'init10', 18, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['480eabb8682babfccedd4aee113e56d2782a57d2de0d9f088f2776f615d3493c', {'expiration': '2020-07-23T05:55:18', 'ref_block_num': 1320, 'ref_block_prefix': 243735362, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['1:0', '1:1', '1:10'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 18}], 'extensions': {}}]], 'extensions': [], 'signatures': ['205ee70fc65f435e116b0ba1c99c7d3104b5787ee671afac7d0381efc0d6b1b92b11d4bfc855931968fe3144ac3681397395a4431d7076fbefb9aa100f590eb3de']}]}


>> vote_for_witness ['nicotest', 'init2', 3, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['48c1ae83b6a9e830ab835f1fa4c16bbc798291f26fe7497722a0c52d741a7f48', {'expiration': '2020-07-23T05:55:18', 'ref_block_num': 1320, 'ref_block_prefix': 243735362, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['1:0', '1:1', '1:2', '1:10'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 3}], 'extensions': {}}]], 'extensions': [], 'signatures': ['2011d143876c2a97b8ab759cca2b706a523cfa7410914927dc00177f8ce2f3194e6a9123126ded7aa6b211829420a3a9de09989a58b4ccaa6fc008a66be3bbfc15']}]}


>> vote_for_witness ['nicotest', 'init3', 3, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['a9061f7db9ea8559527dd37f5afc68512900e17ed2bf99be64e8b5a5c1e07a5c', {'expiration': '2020-07-23T05:55:18', 'ref_block_num': 1320, 'ref_block_prefix': 243735362, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['1:0', '1:1', '1:2', '1:3', '1:10'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 3}], 'extensions': {}}]], 'extensions': [], 'signatures': ['2034868b6def593d994ba457ec95e8eac45050acf23949a3306cce7accb9f29e3932a92a505f7615ac6440538285d2e2a639050f9998fc02cdeba5f222c959064d']}]}


>> vote_for_witness ['nicotest', 'init4', 19, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['7147ff735b15926dc65a0810a39c3639129825131da996cff9c7ada6289bed6d', {'expiration': '2020-07-23T05:55:18', 'ref_block_num': 1320, 'ref_block_prefix': 243735362, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['1:0', '1:1', '1:2', '1:3', '1:4', '1:10'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 19}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f2e6efb23e162dd0586a0033ef57fba56479c617c08c49e4ffc47605e1195e2043ba474bb432a22aee8ad02f334790955ad68e60a2007d3adc78e133833f9cfc6']}]}


>> vote_for_witness ['nicotest', 'init5', 20, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['89c4f7c08d75d0343e192d37e804bdd8bffd14a50e2ac5398cd6fd1aba735ea5', {'expiration': '2020-07-23T05:55:18', 'ref_block_num': 1320, 'ref_block_prefix': 243735362, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['1:0', '1:1', '1:2', '1:3', '1:4', '1:5', '1:10'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 20}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f1db1d5c958e538b4552cb350f754c5faee66ecc9d69e912b9c3e518b2f79a4675c1c6d1887906d3e299cfafdd3e88149f23fd0096ba03cf786be798e6fd28b67']}]}


>> vote_for_witness ['nicotest', 'init6', 10, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['b0123a2d4f94826702bfb0555780e3b5255aa9a4aa912faf8d2812ef08f9f7c0', {'expiration': '2020-07-23T05:55:18', 'ref_block_num': 1320, 'ref_block_prefix': 243735362, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['1:0', '1:1', '1:2', '1:3', '1:4', '1:5', '1:6', '1:10'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 10}], 'extensions': {}}]], 'extensions': [], 'signatures': ['205eae3529102763af6d9c82ff8706123d186a2aee7e6f70877b1ab0c4e6b16fc95fcccba7d6d4da8db0bbc700f2d93c6d1f3ed1839bd94d97dd9211a61c33eddf']}]}


>> vote_for_witness ['nicotest', 'init7', 11, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['2fcae07edb1e9b765c63bd217e292875afe3d9df2afde59f334e9db3282e5c31', {'expiration': '2020-07-23T05:55:18', 'ref_block_num': 1320, 'ref_block_prefix': 243735362, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['1:0', '1:1', '1:2', '1:3', '1:4', '1:5', '1:6', '1:7', '1:10'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 11}], 'extensions': {}}]], 'extensions': [], 'signatures': ['200c5ca4149be0c19baeabc316928b98a3857c903f574649296dfd40a12c48439816d1df8d808ba01b9f962dc40a97e97f47253d0fc985b1cf151af5713a6cdc34']}]}


>> vote_for_witness ['nicotest', 'init8', 14, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['c8cd200953748f9774ab2a5196826956a79faf04b49add959ed5bb85573e0335', {'expiration': '2020-07-23T05:55:18', 'ref_block_num': 1320, 'ref_block_prefix': 243735362, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['1:0', '1:1', '1:2', '1:3', '1:4', '1:5', '1:6', '1:7', '1:8', '1:10'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 14}], 'extensions': {}}]], 'extensions': [], 'signatures': ['2013355c5d37c92b3e456b3208afa2543b8f5cd6371c76931656d74528adf4e30074865f0cb01d0db8bf865a2f7e4c42fceaa6b38f429295ffa04c7a300412d700']}]}


>> vote_for_witness ['nicotest', 'init9', 6, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['506f66594529b4bf0c9b298450f4fe51eaf510c1b77f25d6f88845b98d0d5046', {'expiration': '2020-07-23T05:55:18', 'ref_block_num': 1320, 'ref_block_prefix': 243735362, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['1:0', '1:1', '1:2', '1:3', '1:4', '1:5', '1:6', '1:7', '1:8', '1:9', '1:10'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 6}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f2fc69742d3769178c6a156e01c0ba2b425c0e4072139fbe217099268fe5be8b946d8b7bb3de559fbed075873ff9d0f6d4e35fff4ab69fcba9e4d0f439c2eaf8b']}]}



# 4. test vote for committee
>> get_object ['2.15.0']

{'id': 1, 'jsonrpc': '2.0', 'result': [{'contract_private_data_size': 3072, 'committee_max_votes': 11, 'contract_total_data_size': 10485760, 'contract_max_data_size': 2147483648, 'id': '2.15.0', 'witness_max_votes': 11}]}


[{'contract_private_data_size': 3072, 'committee_max_votes': 11, 'contract_total_data_size': 10485760, 'contract_max_data_size': 2147483648, 'id': '2.15.0', 'witness_max_votes': 11}]
>> list_committee_members ['', 12]

{'id': 1, 'jsonrpc': '2.0', 'result': [['init0', '1.5.0'], ['init1', '1.5.1'], ['init10', '1.5.10'], ['init2', '1.5.2'], ['init3', '1.5.3'], ['init4', '1.5.4'], ['init5', '1.5.5'], ['init6', '1.5.6'], ['init7', '1.5.7'], ['init8', '1.5.8'], ['init9', '1.5.9'], ['nicotest', '1.5.11']]}


committees: [['init0', '1.5.0'], ['init1', '1.5.1'], ['init10', '1.5.10'], ['init2', '1.5.2'], ['init3', '1.5.3'], ['init4', '1.5.4'], ['init5', '1.5.5'], ['init6', '1.5.6'], ['init7', '1.5.7'], ['init8', '1.5.8'], ['init9', '1.5.9'], ['nicotest', '1.5.11']]
>> list_account_balances ['nicotest']

{'id': 1, 'jsonrpc': '2.0', 'result': [{'asset_id': '1.3.0', 'amount': '9780000144379133'}]}


[{'asset_id': '1.3.0', 'amount': '9780000144379133'}]
>> vote_for_committee_member ['nicotest', 'init0', 6, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['b640a9320e807674819b896fd036c04190e40ae3fb1d0580a7e58ced67795431', {'expiration': '2020-07-23T05:55:18', 'ref_block_num': 1320, 'ref_block_prefix': 243735362, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['0:11'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 6}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f1808cd61ce12f17e4f99e925b0a0be9d20988dbb1206a88ca237f08ecc76b4521d9c3c9083f0b1de81eb5acef8a574ad7bce95d729afadfbe8dfd33b2ecb64d4']}]}


>> vote_for_committee_member ['nicotest', 'init1', 4, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['af280121fa6bc5e8333010425a5446fe18e4d96112a508e994cfd125299c8145', {'expiration': '2020-07-23T05:55:18', 'ref_block_num': 1320, 'ref_block_prefix': 243735362, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['0:11', '0:12'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 4}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f6921ad4fb23ce379c9686af6124179dd3b729158574514f26b7a6527d222c3b41cd916e83010c6d9f9e1332e6eca1346464f3c67793f62b0742b4705a4d2d106']}]}


>> vote_for_committee_member ['nicotest', 'init10', 5, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['d7c610c9d6d9167030f2520168b0c2c5e345d286f78fc53284adbb5346d6d364', {'expiration': '2020-07-23T05:55:18', 'ref_block_num': 1320, 'ref_block_prefix': 243735362, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['0:11', '0:12', '0:21'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 5}], 'extensions': {}}]], 'extensions': [], 'signatures': ['201247f50406a040bbc99af9e7b8507002cffbdc531f0560a5b68a231a1faa0c860b7bd0852759d872fe6c2135931a5d7983e2586a45af52954abb0c4e40d78867']}]}


>> vote_for_committee_member ['nicotest', 'init2', 1, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['304f60043da6140cacde4987fe530f329bda5d4706b1c33ee0e91617c46846fe', {'expiration': '2020-07-23T05:55:18', 'ref_block_num': 1320, 'ref_block_prefix': 243735362, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['0:11', '0:12', '0:13', '0:21'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 1}], 'extensions': {}}]], 'extensions': [], 'signatures': ['2034c03301cf581fbdbc8f517b100f3235c425d8cae332becfdb24d3f79e19c7534a3cb4a6c12f6d5a1da4b8a7e112d081df44ad5e5057d6b964726b231be21dce']}]}


>> vote_for_committee_member ['nicotest', 'init3', 6, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['e59902892f19349f967f0ca046fe0a877d7e9b4f2d87f4d83470cfb4dda8602e', {'expiration': '2020-07-23T05:55:18', 'ref_block_num': 1320, 'ref_block_prefix': 243735362, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['0:11', '0:12', '0:13', '0:14', '0:21'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 6}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f7b9631d6e49151661c087716f66bf9cd378500e1493da52f2efec4add959e2c45bfc97886763d17f338da0e0cf0df0846602798c679f1f2f98d650ebbea35d2f']}]}


>> vote_for_committee_member ['nicotest', 'init4', 12, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['e94662651806a41b3118c08884579838f368e771f70d949733bc15d3559625d5', {'expiration': '2020-07-23T05:55:18', 'ref_block_num': 1320, 'ref_block_prefix': 243735362, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['0:11', '0:12', '0:13', '0:14', '0:15', '0:21'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 12}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f201734a1261af31fd36dc9efd91c3a4046e04748446b6a85e6caca8940acb2d224b0cf453e0412b8ce69b28ebef41b5112642cbfabb6681b919340a643a39f43']}]}


>> vote_for_committee_member ['nicotest', 'init5', 15, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['889ec905e5ba8300465533dc4d276b1ff945ee1308e963de6e2d9b12b1336c2c', {'expiration': '2020-07-23T05:55:18', 'ref_block_num': 1320, 'ref_block_prefix': 243735362, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['0:11', '0:12', '0:13', '0:14', '0:15', '0:16', '0:21'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 15}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f62332cb305417f72915d6c69889e94a852a1f561c861787a406384e1af27ebb20143912323fd6cdb01201f39c6b823ffb1bc67d1cf5a390482dda29bfb28eba5']}]}


>> vote_for_committee_member ['nicotest', 'init6', 18, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['6d3c9d509fe70b550a15a1a753ec9fd8877a84d38fb0929363e04dd012d1cd79', {'expiration': '2020-07-23T05:55:18', 'ref_block_num': 1320, 'ref_block_prefix': 243735362, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['0:11', '0:12', '0:13', '0:14', '0:15', '0:16', '0:17', '0:21'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 18}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f2805117a18ebada403a2d75e5a35d307593b1d88740f39146879ff2b61a7235e7a1009d54788e69fdc747d3b420cf388ce22538f7662f40ebdd8df59539b4cf9']}]}


>> vote_for_committee_member ['nicotest', 'init7', 4, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['ac94babafa42ab55d968a30b15db68d9b0287f80c30377903a2e592508295560', {'expiration': '2020-07-23T05:55:20', 'ref_block_num': 1321, 'ref_block_prefix': 1195637801, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['0:11', '0:12', '0:13', '0:14', '0:15', '0:16', '0:17', '0:18', '0:21'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 4}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f28ca8546bcd0f06437f163da0fb55f3376ac6d76632f6a96cde9bba423a785fb2c6ca0a8c63c006a86408fd97606fb1adcabaa00e0c3d25dd83604bbcf0ab428']}]}


>> vote_for_committee_member ['nicotest', 'init8', 14, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['421ec7de327f089a2e9cd927ea709b9fd2b9a1a3e48389b7db45b967c851a880', {'expiration': '2020-07-23T05:55:20', 'ref_block_num': 1321, 'ref_block_prefix': 1195637801, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['0:11', '0:12', '0:13', '0:14', '0:15', '0:16', '0:17', '0:18', '0:19', '0:21'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 14}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f0a979601e480d839438e4cde071b5cd2175d7ae082cf893939714bd0641ac5035612ae2674e2b1c2eb3ef99521762e96e1b453477f706750a71b3adac7b5f3aa']}]}


>> vote_for_committee_member ['nicotest', 'init9', 6, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['f38cba77949a8bacd9a52afbf58ba8feb9674e30de6dc2d5c1b81d8cb3f07a22', {'expiration': '2020-07-23T05:55:20', 'ref_block_num': 1321, 'ref_block_prefix': 1195637801, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['0:11', '0:12', '0:13', '0:14', '0:15', '0:16', '0:17', '0:18', '0:19', '0:20', '0:21'], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 6}], 'extensions': {}}]], 'extensions': [], 'signatures': ['2023dc046535c74b81994b416db0293b389bfebb25c15ad9afc89144ab967e416d18b1171935aa0f72e8785843312ed265c1c598da6fab51203aa2a7cbf512ebc9']}]}


>> vote_for_committee_member ['nicotest', 'nicotest', 5, True]

{'id': 1, 'jsonrpc': '2.0', 'error': {'message': 'unspecified: Assert Exception: num_committee <= committee_number_of_vote: Voted for more committee members than currently allowed (11)', 'code': 1}}


AssertionError()

# 5. test cancle vote for witness
>> vote_for_witness ['nicotest', 'init0', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['a5d4b2c3a6cb2a6d42d356765e38642ff50d832c586351f3e2a92643935168b9', {'expiration': '2020-07-23T05:55:30', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['206ac25f245a93061a8bf4ec4b371960770bf303b519076701994f2ae282dafbaf0c6e8d18bf9cf782754d426884fad5e51ab07b941da3ba7bc3be00fe9074243e']}]}


>> vote_for_witness ['nicotest', 'init1', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['92a1fe69a9e615238271de75aec59657a2e2a901f4c97d8003fa8e7c030dd193', {'expiration': '2020-07-23T05:55:31', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['204eba9bbc43384ac5bdb568192b6d1c3f1d733d5f0e5c24280c6faeb375bec0295409399798b46e214f12d2cbc21ad920516e077e5eb288338c2ecacd789df9a4']}]}


>> vote_for_witness ['nicotest', 'init10', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['8c7879b0f64207d9fec3fb2f8642c477a51147a704ac79b3bfede16b2e17d483', {'expiration': '2020-07-23T05:55:32', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f03063e5152f02d370428c1b9f5e19c0b0dea078be6949cb87da23a13d3bc80a866286970d4a7e3c137819cec265352c243d9e0d9d2f35ba4c357d6237c9bb14f']}]}


>> vote_for_witness ['nicotest', 'init2', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['5b23f4ffdc629519e656239616df22741685799ebec0c94fe29679f4416cdf6c', {'expiration': '2020-07-23T05:55:33', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f11e9fd8bb84f0f08f325eb15ca2c24883d85ed2696ada87a6f75565061c13821506e6b3e75ac499276ad7df74a98957bdc47dab250f7704ac05f1ed4467c390a']}]}


>> vote_for_witness ['nicotest', 'init3', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['9564042a0d2807e9ca15927d372cb1cfcd62c1617a87cc371c4c31357b68f6c6', {'expiration': '2020-07-23T05:55:34', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f1489488c8ba4a4ff9d0cfb2163417961acc27fd3b8a0ba53ad363cdcb6d553a267c2cf34f73b0377abc3087b1e9325742c4debd038d10e00fc8381a374eb488e']}]}


>> vote_for_witness ['nicotest', 'init4', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['644502aa5e818e3a169d4a601b7007f16606c873ede57f6e8acf88578c97a137', {'expiration': '2020-07-23T05:55:35', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f5b592319f6cfe8c573e1ad7300ab67168cbb3ef61d7db3accc8d5279bad1f1a86b01580a49600c85377daad1e6545f79fd94126fd1a9878249d93553f693bc76']}]}


>> vote_for_witness ['nicotest', 'init5', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['4003a98f713fd9713ca21b433d0fab04e36c0d59449bb218475774c112943f44', {'expiration': '2020-07-23T05:55:36', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['207e88e8e27170440794373eed6b0edd37862e2d457d57418a78474070233970873fe6c882a1e473b7dfc03b0f3412867963d1874598156ee22e5df0dbf63028cd']}]}


>> vote_for_witness ['nicotest', 'init6', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['6e72e0fdfb678be2d523f41947e1fe98e1ab08712e1313bea22b90789885b3ec', {'expiration': '2020-07-23T05:55:37', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f2c58903e52cbeb926304ba0dc8acc83df5b252cb922e6c4fdbdaa02384c707371cb5d70fefcd995183848d66d854794f6cfb075e82ad9eabc5a8340a03f84179']}]}


>> vote_for_witness ['nicotest', 'init7', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['8eda5bf648ff14c5ede50e321ba4d64738e2e272095e2fbe8f0ad8916ed332b9', {'expiration': '2020-07-23T05:55:38', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f5f914ee4126c451024887949465ca4d6591b8f78377f619ab8e08e88aa781e4307421ca08983241090fb721d86e9ccfa1e3271f9f4a6b9bfd855774c53db8bf7']}]}


>> vote_for_witness ['nicotest', 'init8', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['7ad7dd19c4eff611896c0ec465c7079cbb7a5fe28ba84e87893f036974f817bb', {'expiration': '2020-07-23T05:55:39', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['205d6ba54e89ae758515a6c25c9f8d53dafd39a1278f0f87df158987d3af149eca048fb5f19d399873879e366cfd6364efce9ada334241029dfeca22ed28015c97']}]}


>> vote_for_witness ['nicotest', 'init9', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['604345ed8481721e5bb0e7d86fef168e424ff836b6317c2e529224d04f1ad8e6', {'expiration': '2020-07-23T05:55:40', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f775c4b1f147cd4d154ec02247a5d4fcf9d49c91fa0f344e42c61c76209060853753a16f32e898aa1f3d12633d6486364cd5b4fade2fdd71a2dfdeeffebf4caf9']}]}



# 6. test  cancle vote for committee
>> vote_for_committee_member ['nicotest', 'init0', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['cd64c8b73c3bea818e2f91b615a310e4a6d56b4948322cd14c579f407cb2fa6d', {'expiration': '2020-07-23T05:55:30', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['2004ac73d2397acc13b98f475ee4e2aa7e43edebb48e40f6254ab8ff7d1acaa163652e49d3bcd61041dfb7a00220767aa466fc77efc050544eb5da011c6cdb11b6']}]}


>> vote_for_committee_member ['nicotest', 'init1', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['2bb22f4239bb5e650cf1bbb2048381b9b3a27f27733fdc9ece56befb0d9b10da', {'expiration': '2020-07-23T05:55:31', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['2056651f6696983bda4aa3ae0ac2913984725e7fe31cc831899d629e0e8be133c5541a0fd5965f5df7a5382f8b31e9e4f508ac733cd21c83feeb10469d0db75907']}]}


>> vote_for_committee_member ['nicotest', 'init10', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['b67c1e9511dc9a5e63386c8d8d651c38fb866633d6a533fd240590fb714d665d', {'expiration': '2020-07-23T05:55:32', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['201de1f65e239c17f0854e163c07e06bd6f5291973408ea27e79788a26eb9c1f6561dfb98bb8b01a49e3cb38c55455247c426c0f5a1dad5cbc1df0b143c67c61d6']}]}


>> vote_for_committee_member ['nicotest', 'init2', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['1f8b2252a94e38f6c99ddc44c6b14b3510332f7f947bf1b549291ef071cfb33e', {'expiration': '2020-07-23T05:55:33', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f01f98ccd383ae5e6c04d8a116fc7cb1197b5eb7e5449da1f509cff2ec35bdbe50fcf0e7233d8446d33446ae1f68640591d8c7579c7cc32e1a343ecda5c77f2a2']}]}


>> vote_for_committee_member ['nicotest', 'init3', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['92d812d9f9775c09b0e511542284ac8ce0810cd1ac98af700d37965ea662bbe4', {'expiration': '2020-07-23T05:55:34', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['20311c3a9236495bd61f4dc11bcea57ef39357ec4d68f209bd23db3d5130c33af93b3014226209505f94b6c4127c574ec9240feb315f3a0553be6a44e8c84b1a19']}]}


>> vote_for_committee_member ['nicotest', 'init4', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['07410766b6cff217eb9d10e81487f847a4307ae6c021e84b037d6a53c0663480', {'expiration': '2020-07-23T05:55:35', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['203472da087a61da045159409ff0f5cad1e5fe98bc0a3e51a5bc92e88b99dbac887b3af1419cd6f12e70351710b3103a30d785341ba490f2a2014c3107d012cc40']}]}


>> vote_for_committee_member ['nicotest', 'init5', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['88413437f5bff8cbc128a43ba9dfa12c145219aab158f7ee618f1d83ab9fab7c', {'expiration': '2020-07-23T05:55:36', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['2001b4b1d969b1e73613644fa60b5667fc3496810e375c053e90e549925e9cbfb46d4a77301f32f5cb30f2ac191c16a886d66dcac4939d7fcfc635755dfab536e1']}]}


>> vote_for_committee_member ['nicotest', 'init6', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['f1c8fcddaf97e643efb74a2be593a7d3a35fd278995aa0a9e5d173a759b7065e', {'expiration': '2020-07-23T05:55:37', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f4805ed6d5de1b60504270b89a85796ab84b82fabb3c0bac8c0de4c0487fe83362a886605e7898caab8bbe5a9dc0d6f9aca2e8fb42c0dec13f963c2d9543618f9']}]}


>> vote_for_committee_member ['nicotest', 'init7', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['a2a6d665a6660372dab735b1a643d258e417d4ead14d93cab991cf8fc5f2d792', {'expiration': '2020-07-23T05:55:38', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f62c7f26bf95f0814cca33f1bf75a98eba6f2ee7ff1fed771087b35f575a5e9d139830152242d1dc21796410ce29264e852c27aa780a9c45ee0dfee3c7dff74d0']}]}


>> vote_for_committee_member ['nicotest', 'init8', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['939ebe57d107f42f0928316e53b51c77d496abb478e0e033300af1f1dd1f89ee', {'expiration': '2020-07-23T05:55:39', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['2032406cd517da927fc5b35420982f72caf5aa975096fcefbbbf3522f5cab3a3463cd0a3ad0284ad07c82c8298df07e2bffb87145d877f33c16a8c4d643ae36433']}]}


>> vote_for_committee_member ['nicotest', 'init9', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['25efb55c1ae59cb5216ae7a26be8335655e18c83c1370d6076b6bace2fc1228f', {'expiration': '2020-07-23T05:55:40', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['207a8ad1b9ee4862be773b32256d24d2bbef484227c01f169a67f0bde5e611c6cd198f540154522a4dec3de8d348aa5c58ecb5efa3ebac32c7c77173785a3fe5c7']}]}


>> vote_for_committee_member ['nicotest', 'nicotest', 0, True]

{'id': 1, 'jsonrpc': '2.0', 'result': ['2167c4bb40680ae29e569c2465c6b268281f1179970b5ed2fd418a0c38730cdf', {'expiration': '2020-07-23T05:55:41', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[6, {'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'asset_id': '1.3.0', 'amount': 0}], 'extensions': {}}]], 'extensions': [], 'signatures': ['1f3751e570ef54344d7b88b8b9ef2a742876e490232ca8bb607657ef390264246d419a7b231d8e12a7eafd548d5c2c013a7701b1c404cbbe479bc3784949cbfe03']}]}


test vote for xxx done
=============================================

# contract api test
contract_name: contract.release115.gcpdbne, test account: nicotest
1. create contract from file and call test
>> get_contract ['contract.release115.gcpdbne']

{'id': 1, 'jsonrpc': '2.0', 'error': {'message': 'unspecified: Assert Exception: contract_itr != con_index.end(): The contract (contract.release115.gcpdbne) does not exist', 'code': 1}}


>> create_contract_from_file ['nicotest', 'contract.release115.gcpdbne', 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz', '/home/ck/xukang/CocosBCX/feature_test/release1.1.5/contract_api_get_contract_public_data.lua', 'true']

{'id': 1, 'jsonrpc': '2.0', 'result': ['747cc7b348330f86825c2d4a77f9b08dcf6de420d73e1dba36281eee02c89d3f', {'expiration': '2020-07-23T05:55:30', 'ref_block_num': 1325, 'ref_block_prefix': 3897511320, 'operations': [[34, {'name': 'contract.release115.gcpdbne', 'owner': '1.2.16', 'extensions': [], 'contract_authority': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz', 'data': 'function init()     read_list = {         public_data = {             is_init = true         }     }     chainhelper:read_chain();      public_data.userdata = {};     public_data.is_init = true;      write_list = {         public_data = {}     }     chainhelper:write_chain(); end  function insert(id, name)     read_list = {         public_data = {userdata=true}     }     chainhelper:read_chain()      local userdata = public_data.userdata;     userdata[id] = name     public_data.userdata = userdata      write_list = {         public_data = {userdata=true}     }     chainhelper:write_chain(); end  function test(name_or_id)      data = chainhelper:get_contract_public_data(name_or_id)      jsonStr = cjson.encode(data)     chainhelper:log("contract: " .. name_or_id .. ", public_data: " .. jsonStr) end'}]], 'extensions': [], 'signatures': ['1f2b98025b63d56597605fdac40e22503eeb051855931d4d4a62bed6132485532119bfecb489d67bfebf7c3b45d056e9f31e7339737c0e2cba18e75541aead3ad4']}]}


>> call_contract_function ['nicotest', 'contract.release115.gcpdbne', 'init', [], 'true']

{'id': 1, 'jsonrpc': '2.0', 'result': ['585518ff15ca086ae0a7cfccb5da09fe8a70949b4425ee878fe376e97297f6f5', {'expiration': '2020-07-23T05:55:34', 'ref_block_num': 1326, 'ref_block_prefix': 3735587175, 'operations': [[35, {'extensions': [], 'contract_id': '1.16.8', 'function_name': 'init', 'value_list': [], 'caller': '1.2.16'}]], 'extensions': [], 'signatures': ['20258640a583665fd5a04d70f9f3a59b8ee74ac17ced92129ef6a5728aee2cb2186bf3920364a50fb96fccfcd9b30da5af168f94b3e9aec31bd0652d2446096dc6']}]}


>> get_transaction_by_id ['585518ff15ca086ae0a7cfccb5da09fe8a70949b4425ee878fe376e97297f6f5']

{'id': 1, 'jsonrpc': '2.0', 'result': {'expiration': '2020-07-23T05:55:34', 'ref_block_num': 1326, 'ref_block_prefix': 3735587175, 'operations': [[35, {'extensions': [], 'contract_id': '1.16.8', 'function_name': 'init', 'value_list': [], 'caller': '1.2.16'}]], 'extensions': [], 'signatures': ['20258640a583665fd5a04d70f9f3a59b8ee74ac17ced92129ef6a5728aee2cb2186bf3920364a50fb96fccfcd9b30da5af168f94b3e9aec31bd0652d2446096dc6'], 'operation_results': [[4, {'contract_id': '1.16.8', 'relevant_datasize': 26, 'existed_pv': False, 'contract_affecteds': [], 'fees': [{'asset_id': '1.3.0', 'amount': 2272225}], 'real_running_time': 240, 'process_value': ''}]]}}


tx_id: 585518ff15ca086ae0a7cfccb5da09fe8a70949b4425ee878fe376e97297f6f5, result: [[4, {'contract_id': '1.16.8', 'relevant_datasize': 26, 'existed_pv': False, 'contract_affecteds': [], 'fees': [{'asset_id': '1.3.0', 'amount': 2272225}], 'real_running_time': 240, 'process_value': ''}]]
>> call_contract_function ['nicotest', 'contract.release115.gcpdbne', 'insert', [[2, {'v': '00511'}], [2, {'v': 'zhang_511'}]], 'true']

{'id': 1, 'jsonrpc': '2.0', 'result': ['31bb48622ecdd8aa7dba305ddf75be5c2c1ca4cb2096a731bed456de9ad727ca', {'expiration': '2020-07-23T05:55:38', 'ref_block_num': 1330, 'ref_block_prefix': 3949464390, 'operations': [[35, {'extensions': [], 'contract_id': '1.16.8', 'function_name': 'insert', 'value_list': [[2, {'v': '00511'}], [2, {'v': 'zhang_511'}]], 'caller': '1.2.16'}]], 'extensions': [], 'signatures': ['1f4867d46c96911b5ab5de687f32b5262e9848a4b70b12d0e59a96f7f2d9cef4494ba2dfa8a38c8a2c5ed532aea8e73dcf0caf8d25286111b02ded4136825b98f2']}]}


>> get_transaction_by_id ['31bb48622ecdd8aa7dba305ddf75be5c2c1ca4cb2096a731bed456de9ad727ca']

{'id': 1, 'jsonrpc': '2.0', 'result': {'expiration': '2020-07-23T05:55:38', 'ref_block_num': 1330, 'ref_block_prefix': 3949464390, 'operations': [[35, {'extensions': [], 'contract_id': '1.16.8', 'function_name': 'insert', 'value_list': [[2, {'v': '00511'}], [2, {'v': 'zhang_511'}]], 'caller': '1.2.16'}]], 'extensions': [], 'signatures': ['1f4867d46c96911b5ab5de687f32b5262e9848a4b70b12d0e59a96f7f2d9cef4494ba2dfa8a38c8a2c5ed532aea8e73dcf0caf8d25286111b02ded4136825b98f2'], 'operation_results': [[4, {'contract_id': '1.16.8', 'relevant_datasize': 44, 'existed_pv': False, 'contract_affecteds': [], 'fees': [{'asset_id': '1.3.0', 'amount': 2320335}], 'real_running_time': 251, 'process_value': ''}]]}}


tx_id: 31bb48622ecdd8aa7dba305ddf75be5c2c1ca4cb2096a731bed456de9ad727ca, result: [[4, {'contract_id': '1.16.8', 'relevant_datasize': 44, 'existed_pv': False, 'contract_affecteds': [], 'fees': [{'asset_id': '1.3.0', 'amount': 2320335}], 'real_running_time': 251, 'process_value': ''}]]
>> call_contract_function ['nicotest', 'contract.release115.gcpdbne', 'insert', [[2, {'v': '00690'}], [2, {'v': 'zhang_690'}]], 'true']

{'id': 1, 'jsonrpc': '2.0', 'result': ['b6105bbf340f42ede8c2f57c60fbb9601d712671c6c5edc2419995d7d400257a', {'expiration': '2020-07-23T05:55:40', 'ref_block_num': 1331, 'ref_block_prefix': 2705945023, 'operations': [[35, {'extensions': [], 'contract_id': '1.16.8', 'function_name': 'insert', 'value_list': [[2, {'v': '00690'}], [2, {'v': 'zhang_690'}]], 'caller': '1.2.16'}]], 'extensions': [], 'signatures': ['2010621900222322e13564723d20b0e383140382fa036964e6e81fe0ff95f8941817f4ad7e1a882bc820c8edc97e51acb67c86f78e38586cd94fb5c18563e7485a']}]}


>> get_transaction_by_id ['b6105bbf340f42ede8c2f57c60fbb9601d712671c6c5edc2419995d7d400257a']

{'id': 1, 'jsonrpc': '2.0', 'result': {'expiration': '2020-07-23T05:55:40', 'ref_block_num': 1331, 'ref_block_prefix': 2705945023, 'operations': [[35, {'extensions': [], 'contract_id': '1.16.8', 'function_name': 'insert', 'value_list': [[2, {'v': '00690'}], [2, {'v': 'zhang_690'}]], 'caller': '1.2.16'}]], 'extensions': [], 'signatures': ['2010621900222322e13564723d20b0e383140382fa036964e6e81fe0ff95f8941817f4ad7e1a882bc820c8edc97e51acb67c86f78e38586cd94fb5c18563e7485a'], 'operation_results': [[4, {'contract_id': '1.16.8', 'relevant_datasize': 62, 'existed_pv': False, 'contract_affecteds': [], 'fees': [{'asset_id': '1.3.0', 'amount': 2373913}], 'real_running_time': 287, 'process_value': ''}]]}}


tx_id: b6105bbf340f42ede8c2f57c60fbb9601d712671c6c5edc2419995d7d400257a, result: [[4, {'contract_id': '1.16.8', 'relevant_datasize': 62, 'existed_pv': False, 'contract_affecteds': [], 'fees': [{'asset_id': '1.3.0', 'amount': 2373913}], 'real_running_time': 287, 'process_value': ''}]]
>> get_contract ['contract.release115.gcpdbne']

{'id': 1, 'jsonrpc': '2.0', 'result': {'name': 'contract.release115.gcpdbne', 'owner': '1.2.16', 'contract_authority': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz', 'current_version': '747cc7b348330f86825c2d4a77f9b08dcf6de420d73e1dba36281eee02c89d3f', 'lua_code_b_id': '2.2.8', 'contract_data': [[{'key': [2, {'v': 'is_init'}]}, [3, {'v': True}]], [{'key': [2, {'v': 'userdata'}]}, [4, {'v': [[{'key': [2, {'v': '00511'}]}, [2, {'v': 'zhang_511'}]], [{'key': [2, {'v': '00690'}]}, [2, {'v': 'zhang_690'}]]]}]]], 'user_invoke_share_percent': 100, 'id': '1.16.8', 'creation_date': '2020-07-23T05:35:00', 'check_contract_authority': False, 'is_release': False, 'contract_ABI': [[{'key': [2, {'v': 'init'}]}, [5, {'arglist': [], 'is_var_arg': False}]], [{'key': [2, {'v': 'insert'}]}, [5, {'arglist': ['id', 'name'], 'is_var_arg': False}]], [{'key': [2, {'v': 'test'}]}, [5, {'arglist': ['name_or_id'], 'is_var_arg': False}]]]}}


{'name': 'contract.release115.gcpdbne', 'owner': '1.2.16', 'contract_authority': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz', 'current_version': '747cc7b348330f86825c2d4a77f9b08dcf6de420d73e1dba36281eee02c89d3f', 'lua_code_b_id': '2.2.8', 'contract_data': [[{'key': [2, {'v': 'is_init'}]}, [3, {'v': True}]], [{'key': [2, {'v': 'userdata'}]}, [4, {'v': [[{'key': [2, {'v': '00511'}]}, [2, {'v': 'zhang_511'}]], [{'key': [2, {'v': '00690'}]}, [2, {'v': 'zhang_690'}]]]}]]], 'user_invoke_share_percent': 100, 'id': '1.16.8', 'creation_date': '2020-07-23T05:35:00', 'check_contract_authority': False, 'is_release': False, 'contract_ABI': [[{'key': [2, {'v': 'init'}]}, [5, {'arglist': [], 'is_var_arg': False}]], [{'key': [2, {'v': 'insert'}]}, [5, {'arglist': ['id', 'name'], 'is_var_arg': False}]], [{'key': [2, {'v': 'test'}]}, [5, {'arglist': ['name_or_id'], 'is_var_arg': False}]]]}
>> call_contract_function ['nicotest', 'contract.release115.gcpdbne', 'test', [[2, {'v': 'contract.release115.gcpdbne'}]], 'true']

{'id': 1, 'jsonrpc': '2.0', 'result': ['40689cb3eef951d65a000383e30c5b56e888b32a5d0f204611185e4a66d7b245', {'expiration': '2020-07-23T05:55:50', 'ref_block_num': 1334, 'ref_block_prefix': 3221638287, 'operations': [[35, {'extensions': [], 'contract_id': '1.16.8', 'function_name': 'test', 'value_list': [[2, {'v': 'contract.release115.gcpdbne'}]], 'caller': '1.2.16'}]], 'extensions': [], 'signatures': ['206f17e43c57abcfc5d9fda9cedb4c0149d3f9214de237f95568400d569847837f79a9a6489f07eebd133d1442c3c819011a97c8d645303e0be2bdf891038d3b6f']}]}


>> get_transaction_by_id ['40689cb3eef951d65a000383e30c5b56e888b32a5d0f204611185e4a66d7b245']

{'id': 1, 'jsonrpc': '2.0', 'result': {'expiration': '2020-07-23T05:55:50', 'ref_block_num': 1334, 'ref_block_prefix': 3221638287, 'operations': [[35, {'extensions': [], 'contract_id': '1.16.8', 'function_name': 'test', 'value_list': [[2, {'v': 'contract.release115.gcpdbne'}]], 'caller': '1.2.16'}]], 'extensions': [], 'signatures': ['206f17e43c57abcfc5d9fda9cedb4c0149d3f9214de237f95568400d569847837f79a9a6489f07eebd133d1442c3c819011a97c8d645303e0be2bdf891038d3b6f'], 'operation_results': [[4, {'contract_id': '1.16.8', 'relevant_datasize': 193, 'existed_pv': False, 'contract_affecteds': [[3, {'message': 'contract: contract.release115.gcpdbne, public_data: {"is_init":true,"userdata":{"00511":"zhang_511","00690":"zhang_690"}}', 'affected_account': '1.2.16'}]], 'fees': [{'asset_id': '1.3.0', 'amount': 2481632}], 'real_running_time': 258, 'process_value': ''}]]}}


tx_id: 40689cb3eef951d65a000383e30c5b56e888b32a5d0f204611185e4a66d7b245, result: [[4, {'contract_id': '1.16.8', 'relevant_datasize': 193, 'existed_pv': False, 'contract_affecteds': [[3, {'message': 'contract: contract.release115.gcpdbne, public_data: {"is_init":true,"userdata":{"00511":"zhang_511","00690":"zhang_690"}}', 'affected_account': '1.2.16'}]], 'fees': [{'asset_id': '1.3.0', 'amount': 2481632}], 'real_running_time': 258, 'process_value': ''}]]
test_contract_get_contract_public_data done

------------------------------------------------

contract_name: contract.release115.gcpdfou, test account: nicotest
### 1. create contract from file and call test
>> get_contract ['contract.release115.gcpdfou']

{'id': 1, 'jsonrpc': '2.0', 'error': {'message': 'unspecified: Assert Exception: contract_itr != con_index.end(): The contract (contract.release115.gcpdfou) does not exist', 'code': 1}}


>> create_contract_from_file ['nicotest', 'contract.release115.gcpdfou', 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz', '/home/ck/xukang/CocosBCX/feature_test/release1.1.5/contract_api_integer_max_and_min.lua', 'true']

{'id': 1, 'jsonrpc': '2.0', 'result': ['d9b222cae3ab41ac283da0c63ffb385b3731fdab0ef7ce3af2b306af560efcc9', {'expiration': '2020-07-23T05:55:52', 'ref_block_num': 1336, 'ref_block_prefix': 3145918978, 'operations': [[34, {'name': 'contract.release115.gcpdfou', 'owner': '1.2.16', 'extensions': [], 'contract_authority': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz', 'data': 'function test_integer_max()     chainhelper:log(chainhelper:integer_max())         local tmpmax = chainhelper:integer_max()     chainhelper:log(tmpmax)  end  function test_integer_min()     chainhelper:log(chainhelper:integer_min())         local tmpmin = chainhelper:integer_min()     chainhelper:log(tmpmin)  end  '}]], 'extensions': [], 'signatures': ['1f1dc2f21740ed7c64db47809ab5901964c40a37483f34e5dc2b0fd10c31ae490240cf44b44c6a8640b635464ddab91c286f7419fa8ac962f5e8c20f8952d02423']}]}


>> call_contract_function ['nicotest', 'contract.release115.gcpdfou', 'test_integer_max', [], 'true']

{'id': 1, 'jsonrpc': '2.0', 'result': ['665e82724c888f794285b675033cb116e0be41943cd95321b5b6f04e06050541', {'expiration': '2020-07-23T05:55:58', 'ref_block_num': 1338, 'ref_block_prefix': 72600085, 'operations': [[35, {'extensions': [], 'contract_id': '1.16.9', 'function_name': 'test_integer_max', 'value_list': [], 'caller': '1.2.16'}]], 'extensions': [], 'signatures': ['1f526e5f7b4afaaa71c1fa32fd023ccfdea62fb3f58d9e29174d1844d088a4ccf0195cee1f6ad16f8e53facbfce4eaaa5cab658b3b9e683cf7050c4abba07bdf7f']}]}


>> get_transaction_by_id ['665e82724c888f794285b675033cb116e0be41943cd95321b5b6f04e06050541']

{'id': 1, 'jsonrpc': '2.0', 'result': {'expiration': '2020-07-23T05:55:58', 'ref_block_num': 1338, 'ref_block_prefix': 72600085, 'operations': [[35, {'extensions': [], 'contract_id': '1.16.9', 'function_name': 'test_integer_max', 'value_list': [], 'caller': '1.2.16'}]], 'extensions': [], 'signatures': ['1f526e5f7b4afaaa71c1fa32fd023ccfdea62fb3f58d9e29174d1844d088a4ccf0195cee1f6ad16f8e53facbfce4eaaa5cab658b3b9e683cf7050c4abba07bdf7f'], 'operation_results': [[4, {'contract_id': '1.16.9', 'relevant_datasize': 61, 'existed_pv': False, 'contract_affecteds': [[3, {'message': '9223372036854775807', 'affected_account': '1.2.16'}], [3, {'message': '9223372036854775807', 'affected_account': '1.2.16'}]], 'fees': [{'asset_id': '1.3.0', 'amount': 2304124}], 'real_running_time': 226, 'process_value': ''}]]}}


tx_id: 665e82724c888f794285b675033cb116e0be41943cd95321b5b6f04e06050541, result: [[4, {'contract_id': '1.16.9', 'relevant_datasize': 61, 'existed_pv': False, 'contract_affecteds': [[3, {'message': '9223372036854775807', 'affected_account': '1.2.16'}], [3, {'message': '9223372036854775807', 'affected_account': '1.2.16'}]], 'fees': [{'asset_id': '1.3.0', 'amount': 2304124}], 'real_running_time': 226, 'process_value': ''}]]
>> call_contract_function ['nicotest', 'contract.release115.gcpdfou', 'test_integer_min', [], 'true']

{'id': 1, 'jsonrpc': '2.0', 'result': ['8c467b6bb854757680f9ba8e7eb583b61d15037848cfee024338dc0af8bc39bf', {'expiration': '2020-07-23T05:56:02', 'ref_block_num': 1339, 'ref_block_prefix': 2439462618, 'operations': [[35, {'extensions': [], 'contract_id': '1.16.9', 'function_name': 'test_integer_min', 'value_list': [], 'caller': '1.2.16'}]], 'extensions': [], 'signatures': ['20724ac63049e7e86540a496f92ab9d6e4b01e07da3004099d8f9742f5ce786067063d6c91bb523f58961f5b30afefb10ead4bdec7d054056168a314088951c7f5']}]}


>> get_transaction_by_id ['8c467b6bb854757680f9ba8e7eb583b61d15037848cfee024338dc0af8bc39bf']

{'id': 1, 'jsonrpc': '2.0', 'result': {'expiration': '2020-07-23T05:56:02', 'ref_block_num': 1339, 'ref_block_prefix': 2439462618, 'operations': [[35, {'extensions': [], 'contract_id': '1.16.9', 'function_name': 'test_integer_min', 'value_list': [], 'caller': '1.2.16'}]], 'extensions': [], 'signatures': ['20724ac63049e7e86540a496f92ab9d6e4b01e07da3004099d8f9742f5ce786067063d6c91bb523f58961f5b30afefb10ead4bdec7d054056168a314088951c7f5'], 'operation_results': [[4, {'contract_id': '1.16.9', 'relevant_datasize': 63, 'existed_pv': False, 'contract_affecteds': [[3, {'message': '-9223372036854775808', 'affected_account': '1.2.16'}], [3, {'message': '-9223372036854775808', 'affected_account': '1.2.16'}]], 'fees': [{'asset_id': '1.3.0', 'amount': 2311077}], 'real_running_time': 231, 'process_value': ''}]]}}


tx_id: 8c467b6bb854757680f9ba8e7eb583b61d15037848cfee024338dc0af8bc39bf, result: [[4, {'contract_id': '1.16.9', 'relevant_datasize': 63, 'existed_pv': False, 'contract_affecteds': [[3, {'message': '-9223372036854775808', 'affected_account': '1.2.16'}], [3, {'message': '-9223372036854775808', 'affected_account': '1.2.16'}]], 'fees': [{'asset_id': '1.3.0', 'amount': 2311077}], 'real_running_time': 231, 'process_value': ''}]]
------------------------------------------------

=============================================

ck@ubuntu:~/xukang/CocosBCX/feature_test/release1.1.5$ 
```  