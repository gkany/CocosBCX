# 1. 本地测试  
``` text  
>> unlock ['123456']

{'jsonrpc': '2.0', 'result': None, 'id': 1}


setUpClass done

s>> register_nh_asset_creator ['nicotest', 'true']

{'jsonrpc': '2.0', 'id': 1, 'error': {'code': 1, 'message': 'unspecified: Assert Exception: nh_asset_creator_idx.find(o.fee_paying_account) == nh_asset_creator_idx.end(): You had registered to a nh asset creater.'}}


>> call [0, 'lookup_world_view', [['test_wvexxr']]]

{'jsonrpc': '2.0', 'result': [None], 'id': 1}


create_world_view
>> create_world_view ['nicotest', 'test_wvexxr', 'true']

{'jsonrpc': '2.0', 'result': ['8ea584b5927dfad28d9c26e46c321af04ee62737d1b6ddb25f679fcbd5ba7f95', {'expiration': '2020-07-24T09:20:30', 'operations': [[38, {'world_view': 'test_wvexxr', 'fee_paying_account': '1.2.16'}]], 'ref_block_prefix': 3855428405, 'ref_block_num': 11619, 'extensions': [], 'signatures': ['1f287e922d026cff8031d3586b9e0c04b9de392763e46ef67c1a51ff229dda27e32904cf0f27dc452f01a7ab2fd3b83f9cebae3df54036c80c8cb75feff27b7b19']}], 'id': 1}


>> call [0, 'lookup_world_view', [['test_wvexxr']]]

{'jsonrpc': '2.0', 'result': [{'world_view': 'test_wvexxr', 'world_view_creator': '4.0.0', 'related_nht_creator': ['4.0.0'], 'id': '4.1.8'}], 'id': 1}


>> create_nh_asset ['nicotest', 'nicotest', 'COCOS', 'test_wvexxr', "'nh_symbol': 'UDF'", True]

{'jsonrpc': '2.0', 'result': ['5f066d73909f77b888abca81622842ff6180865475d3aab16f207da984bb02cb', {'expiration': '2020-07-24T09:20:38', 'operations': [[40, {'world_view': 'test_wvexxr', 'base_describe': "'nh_symbol': 'UDF'", 'asset_id': 'COCOS', 'fee_paying_account': '1.2.16', 'owner': '1.2.16'}]], 'ref_block_prefix': 3234712476, 'ref_block_num': 11620, 'extensions': [], 'signatures': ['1f3238eb4e4b2a4185bfaa3c3455d1ab28ca383c8cdebb0cea4b7055169767436f1a7f859e4a397a14193638777d0e8f07e27eb2947485dae66b6c56b8235e8df8']}], 'id': 1}


>> get_transaction_by_id ['5f066d73909f77b888abca81622842ff6180865475d3aab16f207da984bb02cb']

{'jsonrpc': '2.0', 'result': {'expiration': '2020-07-24T09:20:38', 'operation_results': [[2, {'fees': [{'amount': 100000, 'asset_id': '1.3.0'}], 'result': '4.2.25', 'real_running_time': 85}]], 'operations': [[40, {'world_view': 'test_wvexxr', 'base_describe': "'nh_symbol': 'UDF'", 'asset_id': 'COCOS', 'fee_paying_account': '1.2.16', 'owner': '1.2.16'}]], 'ref_block_prefix': 3234712476, 'ref_block_num': 11620, 'extensions': [], 'signatures': ['1f3238eb4e4b2a4185bfaa3c3455d1ab28ca383c8cdebb0cea4b7055169767436f1a7f859e4a397a14193638777d0e8f07e27eb2947485dae66b6c56b8235e8df8']}, 'id': 1}


tx_id: 5f066d73909f77b888abca81622842ff6180865475d3aab16f207da984bb02cb, result: [[2, {'fees': [{'amount': 100000, 'asset_id': '1.3.0'}], 'result': '4.2.25', 'real_running_time': 85}]]
>> create_nh_asset ['nicotest', 'nicotest', 'COCOS', 'test_wvexxr', "'nh_symbol': 'KFQAB'", True]

{'jsonrpc': '2.0', 'result': ['fc8f8890fb7e2f346011bec4a36892c168de54840f1282e5154885997ee9a6f3', {'expiration': '2020-07-24T09:20:44', 'operations': [[40, {'world_view': 'test_wvexxr', 'base_describe': "'nh_symbol': 'KFQAB'", 'asset_id': 'COCOS', 'fee_paying_account': '1.2.16', 'owner': '1.2.16'}]], 'ref_block_prefix': 1812272106, 'ref_block_num': 11622, 'extensions': [], 'signatures': ['1f6130d5f8315bce65287b93108a8837b1becb1ff762dbd2a9e44d29c588161caa4b3808953e70f29025d2c4a3c470e2bce58d83c7acc5ac321a1370bb11b3d83c']}], 'id': 1}


>> get_transaction_by_id ['fc8f8890fb7e2f346011bec4a36892c168de54840f1282e5154885997ee9a6f3']

{'jsonrpc': '2.0', 'result': {'expiration': '2020-07-24T09:20:44', 'operation_results': [[2, {'fees': [{'amount': 100000, 'asset_id': '1.3.0'}], 'result': '4.2.26', 'real_running_time': 65}]], 'operations': [[40, {'world_view': 'test_wvexxr', 'base_describe': "'nh_symbol': 'KFQAB'", 'asset_id': 'COCOS', 'fee_paying_account': '1.2.16', 'owner': '1.2.16'}]], 'ref_block_prefix': 1812272106, 'ref_block_num': 11622, 'extensions': [], 'signatures': ['1f6130d5f8315bce65287b93108a8837b1becb1ff762dbd2a9e44d29c588161caa4b3808953e70f29025d2c4a3c470e2bce58d83c7acc5ac321a1370bb11b3d83c']}, 'id': 1}


tx_id: fc8f8890fb7e2f346011bec4a36892c168de54840f1282e5154885997ee9a6f3, result: [[2, {'fees': [{'amount': 100000, 'asset_id': '1.3.0'}], 'result': '4.2.26', 'real_running_time': 65}]]
>> create_nh_asset ['nicotest', 'nicotest', 'COCOS', 'test_wvexxr', "{'name':'ChinaJoy 2020 NFT门票','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy 首套NFT门票，仅供ChinaJoy Plus 2020上线期间使用，该门票不可进入ChinaJoy线下展会。'}", True]

{'jsonrpc': '2.0', 'result': ['108bf1b83f904b1e79d74074275191ffc8572b114447c1c785462979a0c6a77c', {'expiration': '2020-07-24T09:20:48', 'operations': [[40, {'world_view': 'test_wvexxr', 'base_describe': "{'name':'ChinaJoy 2020 NFTu95e8u7968','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy u9996u5957NFTu95e8u7968uff0cu4ec5u4f9bChinaJoy Plus 2020u4e0au7ebfu671fu95f4u4f7fu7528uff0cu8be5u95e8u7968u4e0du53efu8fdbu5165ChinaJoyu7ebfu4e0bu5c55u4f1au3002'}", 'asset_id': 'COCOS', 'fee_paying_account': '1.2.16', 'owner': '1.2.16'}]], 'ref_block_prefix': 1812272106, 'ref_block_num': 11622, 'extensions': [], 'signatures': ['20587be36d905810ce0acf38e33187f36c9419049631203500f67ff8f7cb4e5fbe66fba7edfdcaf7bdbd5d6dae902916c800f5d86ce8f6f045034656965e570c19']}], 'id': 1}


>> get_transaction_by_id ['108bf1b83f904b1e79d74074275191ffc8572b114447c1c785462979a0c6a77c']

{'jsonrpc': '2.0', 'result': {'expiration': '2020-07-24T09:20:48', 'operation_results': [[2, {'fees': [{'amount': 100000, 'asset_id': '1.3.0'}], 'result': '4.2.27', 'real_running_time': 43}]], 'operations': [[40, {'world_view': 'test_wvexxr', 'base_describe': "{'name':'ChinaJoy 2020 NFTu95e8u7968','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy u9996u5957NFTu95e8u7968uff0cu4ec5u4f9bChinaJoy Plus 2020u4e0au7ebfu671fu95f4u4f7fu7528uff0cu8be5u95e8u7968u4e0du53efu8fdbu5165ChinaJoyu7ebfu4e0bu5c55u4f1au3002'}", 'asset_id': 'COCOS', 'fee_paying_account': '1.2.16', 'owner': '1.2.16'}]], 'ref_block_prefix': 1812272106, 'ref_block_num': 11622, 'extensions': [], 'signatures': ['20587be36d905810ce0acf38e33187f36c9419049631203500f67ff8f7cb4e5fbe66fba7edfdcaf7bdbd5d6dae902916c800f5d86ce8f6f045034656965e570c19']}, 'id': 1}


tx_id: 108bf1b83f904b1e79d74074275191ffc8572b114447c1c785462979a0c6a77c, result: [[2, {'fees': [{'amount': 100000, 'asset_id': '1.3.0'}], 'result': '4.2.27', 'real_running_time': 43}]]
>> create_nh_asset ['nicotest', 'nicotest', 'COCOS', 'test_wvexxr', "{'name':'ChinaJoy 2020 NFT门票','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy 首套NFT门票，仅供ChinaJoy Plus 2020上线期间使用，该门票不可进入ChinaJoy线下展会'}", True]

{'jsonrpc': '2.0', 'result': ['7abb9701474d0d0b25cb0e0c33164cb860a17c0fd04e926a39b6b478d0951f3e', {'expiration': '2020-07-24T09:20:54', 'operations': [[40, {'world_view': 'test_wvexxr', 'base_describe': "{'name':'ChinaJoy 2020 NFTu95e8u7968','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy u9996u5957NFTu95e8u7968uff0cu4ec5u4f9bChinaJoy Plus 2020u4e0au7ebfu671fu95f4u4f7fu7528uff0cu8be5u95e8u7968u4e0du53efu8fdbu5165ChinaJoyu7ebfu4e0bu5c55u4f1a'}", 'asset_id': 'COCOS', 'fee_paying_account': '1.2.16', 'owner': '1.2.16'}]], 'ref_block_prefix': 2576116709, 'ref_block_num': 11628, 'extensions': [], 'signatures': ['203e0f88584c9172eb64a84fabcabcea463b78203bec6146a5baf42032d7cdd7fb08863ee5fc3dd9a299443e461be3dd7fb28b4c7ee033d4ddd72d2d3e27f79712']}], 'id': 1}


>> get_transaction_by_id ['7abb9701474d0d0b25cb0e0c33164cb860a17c0fd04e926a39b6b478d0951f3e']

{'jsonrpc': '2.0', 'result': {'expiration': '2020-07-24T09:20:54', 'operation_results': [[2, {'fees': [{'amount': 100000, 'asset_id': '1.3.0'}], 'result': '4.2.28', 'real_running_time': 44}]], 'operations': [[40, {'world_view': 'test_wvexxr', 'base_describe': "{'name':'ChinaJoy 2020 NFTu95e8u7968','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy u9996u5957NFTu95e8u7968uff0cu4ec5u4f9bChinaJoy Plus 2020u4e0au7ebfu671fu95f4u4f7fu7528uff0cu8be5u95e8u7968u4e0du53efu8fdbu5165ChinaJoyu7ebfu4e0bu5c55u4f1a'}", 'asset_id': 'COCOS', 'fee_paying_account': '1.2.16', 'owner': '1.2.16'}]], 'ref_block_prefix': 2576116709, 'ref_block_num': 11628, 'extensions': [], 'signatures': ['203e0f88584c9172eb64a84fabcabcea463b78203bec6146a5baf42032d7cdd7fb08863ee5fc3dd9a299443e461be3dd7fb28b4c7ee033d4ddd72d2d3e27f79712']}, 'id': 1}


tx_id: 7abb9701474d0d0b25cb0e0c33164cb860a17c0fd04e926a39b6b478d0951f3e, result: [[2, {'fees': [{'amount': 100000, 'asset_id': '1.3.0'}], 'result': '4.2.28', 'real_running_time': 44}]]
>> create_nh_asset ['nicotest', 'nicotest', 'COCOS', 'test_wvexxr', "{'name':'ChinaJoy 2020 NFT门票','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy 首套NFT门票，仅供ChinaJoy Plus 2020上线期间使用，该门票不可进入ChinaJoy线下展会。。。。。。。。。。。。'}", True]

{'jsonrpc': '2.0', 'result': ['19b16e3e21f4fa92ee7a103bba2a6ff1a9f3ec1bbbb648d0e1f64a04faa4d787', {'expiration': '2020-07-24T09:20:58', 'operations': [[40, {'world_view': 'test_wvexxr', 'base_describe': "{'name':'ChinaJoy 2020 NFTu95e8u7968','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy u9996u5957NFTu95e8u7968uff0cu4ec5u4f9bChinaJoy Plus 2020u4e0au7ebfu671fu95f4u4f7fu7528uff0cu8be5u95e8u7968u4e0du53efu8fdbu5165ChinaJoyu7ebfu4e0bu5c55u4f1au3002u3002u3002u3002u3002u3002u3002u3002u3002u3002u3002u3002'}", 'asset_id': 'COCOS', 'fee_paying_account': '1.2.16', 'owner': '1.2.16'}]], 'ref_block_prefix': 3258437579, 'ref_block_num': 11630, 'extensions': [], 'signatures': ['200c2399e3bc22619cb70dc898351b484923c7b9f33a4bfbe96da5f76d68d0659e3e8eec5db45ccaf61af06fe26510ebf7780d5db454b8f6ecb444735ffefee7bc']}], 'id': 1}


>> get_transaction_by_id ['19b16e3e21f4fa92ee7a103bba2a6ff1a9f3ec1bbbb648d0e1f64a04faa4d787']

{'jsonrpc': '2.0', 'result': {'expiration': '2020-07-24T09:20:58', 'operation_results': [[2, {'fees': [{'amount': 100000, 'asset_id': '1.3.0'}], 'result': '4.2.29', 'real_running_time': 49}]], 'operations': [[40, {'world_view': 'test_wvexxr', 'base_describe': "{'name':'ChinaJoy 2020 NFTu95e8u7968','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy u9996u5957NFTu95e8u7968uff0cu4ec5u4f9bChinaJoy Plus 2020u4e0au7ebfu671fu95f4u4f7fu7528uff0cu8be5u95e8u7968u4e0du53efu8fdbu5165ChinaJoyu7ebfu4e0bu5c55u4f1au3002u3002u3002u3002u3002u3002u3002u3002u3002u3002u3002u3002'}", 'asset_id': 'COCOS', 'fee_paying_account': '1.2.16', 'owner': '1.2.16'}]], 'ref_block_prefix': 3258437579, 'ref_block_num': 11630, 'extensions': [], 'signatures': ['200c2399e3bc22619cb70dc898351b484923c7b9f33a4bfbe96da5f76d68d0659e3e8eec5db45ccaf61af06fe26510ebf7780d5db454b8f6ecb444735ffefee7bc']}, 'id': 1}


tx_id: 19b16e3e21f4fa92ee7a103bba2a6ff1a9f3ec1bbbb648d0e1f64a04faa4d787, result: [[2, {'fees': [{'amount': 100000, 'asset_id': '1.3.0'}], 'result': '4.2.29', 'real_running_time': 49}]]
>> create_nh_asset ['nicotest', 'nicotest', 'COCOS', 'test_wvexxr', "'nh_symbol': 'NZPFKAG'", True]

{'jsonrpc': '2.0', 'result': ['e3828aadaa54c138fa219d3ac55be89aa0db35725037b44b27b46f7cd22d419a', {'expiration': '2020-07-24T09:21:04', 'operations': [[40, {'world_view': 'test_wvexxr', 'base_describe': "'nh_symbol': 'NZPFKAG'", 'asset_id': 'COCOS', 'fee_paying_account': '1.2.16', 'owner': '1.2.16'}]], 'ref_block_prefix': 2550350763, 'ref_block_num': 11632, 'extensions': [], 'signatures': ['2041e1ee3bfbb49e8c9c609247f2ee0b8cf2082e5083333d3704e244a45d5c696059105cdf2a87273b7458533ad5ae4f2fe252ddef7c97921fce37d8b2b5dc37e6']}], 'id': 1}


>> get_transaction_by_id ['e3828aadaa54c138fa219d3ac55be89aa0db35725037b44b27b46f7cd22d419a']

{'jsonrpc': '2.0', 'result': {'expiration': '2020-07-24T09:21:04', 'operation_results': [[2, {'fees': [{'amount': 100000, 'asset_id': '1.3.0'}], 'result': '4.2.30', 'real_running_time': 42}]], 'operations': [[40, {'world_view': 'test_wvexxr', 'base_describe': "'nh_symbol': 'NZPFKAG'", 'asset_id': 'COCOS', 'fee_paying_account': '1.2.16', 'owner': '1.2.16'}]], 'ref_block_prefix': 2550350763, 'ref_block_num': 11632, 'extensions': [], 'signatures': ['2041e1ee3bfbb49e8c9c609247f2ee0b8cf2082e5083333d3704e244a45d5c696059105cdf2a87273b7458533ad5ae4f2fe252ddef7c97921fce37d8b2b5dc37e6']}, 'id': 1}


tx_id: e3828aadaa54c138fa219d3ac55be89aa0db35725037b44b27b46f7cd22d419a, result: [[2, {'fees': [{'amount': 100000, 'asset_id': '1.3.0'}], 'result': '4.2.30', 'real_running_time': 42}]]

----------------------------
tx: 108bf1b83f904b1e79d74074275191ffc8572b114447c1c785462979a0c6a77c, result: [[2, {'fees': [{'amount': 100000, 'asset_id': '1.3.0'}], 'result': '4.2.27', 'real_running_time': 43}]]
tx: 5f066d73909f77b888abca81622842ff6180865475d3aab16f207da984bb02cb, result: [[2, {'fees': [{'amount': 100000, 'asset_id': '1.3.0'}], 'result': '4.2.25', 'real_running_time': 85}]]
tx: 7abb9701474d0d0b25cb0e0c33164cb860a17c0fd04e926a39b6b478d0951f3e, result: [[2, {'fees': [{'amount': 100000, 'asset_id': '1.3.0'}], 'result': '4.2.28', 'real_running_time': 44}]]
tx: e3828aadaa54c138fa219d3ac55be89aa0db35725037b44b27b46f7cd22d419a, result: [[2, {'fees': [{'amount': 100000, 'asset_id': '1.3.0'}], 'result': '4.2.30', 'real_running_time': 42}]]
tx: 19b16e3e21f4fa92ee7a103bba2a6ff1a9f3ec1bbbb648d0e1f64a04faa4d787, result: [[2, {'fees': [{'amount': 100000, 'asset_id': '1.3.0'}], 'result': '4.2.29', 'real_running_time': 49}]]
tx: fc8f8890fb7e2f346011bec4a36892c168de54840f1282e5154885997ee9a6f3, result: [[2, {'fees': [{'amount': 100000, 'asset_id': '1.3.0'}], 'result': '4.2.26', 'real_running_time': 65}]]
----------------------------
test_create_nh_asset done

.>> lock []

{'jsonrpc': '2.0', 'result': None, 'id': 1}


tearDownClass done


----------------------------------------------------------------------
Ran 2 tests in 34.160s

OK (skipped=1)
```  

# 2. 主网测试  
``` text  
>> unlock ['123456']

{'result': None, 'jsonrpc': '2.0', 'id': 1}


setUpClass done

s>> register_nh_asset_creator ['faucet1', 'true']

{'error': {'code': 1, 'message': 'unspecified: Assert Exception: nh_asset_creator_idx.find(o.fee_paying_account) == nh_asset_creator_idx.end(): You had registered to a nh asset creater.'}, 'jsonrpc': '2.0', 'id': 1}


>> call [0, 'lookup_world_view', [['test_wvizhn']]]

{'result': [None], 'jsonrpc': '2.0', 'id': 1}


create_world_view
>> create_world_view ['faucet1', 'test_wvizhn', 'true']

{'result': ['9142e0029d3fd56725d37f644d5340587788647eb45c1d03273a3ad593acf826', {'operations': [[38, {'fee_paying_account': '1.2.18', 'world_view': 'test_wvizhn'}]], 'signatures': ['1f6cf4cb375e448f26ab8d326bdca00040a799d91c0b9d43507c8eb7d8ab0d3d2a56643096ada8b561cda12745f07d0450ba79a71453e134854c883146856e9b17'], 'ref_block_prefix': 399015097, 'ref_block_num': 12422, 'expiration': '2020-07-24T09:25:32', 'extensions': []}], 'jsonrpc': '2.0', 'id': 1}


>> call [0, 'lookup_world_view', [['test_wvizhn']]]

{'result': [None], 'jsonrpc': '2.0', 'id': 1}


>> create_nh_asset ['faucet1', 'faucet1', 'COCOS', 'test_wvizhn', "'nh_symbol': 'UUW'", True]

{'result': ['a5d942e46d3701956f20c24ebc3ea82dbab76f739fa2b8e57017f8c793700f11', {'operations': [[40, {'base_describe': "'nh_symbol': 'UUW'", 'world_view': 'test_wvizhn', 'asset_id': 'COCOS', 'fee_paying_account': '1.2.18', 'owner': '1.2.18'}]], 'signatures': ['1f713f338027583d7c7f0dac34047bace2666a806a0c9787fd5474928619de66a41877acd970543816c6e6f76a72d0038ee976cc3cd5d517ecb9078c64f20ca9c6'], 'ref_block_prefix': 125835667, 'ref_block_num': 12423, 'expiration': '2020-07-24T09:25:34', 'extensions': []}], 'jsonrpc': '2.0', 'id': 1}


>> get_transaction_by_id ['a5d942e46d3701956f20c24ebc3ea82dbab76f739fa2b8e57017f8c793700f11']

{'result': {'operations': [[40, {'base_describe': "'nh_symbol': 'UUW'", 'world_view': 'test_wvizhn', 'asset_id': 'COCOS', 'fee_paying_account': '1.2.18', 'owner': '1.2.18'}]], 'signatures': ['1f713f338027583d7c7f0dac34047bace2666a806a0c9787fd5474928619de66a41877acd970543816c6e6f76a72d0038ee976cc3cd5d517ecb9078c64f20ca9c6'], 'ref_block_prefix': 125835667, 'ref_block_num': 12423, 'expiration': '2020-07-24T09:25:34', 'extensions': [], 'operation_results': [[2, {'result': '4.2.781956', 'real_running_time': 75, 'fees': [{'asset_id': '1.3.1', 'amount': 10000}]}]]}, 'jsonrpc': '2.0', 'id': 1}


tx_id: a5d942e46d3701956f20c24ebc3ea82dbab76f739fa2b8e57017f8c793700f11, result: [[2, {'result': '4.2.781956', 'real_running_time': 75, 'fees': [{'asset_id': '1.3.1', 'amount': 10000}]}]]
>> create_nh_asset ['faucet1', 'faucet1', 'COCOS', 'test_wvizhn', "'nh_symbol': 'RPUTR'", True]

{'result': ['2828450e7f458d629152d975740ab83823907c38ea455ca75ea7dd805ff5df6d', {'operations': [[40, {'base_describe': "'nh_symbol': 'RPUTR'", 'world_view': 'test_wvizhn', 'asset_id': 'COCOS', 'fee_paying_account': '1.2.18', 'owner': '1.2.18'}]], 'signatures': ['1f60b6bcf3bc9bded712fb150669a9efa90c406e68be564c3d3c107f03752b419c52bdb37123d0d45e884ee8975ae856534df2db80179dafe0cabac240b1ead411'], 'ref_block_prefix': 2495659418, 'ref_block_num': 12425, 'expiration': '2020-07-24T09:25:40', 'extensions': []}], 'jsonrpc': '2.0', 'id': 1}


>> get_transaction_by_id ['2828450e7f458d629152d975740ab83823907c38ea455ca75ea7dd805ff5df6d']

{'result': {'operations': [[40, {'base_describe': "'nh_symbol': 'RPUTR'", 'world_view': 'test_wvizhn', 'asset_id': 'COCOS', 'fee_paying_account': '1.2.18', 'owner': '1.2.18'}]], 'signatures': ['1f60b6bcf3bc9bded712fb150669a9efa90c406e68be564c3d3c107f03752b419c52bdb37123d0d45e884ee8975ae856534df2db80179dafe0cabac240b1ead411'], 'ref_block_prefix': 2495659418, 'ref_block_num': 12425, 'expiration': '2020-07-24T09:25:40', 'extensions': [], 'operation_results': [[2, {'result': '4.2.781980', 'real_running_time': 42, 'fees': [{'asset_id': '1.3.1', 'amount': 10000}]}]]}, 'jsonrpc': '2.0', 'id': 1}


tx_id: 2828450e7f458d629152d975740ab83823907c38ea455ca75ea7dd805ff5df6d, result: [[2, {'result': '4.2.781980', 'real_running_time': 42, 'fees': [{'asset_id': '1.3.1', 'amount': 10000}]}]]
>> create_nh_asset ['faucet1', 'faucet1', 'COCOS', 'test_wvizhn', "{'name':'ChinaJoy 2020 NFT门票','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy 首套NFT门票，仅供ChinaJoy Plus 2020上线期间使用，该门票不可进入ChinaJoy线下展会。'}", True]

{'result': ['21957640c91d3ef297b25990cae952fc749d4db4b94931a41be09dab8eadd61e', {'operations': [[40, {'base_describe': "{'name':'ChinaJoy 2020 NFTu95e8u7968','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy u9996u5957NFTu95e8u7968uff0cu4ec5u4f9bChinaJoy Plus 2020u4e0au7ebfu671fu95f4u4f7fu7528uff0cu8be5u95e8u7968u4e0du53efu8fdbu5165ChinaJoyu7ebfu4e0bu5c55u4f1au3002'}", 'world_view': 'test_wvizhn', 'asset_id': 'COCOS', 'fee_paying_account': '1.2.18', 'owner': '1.2.18'}]], 'signatures': ['1f73acb40ca9f759c4f0ba3dc0116dc7945a76c9e00c0e301794fbbdd9f8f1c2cf0c9a1e3ae840832e010b29832a22d5c9efec0cf7e664f28e4bebb99a738a2a65'], 'ref_block_prefix': 1143975881, 'ref_block_num': 12430, 'expiration': '2020-07-24T09:25:46', 'extensions': []}], 'jsonrpc': '2.0', 'id': 1}


>> get_transaction_by_id ['21957640c91d3ef297b25990cae952fc749d4db4b94931a41be09dab8eadd61e']

{'result': {'operations': [[40, {'base_describe': "{'name':'ChinaJoy 2020 NFTu95e8u7968','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy u9996u5957NFTu95e8u7968uff0cu4ec5u4f9bChinaJoy Plus 2020u4e0au7ebfu671fu95f4u4f7fu7528uff0cu8be5u95e8u7968u4e0du53efu8fdbu5165ChinaJoyu7ebfu4e0bu5c55u4f1au3002'}", 'world_view': 'test_wvizhn', 'asset_id': 'COCOS', 'fee_paying_account': '1.2.18', 'owner': '1.2.18'}]], 'signatures': ['1f73acb40ca9f759c4f0ba3dc0116dc7945a76c9e00c0e301794fbbdd9f8f1c2cf0c9a1e3ae840832e010b29832a22d5c9efec0cf7e664f28e4bebb99a738a2a65'], 'ref_block_prefix': 1143975881, 'ref_block_num': 12430, 'expiration': '2020-07-24T09:25:46', 'extensions': [], 'operation_results': [[2, {'result': '4.2.782003', 'real_running_time': 36, 'fees': [{'asset_id': '1.3.1', 'amount': 10000}]}]]}, 'jsonrpc': '2.0', 'id': 1}


tx_id: 21957640c91d3ef297b25990cae952fc749d4db4b94931a41be09dab8eadd61e, result: [[2, {'result': '4.2.782003', 'real_running_time': 36, 'fees': [{'asset_id': '1.3.1', 'amount': 10000}]}]]
>> create_nh_asset ['faucet1', 'faucet1', 'COCOS', 'test_wvizhn', "{'name':'ChinaJoy 2020 NFT门票','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy 首套NFT门票，仅供ChinaJoy Plus 2020上线期间使用，该门票不可进入ChinaJoy线下展会'}", True]

{'result': ['3bd20e80a329764e42a065f1f9c8583447586c1116b3c668153e647d490b472e', {'operations': [[40, {'base_describe': "{'name':'ChinaJoy 2020 NFTu95e8u7968','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy u9996u5957NFTu95e8u7968uff0cu4ec5u4f9bChinaJoy Plus 2020u4e0au7ebfu671fu95f4u4f7fu7528uff0cu8be5u95e8u7968u4e0du53efu8fdbu5165ChinaJoyu7ebfu4e0bu5c55u4f1a'}", 'world_view': 'test_wvizhn', 'asset_id': 'COCOS', 'fee_paying_account': '1.2.18', 'owner': '1.2.18'}]], 'signatures': ['1f38094fd1bac76dec1a96c05cb31ffbab455afb6ca08d032352fee3de1f40908b51e0561b00423b7d0468e7d9c971dbcb9f03af48df70fecbcd5f82998e784269'], 'ref_block_prefix': 903109030, 'ref_block_num': 12433, 'expiration': '2020-07-24T09:25:52', 'extensions': []}], 'jsonrpc': '2.0', 'id': 1}


>> get_transaction_by_id ['3bd20e80a329764e42a065f1f9c8583447586c1116b3c668153e647d490b472e']

{'result': {'operations': [[40, {'base_describe': "{'name':'ChinaJoy 2020 NFTu95e8u7968','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy u9996u5957NFTu95e8u7968uff0cu4ec5u4f9bChinaJoy Plus 2020u4e0au7ebfu671fu95f4u4f7fu7528uff0cu8be5u95e8u7968u4e0du53efu8fdbu5165ChinaJoyu7ebfu4e0bu5c55u4f1a'}", 'world_view': 'test_wvizhn', 'asset_id': 'COCOS', 'fee_paying_account': '1.2.18', 'owner': '1.2.18'}]], 'signatures': ['1f38094fd1bac76dec1a96c05cb31ffbab455afb6ca08d032352fee3de1f40908b51e0561b00423b7d0468e7d9c971dbcb9f03af48df70fecbcd5f82998e784269'], 'ref_block_prefix': 903109030, 'ref_block_num': 12433, 'expiration': '2020-07-24T09:25:52', 'extensions': [], 'operation_results': [[2, {'result': '4.2.782023', 'real_running_time': 79, 'fees': [{'asset_id': '1.3.1', 'amount': 10000}]}]]}, 'jsonrpc': '2.0', 'id': 1}


tx_id: 3bd20e80a329764e42a065f1f9c8583447586c1116b3c668153e647d490b472e, result: [[2, {'result': '4.2.782023', 'real_running_time': 79, 'fees': [{'asset_id': '1.3.1', 'amount': 10000}]}]]
>> create_nh_asset ['faucet1', 'faucet1', 'COCOS', 'test_wvizhn', "{'name':'ChinaJoy 2020 NFT门票','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy 首套NFT门票，仅供ChinaJoy Plus 2020上线期间使用，该门票不可进入ChinaJoy线下展会。。。。。。。。。。。。'}", True]

{'result': ['4f4a3e2120783f4bd944931689976af7a96ea99781d4c4920ce9bd025dd9a1fd', {'operations': [[40, {'base_describe': "{'name':'ChinaJoy 2020 NFTu95e8u7968','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy u9996u5957NFTu95e8u7968uff0cu4ec5u4f9bChinaJoy Plus 2020u4e0au7ebfu671fu95f4u4f7fu7528uff0cu8be5u95e8u7968u4e0du53efu8fdbu5165ChinaJoyu7ebfu4e0bu5c55u4f1au3002u3002u3002u3002u3002u3002u3002u3002u3002u3002u3002u3002'}", 'world_view': 'test_wvizhn', 'asset_id': 'COCOS', 'fee_paying_account': '1.2.18', 'owner': '1.2.18'}]], 'signatures': ['1f226fdeaad1be63c561452f8f6247525c3f3c4a778d8fb53b25ac61aea289a69708dea5ab8e8f5988072d579402c6e72b52a051e7b14d282e610cd37882cd3d60'], 'ref_block_prefix': 3071764569, 'ref_block_num': 12436, 'expiration': '2020-07-24T09:25:58', 'extensions': []}], 'jsonrpc': '2.0', 'id': 1}


>> get_transaction_by_id ['4f4a3e2120783f4bd944931689976af7a96ea99781d4c4920ce9bd025dd9a1fd']

{'result': {'operations': [[40, {'base_describe': "{'name':'ChinaJoy 2020 NFTu95e8u7968','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy u9996u5957NFTu95e8u7968uff0cu4ec5u4f9bChinaJoy Plus 2020u4e0au7ebfu671fu95f4u4f7fu7528uff0cu8be5u95e8u7968u4e0du53efu8fdbu5165ChinaJoyu7ebfu4e0bu5c55u4f1au3002u3002u3002u3002u3002u3002u3002u3002u3002u3002u3002u3002'}", 'world_view': 'test_wvizhn', 'asset_id': 'COCOS', 'fee_paying_account': '1.2.18', 'owner': '1.2.18'}]], 'signatures': ['1f226fdeaad1be63c561452f8f6247525c3f3c4a778d8fb53b25ac61aea289a69708dea5ab8e8f5988072d579402c6e72b52a051e7b14d282e610cd37882cd3d60'], 'ref_block_prefix': 3071764569, 'ref_block_num': 12436, 'expiration': '2020-07-24T09:25:58', 'extensions': [], 'operation_results': [[2, {'result': '4.2.782048', 'real_running_time': 128, 'fees': [{'asset_id': '1.3.1', 'amount': 10000}]}]]}, 'jsonrpc': '2.0', 'id': 1}


tx_id: 4f4a3e2120783f4bd944931689976af7a96ea99781d4c4920ce9bd025dd9a1fd, result: [[2, {'result': '4.2.782048', 'real_running_time': 128, 'fees': [{'asset_id': '1.3.1', 'amount': 10000}]}]]
>> create_nh_asset ['faucet1', 'faucet1', 'COCOS', 'test_wvizhn', "'nh_symbol': 'UIOBCWL'", True]

{'result': ['f119ca243dacdad329924f0dddc5d5475056803a50262b08e533789b9d12d42e', {'operations': [[40, {'base_describe': "'nh_symbol': 'UIOBCWL'", 'world_view': 'test_wvizhn', 'asset_id': 'COCOS', 'fee_paying_account': '1.2.18', 'owner': '1.2.18'}]], 'signatures': ['2033950947c9f570cd2edf34997db679ad8461076463cb8eaf60b895d4df3243675669c324391b171d4e12f8ef6c348b599f22004a911d1757f482d9c69ddd5c8b'], 'ref_block_prefix': 3722394824, 'ref_block_num': 12439, 'expiration': '2020-07-24T09:26:04', 'extensions': []}], 'jsonrpc': '2.0', 'id': 1}


>> get_transaction_by_id ['f119ca243dacdad329924f0dddc5d5475056803a50262b08e533789b9d12d42e']

{'result': {'operations': [[40, {'base_describe': "'nh_symbol': 'UIOBCWL'", 'world_view': 'test_wvizhn', 'asset_id': 'COCOS', 'fee_paying_account': '1.2.18', 'owner': '1.2.18'}]], 'signatures': ['2033950947c9f570cd2edf34997db679ad8461076463cb8eaf60b895d4df3243675669c324391b171d4e12f8ef6c348b599f22004a911d1757f482d9c69ddd5c8b'], 'ref_block_prefix': 3722394824, 'ref_block_num': 12439, 'expiration': '2020-07-24T09:26:04', 'extensions': [], 'operation_results': [[2, {'result': '4.2.782073', 'real_running_time': 73, 'fees': [{'asset_id': '1.3.1', 'amount': 10000}]}]]}, 'jsonrpc': '2.0', 'id': 1}


tx_id: f119ca243dacdad329924f0dddc5d5475056803a50262b08e533789b9d12d42e, result: [[2, {'result': '4.2.782073', 'real_running_time': 73, 'fees': [{'asset_id': '1.3.1', 'amount': 10000}]}]]

----------------------------
tx: a5d942e46d3701956f20c24ebc3ea82dbab76f739fa2b8e57017f8c793700f11, result: [[2, {'result': '4.2.781956', 'real_running_time': 75, 'fees': [{'asset_id': '1.3.1', 'amount': 10000}]}]]
tx: f119ca243dacdad329924f0dddc5d5475056803a50262b08e533789b9d12d42e, result: [[2, {'result': '4.2.782073', 'real_running_time': 73, 'fees': [{'asset_id': '1.3.1', 'amount': 10000}]}]]
tx: 2828450e7f458d629152d975740ab83823907c38ea455ca75ea7dd805ff5df6d, result: [[2, {'result': '4.2.781980', 'real_running_time': 42, 'fees': [{'asset_id': '1.3.1', 'amount': 10000}]}]]
tx: 3bd20e80a329764e42a065f1f9c8583447586c1116b3c668153e647d490b472e, result: [[2, {'result': '4.2.782023', 'real_running_time': 79, 'fees': [{'asset_id': '1.3.1', 'amount': 10000}]}]]
tx: 4f4a3e2120783f4bd944931689976af7a96ea99781d4c4920ce9bd025dd9a1fd, result: [[2, {'result': '4.2.782048', 'real_running_time': 128, 'fees': [{'asset_id': '1.3.1', 'amount': 10000}]}]]
tx: 21957640c91d3ef297b25990cae952fc749d4db4b94931a41be09dab8eadd61e, result: [[2, {'result': '4.2.782003', 'real_running_time': 36, 'fees': [{'asset_id': '1.3.1', 'amount': 10000}]}]]
----------------------------
test_create_nh_asset done

.>> lock []

{'result': None, 'jsonrpc': '2.0', 'id': 1}


tearDownClass done


----------------------------------------------------------------------
Ran 2 tests in 39.634s

OK (skipped=1)
```  