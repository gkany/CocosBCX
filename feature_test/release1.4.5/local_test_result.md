测试运行和结果：  
``` text  
dev@ubuntu:~/data/mrepo/CocosBCX/feature_test/release1.4.5$ python3 release.py 
>> unlock ['123456']

{'result': None, 'jsonrpc': '2.0', 'id': 1}


# cli_wallet api test
contract_name: contract.release115say, test account: nicotest
1. create contract from file and call test
>> get_contract ['contract.release115say']

{'jsonrpc': '2.0', 'error': {'code': 1, 'message': 'unspecified: Assert Exception: contract_itr != con_index.end(): The contract (contract.release115say) does not exist'}, 'id': 1}


>> create_contract_from_file ['nicotest', 'contract.release115say', 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz', '/home/dev/data/mrepo/CocosBCX/feature_test/release1.4.5/contract_create.lua', 'true']

{'result': ['1b8b04d8bd86643f2c888e6b8669db08e62128b35f837f2dc3ac219638173c0c', {'expiration': '2020-07-23T04:10:42', 'operations': [[34, {'owner': '1.2.16', 'extensions': [], 'contract_authority': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz', 'name': 'contract.release115say', 'data': 'function contract_test() \tchainhelper:log("Hi, create contract from file")  end'}]], 'extensions': [], 'ref_block_num': 5386, 'signatures': ['1f055c6161d906f134096ddedfccb93ddea787d97bf6de9f81aa84610c3d6fe5470b649cdbe939699e435335f3bea2cf590ba3115b79214157f150d56b5739188b'], 'ref_block_prefix': 2453073715}], 'jsonrpc': '2.0', 'id': 1}


>> call_contract_function ['nicotest', 'contract.release115say', 'contract_test', [], 'true']

{'result': ['fa67a1ef0236638b53b47d33d9a92f8078c169685c2f46f92ad256b078d160c7', {'expiration': '2020-07-23T04:10:46', 'operations': [[35, {'contract_id': '1.16.10', 'function_name': 'contract_test', 'caller': '1.2.16', 'value_list': [], 'extensions': []}]], 'extensions': [], 'ref_block_num': 5387, 'signatures': ['2067ccd22eb103f44c6f7290004df175f5e9ea02d5188dbfbf1971f56afad935885aa962a74cb204bb62d1331cb4b69937f5ea79cb3350827c3ed234d7d83926dd'], 'ref_block_prefix': 3672234824}], 'jsonrpc': '2.0', 'id': 1}


>> get_transaction_by_id ['fa67a1ef0236638b53b47d33d9a92f8078c169685c2f46f92ad256b078d160c7']

{'result': {'expiration': '2020-07-23T04:10:46', 'operation_results': [[4, {'contract_id': '1.16.10', 'existed_pv': False, 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'Hi, create contract from file'}]], 'process_value': '', 'real_running_time': 1330, 'fees': [{'amount': 3386640, 'asset_id': '1.3.1'}], 'relevant_datasize': 42}], [1, {'real_running_time': 558, 'fees': [{'amount': 100000, 'asset_id': '1.3.1'}]}]], 'operations': [[35, {'contract_id': '1.16.10', 'function_name': 'contract_test', 'caller': '1.2.16', 'value_list': [], 'extensions': []}]], 'extensions': [], 'ref_block_num': 5387, 'signatures': ['2067ccd22eb103f44c6f7290004df175f5e9ea02d5188dbfbf1971f56afad935885aa962a74cb204bb62d1331cb4b69937f5ea79cb3350827c3ed234d7d83926dd'], 'ref_block_prefix': 3672234824}, 'jsonrpc': '2.0', 'id': 1}


tx_id: fa67a1ef0236638b53b47d33d9a92f8078c169685c2f46f92ad256b078d160c7, result: [[4, {'contract_id': '1.16.10', 'existed_pv': False, 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'Hi, create contract from file'}]], 'process_value': '', 'real_running_time': 1330, 'fees': [{'amount': 3386640, 'asset_id': '1.3.1'}], 'relevant_datasize': 42}], [1, {'real_running_time': 558, 'fees': [{'amount': 100000, 'asset_id': '1.3.1'}]}]]
2. contract revise from file and call test
>> get_contract ['contract.release115say']

{'result': {'creation_date': '2020-07-23T03:50:12', 'user_invoke_share_percent': 100, 'owner': '1.2.16', 'contract_data': [], 'contract_authority': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz', 'contract_ABI': [[{'key': [2, {'v': 'contract_test'}]}, [5, {'arglist': [], 'is_var_arg': False}]]], 'lua_code_b_id': '2.2.10', 'id': '1.16.10', 'check_contract_authority': False, 'is_release': False, 'current_version': '1b8b04d8bd86643f2c888e6b8669db08e62128b35f837f2dc3ac219638173c0c', 'name': 'contract.release115say'}, 'jsonrpc': '2.0', 'id': 1}


>> revise_contract_from_file ['nicotest', 'contract.release115say', '/home/dev/data/mrepo/CocosBCX/feature_test/release1.4.5/contract_revise.lua', 'true']

{'result': ['ed2b61ae1db13f5c0f6f0139eaf4ab9ef058971c111770d5af2949d693ac2512', {'expiration': '2020-07-23T04:10:50', 'operations': [[50, {'contract_id': '1.16.10', 'reviser': '1.2.16', 'extensions': [], 'data': 'function contract_test() \tchainhelper:log("Hi, revise contract from file")  end'}]], 'extensions': [], 'ref_block_num': 5389, 'signatures': ['202993c3175ecb14a73d5c82d77a8220e643f3b7e1aac9a98995fdf82a6eafaece2508cef1f344cb4206e4995d221955a62c4ffaa69f274988423b4ead9d0f36c7'], 'ref_block_prefix': 3494198115}], 'jsonrpc': '2.0', 'id': 1}


>> call_contract_function ['nicotest', 'contract.release115say', 'contract_test', [], 'true']

{'result': ['b111e07add6a170b2ea473c4dc2ad84cf81a6d22589803340d5401a24be615ae', {'expiration': '2020-07-23T04:10:52', 'operations': [[35, {'contract_id': '1.16.10', 'function_name': 'contract_test', 'caller': '1.2.16', 'value_list': [], 'extensions': []}]], 'extensions': [], 'ref_block_num': 5389, 'signatures': ['20026523d5024e9b1600750ff0507ad8d76069b283a3d338a24ba369e0e2f806fc63e57d7811b896e4becaf634b44792f3791b96cab7b345867c953838cd999ec2'], 'ref_block_prefix': 3494198115}], 'jsonrpc': '2.0', 'id': 1}


>> get_transaction_by_id ['b111e07add6a170b2ea473c4dc2ad84cf81a6d22589803340d5401a24be615ae']

{'result': {'expiration': '2020-07-23T04:10:52', 'operation_results': [[4, {'contract_id': '1.16.10', 'existed_pv': False, 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'Hi, revise contract from file'}]], 'process_value': '', 'real_running_time': 1314, 'fees': [{'amount': 3370640, 'asset_id': '1.3.1'}], 'relevant_datasize': 42}]], 'operations': [[35, {'contract_id': '1.16.10', 'function_name': 'contract_test', 'caller': '1.2.16', 'value_list': [], 'extensions': []}]], 'extensions': [], 'ref_block_num': 5389, 'signatures': ['20026523d5024e9b1600750ff0507ad8d76069b283a3d338a24ba369e0e2f806fc63e57d7811b896e4becaf634b44792f3791b96cab7b345867c953838cd999ec2'], 'ref_block_prefix': 3494198115}, 'jsonrpc': '2.0', 'id': 1}


tx_id: b111e07add6a170b2ea473c4dc2ad84cf81a6d22589803340d5401a24be615ae, result: [[4, {'contract_id': '1.16.10', 'existed_pv': False, 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'Hi, revise contract from file'}]], 'process_value': '', 'real_running_time': 1314, 'fees': [{'amount': 3370640, 'asset_id': '1.3.1'}], 'relevant_datasize': 42}]]
release_cli_wallet_api done

# vote function test
# 1. test cli_wallet api: get_global_extensions_properties
>> get_global_extensions_properties []

{'result': {'contract_max_data_size': 2147483648, 'id': '2.15.0', 'witness_max_votes': 7, 'contract_total_data_size': 10485760, 'contract_private_data_size': 3072, 'committee_max_votes': 9}, 'jsonrpc': '2.0', 'id': 1}


# 2. test chain_api_get_global_property_extensions
>> call [0, 'get_global_property_extensions', [[]]]

{'result': {'contract_max_data_size': 2147483648, 'id': '2.15.0', 'witness_max_votes': 7, 'contract_total_data_size': 10485760, 'contract_private_data_size': 3072, 'committee_max_votes': 9}, 'jsonrpc': '2.0', 'id': 1}



# 3. test vote for witness
>> get_object ['2.15.0']

{'result': [{'contract_max_data_size': 2147483648, 'id': '2.15.0', 'witness_max_votes': 7, 'contract_total_data_size': 10485760, 'contract_private_data_size': 3072, 'committee_max_votes': 9}], 'jsonrpc': '2.0', 'id': 1}


[{'contract_max_data_size': 2147483648, 'id': '2.15.0', 'witness_max_votes': 7, 'contract_total_data_size': 10485760, 'contract_private_data_size': 3072, 'committee_max_votes': 9}]
>> list_witnesses ['', 8]

{'result': [['init0', '1.6.1'], ['init1', '1.6.2'], ['init10', '1.6.11'], ['init2', '1.6.3'], ['init3', '1.6.4'], ['init4', '1.6.5'], ['init5', '1.6.6'], ['init6', '1.6.7']], 'jsonrpc': '2.0', 'id': 1}


witnesses: [['init0', '1.6.1'], ['init1', '1.6.2'], ['init10', '1.6.11'], ['init2', '1.6.3'], ['init3', '1.6.4'], ['init4', '1.6.5'], ['init5', '1.6.6'], ['init6', '1.6.7']]
>> list_account_balances ['nicotest']

{'result': [{'amount': '9779869040028567', 'asset_id': '1.3.0'}, {'amount': '196055530812', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}


[{'amount': '9779869040028567', 'asset_id': '1.3.0'}, {'amount': '196055530812', 'asset_id': '1.3.1'}]
>> vote_for_witness ['nicotest', 'init0', 7, True]

{'result': ['2a20077d417458061a550ff74744ce2c4cc99d963cbcf748cbb3f5a0a81b1904', {'expiration': '2020-07-23T04:10:58', 'operations': [[6, {'lock_with_vote': [1, {'amount': 7, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['1:0'], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5394, 'signatures': ['1f53c0c7d658c94369bad13e75d021e30da5f068453561676c4d098318e3205ebb65beeee16a7f302d113824667d3a3ea5a4e600160122cf8f33adfc12e5dbc816'], 'ref_block_prefix': 3234396664}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_witness ['nicotest', 'init1', 8, True]

{'result': ['b6a7d6dfc7ee259eccc9fb6da75ed61b8567e3d5a9a516e82ef791e52530e875', {'expiration': '2020-07-23T04:10:58', 'operations': [[6, {'lock_with_vote': [1, {'amount': 8, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['1:0', '1:1'], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5394, 'signatures': ['1f7e31aac751002e04df631ac850717342aa999009449cab6c6f70ceeb56b99cb40e07422a7d44761c982812023e4dabbce1f290e52f3f02d43f30581befd2aae4'], 'ref_block_prefix': 3234396664}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_witness ['nicotest', 'init10', 1, True]

{'result': ['0a57776f69c43be727122e409d150a40a508da1b1d0fb0631328facb9fa91efd', {'expiration': '2020-07-23T04:10:58', 'operations': [[6, {'lock_with_vote': [1, {'amount': 1, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['1:0', '1:1', '1:10'], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5394, 'signatures': ['206ba2adeebd56204c194ede5cdbf392d8d94b5b39fd8c119865649a4e6e537ed156a269e26c4d76d71b90ba8d1f4ca3ed8ec54d5296901e3fba4e72fe4e42e0b9'], 'ref_block_prefix': 3234396664}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_witness ['nicotest', 'init2', 12, True]

{'result': ['218b3cf49453fd5a4b265efd8c74b929a2c0d224adcd41a03812794d9cccb27a', {'expiration': '2020-07-23T04:10:58', 'operations': [[6, {'lock_with_vote': [1, {'amount': 12, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['1:0', '1:1', '1:2', '1:10'], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5394, 'signatures': ['1f180f9bd3c5f71251d490a6cea2fa756bdd57ad443016bde602474841a6a5b52877ccc4b216e8a4d63366f334067c14f0dfcd3f0849736814d28731bc679fa3da'], 'ref_block_prefix': 3234396664}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_witness ['nicotest', 'init3', 1, True]

{'result': ['43260bea4a6ee9ebc8a1e170140ef4510578f40e3bdd5ab3257d048669d9033e', {'expiration': '2020-07-23T04:10:58', 'operations': [[6, {'lock_with_vote': [1, {'amount': 1, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['1:0', '1:1', '1:2', '1:3', '1:10'], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5394, 'signatures': ['1f753efab7e8f4373502e301e38a6097ec6855095bdce89884555a597f8b581765177b960bcb2ac82e96e44a2f0663e1efc3dd1732f3d06297acbe26a976aae993'], 'ref_block_prefix': 3234396664}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_witness ['nicotest', 'init4', 20, True]

{'result': ['cb949ce688e5a3afc39394b9340a686fd76ff8051496cdd1a162cf6dfabe3734', {'expiration': '2020-07-23T04:10:58', 'operations': [[6, {'lock_with_vote': [1, {'amount': 20, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['1:0', '1:1', '1:2', '1:3', '1:4', '1:10'], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5394, 'signatures': ['1f31b422aac8ab71bdb7df529d68a0b9018a56be5574f98ddfe21db6e34c5577be559684fd69eb6309186903dc7ca806bf582333222d3c174b98c8cdd8b0a36859'], 'ref_block_prefix': 3234396664}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_witness ['nicotest', 'init5', 10, True]

{'result': ['53ee764cedfb8af8c429d4c22eefaa5e33de99ee133538c088a856d3e3a585ae', {'expiration': '2020-07-23T04:10:58', 'operations': [[6, {'lock_with_vote': [1, {'amount': 10, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['1:0', '1:1', '1:2', '1:3', '1:4', '1:5', '1:10'], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5394, 'signatures': ['20252c62f500b7552dae4b263390f6787c929168b6f513a6f6edbf842ef4b20468345fd2e35ce4c0fafc05ece2e50f33c1dff3d97e031736ac1ebd60cd464cc121'], 'ref_block_prefix': 3234396664}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_witness ['nicotest', 'init6', 10, True]

{'jsonrpc': '2.0', 'error': {'code': 1, 'message': 'unspecified: Assert Exception: num_witness <= witness_number_of_vote: Voted for more witnesses than currently allowed (7)'}, 'id': 1}


AssertionError()

# 4. test vote for committee
>> get_object ['2.15.0']

{'result': [{'contract_max_data_size': 2147483648, 'id': '2.15.0', 'witness_max_votes': 7, 'contract_total_data_size': 10485760, 'contract_private_data_size': 3072, 'committee_max_votes': 9}], 'jsonrpc': '2.0', 'id': 1}


[{'contract_max_data_size': 2147483648, 'id': '2.15.0', 'witness_max_votes': 7, 'contract_total_data_size': 10485760, 'contract_private_data_size': 3072, 'committee_max_votes': 9}]
>> list_committee_members ['', 10]

{'result': [['init0', '1.5.0'], ['init1', '1.5.1'], ['init10', '1.5.10'], ['init2', '1.5.2'], ['init3', '1.5.3'], ['init4', '1.5.4'], ['init5', '1.5.5'], ['init6', '1.5.6'], ['init7', '1.5.7'], ['init8', '1.5.8']], 'jsonrpc': '2.0', 'id': 1}


committees: [['init0', '1.5.0'], ['init1', '1.5.1'], ['init10', '1.5.10'], ['init2', '1.5.2'], ['init3', '1.5.3'], ['init4', '1.5.4'], ['init5', '1.5.5'], ['init6', '1.5.6'], ['init7', '1.5.7'], ['init8', '1.5.8']]
>> list_account_balances ['nicotest']

{'result': [{'amount': '9779869040028539', 'asset_id': '1.3.0'}, {'amount': '196041473393', 'asset_id': '1.3.1'}], 'jsonrpc': '2.0', 'id': 1}


[{'amount': '9779869040028539', 'asset_id': '1.3.0'}, {'amount': '196041473393', 'asset_id': '1.3.1'}]
>> vote_for_committee_member ['nicotest', 'init0', 14, True]

{'result': ['1c2cad12032e43aa0ce2b5370f483e68734a14770f27e27c4d92169069bf3f69', {'expiration': '2020-07-23T04:10:58', 'operations': [[6, {'lock_with_vote': [0, {'amount': 14, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['0:11'], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5394, 'signatures': ['202df4f6b52108ecd388fe36dbe090b4af458ef17da4fe8650f7bfd21a0c66a68a1ab10d7d9be51c7cbdefafaae7b1c89c78660b8731f09b80d890221fe3410561'], 'ref_block_prefix': 3234396664}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_committee_member ['nicotest', 'init1', 13, True]

{'result': ['63ba1a700ffdce6f8b9ac5360fff7814141b50c85fa2b71a0d4abb0a57f4ac6c', {'expiration': '2020-07-23T04:10:58', 'operations': [[6, {'lock_with_vote': [0, {'amount': 13, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['0:11', '0:12'], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5394, 'signatures': ['201e8add0d88b7bea6c24b7151b950fc103f47c0ef9312289e5f0200807e10e2112265a0ff26737c8d7a922177fb624c20e4ddb43ffc0778fa78dbf6e7e172fe95'], 'ref_block_prefix': 3234396664}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_committee_member ['nicotest', 'init10', 14, True]

{'result': ['8178e5e6d7a6929657a5ce3c6c4c777a36b908116b23551d134ae9aedda52223', {'expiration': '2020-07-23T04:10:58', 'operations': [[6, {'lock_with_vote': [0, {'amount': 14, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['0:11', '0:12', '0:21'], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5394, 'signatures': ['1f3385667e0ce57ca919d84893ad67d6fa6ec12850df1e3dc50fede797fd2717bb272d87c1720835ed39d22831d87682251c0e60ccec24c9b2ce9c1afb29492aab'], 'ref_block_prefix': 3234396664}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_committee_member ['nicotest', 'init2', 20, True]

{'result': ['6ac0519a63a6b768c574a48e2827909fbdacb2dbda987a9b897522e596ec4f75', {'expiration': '2020-07-23T04:10:58', 'operations': [[6, {'lock_with_vote': [0, {'amount': 20, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['0:11', '0:12', '0:13', '0:21'], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5394, 'signatures': ['207b690e2e5f65fea2b387db508879ec618578f9cbe788131e815d83c13503fd9f61e874987614a536fdda9081e4feb1895d0f9be52fec8e0e23ea1bd44ad39b3f'], 'ref_block_prefix': 3234396664}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_committee_member ['nicotest', 'init3', 8, True]

{'result': ['c3c8ecafe0d70cef0866098f03c4a1ff218b0b8d4db076aa9569567b9e565373', {'expiration': '2020-07-23T04:10:58', 'operations': [[6, {'lock_with_vote': [0, {'amount': 8, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['0:11', '0:12', '0:13', '0:14', '0:21'], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5394, 'signatures': ['1f0726b3c4417062996c80453768524d5eca5a6589c7ae972af08eaa811a4b12462ee764e233c7a34c17398b809d91d92a298f813a45d164702c903a484667fe2e'], 'ref_block_prefix': 3234396664}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_committee_member ['nicotest', 'init4', 2, True]

{'result': ['001e5e2314fd2ca820c3b24470f4e7ac48bd4289b0a061fc9086e42d6f317b79', {'expiration': '2020-07-23T04:10:58', 'operations': [[6, {'lock_with_vote': [0, {'amount': 2, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['0:11', '0:12', '0:13', '0:14', '0:15', '0:21'], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5394, 'signatures': ['2048d8239b03987baa163afcb06f607f0a380a7b8f048bfc3822828452bc98edd60b3037515c647c1da387fce0ad60e627a3f54a9234d2e0ccad7b6592e173dc8c'], 'ref_block_prefix': 3234396664}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_committee_member ['nicotest', 'init5', 12, True]

{'result': ['c3b811f8a5c44d38cce3a68585ea396e6494fbd598da359b2dfa6b1fa9a8603e', {'expiration': '2020-07-23T04:10:58', 'operations': [[6, {'lock_with_vote': [0, {'amount': 12, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['0:11', '0:12', '0:13', '0:14', '0:15', '0:16', '0:21'], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5394, 'signatures': ['1f1aaeb77509f41bd890eb58b8f15011f92b1e2561fc2b4f6e521b524631e27642498d5c5616c69f9c7e65154298c2e346049c0f93722431ff81196852b3174bf8'], 'ref_block_prefix': 3234396664}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_committee_member ['nicotest', 'init6', 7, True]

{'result': ['b601e1e17846225d49f832eaeaa6cc9135a8d249259af55fa5d10f9b0b09d3f8', {'expiration': '2020-07-23T04:10:58', 'operations': [[6, {'lock_with_vote': [0, {'amount': 7, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['0:11', '0:12', '0:13', '0:14', '0:15', '0:16', '0:17', '0:21'], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5394, 'signatures': ['1f31712073aa43ca76533935cc14ed5f98cd450e9bd9addcb9b10b8b4f57901b2d342dada4f3a3fb34fc00d104fa5517778822f1b034ad25dd7769205cd4f9dd4f'], 'ref_block_prefix': 3234396664}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_committee_member ['nicotest', 'init7', 15, True]

{'result': ['fa594fc3953e52cab93c00224c919f923ab003b3a9112274c5984d840363664a', {'expiration': '2020-07-23T04:10:58', 'operations': [[6, {'lock_with_vote': [0, {'amount': 15, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': ['0:11', '0:12', '0:13', '0:14', '0:15', '0:16', '0:17', '0:18', '0:21'], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5394, 'signatures': ['1f27661cc36102b93a79368655711f390336c69ab19c608b2960d285a0c58a12e644bce2b587ba4851a93976a3320a4a75321859c7d29dcc3e9129eb86a8f98824'], 'ref_block_prefix': 3234396664}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_committee_member ['nicotest', 'init8', 4, True]

{'jsonrpc': '2.0', 'error': {'code': 1, 'message': 'unspecified: Assert Exception: num_committee <= committee_number_of_vote: Voted for more committee members than currently allowed (9)'}, 'id': 1}


AssertionError()

# 5. test cancle vote for witness
>> vote_for_witness ['nicotest', 'init0', 0, True]

{'result': ['7768740c2019165612be00f95eb91a9a71fbed64a0398d82b2b9e5d4049d9e4c', {'expiration': '2020-07-23T04:11:08', 'operations': [[6, {'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['1f14e04c214a40810d9b4bba0f6f4ebc0e863e5115540b9a281e41f1861f0a2e6c696f25878f0cdce6fc260f54d81d30ff7d26c5c45d7a8ad51194fc382b7610d5'], 'ref_block_prefix': 4127874371}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_witness ['nicotest', 'init1', 0, True]

{'result': ['bb6731f0ffbfaf608487dca007b63cc006b99a6a3724ad13cfb6debb0c53e101', {'expiration': '2020-07-23T04:11:09', 'operations': [[6, {'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['1f36bce5cd51512f8486b9f833048f6c04aab8fc914e8625e4b83a5ba8114abbe40bb52991d1bfa2f000cc5c9ae305621964b4042772720640d2f1f5a14544a933'], 'ref_block_prefix': 4127874371}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_witness ['nicotest', 'init10', 0, True]

{'result': ['ec5e2c12ed8a63daeaa826e7cb469d487693e36e72f91112b85ee10adfd1359c', {'expiration': '2020-07-23T04:11:10', 'operations': [[6, {'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['202d2f13ebf4538b4c08818c89df7981f0274b0e3c8af33257e9cad6c085c3174f1d1f06e0f0d80e667b1965b164a98cf795103f965d2c170e855a2f2bf774ef3e'], 'ref_block_prefix': 4127874371}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_witness ['nicotest', 'init2', 0, True]

{'result': ['83f310729c29f3d69fd47c1ec97c57b4843319981613844166bcc63d48d46442', {'expiration': '2020-07-23T04:11:11', 'operations': [[6, {'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['207593470c9f3e835ccdaec11b36a75fd2b24ddbd7e2e6818715e95b059f96b5a8482ebf129908cd79dfb8bb0112b508740d66fb3f3dc9d43e8de94e6e4df098f2'], 'ref_block_prefix': 4127874371}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_witness ['nicotest', 'init3', 0, True]

{'result': ['47ee7cf0f6e40bfa16f3b4f2210b5dd0d2b142f57f65b408fd152bd0edd7fd2f', {'expiration': '2020-07-23T04:11:12', 'operations': [[6, {'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['204af11cf71de50b5156b7845159820e312e15ed1bfe263f1795dcf5c5c7d704511285e05bb54d4a8549ab48f8f4a26fe52bbcde8a5033477d8d3fd35040e1990d'], 'ref_block_prefix': 4127874371}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_witness ['nicotest', 'init4', 0, True]

{'result': ['8338195a1f83dcb90bcb000b874ebd4f14a827f3ff3b175787dc12f3664ca4bd', {'expiration': '2020-07-23T04:11:13', 'operations': [[6, {'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['1f576fa3fe02e6b629e82f7b3bcb0997e88c80ecf9ca5e6a2ec04b4f5bcf032b5334a77cdef54693443d8f1281949d3de08b08fec240cd86971d34cdb64d140c32'], 'ref_block_prefix': 4127874371}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_witness ['nicotest', 'init5', 0, True]

{'result': ['eb612699ce83b20d1e0a16645e527ba08cc69e5cf5913613ac9b871ce54d5720', {'expiration': '2020-07-23T04:11:14', 'operations': [[6, {'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['202c8953dd2199310b46ad0648b4cae4ec800261771fcf9078b2f11940deb2deee177e71baceae976ed2f1797a0e661193ddf351346b3fe7a23d5c601321c1e390'], 'ref_block_prefix': 4127874371}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_witness ['nicotest', 'init6', 0, True]

{'result': ['3a661f4e2411c700881a90bcfc11541f60ffca959958361984a42398f34e8796', {'expiration': '2020-07-23T04:11:15', 'operations': [[6, {'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['1f4d43264384a08c1eda21d4cbd72654b197a68cf4536bbaf1a07552d3f0d29ca343d328381a26031a4a8dae9456f55fb6960339d45457116d15592c7203528db4'], 'ref_block_prefix': 4127874371}], 'jsonrpc': '2.0', 'id': 1}



# 6. test  cancle vote for committee
>> vote_for_committee_member ['nicotest', 'init0', 0, True]

{'result': ['1cdb56aefbf9824689d101863e41314631a5162a26089f2042c888f59c9fe3b4', {'expiration': '2020-07-23T04:11:08', 'operations': [[6, {'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['1f1fc388e9c8616018f0136d74ef06c296e887fd21caa509a2cadc35d3606c06a963100940b5a1e03367e850fec792e5c3c8bbaf9ea4421eb9f7a2197f94ee28c8'], 'ref_block_prefix': 4127874371}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_committee_member ['nicotest', 'init1', 0, True]

{'result': ['865f562a26cc00bb0d7ec4aaf59f445ab011caa4166c03a7a759c3b2db19e473', {'expiration': '2020-07-23T04:11:09', 'operations': [[6, {'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['1f115baa441bd6a5c8704d2f74455a0a2bd113847c749920c88ea97471242257c540c8e5cc523b44b0d8e6aa1353f37d493e55564537258d46d14e043cc90fd3a3'], 'ref_block_prefix': 4127874371}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_committee_member ['nicotest', 'init10', 0, True]

{'result': ['9b2dc8e07e21ea404744a6eb860a75693db1088549cb78291dc4a4ae701feaec', {'expiration': '2020-07-23T04:11:10', 'operations': [[6, {'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['20107a08c03edf54ea390363a0dfeccbf62e454bc55e827cd30d61b73342eb8fc353ca5106a3241f16f1d2a86d952178f0f8157e4b88b919d69eb045f1975c3fc9'], 'ref_block_prefix': 4127874371}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_committee_member ['nicotest', 'init2', 0, True]

{'result': ['efeb84544aee62d610ba26cc813a6ff4bc6648acf2a6686371d76ea427cf55d6', {'expiration': '2020-07-23T04:11:11', 'operations': [[6, {'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['20149a25457a99868d41101bf37bc69d3ae2ed6c76e7fb68a59a3817ac90c88f4d0cde4576738bbaa7e09435215fdd1b19bb49869a00088d1708a1a1f1abc9e23c'], 'ref_block_prefix': 4127874371}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_committee_member ['nicotest', 'init3', 0, True]

{'result': ['64f8e92d499573918d10044f6b47ada0b5d16028f828d01a60af91e39be58a1c', {'expiration': '2020-07-23T04:11:12', 'operations': [[6, {'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['1f4cb765afbebd6ed37c135dc6b08e9efda3d039d6cb1cc2dbfcc54ebc2795281f76c8a9d77c4a8cf5e1ee4f1f6fab5a5586191edb84c74a9750d0d0e514fa5ec7'], 'ref_block_prefix': 4127874371}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_committee_member ['nicotest', 'init4', 0, True]

{'result': ['4f6601ab9eeda2c3610aec6969c426c0b7dcc7ce4b240d484d1cfb70e2e63f25', {'expiration': '2020-07-23T04:11:13', 'operations': [[6, {'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['2002b104cf5ec34f111a3f95d91d4c6c41086f5d0a209376960dfad05404565a821dd07e3587c268f7fba3dd7defc1d5949e97f1bad3944470034520b8ba2416bd'], 'ref_block_prefix': 4127874371}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_committee_member ['nicotest', 'init5', 0, True]

{'result': ['0779fd06ab3bae72eb16d329b2f5219f120f1367b8f810fe7e445451a21686a1', {'expiration': '2020-07-23T04:11:14', 'operations': [[6, {'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['204ef1693645ba00953a0547f87687eb208901d8b939f78fd8612afe3cfa182a8175478ba83185890eb1fb7ffeb76c739f4cbcdc7952ab427b6a05f0df56b7b911'], 'ref_block_prefix': 4127874371}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_committee_member ['nicotest', 'init6', 0, True]

{'result': ['08c72b4bf225dbeeca14da09b510a06bed6621a0f2f12df4aae1da5d84880b72', {'expiration': '2020-07-23T04:11:15', 'operations': [[6, {'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['2063c4aba05f9a4a61b0dd3d5ff90681096cfe4d53f800b768c382eb5de5943b9733ead6c446c8cb2f918ff3a15f1bbc062c236e8d99e3702644bd8085aadab901'], 'ref_block_prefix': 4127874371}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_committee_member ['nicotest', 'init7', 0, True]

{'result': ['b75c3a655731ad2aa0953fec51f8f0e1080910c8bd4d7bc41b0adfe4c54108d3', {'expiration': '2020-07-23T04:11:16', 'operations': [[6, {'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['1f3f2c55343e2c6889ece90f1e9ad8e8034848b47508d2fc35a9562d4e9bda79ac77265b3d8e5c20c83a25bd1e63b2a084e695e3dbab57c3f8a5425024b2e1efa9'], 'ref_block_prefix': 4127874371}], 'jsonrpc': '2.0', 'id': 1}


>> vote_for_committee_member ['nicotest', 'init8', 0, True]

{'result': ['04751a6ecf92d4518513c0d0b644df65a4a1baf9c80d8450254433772b64982a', {'expiration': '2020-07-23T04:11:17', 'operations': [[6, {'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'account': '1.2.16', 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'votes': [], 'extensions': []}, 'extensions': {}}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['205a810f8fb1ee640cccc51475a1e16445c8b17180e9c3dac727823fe4122ca6d96850c46465acef2241aade22db7fb9cfa3a1806e5a3d4ddb6139a1c13555e1a3'], 'ref_block_prefix': 4127874371}], 'jsonrpc': '2.0', 'id': 1}


test vote for xxx done
# contract api test
contract_name: contract.release115.gcpdsnp, test account: nicotest
1. create contract from file and call test
>> get_contract ['contract.release115.gcpdsnp']

{'jsonrpc': '2.0', 'error': {'code': 1, 'message': 'unspecified: Assert Exception: contract_itr != con_index.end(): The contract (contract.release115.gcpdsnp) does not exist'}, 'id': 1}


>> create_contract_from_file ['nicotest', 'contract.release115.gcpdsnp', 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz', '/home/dev/data/mrepo/CocosBCX/feature_test/release1.4.5/contract_api_get_contract_public_data.lua', 'true']

{'result': ['1327cef44b928a17bcbe172058b2807a7f165ad5a8c8845485558373cc7c6ad9', {'expiration': '2020-07-23T04:11:08', 'operations': [[34, {'owner': '1.2.16', 'extensions': [], 'contract_authority': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz', 'name': 'contract.release115.gcpdsnp', 'data': 'function init()     read_list = {         public_data = {             is_init = true         }     }     chainhelper:read_chain();      public_data.userdata = {};     public_data.is_init = true;      write_list = {         public_data = {}     }     chainhelper:write_chain(); end  function insert(id, name)     read_list = {         public_data = {userdata=true}     }     chainhelper:read_chain()      local userdata = public_data.userdata;     userdata[id] = name     public_data.userdata = userdata      write_list = {         public_data = {userdata=true}     }     chainhelper:write_chain(); end  function test(name_or_id)      data = chainhelper:get_contract_public_data(name_or_id)      jsonStr = cjson.encode(data)     chainhelper:log("contract: " .. name_or_id .. ", public_data: " .. jsonStr) end'}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['205286adeb304cfc2a89cb36daebe45559ed7202955d19b68fedad37c1d20395c4475b893198902ab95baa2e64bb74e9e43631382dc2320b8dbbd929516f01e184'], 'ref_block_prefix': 4127874371}], 'jsonrpc': '2.0', 'id': 1}


>> call_contract_function ['nicotest', 'contract.release115.gcpdsnp', 'init', [], 'true']

{'result': ['afa016b566decec4b69fcba2ff177f9494f659af0763c63188a11b972def9591', {'expiration': '2020-07-23T04:11:12', 'operations': [[35, {'contract_id': '1.16.11', 'function_name': 'init', 'caller': '1.2.16', 'value_list': [], 'extensions': []}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['204026e81382077564f246e0e8ffebb1e612563b12103ff0e2c89a357cfde4dc2c15c1dbbb99bfe8301e8862060db337de3df17b711945ab2f37d0f5998cf224c0'], 'ref_block_prefix': 4127874371}], 'jsonrpc': '2.0', 'id': 1}


>> get_transaction_by_id ['afa016b566decec4b69fcba2ff177f9494f659af0763c63188a11b972def9591']

{'result': {'expiration': '2020-07-23T04:11:12', 'operation_results': [[4, {'contract_id': '1.16.11', 'existed_pv': False, 'contract_affecteds': [], 'process_value': '', 'real_running_time': 1722, 'fees': [{'amount': 3754225, 'asset_id': '1.3.1'}], 'relevant_datasize': 26}]], 'operations': [[35, {'contract_id': '1.16.11', 'function_name': 'init', 'caller': '1.2.16', 'value_list': [], 'extensions': []}]], 'extensions': [], 'ref_block_num': 5397, 'signatures': ['204026e81382077564f246e0e8ffebb1e612563b12103ff0e2c89a357cfde4dc2c15c1dbbb99bfe8301e8862060db337de3df17b711945ab2f37d0f5998cf224c0'], 'ref_block_prefix': 4127874371}, 'jsonrpc': '2.0', 'id': 1}


tx_id: afa016b566decec4b69fcba2ff177f9494f659af0763c63188a11b972def9591, result: [[4, {'contract_id': '1.16.11', 'existed_pv': False, 'contract_affecteds': [], 'process_value': '', 'real_running_time': 1722, 'fees': [{'amount': 3754225, 'asset_id': '1.3.1'}], 'relevant_datasize': 26}]]
>> call_contract_function ['nicotest', 'contract.release115.gcpdsnp', 'insert', [[2, {'v': '00550'}], [2, {'v': 'zhang_550'}]], 'true']

{'result': ['5f6cbac49e5678a6d0a0ec7be4ab2214080edf70cfd329622eb497ec40f5ae53', {'expiration': '2020-07-23T04:11:16', 'operations': [[35, {'contract_id': '1.16.11', 'function_name': 'insert', 'caller': '1.2.16', 'value_list': [[2, {'v': '00550'}], [2, {'v': 'zhang_550'}]], 'extensions': []}]], 'extensions': [], 'ref_block_num': 5400, 'signatures': ['20293d7b580c02427522a818368cb3bbfc6f28b425f0897a38d75415f78870ba4d07d435b25b560d20dd8e8544a05fd0025e2dc08511fb2ce372658a33d1caa3bd'], 'ref_block_prefix': 4269821113}], 'jsonrpc': '2.0', 'id': 1}


>> get_transaction_by_id ['5f6cbac49e5678a6d0a0ec7be4ab2214080edf70cfd329622eb497ec40f5ae53']

{'result': {'expiration': '2020-07-23T04:11:16', 'operation_results': [[4, {'contract_id': '1.16.11', 'existed_pv': False, 'contract_affecteds': [], 'process_value': '', 'real_running_time': 1920, 'fees': [{'amount': 3989335, 'asset_id': '1.3.1'}], 'relevant_datasize': 44}]], 'operations': [[35, {'contract_id': '1.16.11', 'function_name': 'insert', 'caller': '1.2.16', 'value_list': [[2, {'v': '00550'}], [2, {'v': 'zhang_550'}]], 'extensions': []}]], 'extensions': [], 'ref_block_num': 5400, 'signatures': ['20293d7b580c02427522a818368cb3bbfc6f28b425f0897a38d75415f78870ba4d07d435b25b560d20dd8e8544a05fd0025e2dc08511fb2ce372658a33d1caa3bd'], 'ref_block_prefix': 4269821113}, 'jsonrpc': '2.0', 'id': 1}


tx_id: 5f6cbac49e5678a6d0a0ec7be4ab2214080edf70cfd329622eb497ec40f5ae53, result: [[4, {'contract_id': '1.16.11', 'existed_pv': False, 'contract_affecteds': [], 'process_value': '', 'real_running_time': 1920, 'fees': [{'amount': 3989335, 'asset_id': '1.3.1'}], 'relevant_datasize': 44}]]
>> call_contract_function ['nicotest', 'contract.release115.gcpdsnp', 'insert', [[2, {'v': '00786'}], [2, {'v': 'zhang_786'}]], 'true']

{'result': ['a95cf722deab82eebbfad19d6de34922bc0b73045369c5dbb3f0129e099a462d', {'expiration': '2020-07-23T04:11:20', 'operations': [[35, {'contract_id': '1.16.11', 'function_name': 'insert', 'caller': '1.2.16', 'value_list': [[2, {'v': '00786'}], [2, {'v': 'zhang_786'}]], 'extensions': []}]], 'extensions': [], 'ref_block_num': 5404, 'signatures': ['1f3eb8fcf9359870df791ff162fede77d11b974c0e164d9078d0eb2ee55a0f35bf6a9fd743a9be849922745178a3b3411de190763f99d5b7d7e05d61358b8fffb7'], 'ref_block_prefix': 305331986}], 'jsonrpc': '2.0', 'id': 1}


>> get_transaction_by_id ['a95cf722deab82eebbfad19d6de34922bc0b73045369c5dbb3f0129e099a462d']

{'result': {'expiration': '2020-07-23T04:11:20', 'operation_results': [[4, {'contract_id': '1.16.11', 'existed_pv': False, 'contract_affecteds': [], 'process_value': '', 'real_running_time': 2001, 'fees': [{'amount': 4087913, 'asset_id': '1.3.1'}], 'relevant_datasize': 62}]], 'operations': [[35, {'contract_id': '1.16.11', 'function_name': 'insert', 'caller': '1.2.16', 'value_list': [[2, {'v': '00786'}], [2, {'v': 'zhang_786'}]], 'extensions': []}]], 'extensions': [], 'ref_block_num': 5404, 'signatures': ['1f3eb8fcf9359870df791ff162fede77d11b974c0e164d9078d0eb2ee55a0f35bf6a9fd743a9be849922745178a3b3411de190763f99d5b7d7e05d61358b8fffb7'], 'ref_block_prefix': 305331986}, 'jsonrpc': '2.0', 'id': 1}


tx_id: a95cf722deab82eebbfad19d6de34922bc0b73045369c5dbb3f0129e099a462d, result: [[4, {'contract_id': '1.16.11', 'existed_pv': False, 'contract_affecteds': [], 'process_value': '', 'real_running_time': 2001, 'fees': [{'amount': 4087913, 'asset_id': '1.3.1'}], 'relevant_datasize': 62}]]
>> get_contract ['contract.release115.gcpdsnp']

{'result': {'creation_date': '2020-07-23T03:50:38', 'user_invoke_share_percent': 100, 'owner': '1.2.16', 'contract_data': [[{'key': [2, {'v': 'is_init'}]}, [3, {'v': True}]], [{'key': [2, {'v': 'userdata'}]}, [4, {'v': [[{'key': [2, {'v': '00550'}]}, [2, {'v': 'zhang_550'}]], [{'key': [2, {'v': '00786'}]}, [2, {'v': 'zhang_786'}]]]}]]], 'contract_authority': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz', 'contract_ABI': [[{'key': [2, {'v': 'init'}]}, [5, {'arglist': [], 'is_var_arg': False}]], [{'key': [2, {'v': 'insert'}]}, [5, {'arglist': ['id', 'name'], 'is_var_arg': False}]], [{'key': [2, {'v': 'test'}]}, [5, {'arglist': ['name_or_id'], 'is_var_arg': False}]]], 'lua_code_b_id': '2.2.11', 'id': '1.16.11', 'check_contract_authority': False, 'is_release': False, 'current_version': '1327cef44b928a17bcbe172058b2807a7f165ad5a8c8845485558373cc7c6ad9', 'name': 'contract.release115.gcpdsnp'}, 'jsonrpc': '2.0', 'id': 1}


{'creation_date': '2020-07-23T03:50:38', 'user_invoke_share_percent': 100, 'owner': '1.2.16', 'contract_data': [[{'key': [2, {'v': 'is_init'}]}, [3, {'v': True}]], [{'key': [2, {'v': 'userdata'}]}, [4, {'v': [[{'key': [2, {'v': '00550'}]}, [2, {'v': 'zhang_550'}]], [{'key': [2, {'v': '00786'}]}, [2, {'v': 'zhang_786'}]]]}]]], 'contract_authority': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz', 'contract_ABI': [[{'key': [2, {'v': 'init'}]}, [5, {'arglist': [], 'is_var_arg': False}]], [{'key': [2, {'v': 'insert'}]}, [5, {'arglist': ['id', 'name'], 'is_var_arg': False}]], [{'key': [2, {'v': 'test'}]}, [5, {'arglist': ['name_or_id'], 'is_var_arg': False}]]], 'lua_code_b_id': '2.2.11', 'id': '1.16.11', 'check_contract_authority': False, 'is_release': False, 'current_version': '1327cef44b928a17bcbe172058b2807a7f165ad5a8c8845485558373cc7c6ad9', 'name': 'contract.release115.gcpdsnp'}
>> call_contract_function ['nicotest', 'contract.release115.gcpdsnp', 'test', [[2, {'v': 'contract.release115.gcpdsnp'}]], 'true']

{'result': ['3f3502d0ea085b0d10ab64c52a4a16ff6332bdfc7ab74b037117552c65e12366', {'expiration': '2020-07-23T04:11:28', 'operations': [[35, {'contract_id': '1.16.11', 'function_name': 'test', 'caller': '1.2.16', 'value_list': [[2, {'v': 'contract.release115.gcpdsnp'}]], 'extensions': []}]], 'extensions': [], 'ref_block_num': 5408, 'signatures': ['20479034898cc50b96ec76d794e563c98422c9321806398dbb1005943d647111aa35ba5408f482bb2861c5c6c6ac56a924985f60fd3633857c67a16fc340bcc8d6'], 'ref_block_prefix': 2318199279}], 'jsonrpc': '2.0', 'id': 1}


>> get_transaction_by_id ['3f3502d0ea085b0d10ab64c52a4a16ff6332bdfc7ab74b037117552c65e12366']

{'result': {'expiration': '2020-07-23T04:11:28', 'operation_results': [[4, {'contract_id': '1.16.11', 'existed_pv': False, 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'contract: contract.release115.gcpdsnp, public_data: {"userdata":{"00786":"zhang_786","00550":"zhang_550"},"is_init":true}'}]], 'process_value': '', 'real_running_time': 1638, 'fees': [{'amount': 3861632, 'asset_id': '1.3.1'}], 'relevant_datasize': 193}], [1, {'real_running_time': 543, 'fees': [{'amount': 100000, 'asset_id': '1.3.1'}]}]], 'operations': [[35, {'contract_id': '1.16.11', 'function_name': 'test', 'caller': '1.2.16', 'value_list': [[2, {'v': 'contract.release115.gcpdsnp'}]], 'extensions': []}]], 'extensions': [], 'ref_block_num': 5408, 'signatures': ['20479034898cc50b96ec76d794e563c98422c9321806398dbb1005943d647111aa35ba5408f482bb2861c5c6c6ac56a924985f60fd3633857c67a16fc340bcc8d6'], 'ref_block_prefix': 2318199279}, 'jsonrpc': '2.0', 'id': 1}


tx_id: 3f3502d0ea085b0d10ab64c52a4a16ff6332bdfc7ab74b037117552c65e12366, result: [[4, {'contract_id': '1.16.11', 'existed_pv': False, 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'contract: contract.release115.gcpdsnp, public_data: {"userdata":{"00786":"zhang_786","00550":"zhang_550"},"is_init":true}'}]], 'process_value': '', 'real_running_time': 1638, 'fees': [{'amount': 3861632, 'asset_id': '1.3.1'}], 'relevant_datasize': 193}], [1, {'real_running_time': 543, 'fees': [{'amount': 100000, 'asset_id': '1.3.1'}]}]]
test_contract_get_contract_public_data done

contract_name: contract.release115.gcpdpya, test account: nicotest
### 1. create contract from file and call test
>> get_contract ['contract.release115.gcpdpya']

{'jsonrpc': '2.0', 'error': {'code': 1, 'message': 'unspecified: Assert Exception: contract_itr != con_index.end(): The contract (contract.release115.gcpdpya) does not exist'}, 'id': 1}


>> create_contract_from_file ['nicotest', 'contract.release115.gcpdpya', 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz', '/home/dev/data/mrepo/CocosBCX/feature_test/release1.4.5/contract_api_integer_max_and_min.lua', 'true']

{'result': ['a171a0255da58ab3d7996193a6c16200d98f69df034405de61fc9920b44e3031', {'expiration': '2020-07-23T04:11:32', 'operations': [[34, {'owner': '1.2.16', 'extensions': [], 'contract_authority': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz', 'name': 'contract.release115.gcpdpya', 'data': 'function test_integer_max()     chainhelper:log(chainhelper:integer_max())         local tmpmax = chainhelper:integer_max()     chainhelper:log(tmpmax)  end  function test_integer_min()     chainhelper:log(chainhelper:integer_min())         local tmpmin = chainhelper:integer_min()     chainhelper:log(tmpmin)  end  '}]], 'extensions': [], 'ref_block_num': 5408, 'signatures': ['1f782f5e690ae2cc85767edfe654b92b633b6dcb2c9fc4e69a73f8e86977d4985b58c9b6bb6753262940b967b86a44c7c9ec52693100e0ef64cf1b9ab67724bf77'], 'ref_block_prefix': 2318199279}], 'jsonrpc': '2.0', 'id': 1}


>> call_contract_function ['nicotest', 'contract.release115.gcpdpya', 'test_integer_max', [], 'true']

{'result': ['2542c93c1642d2bc6af35c5a148c69446ff0f0c1cb650acbd2aa62879e470fc1', {'expiration': '2020-07-23T04:11:36', 'operations': [[35, {'contract_id': '1.16.12', 'function_name': 'test_integer_max', 'caller': '1.2.16', 'value_list': [], 'extensions': []}]], 'extensions': [], 'ref_block_num': 5408, 'signatures': ['20232697835338d9faa0b0dc9384f74f1e9e6708dbda4aeac3913fce4a4e6019a96d933e656c945b7e7a2f016756af48d54774e830477ca24160ba0e3c36cd8549'], 'ref_block_prefix': 2318199279}], 'jsonrpc': '2.0', 'id': 1}


>> get_transaction_by_id ['2542c93c1642d2bc6af35c5a148c69446ff0f0c1cb650acbd2aa62879e470fc1']

{'result': {'expiration': '2020-07-23T04:11:36', 'operation_results': [[4, {'contract_id': '1.16.12', 'existed_pv': False, 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': '9223372036854775807'}], [3, {'affected_account': '1.2.16', 'message': '9223372036854775807'}]], 'process_value': '', 'real_running_time': 891, 'fees': [{'amount': 2969124, 'asset_id': '1.3.1'}], 'relevant_datasize': 61}]], 'operations': [[35, {'contract_id': '1.16.12', 'function_name': 'test_integer_max', 'caller': '1.2.16', 'value_list': [], 'extensions': []}]], 'extensions': [], 'ref_block_num': 5408, 'signatures': ['20232697835338d9faa0b0dc9384f74f1e9e6708dbda4aeac3913fce4a4e6019a96d933e656c945b7e7a2f016756af48d54774e830477ca24160ba0e3c36cd8549'], 'ref_block_prefix': 2318199279}, 'jsonrpc': '2.0', 'id': 1}


tx_id: 2542c93c1642d2bc6af35c5a148c69446ff0f0c1cb650acbd2aa62879e470fc1, result: [[4, {'contract_id': '1.16.12', 'existed_pv': False, 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': '9223372036854775807'}], [3, {'affected_account': '1.2.16', 'message': '9223372036854775807'}]], 'process_value': '', 'real_running_time': 891, 'fees': [{'amount': 2969124, 'asset_id': '1.3.1'}], 'relevant_datasize': 61}]]
>> call_contract_function ['nicotest', 'contract.release115.gcpdpya', 'test_integer_min', [], 'true']

{'result': ['c22c17a0bc9b823c562a1804546b1b8e0fc1360e2c426203263a4bbcf2069f93', {'expiration': '2020-07-23T04:11:40', 'operations': [[35, {'contract_id': '1.16.12', 'function_name': 'test_integer_min', 'caller': '1.2.16', 'value_list': [], 'extensions': []}]], 'extensions': [], 'ref_block_num': 5414, 'signatures': ['1f179eb11825489024bd9576f4599eebaae79577ebdf7d426c4ef18024c3f41bad08d560a65fd0cd62de07f9502eb5f5fb943f4696f5d9d554ecbf6a5351f148a4'], 'ref_block_prefix': 3343471761}], 'jsonrpc': '2.0', 'id': 1}


>> get_transaction_by_id ['c22c17a0bc9b823c562a1804546b1b8e0fc1360e2c426203263a4bbcf2069f93']

{'result': {'expiration': '2020-07-23T04:11:40', 'operation_results': [[4, {'contract_id': '1.16.12', 'existed_pv': False, 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': '-9223372036854775808'}], [3, {'affected_account': '1.2.16', 'message': '-9223372036854775808'}]], 'process_value': '', 'real_running_time': 1402, 'fees': [{'amount': 3482077, 'asset_id': '1.3.1'}], 'relevant_datasize': 63}]], 'operations': [[35, {'contract_id': '1.16.12', 'function_name': 'test_integer_min', 'caller': '1.2.16', 'value_list': [], 'extensions': []}]], 'extensions': [], 'ref_block_num': 5414, 'signatures': ['1f179eb11825489024bd9576f4599eebaae79577ebdf7d426c4ef18024c3f41bad08d560a65fd0cd62de07f9502eb5f5fb943f4696f5d9d554ecbf6a5351f148a4'], 'ref_block_prefix': 3343471761}, 'jsonrpc': '2.0', 'id': 1}


tx_id: c22c17a0bc9b823c562a1804546b1b8e0fc1360e2c426203263a4bbcf2069f93, result: [[4, {'contract_id': '1.16.12', 'existed_pv': False, 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': '-9223372036854775808'}], [3, {'affected_account': '1.2.16', 'message': '-9223372036854775808'}]], 'process_value': '', 'real_running_time': 1402, 'fees': [{'amount': 3482077, 'asset_id': '1.3.1'}], 'relevant_datasize': 63}]]
```  

