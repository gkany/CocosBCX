
# test result  
``` text  
>> unlock ['123456']
[1;32;40m
{'result': None, 'id': 1, 'jsonrpc': '2.0'}

[0m

>> list_my_accounts []
setUpClass done


>> register_nh_asset_creator ['nicotest', 'true']
[1;32;40m
{'error': {'message': 'unspecified: Assert Exception: nh_asset_creator_idx.find(o.fee_paying_account) == nh_asset_creator_idx.end(): You had registered to a nh asset creater.', 'code': 1}, 'id': 1, 'jsonrpc': '2.0'}

[0m

>> call [0, 'lookup_world_view', [['test_wvoxee']]]
[1;32;40m
{'result': [None], 'id': 1, 'jsonrpc': '2.0'}

[0m
create_world_view

>> create_world_view ['nicotest', 'test_wvoxee', 'true']
[1;32;40m
{'result': ['7ce465ed70a1ab97cf3b3ebaedc21397780d9ad472bfaa6b35de6b256ee2cf34', {'expiration': '2020-09-09T09:34:06', 'extensions': [], 'signatures': ['205b9dcf31e6fc0efc8911a73cbb970c2a4e98694b2866a4a53c6335d05aeac4291e40667dc1b15ed7678c750db01ef627bde093160dbac42be126b9d1bda619d6'], 'ref_block_num': 4587, 'ref_block_prefix': 1072332322, 'operations': [[38, {'world_view': 'test_wvoxee', 'fee_paying_account': '1.2.16'}]]}], 'id': 1, 'jsonrpc': '2.0'}

[0m

>> call [0, 'lookup_world_view', [['test_wvoxee']]]
[1;32;40m
{'result': [{'world_view': 'test_wvoxee', 'related_nht_creator': ['4.0.0'], 'id': '4.1.22', 'world_view_creator': '4.0.0'}], 'id': 1, 'jsonrpc': '2.0'}

[0m

>> get_world_view ['test_wvoxee']
[1;32;40m
{'result': {'world_view': 'test_wvoxee', 'related_nht_creator': ['4.0.0'], 'id': '4.1.22', 'world_view_creator': '4.0.0'}, 'id': 1, 'jsonrpc': '2.0'}

[0m

>> get_world_view ['4.1.22']
[1;32;40m
{'result': {'world_view': 'test_wvoxee', 'related_nht_creator': ['4.0.0'], 'id': '4.1.22', 'world_view_creator': '4.0.0'}, 'id': 1, 'jsonrpc': '2.0'}

[0m
test_cli_wallet_api_get_world_view done


>> register_nh_asset_creator ['nicotest', 'true']
[1;32;40m
{'error': {'message': 'unspecified: Assert Exception: nh_asset_creator_idx.find(o.fee_paying_account) == nh_asset_creator_idx.end(): You had registered to a nh asset creater.', 'code': 1}, 'id': 1, 'jsonrpc': '2.0'}

[0m

>> call [0, 'lookup_world_view', [['test_wvyybk']]]
[1;32;40m
{'result': [None], 'id': 1, 'jsonrpc': '2.0'}

[0m
create_world_view

>> create_world_view ['nicotest', 'test_wvyybk', 'true']
[1;32;40m
{'result': ['8263a9e92a9fce179363d089cc82f2c5d976d0d565316d2501104d65e4615cff', {'expiration': '2020-09-09T09:34:08', 'extensions': [], 'signatures': ['1f183092cce914f8a8a70a09c1c12d61e069788c62580011af795ec37849eb4ccc47bc49d8440f68897328c6dccb35ed58c7e602bcb7e1155ff8ed94836bc4576f'], 'ref_block_num': 4588, 'ref_block_prefix': 4119590488, 'operations': [[38, {'world_view': 'test_wvyybk', 'fee_paying_account': '1.2.16'}]]}], 'id': 1, 'jsonrpc': '2.0'}

[0m

>> call [0, 'lookup_world_view', [['test_wvyybk']]]
[1;32;40m
{'result': [{'world_view': 'test_wvyybk', 'related_nht_creator': ['4.0.0'], 'id': '4.1.23', 'world_view_creator': '4.0.0'}], 'id': 1, 'jsonrpc': '2.0'}

[0m

>> get_contract ['contract.testapitestapigetnftasset']
[1;32;40m
{'result': {'id': '1.16.5', 'current_version': '9602430db95c35f53affa7e1b8aa370524f33243af34b85ef87f04b2524b12ba', 'name': 'contract.testapitestapigetnftasset', 'lua_code_b_id': '2.2.5', 'contract_authority': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'owner': '1.2.16', 'check_contract_authority': False, 'contract_data': [], 'user_invoke_share_percent': 100, 'is_release': False, 'creation_date': '2020-09-09T08:02:48', 'contract_ABI': [[{'key': [2, {'v': 'test_create_nh_asset'}]}, [5, {'arglist': ['owner', 'symbol', 'world_view', 'base_describe', 'enable_logger'], 'is_var_arg': False}]], [{'key': [2, {'v': 'test_get_nft_asset'}]}, [5, {'arglist': ['hash_or_id'], 'is_var_arg': False}]]]}, 'id': 1, 'jsonrpc': '2.0'}

[0m

>> get_contract ['contract.testapitestapigetnftasset']
[1;32;40m
{'result': {'id': '1.16.5', 'current_version': '9602430db95c35f53affa7e1b8aa370524f33243af34b85ef87f04b2524b12ba', 'name': 'contract.testapitestapigetnftasset', 'lua_code_b_id': '2.2.5', 'contract_authority': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'owner': '1.2.16', 'check_contract_authority': False, 'contract_data': [], 'user_invoke_share_percent': 100, 'is_release': False, 'creation_date': '2020-09-09T08:02:48', 'contract_ABI': [[{'key': [2, {'v': 'test_create_nh_asset'}]}, [5, {'arglist': ['owner', 'symbol', 'world_view', 'base_describe', 'enable_logger'], 'is_var_arg': False}]], [{'key': [2, {'v': 'test_get_nft_asset'}]}, [5, {'arglist': ['hash_or_id'], 'is_var_arg': False}]]]}, 'id': 1, 'jsonrpc': '2.0'}

[0m

>> revise_contract_from_file ['nicotest', 'contract.testapitestapigetnftasset', '/home/ck/xukang/CocosBCX/feature_test/release1.1.6/test.lua', 'true']
[1;32;40m
{'result': ['924497034015b0091f14f0707a487aa508a82eb6d96a1fa1a8c9cecffd9455db', {'expiration': '2020-09-09T09:34:10', 'extensions': [], 'signatures': ['2036d7d332a7818e8b323cae59b974e8d921405498ea16e9b81ff784b0da8176ae42b678c066e834a543f8be15976700f43da682fe9530eda67c36968dd4340439'], 'ref_block_num': 4589, 'ref_block_prefix': 178384259, 'operations': [[50, {'reviser': '1.2.16', 'contract_id': '1.16.5', 'extensions': [], 'data': 'function test_create_nh_asset(owner, symbol, world_view, base_describe, enable_logger) \tchainhelper:log("[test_create_nh_asset]symbol: " .. symbol .. ", owner: "..owner) \tnh_asset_id = chainhelper:create_nh_asset(owner, symbol, world_view, base_describe, enable_logger) \tchainhelper:log("new nh_asset_id: " .. nh_asset_id) end   function test_get_nft_asset(hash_or_id) \tchainhelper:log(\'input params: \' .. tostring(hash_or_id)) \tlocal asset = chainhelper:get_nft_asset(hash_or_id); \tchainhelper:log(\'result type: \' .. type(asset)) \tchainhelper:log(\'get_nft_asset result: \' .. tostring(asset)) end '}]]}], 'id': 1, 'jsonrpc': '2.0'}

[0m

>> get_contract ['contract.testapitestapigetnftasset']
[1;32;40m
{'result': {'id': '1.16.5', 'current_version': '924497034015b0091f14f0707a487aa508a82eb6d96a1fa1a8c9cecffd9455db', 'name': 'contract.testapitestapigetnftasset', 'lua_code_b_id': '2.2.5', 'contract_authority': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'owner': '1.2.16', 'check_contract_authority': False, 'contract_data': [], 'user_invoke_share_percent': 100, 'is_release': False, 'creation_date': '2020-09-09T08:02:48', 'contract_ABI': [[{'key': [2, {'v': 'test_create_nh_asset'}]}, [5, {'arglist': ['owner', 'symbol', 'world_view', 'base_describe', 'enable_logger'], 'is_var_arg': False}]], [{'key': [2, {'v': 'test_get_nft_asset'}]}, [5, {'arglist': ['hash_or_id'], 'is_var_arg': False}]]]}, 'id': 1, 'jsonrpc': '2.0'}

[0m
contract_name: contract.testapitestapigetnftasset, contract_id: 1.16.5

>> call_contract_function ['nicotest', 'contract.testapitestapigetnftasset', 'test_create_nh_asset', [[2, {'v': 'nicotest'}], [2, {'v': 'COCOS'}], [2, {'v': 'test_wvyybk'}], [2, {'v': "'nh_symbol': 'OSCGM'"}], [3, {'v': True}]], 'true']
[1;32;40m
{'result': ['d5b1c845e3649782ebb58cdc961b633317cb5d0aaf6aeb6d184ba79dd2593a5c', {'expiration': '2020-09-09T09:34:14', 'extensions': [], 'signatures': ['1f329a078552994d35900c1a7374d014f496fb76b4b40c660226d8aed29a3d60de6615cba35fddd339975d491b7ede6fcb4f19ffa3a7508ba1fab7b43e034655bc'], 'ref_block_num': 4590, 'ref_block_prefix': 3336363800, 'operations': [[35, {'contract_id': '1.16.5', 'value_list': [[2, {'v': 'nicotest'}], [2, {'v': 'COCOS'}], [2, {'v': 'test_wvyybk'}], [2, {'v': "'nh_symbol': 'OSCGM'"}], [3, {'v': True}]], 'function_name': 'test_create_nh_asset', 'extensions': [], 'caller': '1.2.16'}]]}], 'id': 1, 'jsonrpc': '2.0'}

[0m

>> get_transaction_by_id ['d5b1c845e3649782ebb58cdc961b633317cb5d0aaf6aeb6d184ba79dd2593a5c']
[1;32;40m
{'result': {'expiration': '2020-09-09T09:34:14', 'extensions': [], 'operation_results': [[4, {'relevant_datasize': 150, 'process_value': '', 'contract_id': '1.16.5', 'contract_affecteds': [[3, {'message': '[test_create_nh_asset]symbol: COCOS, owner: nicotest', 'affected_account': '1.2.16'}], [1, {'affected_item': '4.2.17', 'affected_account': '1.2.16', 'action': 4}], [1, {'affected_item': '4.2.17', 'affected_account': '1.2.16', 'action': 3}], [3, {'message': 'new nh_asset_id: 4.2.17', 'affected_account': '1.2.16'}]], 'existed_pv': False, 'real_running_time': 491, 'fees': [{'amount': 2712679, 'asset_id': '1.3.0'}]}]], 'signatures': ['1f329a078552994d35900c1a7374d014f496fb76b4b40c660226d8aed29a3d60de6615cba35fddd339975d491b7ede6fcb4f19ffa3a7508ba1fab7b43e034655bc'], 'ref_block_num': 4590, 'ref_block_prefix': 3336363800, 'operations': [[35, {'contract_id': '1.16.5', 'value_list': [[2, {'v': 'nicotest'}], [2, {'v': 'COCOS'}], [2, {'v': 'test_wvyybk'}], [2, {'v': "'nh_symbol': 'OSCGM'"}], [3, {'v': True}]], 'function_name': 'test_create_nh_asset', 'extensions': [], 'caller': '1.2.16'}]]}, 'id': 1, 'jsonrpc': '2.0'}

[0m
tx_id: d5b1c845e3649782ebb58cdc961b633317cb5d0aaf6aeb6d184ba79dd2593a5c, result: [[4, {'relevant_datasize': 150, 'process_value': '', 'contract_id': '1.16.5', 'contract_affecteds': [[3, {'message': '[test_create_nh_asset]symbol: COCOS, owner: nicotest', 'affected_account': '1.2.16'}], [1, {'affected_item': '4.2.17', 'affected_account': '1.2.16', 'action': 4}], [1, {'affected_item': '4.2.17', 'affected_account': '1.2.16', 'action': 3}], [3, {'message': 'new nh_asset_id: 4.2.17', 'affected_account': '1.2.16'}]], 'existed_pv': False, 'real_running_time': 491, 'fees': [{'amount': 2712679, 'asset_id': '1.3.0'}]}]]
### 5. call contract api test: get_nft_asset
>>> list_account_nh_asset

>> list_account_nh_asset ['nicotest', ['test_wvyybk'], 5, 1, 4]
[1;32;40m
{'result': [[{'asset_qualifier': '', 'nh_hash': '110000000000000024d1a9ac43057126a4b796c5a97d0575e5be35e4e24e339e', 'nh_asset_active': '1.2.16', 'describe_with_contract': [], 'nh_asset_owner': '1.2.16', 'create_time': '2020-09-09T09:13:44', 'limit_list': [], 'dealership': '1.2.16', 'nh_asset_creator': '1.2.16', 'base_describe': "'nh_symbol': 'OSCGM'", 'world_view': 'test_wvyybk', 'id': '4.2.17', 'parent': [], 'child': [], 'limit_type': 'black_list'}], 1], 'id': 1, 'jsonrpc': '2.0'}

[0m
nh_assets:  [[{'asset_qualifier': '', 'nh_hash': '110000000000000024d1a9ac43057126a4b796c5a97d0575e5be35e4e24e339e', 'nh_asset_active': '1.2.16', 'describe_with_contract': [], 'nh_asset_owner': '1.2.16', 'create_time': '2020-09-09T09:13:44', 'limit_list': [], 'dealership': '1.2.16', 'nh_asset_creator': '1.2.16', 'base_describe': "'nh_symbol': 'OSCGM'", 'world_view': 'test_wvyybk', 'id': '4.2.17', 'parent': [], 'child': [], 'limit_type': 'black_list'}], 1]

>> call_contract_function ['nicotest', 'contract.testapitestapigetnftasset', 'test_get_nft_asset', [[2, {'v': '4.2.17'}]], 'true']
[1;32;40m
{'result': ['ed134cd41dab89f4f61860ec1b10305dec4474140840db8b20d5a2f2e6259228', {'expiration': '2020-09-09T09:34:16', 'extensions': [], 'signatures': ['1f6e36598c18efc06e0af59b1730f39fdc543191dc14696b08b082eb357eddda12207718644e2a2b2f8d14442b30d2ee67c55864ac588d4a47b13e9ff73613aa26'], 'ref_block_num': 4590, 'ref_block_prefix': 3336363800, 'operations': [[35, {'contract_id': '1.16.5', 'value_list': [[2, {'v': '4.2.17'}]], 'function_name': 'test_get_nft_asset', 'extensions': [], 'caller': '1.2.16'}]]}], 'id': 1, 'jsonrpc': '2.0'}

[0m

>> get_transaction_by_id ['ed134cd41dab89f4f61860ec1b10305dec4474140840db8b20d5a2f2e6259228']
[1;32;40m
{'result': {'expiration': '2020-09-09T09:34:16', 'extensions': [], 'operation_results': [[4, {'relevant_datasize': 506, 'process_value': '', 'contract_id': '1.16.5', 'contract_affecteds': [[3, {'message': 'input params: 4.2.17', 'affected_account': '1.2.16'}], [3, {'message': 'result type: string', 'affected_account': '1.2.16'}], [3, {'message': 'get_nft_asset result: {"id":"4.2.17","nh_hash":"110000000000000024d1a9ac43057126a4b796c5a97d0575e5be35e4e24e339e","nh_asset_creator":"1.2.16","nh_asset_owner":"1.2.16","nh_asset_active":"1.2.16","dealership":"1.2.16","asset_qualifier":"","world_view":"test_wvyybk","base_describe":"\'nh_symbol\': \'OSCGM\'","parent":[],"child":[],"describe_with_contract":[],"create_time":"2020-09-09T09:13:44","limit_list":[],"limit_type":"black_list"}', 'affected_account': '1.2.16'}]], 'existed_pv': False, 'real_running_time': 524, 'fees': [{'amount': 3046460, 'asset_id': '1.3.0'}]}]], 'signatures': ['1f6e36598c18efc06e0af59b1730f39fdc543191dc14696b08b082eb357eddda12207718644e2a2b2f8d14442b30d2ee67c55864ac588d4a47b13e9ff73613aa26'], 'ref_block_num': 4590, 'ref_block_prefix': 3336363800, 'operations': [[35, {'contract_id': '1.16.5', 'value_list': [[2, {'v': '4.2.17'}]], 'function_name': 'test_get_nft_asset', 'extensions': [], 'caller': '1.2.16'}]]}, 'id': 1, 'jsonrpc': '2.0'}

[0m
tx_id: ed134cd41dab89f4f61860ec1b10305dec4474140840db8b20d5a2f2e6259228, result: [[4, {'relevant_datasize': 506, 'process_value': '', 'contract_id': '1.16.5', 'contract_affecteds': [[3, {'message': 'input params: 4.2.17', 'affected_account': '1.2.16'}], [3, {'message': 'result type: string', 'affected_account': '1.2.16'}], [3, {'message': 'get_nft_asset result: {"id":"4.2.17","nh_hash":"110000000000000024d1a9ac43057126a4b796c5a97d0575e5be35e4e24e339e","nh_asset_creator":"1.2.16","nh_asset_owner":"1.2.16","nh_asset_active":"1.2.16","dealership":"1.2.16","asset_qualifier":"","world_view":"test_wvyybk","base_describe":"\'nh_symbol\': \'OSCGM\'","parent":[],"child":[],"describe_with_contract":[],"create_time":"2020-09-09T09:13:44","limit_list":[],"limit_type":"black_list"}', 'affected_account': '1.2.16'}]], 'existed_pv': False, 'real_running_time': 524, 'fees': [{'amount': 3046460, 'asset_id': '1.3.0'}]}]]

>> call_contract_function ['nicotest', 'contract.testapitestapigetnftasset', 'test_get_nft_asset', [[2, {'v': '110000000000000024d1a9ac43057126a4b796c5a97d0575e5be35e4e24e339e'}]], 'true']
[1;32;40m
{'result': ['bf6461ffdb962d387790da1b7c4c84f0b17236400ce143b2cfb0fdf71b8738dc', {'expiration': '2020-09-09T09:34:18', 'extensions': [], 'signatures': ['20348c0fdaac362668c039ad7da92fb05108122c0a06764f697f2b4d535001ad9c598f222d88b13c056eeaf011c00f1f4380ce89c9a3f1a2154673501769bc98dd'], 'ref_block_num': 4590, 'ref_block_prefix': 3336363800, 'operations': [[35, {'contract_id': '1.16.5', 'value_list': [[2, {'v': '110000000000000024d1a9ac43057126a4b796c5a97d0575e5be35e4e24e339e'}]], 'function_name': 'test_get_nft_asset', 'extensions': [], 'caller': '1.2.16'}]]}], 'id': 1, 'jsonrpc': '2.0'}

[0m

>> get_transaction_by_id ['bf6461ffdb962d387790da1b7c4c84f0b17236400ce143b2cfb0fdf71b8738dc']
[1;32;40m
{'result': {'expiration': '2020-09-09T09:34:18', 'extensions': [], 'operation_results': [[4, {'relevant_datasize': 564, 'process_value': '', 'contract_id': '1.16.5', 'contract_affecteds': [[3, {'message': 'input params: 110000000000000024d1a9ac43057126a4b796c5a97d0575e5be35e4e24e339e', 'affected_account': '1.2.16'}], [3, {'message': 'result type: string', 'affected_account': '1.2.16'}], [3, {'message': 'get_nft_asset result: {"id":"4.2.17","nh_hash":"110000000000000024d1a9ac43057126a4b796c5a97d0575e5be35e4e24e339e","nh_asset_creator":"1.2.16","nh_asset_owner":"1.2.16","nh_asset_active":"1.2.16","dealership":"1.2.16","asset_qualifier":"","world_view":"test_wvyybk","base_describe":"\'nh_symbol\': \'OSCGM\'","parent":[],"child":[],"describe_with_contract":[],"create_time":"2020-09-09T09:13:44","limit_list":[],"limit_type":"black_list"}', 'affected_account': '1.2.16'}]], 'existed_pv': False, 'real_running_time': 591, 'fees': [{'amount': 3226741, 'asset_id': '1.3.0'}]}]], 'signatures': ['20348c0fdaac362668c039ad7da92fb05108122c0a06764f697f2b4d535001ad9c598f222d88b13c056eeaf011c00f1f4380ce89c9a3f1a2154673501769bc98dd'], 'ref_block_num': 4590, 'ref_block_prefix': 3336363800, 'operations': [[35, {'contract_id': '1.16.5', 'value_list': [[2, {'v': '110000000000000024d1a9ac43057126a4b796c5a97d0575e5be35e4e24e339e'}]], 'function_name': 'test_get_nft_asset', 'extensions': [], 'caller': '1.2.16'}]]}, 'id': 1, 'jsonrpc': '2.0'}

[0m
tx_id: bf6461ffdb962d387790da1b7c4c84f0b17236400ce143b2cfb0fdf71b8738dc, result: [[4, {'relevant_datasize': 564, 'process_value': '', 'contract_id': '1.16.5', 'contract_affecteds': [[3, {'message': 'input params: 110000000000000024d1a9ac43057126a4b796c5a97d0575e5be35e4e24e339e', 'affected_account': '1.2.16'}], [3, {'message': 'result type: string', 'affected_account': '1.2.16'}], [3, {'message': 'get_nft_asset result: {"id":"4.2.17","nh_hash":"110000000000000024d1a9ac43057126a4b796c5a97d0575e5be35e4e24e339e","nh_asset_creator":"1.2.16","nh_asset_owner":"1.2.16","nh_asset_active":"1.2.16","dealership":"1.2.16","asset_qualifier":"","world_view":"test_wvyybk","base_describe":"\'nh_symbol\': \'OSCGM\'","parent":[],"child":[],"describe_with_contract":[],"create_time":"2020-09-09T09:13:44","limit_list":[],"limit_type":"black_list"}', 'affected_account': '1.2.16'}]], 'existed_pv': False, 'real_running_time': 591, 'fees': [{'amount': 3226741, 'asset_id': '1.3.0'}]}]]
test_contract_get_nft_asset done


>> lock []
[1;32;40m
{'result': None, 'id': 1, 'jsonrpc': '2.0'}

[0m
tearDownClass done

..
----------------------------------------------------------------------
Ran 2 tests in 14.238s

OK
```  

