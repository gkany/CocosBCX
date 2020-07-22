执行过程和结果：  
``` text  
# 1. test cli_wallet api: get_global_extensions_properties
>> get_global_extensions_properties []
{'jsonrpc': '2.0', 'id': 1, 'result': {'contract_max_data_size': 2147483648, 'witness_max_votes': 11, 'committee_max_votes': 11, 'id': '2.15.0', 'contract_private_data_size': 3072, 'contract_total_data_size': 10485760}}


# 2. test vote for witness
>> get_object ['2.15.0']
{'jsonrpc': '2.0', 'id': 1, 'result': [{'contract_max_data_size': 2147483648, 'witness_max_votes': 11, 'committee_max_votes': 11, 'id': '2.15.0', 'contract_private_data_size': 3072, 'contract_total_data_size': 10485760}]}

>> get_object 2.15.0
 [{'contract_max_data_size': 2147483648, 'witness_max_votes': 11, 'committee_max_votes': 11, 'id': '2.15.0', 'contract_private_data_size': 3072, 'contract_total_data_size': 10485760}]

[{'contract_max_data_size': 2147483648, 'witness_max_votes': 11, 'committee_max_votes': 11, 'id': '2.15.0', 'contract_private_data_size': 3072, 'contract_total_data_size': 10485760}]
>> list_witnesses ['', 12]
{'jsonrpc': '2.0', 'id': 1, 'result': [['aaabp', '1.6.21'], ['alice999', '1.6.39'], ['beijing-bp', '1.6.22'], ['bigcocos', '1.6.25'], ['binancestaking', '1.6.40'], ['block-witness', '1.6.41'], ['blockchainkeys', '1.6.15'], ['chainplay-bp', '1.6.23'], ['cocos-init0', '1.6.1'], ['cocos-init1', '1.6.2'], ['cocos-init10', '1.6.11'], ['cocos-init11', '1.6.12']]}

witnesses: [['aaabp', '1.6.21'], ['alice999', '1.6.39'], ['beijing-bp', '1.6.22'], ['bigcocos', '1.6.25'], ['binancestaking', '1.6.40'], ['block-witness', '1.6.41'], ['blockchainkeys', '1.6.15'], ['chainplay-bp', '1.6.23'], ['cocos-init0', '1.6.1'], ['cocos-init1', '1.6.2'], ['cocos-init10', '1.6.11'], ['cocos-init11', '1.6.12']]
>> list_account_balances ['release1142']
{'jsonrpc': '2.0', 'id': 1, 'result': [{'amount': 4499943, 'asset_id': '1.3.0'}, {'amount': 867061, 'asset_id': '1.3.1'}]}

[{'amount': 4499943, 'asset_id': '1.3.0'}, {'amount': 867061, 'asset_id': '1.3.1'}]
>> vote_for_witness ['release1142', 'aaabp', 20, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['4cd75ef8f952262841ac9922919390af4f55b093d97a40ab31e63ecfdd2ac15c', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['1:0', '1:1', '1:10', '1:27', '1:35', '1:37', '1:38', '1:41', '1:72', '1:74', '1:76'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 20, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:58', 'extensions': [], 'signatures': ['1f3733f93368172d982763ccf032ac1f5cb78eb566e4cde29e227ad212201c642a4def9cc52759886a38ddccab66499b74da24bff9e75457cb493974048f1ade3a'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_witness ['release1142', 'alice999', 14, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['a316847e488d5d2c63d7578a87be44e9104c83e9447a478f2c42ba3cb8990fd5', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['1:0', '1:1', '1:10', '1:27', '1:35', '1:37', '1:38', '1:41', '1:72', '1:74', '1:76'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 14, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:58', 'extensions': [], 'signatures': ['204fd168d2131240762e6a1e1ea9a64da3c1a28b6a6a6c9b3d4942c2e78e5f60340916381724074503a6a27193be5f6a719b99b3821c91d35df59564a413a780c2'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_witness ['release1142', 'beijing-bp', 20, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['f1e954645f1e33467711cb5d8efb66d85230ec86c0e31cfed85fe3dc5591ed63', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['1:0', '1:1', '1:10', '1:27', '1:35', '1:37', '1:38', '1:41', '1:72', '1:74', '1:76'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 20, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:59', 'extensions': [], 'signatures': ['1f76dd4b98d887581bcb4d3a082a5ab01f9794923b587454a960900ef71d11f664394b79892d2fd45320fa952c759487d124ad8f59657adbed9df2f6e754b7d91d'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_witness ['release1142', 'bigcocos', 9, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['7c43f02889425fa9a8b820d0aeda62a6082e2b4f61c628aecbe09b0a44f1c302', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['1:0', '1:1', '1:10', '1:27', '1:35', '1:37', '1:38', '1:41', '1:72', '1:74', '1:76'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 9, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:58', 'extensions': [], 'signatures': ['1f367c97859ac8ba99d6de10e4ce784b4db0d22a54549e43145d32d34a2fad8edc3d0dd584dbaf60f56518904c513ee314b064943f7c9a3dbb1726ab7784f30c0f'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_witness ['release1142', 'binancestaking', 7, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['60ecc19b8824eb5a23fa2e06bd7f7b5868a5635703ff508bec260468ea9f461b', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['1:0', '1:1', '1:10', '1:27', '1:35', '1:37', '1:38', '1:41', '1:72', '1:74', '1:76'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 7, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:58', 'extensions': [], 'signatures': ['206b0de6523ed13a7687df22b4bbb8e52052dba18ac6816bc72d0944f1cec41da810c025113dab8644f04e13fcd073357a36f6fe02117ee9ab6a296d320223f9cc'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_witness ['release1142', 'block-witness', 7, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['fda2f0343c960cf4d4e80ed930c4b0d105e72a75c8660703088a466f7ce17deb', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['1:0', '1:1', '1:10', '1:27', '1:35', '1:37', '1:38', '1:41', '1:72', '1:74', '1:76'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 7, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:59', 'extensions': [], 'signatures': ['2036ee0d38936a428c9000f00171975f8861943182b25b6014948e18a1ea8773227df18ea3b20ed57e352e7e5adf59a560f703686da22fdb2f671ea0bedf3902dd'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_witness ['release1142', 'blockchainkeys', 11, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['4d454f8931d37e58138016c5876fdd70a160b98c78d1c2a37ddb2720e9ac6c1b', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['1:0', '1:1', '1:10', '1:27', '1:35', '1:37', '1:38', '1:41', '1:72', '1:74', '1:76'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 11, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:58', 'extensions': [], 'signatures': ['207469ed083abee2ee52ce495d6b4bbef68a72b1834fd2d04866b9b83b3f0fa8ba5768bfb322cbc3941963dcde5ffda00568e5d465e6f3b14503f5d96a1dadca61'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_witness ['release1142', 'chainplay-bp', 4, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['61b881d27127e22d203d06b8a9e726513407945ea83e59a7de0be23be2d96f40', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['1:0', '1:1', '1:10', '1:27', '1:35', '1:37', '1:38', '1:41', '1:72', '1:74', '1:76'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 4, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:58', 'extensions': [], 'signatures': ['202c122fa9059f74a8b8cf4e2b69d6654545aca7b8463d7969df027229707eb17e0444ac51a4afe3911c585ceeec3a5d79893dc989e2180f3a8e0849e40461bd70'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_witness ['release1142', 'cocos-init0', 16, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['53a223acf689247afede2857c7f5ecaa9121cb52a7d8d5ea41662d56cf432107', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['1:0', '1:1', '1:10', '1:27', '1:35', '1:37', '1:38', '1:41', '1:72', '1:74', '1:76'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 16, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:58', 'extensions': [], 'signatures': ['204c31544c9ebebc3bd5d3c1f0e89ba5d8f56ba44318ccd3ec1ff22ec8cbd8b74f23e664ea9b069d42d049e8519ff1054d0687349b5420ace970de855e5f857d28'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_witness ['release1142', 'cocos-init1', 19, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['7425adbeefca757c7afcaf7bbd5dd2826197a4f01f11ef1db48c4f9e87da0ff6', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['1:0', '1:1', '1:10', '1:27', '1:35', '1:37', '1:38', '1:41', '1:72', '1:74', '1:76'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 19, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:58', 'extensions': [], 'signatures': ['1f522fc8ad1996e365f4474dd2f88ecae8f092d8050edc108c776837e2056f58807a0450720a4613de3fece47155b0f452f6757855c95b23379d0e2202be0b3f9b'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_witness ['release1142', 'cocos-init10', 17, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['0dd5e2e5d09445aa2f7aa5971bbe95143963f7fd4d1d808fc82a347bba3ba663', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['1:0', '1:1', '1:10', '1:27', '1:35', '1:37', '1:38', '1:41', '1:72', '1:74', '1:76'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 17, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:58', 'extensions': [], 'signatures': ['1f463ff78c37eb074f41eb5d6feb9083780f54bea5a3a1de89da100e3c01e2ceb71764e9995c29513534a2014e3bcf8ad1e39d42edeebfa597b123615ee000d934'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_witness ['release1142', 'cocos-init11', 11, True]
{'jsonrpc': '2.0', 'id': 1, 'error': {'code': 1, 'message': 'unspecified: Assert Exception: num_witness <= witness_number_of_vote: Voted for more witnesses than currently allowed (11)'}}

KeyError('result',)

# 3. test vote for committee
>> get_object ['2.15.0']
{'jsonrpc': '2.0', 'id': 1, 'result': [{'contract_max_data_size': 2147483648, 'witness_max_votes': 11, 'committee_max_votes': 11, 'id': '2.15.0', 'contract_private_data_size': 3072, 'contract_total_data_size': 10485760}]}

>> get_object 2.15.0
 [{'contract_max_data_size': 2147483648, 'witness_max_votes': 11, 'committee_max_votes': 11, 'id': '2.15.0', 'contract_private_data_size': 3072, 'contract_total_data_size': 10485760}]

[{'contract_max_data_size': 2147483648, 'witness_max_votes': 11, 'committee_max_votes': 11, 'id': '2.15.0', 'contract_private_data_size': 3072, 'contract_total_data_size': 10485760}]
>> list_committee_members ['', 12]
{'jsonrpc': '2.0', 'id': 1, 'result': [['aaabp', '1.5.14'], ['admin', '1.5.27'], ['alice999', '1.5.34'], ['australia-nodes', '1.5.26'], ['bakkt', '1.5.33'], ['beijing-bp', '1.5.15'], ['binancestaking', '1.5.35'], ['blockchainkeys', '1.5.13'], ['chainplay', '1.5.28'], ['cocos-club', '1.5.24'], ['cocos-coffee', '1.5.25'], ['cocos-init0', '1.5.0']]}

committees: [['aaabp', '1.5.14'], ['admin', '1.5.27'], ['alice999', '1.5.34'], ['australia-nodes', '1.5.26'], ['bakkt', '1.5.33'], ['beijing-bp', '1.5.15'], ['binancestaking', '1.5.35'], ['blockchainkeys', '1.5.13'], ['chainplay', '1.5.28'], ['cocos-club', '1.5.24'], ['cocos-coffee', '1.5.25'], ['cocos-init0', '1.5.0']]
>> list_account_balances ['release1142']
{'jsonrpc': '2.0', 'id': 1, 'result': [{'amount': 4499915, 'asset_id': '1.3.0'}, {'amount': 861451, 'asset_id': '1.3.1'}]}

[{'amount': 4499915, 'asset_id': '1.3.0'}, {'amount': 861451, 'asset_id': '1.3.1'}]
>> vote_for_committee_member ['release1142', 'aaabp', 15, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['08440fbb3d493d2af2a09292af5ead58aca605d9e3bd61fc28e5d299a5b58cd1', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['0:32', '0:36', '0:61', '0:62', '0:69', '0:73'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 15, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:58', 'extensions': [], 'signatures': ['1f33f5a32799a8ff8f3ba7694254ede8c7dc1c9289134d4e973341aa388d4d136a3e3da377dbb9e7cbf706370ae71ba64fafaf7390b2bb9cfdb0352e80267e1ff2'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_committee_member ['release1142', 'admin', 18, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['e6ab9123cbeb6cea59806cd1a6157209cfa79eeddd74a1f63cba2893510bfd75', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['0:32', '0:36', '0:61', '0:62', '0:69', '0:73'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 18, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:58', 'extensions': [], 'signatures': ['1f1851b93810972a57aa7c30e3864d8a220bc8a4b236cc0e06cc8a2c53f949333976ed15541e0f1057f66da82089687fcc9c59bfb61d786aee73c9b763c4bbd145'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_committee_member ['release1142', 'alice999', 3, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['084ed90fa405442607e8912877ae7d50b3ea3255a541fd354303c5ae33656451', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['0:32', '0:36', '0:61', '0:62', '0:69', '0:73'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 3, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:58', 'extensions': [], 'signatures': ['1f099bbf31e78c6ff78bb3bc9104dfdd2c3c03bbb8c88449c93c999467fe24f70c03a047cfa80bc1725f63dbc64554dfcb57856fcda015e33833e171844401ebab'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_committee_member ['release1142', 'australia-nodes', 10, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['607c2bf51753c4893e8b8dfce19e314db3d415414f7fac87a74af001fc376c6f', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['0:32', '0:36', '0:61', '0:62', '0:69', '0:73'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 10, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:58', 'extensions': [], 'signatures': ['207502f6e1c85cda2cb02873bbc5afc0739e503e64593ff6ae0c67af4e0692a8f60c0886b67c9a841eeea5a528cf7e403457273cc41c989ecc575e543ac01aaf92'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_committee_member ['release1142', 'bakkt', 20, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['37ccca6aa8f9933600fc4730cb0171590234ee0e9cb44ea4285623d5aee90db0', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['0:32', '0:36', '0:61', '0:62', '0:69', '0:73'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 20, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:58', 'extensions': [], 'signatures': ['20502aebc305001a9bd316400557504c4fa4234a258ec3c09b0d8d3eb22ad8cdde1394031dda31be61863beed9f933a78f1c3fe1a592dc54ca45f1f2a4f05a2d6a'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_committee_member ['release1142', 'beijing-bp', 3, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['6c86720b2e0e95c866ccdf6ec6695362c45eee6738cd01a53676d7cacd0ad02f', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['0:32', '0:36', '0:61', '0:62', '0:69', '0:73'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 3, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:59', 'extensions': [], 'signatures': ['20168c61bc5fa96be7cc3fc1fb3dc83c2d54cfb5c324e7cb8ca1a110bb856619e7742fd69c7e837678d6f27b89f8a277bd86b9fb4f722f0e1407490cf84af4643e'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_committee_member ['release1142', 'binancestaking', 7, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['9d6cebed0d5e4ae73a8fa4bdac1391cb4a3ceae56eee829a5f68354de083e59c', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['0:32', '0:36', '0:61', '0:62', '0:69', '0:73', '0:75'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 7, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:58', 'extensions': [], 'signatures': ['2010c59e690bbe375d1617da708c58d241c68c263a8775cfc4a908d2ba817a988d252e0d61613b8e1aa185a67232c5a7e973f88784c4f665e00a53d51a1ecb6bfe'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_committee_member ['release1142', 'blockchainkeys', 20, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['1f974bc7b0bd7088691616a409e2ace50bc8d7b6e1db8f5fe6564e3ad60968b0', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['0:28', '0:32', '0:36', '0:61', '0:62', '0:69', '0:73', '0:75'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 20, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:58', 'extensions': [], 'signatures': ['205a092394627f2925d7414b2e60bf21ec0f8d41a8b3f1cc172c79d4ef25af844376e2737281624d589477093f7cdf1452ff0f6f172591b52f9a35c62099ec633d'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_committee_member ['release1142', 'chainplay', 9, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['baf00e8ac5214b5ea8d43cb154fa86c2403f945bf2620cf4afdc535cce94d92f', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['0:28', '0:32', '0:36', '0:61', '0:62', '0:63', '0:69', '0:73', '0:75'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 9, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:58', 'extensions': [], 'signatures': ['1f641ca07790795e38579013f6bfa0295335cb8c52d026b7edcd849d146bcc58cf3d6d4f3c66a4be47b7dd9fa581a1be10ae2ae16674c1caae58b81e3107565eb6'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_committee_member ['release1142', 'cocos-club', 6, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['a453289b1b77a219766ae1b27e77cd022e8e6bc748c7b6a1b83e889fdec984bc', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['0:28', '0:32', '0:36', '0:58', '0:61', '0:62', '0:63', '0:69', '0:73', '0:75'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 6, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:58', 'extensions': [], 'signatures': ['1f722a291fd983abe87353ad7b60e5f6a0d2decbd186a52d456b663a7ea17be5f009c99769c1ef24d59545e1770a558fd66449aafe8a23264b3b7976dcd195dc10'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_committee_member ['release1142', 'cocos-coffee', 18, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['b7a6a30bf4792597d460a81070262f1caa567de02d46633cb1dc362e06fdffa6', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': ['0:28', '0:32', '0:36', '0:58', '0:59', '0:61', '0:62', '0:63', '0:69', '0:73', '0:75'], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 18, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:37:58', 'extensions': [], 'signatures': ['207dad66bf548e0752c34a28ba763096df370ba92a322d47f487d6d8120a71ab1165ece7a39d5d6c3be6732270436367e1048bd304bde4e9ff0812803f59a4e752'], 'ref_block_num': 62886, 'ref_block_prefix': 4283854778}]}

>> vote_for_committee_member ['release1142', 'cocos-init0', 10, True]
{'jsonrpc': '2.0', 'id': 1, 'error': {'code': 1, 'message': 'unspecified: Assert Exception: num_committee <= committee_number_of_vote: Voted for more committee members than currently allowed (11)'}}

KeyError('result',)

# 4. test cancle vote for witness
>> vote_for_witness ['release1142', 'aaabp', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['969c2f2fd20949523b358f86d48d6ec43fbabf385422ca8f6a28329427068704', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:08', 'extensions': [], 'signatures': ['1f3196186bf0325aa95ccb64ba926776914291d3b8c2f3b692528932aad76813a87cb95cdf3b6508bba3c553d0e05b89373c5d8ff0886c16e9d0275c61883f3646'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_witness ['release1142', 'alice999', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['bb1d15c63de40808e11a02cfe266eb4491e3fb05ed6ad1df5ae64ea326feb6b9', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:09', 'extensions': [], 'signatures': ['20309a8e4e2d2e70420c66d7e489ad572443684f0023de2e5a037cf1a10831c75a68cf192a0d62165bbb641240a2ccc071fe14883d6304a8dedee05b68725e3aa6'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_witness ['release1142', 'beijing-bp', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['fac620743e158db841c598867656a1343c5a3cc131d65b819c70e103d63922b2', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:10', 'extensions': [], 'signatures': ['1f4cae5e599f3d235ed143b8867144d5581033110b417ad639c1cfe98039c9215332c5cdb6ae411bece60698f646e63c99c01884a50391a2b39707418b6823313f'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_witness ['release1142', 'bigcocos', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['89a77b7a01a02e4cedba1a0c5b9393c4417b2e053b151bb45d2ab96d6237653a', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:11', 'extensions': [], 'signatures': ['1f0ba9a92f18676014bfa2493a27c283a83f8c5e9323e85233794ae0110b57acbc153b2150996d56c8060c16293bc38eb45080ad5092aae4d11fbae743f0c23a78'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_witness ['release1142', 'binancestaking', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['76a1d33da3def962bea6f3b9c42d99bf254547208f63ddabcee7fe80aa8ca369', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:12', 'extensions': [], 'signatures': ['2014c4b2bdf0632abcbf789325d377092b0ee4932cfbdf1933e4b8d62cbdd548d45f0b6485d427fbd6da59174c34c50d015600c067ef7d3407e0c681013a19592c'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_witness ['release1142', 'block-witness', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['ff4016f29f98962dd9d6be5e75dd98c2724d9fd762002edb7097845cd4183b4b', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:13', 'extensions': [], 'signatures': ['205b97db12be46e49d6294f81e9ff1dda34275a796569727280be5a964bd03483d4b7f0a4d85da6487915cf4aaac4111c330f1b07223ec76d8a937511a7d11b612'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_witness ['release1142', 'blockchainkeys', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['a1922cba739b9bd22e8f4df1db7c1c619e47189e6fd2b3f8db5eef41bd043772', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:14', 'extensions': [], 'signatures': ['1f4ee9c03c03ade40828d18f58b4a9293fb78a214a722d14c1b1005ddc4e413897675180345094a54f4350683b1a04a0ef1f385d3ad0d57356dc1b6c2d7a8e32b1'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_witness ['release1142', 'chainplay-bp', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['2c167bee38b9c85081d91d52549c84fe1a960c1dd9804b1739edeeb12f252f0d', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:15', 'extensions': [], 'signatures': ['1f21acb12c343bb976bca6128d06ff2c8e182940039a9c14af286a295d5171cfba4e1222875d7bce64eafb9fbeb703b13b06baacdfe45e9e3f5ec63d0690b97ddb'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_witness ['release1142', 'cocos-init0', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['0a80807bff695d88d0a5c868192c8ad4da767de3a8148c459bbaf97db9b6dc56', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:16', 'extensions': [], 'signatures': ['1f1886d4c136236a6543eb464109c85d3405e48be71cd76518b3aa365f0097d47b2638d860d67e2f1e1ebacef83a159eb41586eabd21475337609ed00feca7d619'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_witness ['release1142', 'cocos-init1', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['354d32cbe017a7e85325e59b1c6b00ae50426a9ce7ddb3b572cb817fcc26277e', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:17', 'extensions': [], 'signatures': ['1f68e6010524cee8f190458b216ababa599e2e4c861554e0d106b524bf38a36982266255d555ff1df5012c55830e5331c4d25a89f3e7eb177de9cf933e3deeaf95'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_witness ['release1142', 'cocos-init10', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['222496e94f34a215211b91ca7270618426cf919084cd2df7ddd61a1f9ed58a64', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:18', 'extensions': [], 'signatures': ['1f5a3e7414a2f27ad8865af762bc62a104d3ee172622deddb802446c9a084dc9ea2a11f1765eaa89cfedb65c3d13b1c18fd7529f08cb648f533495ebca26b8a392'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_witness ['release1142', 'cocos-init11', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['731891c1438296ae175ecaa9d5cc5b9b8526da08e3c3cbb628eae7a8bbdff176', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:19', 'extensions': [], 'signatures': ['2043bcea49c87aeead3773b3bbbdc8ac70b249740bb030c415f6a006e89c1d324b23c1172ced6045893499c929fc52e04a3c4f8a01360e47aa4e9abdf0861729ff'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}


# 5. test  cancle vote for committee
>> vote_for_committee_member ['release1142', 'aaabp', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['323aef106557ffa863841da9ca0931cff3fd57cc902f245852723b9bba251859', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:08', 'extensions': [], 'signatures': ['207ef65d1041843a7842bd716738c4639f89a67a25e257274be98ce84d29092f6a18975894a72418228b0d747b6868e05befcce92f73b6272dc9c1e84bc6749965'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_committee_member ['release1142', 'admin', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['864af4c5160f816a10b3dde9c32ecea5e6b01cc16e39d491101c04e7ec44bcf7', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:09', 'extensions': [], 'signatures': ['2012f9630a511b78a12d8953cbba7e1d43b7ca87086b8bf9722ae88f211fdf86766d72986e69b3a6e553ac80341804eb98759337676a47191fab2779325b5d8f2c'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_committee_member ['release1142', 'alice999', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['85586d5204ca2285e595bba52588cc62303e41e56e17281e6c2246b13b25bfb1', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:10', 'extensions': [], 'signatures': ['2031ea34c707d8eaceff5b6e2f7f6c5359abb3aace3eecfaa3bb0b80f4c86a0be75f72e96a9554b622e63e48de9a6e0397b6d7db882a18c5fc1314d03ef96c886d'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_committee_member ['release1142', 'australia-nodes', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['ae2b2be6381fdc44ba504d1f3fb0832ba06f720427167e777b2e52b180791be1', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:11', 'extensions': [], 'signatures': ['1f337681fcd76ff68cd71f5bd04a54eff64bcd909cd893470949d46b644840d79b7214b8bfb7ca5d704762c16b3f12ad50d837c623d4a0a36d8775f74ef6c73e2d'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_committee_member ['release1142', 'bakkt', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['3e30778f27c01b2e3e48996322e3b9f02c1ca16811736e7888c75c6b131ca594', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:12', 'extensions': [], 'signatures': ['1f26a9d7590eab0363624f9bc7869f23ee2ad0d67d3e71d702e01e9232d7f3ed9840e3f7d20ec50f1663a99812ec2df1a67d6697a9414d04117015ee18925d1eb7'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_committee_member ['release1142', 'beijing-bp', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['fa42c1bdc3efb2472050e2208c1562075b30e7c362da2502e31f63f46d12d1a4', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:13', 'extensions': [], 'signatures': ['1f4ca653fbb30c1c85b427315d6fe4ff1a05d5f836085ca4b50d59f5e6c988115f213238ec89bc3878e092e077dafdca6ea2f3718d9984a242d4dc178e32fe3d3d'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_committee_member ['release1142', 'binancestaking', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['735d8910265c31e253871d39d7e3b23bcd93fdf533de4569562de7aa601e24e0', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:14', 'extensions': [], 'signatures': ['2006015cd8e3ed56b312c95af6d19865fd8ae74817ddda466a99ac3c278a3b052a3dd3e8ad82571998b47630a145d7e539502c1cd68ea21c522b49d1774538ed37'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_committee_member ['release1142', 'blockchainkeys', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['8e0db1376769b98675c0aa452b8c71903fa7b55a4d0eed5efe1defb304f7badc', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:15', 'extensions': [], 'signatures': ['204dfbe9cb809cf5b9c54ee11da16a338677248568c6f91c06b88a097e61920b0e514214c34dff15e91cab5189c3b0210044db0d1a4eeaa13e99394bca2546c753'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_committee_member ['release1142', 'chainplay', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['4983f8a0aff45a80d27aef955a4d8b184c426823e2e362f03dbaa61187eaac54', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:16', 'extensions': [], 'signatures': ['2055fbcbaa1f7647f34d9a65fd64126afb1dbb459b8a947cef578e20eb7edcf0cb6792c38368dfe2c1ed5bd4746aa90f7582ba87308f3e5fc6b7bc72c99a5837ff'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_committee_member ['release1142', 'cocos-club', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['5fbdfe8a3727c15a4ae265a04421bd28d78bf04a8214b36d147d484e4269117a', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:17', 'extensions': [], 'signatures': ['203d1df13c38948c9de19c07bfad52197b0293894837b3471902af1d46b110345822da65e27d332182f5f33a457dbe982ef5f12d21d190728e3dd7ec908aef03b0'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_committee_member ['release1142', 'cocos-coffee', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['64daf8cd9850024ef8dbc4ef50d9192c40a841a43ea822cf21d127cb41a0bb2c', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:18', 'extensions': [], 'signatures': ['20458f582849a9d6b9382339e5797ebee4d09ec112b34f39bc1d337f6c6923e7216ec41a0b7b0ec03a4b8c0a3a4d345da803cab9462a8136873c3b76dcebfb1401'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

>> vote_for_committee_member ['release1142', 'cocos-init0', 0, True]
{'jsonrpc': '2.0', 'id': 1, 'result': ['aec41ae078df6b8e64700d44ed729f91e96fd0a35f801fe7292598c59e821be9', {'operations': [[6, {'account': '1.2.855467', 'new_options': {'votes': [], 'extensions': [], 'memo_key': 'COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz'}, 'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}], 'extensions': {}}]], 'expiration': '2020-07-22T12:38:19', 'extensions': [], 'signatures': ['1f481ad8f86dca84c1c678b8f5633beb4a4ce9f9dfb8a4858e809e6d6b7bc6b12174ba8c3691936efdfc62b24af10677d34ea87e2362883684ff218e2068fec0c2'], 'ref_block_num': 62887, 'ref_block_prefix': 207043338}]}

test vote for xxx done
```  