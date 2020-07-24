
# 1. 修改最大投票数测试  
**测试过程和结果：**  
```  text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/release1.1.5/proposal$ python3 proposal.py 
>> get_dynamic_global_properties []
{'result': {'recent_slots_filled': '2653243411677887396011297832936923119', 'next_maintenance_time': '2020-07-23T06:30:00', 'last_irreversible_block_num': 103, 'witness_budget': 2600000000, 'current_witness': '1.6.3', 'dynamic_flags': 0, 'id': '2.1.0', 'recently_missed_count': 0, 'last_budget_time': '2020-07-23T06:20:00', 'time': '2020-07-23T06:21:36', 'head_block_id': '0000006f072e4dc5d8642e2002440ab243652283', 'current_transaction_count': 0, 'head_block_number': 111, 'current_aslot': 21000795, 'accounts_registered_this_interval': 0}, 'jsonrpc': '2.0', 'id': 1}

next_maintenance_time: 2020-07-23T06:30:00, now time: 2020-07-23T06:21:36
time_delta: 504
>> get_global_properties []
{'result': {'active_witnesses': ['1.6.1', '1.6.2', '1.6.3', '1.6.4', '1.6.5', '1.6.6', '1.6.7', '1.6.8', '1.6.9', '1.6.10', '1.6.11'], 'active_committee_members': ['1.5.0', '1.5.1', '1.5.2', '1.5.3', '1.5.4', '1.5.5', '1.5.6', '1.5.7', '1.5.8', '1.5.9', '1.5.10'], 'parameters': {'cashback_vb_period_seconds': 86400, 'witness_candidate_freeze': '5000000000000', 'cashback_vote_period_seconds': 259200, 'candidate_award_budget': '20000000000', 'account_fee_scale_bitshifts': 4, 'maximum_asset_feed_publishers': 10, 'committee_candidate_freeze': '5000000000000', 'block_interval': 2, 'maximum_block_size': 2000000, 'committee_number_of_election': 11, 'witness_number_of_election': 11, 'current_fees': {'maximun_handling_fee': 10000000, 'parameters': [[0, {'price_per_kbyte': 1000000, 'fee': 2000000}], [1, {'fee': 500000}], [2, {'fee': 0}], [3, {'fee': 2000000}], [4, {}], [5, {'premium_fee': 200000000, 'basic_fee': 500000, 'price_per_kbyte': 100000}], [6, {'price_per_kbyte': 100000, 'fee': 2000000}], [7, {'membership_annual_fee': 200000000, 'membership_lifetime_fee': 1000000000}], [8, {'long_symbol': 500000000, 'symbol4': '30000000000', 'symbol3': '50000000000', 'price_per_kbyte': 10}], [9, {'price_per_kbyte': 10, 'fee': 50000000}], [10, {'price_per_kbyte': 100000, 'fee': 2000000}], [11, {'fee': 50000000}], [12, {'fee': 50000000}], [13, {'price_per_kbyte': 100000, 'fee': 2000000}], [14, {'fee': 2000000}], [15, {'fee': 10000000}], [16, {'fee': 50000000}], [17, {'fee': 100000}], [18, {'fee': 500000000}], [19, {'fee': 2000000}], [20, {'price_per_kbyte': 10, 'fee': 2000000}], [21, {'price_per_kbyte': 10, 'fee': 2000000}], [22, {'fee': 100000}], [23, {'fee': 500000000}], [24, {'fee': 2000000}], [25, {'fee': 100000}], [26, {'fee': 100000}], [27, {'fee': 2000000}], [28, {'fee': 100000}], [29, {}], [30, {}], [31, {'fee': 2000000}], [32, {'fee': 2000000}], [33, {}], [34, {'price_per_kbyte': 1000000, 'fee': 2000000}], [35, {'price_per_millisecond': 1000000, 'price_per_kbyte': 1000000, 'fee': 2000000}], [36, {'price_per_kbyte': 1000000, 'fee': 2000000}], [37, {'fee': 100000}], [38, {'fee': 100000}], [39, {'fee': 100000}], [40, {'fee': 100000}], [41, {'fee': 100000}], [42, {'fee': 100000}], [43, {'fee': 100000}], [44, {'fee': 0}], [45, {'fee': 0}], [46, {'price_per_kbyte': 1000000, 'fee': 100000}], [47, {'price_per_related_account': 100000}], [48, {'price_per_kbyte': 1000000, 'fee': 100000}], [49, {'fee': 100000}], [50, {'price_per_kbyte': 1000000, 'fee': 2000000}], [51, {'price_per_kbyte': 10, 'fee': 2000000}], [52, {'fee': 2000000}], [53, {'fee': 2000000}], [54, {'fee': 100000}], [55, {'fee': 50000000}], [56, {'fee': 100000}], [57, {'fee': 100000}]], 'scale': 10000}, 'crontab_suspend_threshold': 3, 'committee_proposal_review_period': 120, 'extensions': [], 'unsuccessful_candidates_percent': 5000, 'witness_pay_vesting_seconds': 86400, 'maximum_time_until_expiration': 86400, 'cashback_gas_period_seconds': 86400, 'assigned_task_life_cycle': 300, 'maximum_run_time_ratio': 7500, 'maintenance_skip_slots': 3, 'max_authority_depth': 2, 'maximum_proposal_lifetime': 2419200, 'maximum_authority_membership': 10, 'maintenance_interval': 600, 'accounts_per_fee_scale': 1000, 'committee_percent_of_candidate_award': 5500, 'witness_pay_per_block': 10000000, 'worker_budget_per_day': '50000000000', 'crontab_suspend_expiration': 2592000, 'maximum_nh_asset_order_expiration': 1209600}, 'id': '2.0.0', 'next_available_vote_id': 22}, 'jsonrpc': '2.0', 'id': 1}

committee_proposal_review_period: 120
expire_time: 2020-07-23T06:28:30
>> propose_extensions_parameter_change ['init0', '2020-07-23T06:28:30', {'committee_max_votes': 7, 'witness_max_votes': 9}, True]
{'result': ['1318178eebb1714f0d005bdc7751921c79e739d68aeb35d9035a3ad90005b3ba', {'ref_block_num': 102, 'ref_block_prefix': 2765717503, 'expiration': '2020-07-23T06:42:06', 'signatures': ['1f326345c08f1e441e840e0c271db6b57c5931dc250fcfef2a137eb09edd62620321d00c1f11113e391940720ac580720909e0d9c293a7e301df27ddf917ae8995'], 'operations': [[20, {'extensions': [], 'review_period_seconds': 120, 'expiration_time': '2020-07-23T06:28:30', 'fee_paying_account': '1.2.5', 'proposed_ops': [{'op': [57, {'committee_max_votes': 7, 'contract_private_data_size': 3072, 'contract_max_data_size': 2147483648, 'contract_total_data_size': 10485760, 'witness_max_votes': 9}]}]}]], 'extensions': []}], 'jsonrpc': '2.0', 'id': 1}

tx_id: 1318178eebb1714f0d005bdc7751921c79e739d68aeb35d9035a3ad90005b3ba
>> get_transaction_in_block_info ['1318178eebb1714f0d005bdc7751921c79e739d68aeb35d9035a3ad90005b3ba']
{'result': {'trx_hash': '1318178eebb1714f0d005bdc7751921c79e739d68aeb35d9035a3ad90005b3ba', 'trx_in_block': 0, 'id': '3.1.2', 'block_num': 112}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info 1318178eebb1714f0d005bdc7751921c79e739d68aeb35d9035a3ad90005b3ba
 {'trx_hash': '1318178eebb1714f0d005bdc7751921c79e739d68aeb35d9035a3ad90005b3ba', 'trx_in_block': 0, 'id': '3.1.2', 'block_num': 112}

>> get_block [112]
{'result': {'block_id': '00000070344e6694e3dda078bc7f1693d51ae281', 'witness_signature': '201abde9d3e21fc3b3144517300a047db8ea554c49eb4cccf8fcb6830de5b369b8075093222d65c4b9ffa5432aab467173ead1cdeeec0c3a2ae460cf7ac758618b', 'transaction_merkle_root': '7ed34076c8024ac0a6519bbbac3a59c04363457d', 'previous': '0000006f072e4dc5d8642e2002440ab243652283', 'timestamp': '2020-07-23T06:21:38', 'witness': '1.6.4', 'transactions': [['1318178eebb1714f0d005bdc7751921c79e739d68aeb35d9035a3ad90005b3ba', {'ref_block_num': 102, 'ref_block_prefix': 2765717503, 'expiration': '2020-07-23T06:42:06', 'operation_results': [[2, {'result': '1.10.1', 'fees': [{'asset_id': '1.3.0', 'amount': 2000000}], 'real_running_time': 61}]], 'signatures': ['1f326345c08f1e441e840e0c271db6b57c5931dc250fcfef2a137eb09edd62620321d00c1f11113e391940720ac580720909e0d9c293a7e301df27ddf917ae8995'], 'operations': [[20, {'extensions': [], 'review_period_seconds': 120, 'expiration_time': '2020-07-23T06:28:30', 'fee_paying_account': '1.2.5', 'proposed_ops': [{'op': [57, {'committee_max_votes': 7, 'contract_private_data_size': 3072, 'contract_max_data_size': 2147483648, 'contract_total_data_size': 10485760, 'witness_max_votes': 9}]}]}]], 'extensions': []}]]}, 'jsonrpc': '2.0', 'id': 1}

block: {'block_id': '00000070344e6694e3dda078bc7f1693d51ae281', 'witness_signature': '201abde9d3e21fc3b3144517300a047db8ea554c49eb4cccf8fcb6830de5b369b8075093222d65c4b9ffa5432aab467173ead1cdeeec0c3a2ae460cf7ac758618b', 'transaction_merkle_root': '7ed34076c8024ac0a6519bbbac3a59c04363457d', 'previous': '0000006f072e4dc5d8642e2002440ab243652283', 'timestamp': '2020-07-23T06:21:38', 'witness': '1.6.4', 'transactions': [['1318178eebb1714f0d005bdc7751921c79e739d68aeb35d9035a3ad90005b3ba', {'ref_block_num': 102, 'ref_block_prefix': 2765717503, 'expiration': '2020-07-23T06:42:06', 'operation_results': [[2, {'result': '1.10.1', 'fees': [{'asset_id': '1.3.0', 'amount': 2000000}], 'real_running_time': 61}]], 'signatures': ['1f326345c08f1e441e840e0c271db6b57c5931dc250fcfef2a137eb09edd62620321d00c1f11113e391940720ac580720909e0d9c293a7e301df27ddf917ae8995'], 'operations': [[20, {'extensions': [], 'review_period_seconds': 120, 'expiration_time': '2020-07-23T06:28:30', 'fee_paying_account': '1.2.5', 'proposed_ops': [{'op': [57, {'committee_max_votes': 7, 'contract_private_data_size': 3072, 'contract_max_data_size': 2147483648, 'contract_total_data_size': 10485760, 'witness_max_votes': 9}]}]}]], 'extensions': []}]]}

tx_pair: ['1318178eebb1714f0d005bdc7751921c79e739d68aeb35d9035a3ad90005b3ba', {'ref_block_num': 102, 'ref_block_prefix': 2765717503, 'expiration': '2020-07-23T06:42:06', 'operation_results': [[2, {'result': '1.10.1', 'fees': [{'asset_id': '1.3.0', 'amount': 2000000}], 'real_running_time': 61}]], 'signatures': ['1f326345c08f1e441e840e0c271db6b57c5931dc250fcfef2a137eb09edd62620321d00c1f11113e391940720ac580720909e0d9c293a7e301df27ddf917ae8995'], 'operations': [[20, {'extensions': [], 'review_period_seconds': 120, 'expiration_time': '2020-07-23T06:28:30', 'fee_paying_account': '1.2.5', 'proposed_ops': [{'op': [57, {'committee_max_votes': 7, 'contract_private_data_size': 3072, 'contract_max_data_size': 2147483648, 'contract_total_data_size': 10485760, 'witness_max_votes': 9}]}]}]], 'extensions': []}]
[0]: 1318178eebb1714f0d005bdc7751921c79e739d68aeb35d9035a3ad90005b3ba

tx: {'ref_block_num': 102, 'ref_block_prefix': 2765717503, 'expiration': '2020-07-23T06:42:06', 'operation_results': [[2, {'result': '1.10.1', 'fees': [{'asset_id': '1.3.0', 'amount': 2000000}], 'real_running_time': 61}]], 'signatures': ['1f326345c08f1e441e840e0c271db6b57c5931dc250fcfef2a137eb09edd62620321d00c1f11113e391940720ac580720909e0d9c293a7e301df27ddf917ae8995'], 'operations': [[20, {'extensions': [], 'review_period_seconds': 120, 'expiration_time': '2020-07-23T06:28:30', 'fee_paying_account': '1.2.5', 'proposed_ops': [{'op': [57, {'committee_max_votes': 7, 'contract_private_data_size': 3072, 'contract_max_data_size': 2147483648, 'contract_total_data_size': 10485760, 'witness_max_votes': 9}]}]}]], 'extensions': []}

operation_results: [[2, {'result': '1.10.1', 'fees': [{'asset_id': '1.3.0', 'amount': 2000000}], 'real_running_time': 61}]]
propose_id: 1.10.1
>> get_object ['1.10.1']
{'result': [{'allow_execution': False, 'available_active_approvals': [], 'review_period_time': '2020-07-23T06:26:30', 'required_active_approvals': ['1.2.0'], 'trx_hash': '1318178eebb1714f0d005bdc7751921c79e739d68aeb35d9035a3ad90005b3ba', 'expiration_time': '2020-07-23T06:28:30', 'available_owner_approvals': [], 'available_key_approvals': [], 'proposed_transaction': {'ref_block_num': 0, 'extensions': ['1.10.1'], 'ref_block_prefix': 0, 'operations': [[57, {'committee_max_votes': 7, 'contract_private_data_size': 3072, 'contract_max_data_size': 2147483648, 'contract_total_data_size': 10485760, 'witness_max_votes': 9}]], 'expiration': '2020-07-23T06:28:30'}, 'id': '1.10.1', 'required_owner_approvals': []}], 'jsonrpc': '2.0', 'id': 1}

>> get_object 1.10.1
 [{'allow_execution': False, 'available_active_approvals': [], 'review_period_time': '2020-07-23T06:26:30', 'required_active_approvals': ['1.2.0'], 'trx_hash': '1318178eebb1714f0d005bdc7751921c79e739d68aeb35d9035a3ad90005b3ba', 'expiration_time': '2020-07-23T06:28:30', 'available_owner_approvals': [], 'available_key_approvals': [], 'proposed_transaction': {'ref_block_num': 0, 'extensions': ['1.10.1'], 'ref_block_prefix': 0, 'operations': [[57, {'committee_max_votes': 7, 'contract_private_data_size': 3072, 'contract_max_data_size': 2147483648, 'contract_total_data_size': 10485760, 'witness_max_votes': 9}]], 'expiration': '2020-07-23T06:28:30'}, 'id': '1.10.1', 'required_owner_approvals': []}]

propose object: [{'allow_execution': False, 'available_active_approvals': [], 'review_period_time': '2020-07-23T06:26:30', 'required_active_approvals': ['1.2.0'], 'trx_hash': '1318178eebb1714f0d005bdc7751921c79e739d68aeb35d9035a3ad90005b3ba', 'expiration_time': '2020-07-23T06:28:30', 'available_owner_approvals': [], 'available_key_approvals': [], 'proposed_transaction': {'ref_block_num': 0, 'extensions': ['1.10.1'], 'ref_block_prefix': 0, 'operations': [[57, {'committee_max_votes': 7, 'contract_private_data_size': 3072, 'contract_max_data_size': 2147483648, 'contract_total_data_size': 10485760, 'witness_max_votes': 9}]], 'expiration': '2020-07-23T06:28:30'}, 'id': '1.10.1', 'required_owner_approvals': []}]
>> transfer ['init0', 'committee-account', 3, 'COCOS', ['', False], True]
{'result': ['3124feb4e35d7bb34394de6646c8462ba42e39e4a26dd530b3e24c9a4a74b927', {'ref_block_num': 103, 'ref_block_prefix': 421427482, 'expiration': '2020-07-23T06:42:08', 'signatures': ['1f78f8073298297bbec3ec16050d97f8a052c9f2b1d1ad456fcdf16cbfd99751e208eff2b99118a096c00637d8aee9ee8f113d06cc1c938c3bae28a8ed92e184d4'], 'operations': [[0, {'amount': {'asset_id': '1.3.0', 'amount': 300000}, 'from': '1.2.5', 'extensions': [], 'to': '1.2.0'}]], 'extensions': []}], 'jsonrpc': '2.0', 'id': 1}

>> approve_proposal ['init0', '1.10.1', {'active_approvals_to_add': ['init0']}, True]
 ['575aaf0d4589b3f16f3c978eceeff8113443005d74ecdc94e0dce59678db92b1', {'ref_block_num': 103, 'ref_block_prefix': 421427482, 'expiration': '2020-07-23T06:42:08', 'signatures': ['20426272dda1e3a3b214ff1687843092cd34a28a096dec5b97ca8d1323b63acb1143e205bf1fc455a2801f870fe675f7708f3b5554f2a2de24a1b85b62e62f2713'], 'operations': [[21, {'active_approvals_to_add': ['1.2.5'], 'fee_paying_account': '1.2.5', 'proposal': '1.10.1', 'key_approvals_to_remove': [], 'extensions': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': [], 'key_approvals_to_add': [], 'owner_approvals_to_remove': []}]], 'extensions': []}]

>> approve_proposal ['init1', '1.10.1', {'active_approvals_to_add': ['init1']}, True]
 ['eb66b5269aa0b1ab9115b25d83d63e9d3041e2031d6a7370f3332b5517056968', {'ref_block_num': 103, 'ref_block_prefix': 421427482, 'expiration': '2020-07-23T06:42:08', 'signatures': ['204142add0f032fd5bdf9ea9dd3a6653a92978e6e10fa7ba0fc5e7835b408040c21844e70d07be47b7690ad31fe7e289f5b98c8baee22c42a55da0fc88495ebe89'], 'operations': [[21, {'active_approvals_to_add': ['1.2.6'], 'fee_paying_account': '1.2.6', 'proposal': '1.10.1', 'key_approvals_to_remove': [], 'extensions': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': [], 'key_approvals_to_add': [], 'owner_approvals_to_remove': []}]], 'extensions': []}]

>> approve_proposal ['init2', '1.10.1', {'active_approvals_to_add': ['init2']}, True]
 ['4518b5a2b6655a2397433a8fac89e16be2361e3f6e91d96cd2ecf904f8429133', {'ref_block_num': 103, 'ref_block_prefix': 421427482, 'expiration': '2020-07-23T06:42:08', 'signatures': ['1f6fb06c812ee022f76ec742b206e7b5cf8e9267273d00ec51718052edf8fd2886584255515a8a16c0a94b7f199b7366b61f9e1bb7a88e043fe8a20212bed9fd0e'], 'operations': [[21, {'active_approvals_to_add': ['1.2.7'], 'fee_paying_account': '1.2.7', 'proposal': '1.10.1', 'key_approvals_to_remove': [], 'extensions': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': [], 'key_approvals_to_add': [], 'owner_approvals_to_remove': []}]], 'extensions': []}]

>> approve_proposal ['init3', '1.10.1', {'active_approvals_to_add': ['init3']}, True]
 ['7523ad9b7cbf6f1b58615ac01d586ead46bc1ac26034a7eb3efdfd6ff187ab40', {'ref_block_num': 103, 'ref_block_prefix': 421427482, 'expiration': '2020-07-23T06:42:08', 'signatures': ['1f30548769065bdab580a0ecc4ba894f87bc9817d80fda1a3247ef9b0c7ccf9d0873fad8aaba8d7afef7738024a375e10cd9cd00fce724c3adff6ad01552880b0b'], 'operations': [[21, {'active_approvals_to_add': ['1.2.8'], 'fee_paying_account': '1.2.8', 'proposal': '1.10.1', 'key_approvals_to_remove': [], 'extensions': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': [], 'key_approvals_to_add': [], 'owner_approvals_to_remove': []}]], 'extensions': []}]

>> approve_proposal ['init4', '1.10.1', {'active_approvals_to_add': ['init4']}, True]
 ['fdedf784183332de22e27fd2d629defa6e8cb4257507e936b3c0c7069afda5e5', {'ref_block_num': 103, 'ref_block_prefix': 421427482, 'expiration': '2020-07-23T06:42:08', 'signatures': ['2010e2bae844eb924955a3e3a7bd6d87aa4a092d81d27b640fc56c050074d545701c4b5b8270661a000374217e80116c6aa94e00aef474150f00d6a9d34d797885'], 'operations': [[21, {'active_approvals_to_add': ['1.2.9'], 'fee_paying_account': '1.2.9', 'proposal': '1.10.1', 'key_approvals_to_remove': [], 'extensions': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': [], 'key_approvals_to_add': [], 'owner_approvals_to_remove': []}]], 'extensions': []}]

>> approve_proposal ['init5', '1.10.1', {'active_approvals_to_add': ['init5']}, True]
 ['4afff4173e804d5298511b071e162bf6ea4e2404e87c1d440a3d18b67b179dc8', {'ref_block_num': 103, 'ref_block_prefix': 421427482, 'expiration': '2020-07-23T06:42:08', 'signatures': ['1f43948908dff6b8b24ff465d18443a148e25e58f6a57abbf7ae9379367e966a5054efb395ef7a1a4e6b2c9bf62f95f32da93c284f94e6fa384dd3f440e274471f'], 'operations': [[21, {'active_approvals_to_add': ['1.2.10'], 'fee_paying_account': '1.2.10', 'proposal': '1.10.1', 'key_approvals_to_remove': [], 'extensions': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': [], 'key_approvals_to_add': [], 'owner_approvals_to_remove': []}]], 'extensions': []}]

>> approve_proposal ['init6', '1.10.1', {'active_approvals_to_add': ['init6']}, True]
 ['a30c4821bcb7b48338c96058026f282d291fe5e9452d6e159085027dc2d26642', {'ref_block_num': 103, 'ref_block_prefix': 421427482, 'expiration': '2020-07-23T06:42:08', 'signatures': ['1f47282456f1788e6fd530f56618b4de9f22b16ca8d8b3093b086ab71f7d04c97567cb3edac795fd0a8f423190e23238e82ffafe2e19bc8c21cea15889b66b1965'], 'operations': [[21, {'active_approvals_to_add': ['1.2.11'], 'fee_paying_account': '1.2.11', 'proposal': '1.10.1', 'key_approvals_to_remove': [], 'extensions': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': [], 'key_approvals_to_add': [], 'owner_approvals_to_remove': []}]], 'extensions': []}]

>> approve_proposal ['init7', '1.10.1', {'active_approvals_to_add': ['init7']}, True]
 ['f476bb6c5f493022dbbb6e77e7b7cde332e2ec47643587c38fd4f554a44ea8da', {'ref_block_num': 103, 'ref_block_prefix': 421427482, 'expiration': '2020-07-23T06:42:08', 'signatures': ['1f2d01174af398ade8c3e0196714fd9ea29752ae9e41e60f73d5f88d1c15be899c6fe508e7f751f87f6fcc33ae220dbedc3fedb3b089bef2dd79de978bc797b760'], 'operations': [[21, {'active_approvals_to_add': ['1.2.12'], 'fee_paying_account': '1.2.12', 'proposal': '1.10.1', 'key_approvals_to_remove': [], 'extensions': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': [], 'key_approvals_to_add': [], 'owner_approvals_to_remove': []}]], 'extensions': []}]

>> approve_proposal ['init8', '1.10.1', {'active_approvals_to_add': ['init8']}, True]
 ['e1d22cb5359967470041462aa9fae68d8a95918afa762124ca47962330c3f3dc', {'ref_block_num': 103, 'ref_block_prefix': 421427482, 'expiration': '2020-07-23T06:42:08', 'signatures': ['204bb9296a9d7b2de60bdf84acad5d622ad20bc459dfba2fdf832f9cd2f3ca9852044ea6aff4f8da219e7cf27671dba1427d8a6a041a89340d20cc476a69acecad'], 'operations': [[21, {'active_approvals_to_add': ['1.2.13'], 'fee_paying_account': '1.2.13', 'proposal': '1.10.1', 'key_approvals_to_remove': [], 'extensions': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': [], 'key_approvals_to_add': [], 'owner_approvals_to_remove': []}]], 'extensions': []}]

>> approve_proposal ['init9', '1.10.1', {'active_approvals_to_add': ['init9']}, True]
 ['b9cf367dbef18fa25ad7c6a9091bdb7761c6a6bd550379ded8427e0ef156642c', {'ref_block_num': 103, 'ref_block_prefix': 421427482, 'expiration': '2020-07-23T06:42:08', 'signatures': ['1f2ffed41ce65e851269c4fe70533aed3c85ce0a6f8b2bd01ba653370b369e972e691ed71a7298168530e23b37e519f445288b9705d611ddc48307c19102de76e9'], 'operations': [[21, {'active_approvals_to_add': ['1.2.14'], 'fee_paying_account': '1.2.14', 'proposal': '1.10.1', 'key_approvals_to_remove': [], 'extensions': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': [], 'key_approvals_to_add': [], 'owner_approvals_to_remove': []}]], 'extensions': []}]

>> approve_proposal ['init10', '1.10.1', {'active_approvals_to_add': ['init10']}, True]
 ['fbbf24d6cee085d5509c1f06351348ce8229b52d2f07d78544fb1278af0eb589', {'ref_block_num': 103, 'ref_block_prefix': 421427482, 'expiration': '2020-07-23T06:42:08', 'signatures': ['20513203ec5e7330db5900a2f8c37f0168b85fe9e39ee6009b1e5dd5f1798600030a4e360952875533bba159fa6bf44381633f234bdd12d28359130ded7f32eb8f'], 'operations': [[21, {'active_approvals_to_add': ['1.2.15'], 'fee_paying_account': '1.2.15', 'proposal': '1.10.1', 'key_approvals_to_remove': [], 'extensions': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': [], 'key_approvals_to_add': [], 'owner_approvals_to_remove': []}]], 'extensions': []}]

>> get_object ['1.10.1']
{'result': [{'allow_execution': True, 'available_active_approvals': ['1.2.5', '1.2.6', '1.2.7', '1.2.8', '1.2.9', '1.2.10', '1.2.11', '1.2.12', '1.2.13', '1.2.14', '1.2.15'], 'review_period_time': '2020-07-23T06:26:30', 'required_active_approvals': ['1.2.0'], 'trx_hash': '1318178eebb1714f0d005bdc7751921c79e739d68aeb35d9035a3ad90005b3ba', 'expiration_time': '2020-07-23T06:28:30', 'available_owner_approvals': [], 'available_key_approvals': [], 'proposed_transaction': {'ref_block_num': 112, 'extensions': ['1.10.1'], 'ref_block_prefix': 2489732660, 'operations': [[57, {'committee_max_votes': 7, 'contract_private_data_size': 3072, 'contract_max_data_size': 2147483648, 'contract_total_data_size': 10485760, 'witness_max_votes': 9}]], 'expiration': '2020-07-23T06:33:30'}, 'id': '1.10.1', 'required_owner_approvals': []}], 'jsonrpc': '2.0', 'id': 1}

>> get_object 1.10.1
 [{'allow_execution': True, 'available_active_approvals': ['1.2.5', '1.2.6', '1.2.7', '1.2.8', '1.2.9', '1.2.10', '1.2.11', '1.2.12', '1.2.13', '1.2.14', '1.2.15'], 'review_period_time': '2020-07-23T06:26:30', 'required_active_approvals': ['1.2.0'], 'trx_hash': '1318178eebb1714f0d005bdc7751921c79e739d68aeb35d9035a3ad90005b3ba', 'expiration_time': '2020-07-23T06:28:30', 'available_owner_approvals': [], 'available_key_approvals': [], 'proposed_transaction': {'ref_block_num': 112, 'extensions': ['1.10.1'], 'ref_block_prefix': 2489732660, 'operations': [[57, {'committee_max_votes': 7, 'contract_private_data_size': 3072, 'contract_max_data_size': 2147483648, 'contract_total_data_size': 10485760, 'witness_max_votes': 9}]], 'expiration': '2020-07-23T06:33:30'}, 'id': '1.10.1', 'required_owner_approvals': []}]

ck@ubuntu:~/xukang/CocosBCX/feature_test/release1.1.5/proposal$ 
```  
从结果看，提案创建成功  
经过一段时间后，查看结果，修改最大投票数提案已执行成功：  
``` text  
unlocked >>> 
get_object 2.15.0 
unlocked >>> get_object 2.15.0 
[{
    "id": "2.15.0",
    "witness_max_votes": 11,
    "committee_max_votes": 11,
    "contract_private_data_size": 3072,
    "contract_total_data_size": 10485760,
    "contract_max_data_size": 2147483648
  }
]

unlocked >>> 
get_object 1.11.0
unlocked >>> get_object 1.11.0
[{
    "id": "1.11.0",
    "op": [
      29,{
        "deposit_to_account": "1.2.16",
        "balance_to_claim": "1.15.0",
        "balance_owner_key": "COCOS7yE9skpBAirth3eSNMRtwq1jYswEE3uSbbuAtXTz88HtbpQsZf",
        "total_claimed": {
          "amount": "9780000000000000",
          "asset_id": "1.3.0"
        }
      }
    ],
    "result": [
      1,{
        "real_running_time": 62
      }
    ],
    "block_num": 34,
    "trx_in_block": 0,
    "op_in_trx": 0,
    "virtual_op": 47
  }
]

unlocked >>> 
get_object 1.10.1
unlocked >>> get_object 1.10.1
[{
    "id": "1.10.1",
    "expiration_time": "2020-07-23T06:28:30",
    "review_period_time": "2020-07-23T06:26:30",
    "proposed_transaction": {
      "ref_block_num": 112,
      "ref_block_prefix": 2489732660,
      "expiration": "2020-07-23T06:33:30",
      "operations": [[
          57,{
            "witness_max_votes": 9,
            "committee_max_votes": 7,
            "contract_private_data_size": 3072,
            "contract_total_data_size": 10485760,
            "contract_max_data_size": 2147483648
          }
        ]
      ],
      "extensions": [
        "1.10.1"
      ]
    },
    "required_active_approvals": [
      "1.2.0"
    ],
    "available_active_approvals": [
      "1.2.5",
      "1.2.6",
      "1.2.7",
      "1.2.8",
      "1.2.9",
      "1.2.10",
      "1.2.11",
      "1.2.12",
      "1.2.13",
      "1.2.14",
      "1.2.15"
    ],
    "required_owner_approvals": [],
    "available_owner_approvals": [],
    "available_key_approvals": [],
    "trx_hash": "1318178eebb1714f0d005bdc7751921c79e739d68aeb35d9035a3ad90005b3ba",
    "allow_execution": true
  }
]

unlocked >>> 
get_object 1.10.1 
unlocked >>> get_object 1.10.1 
[
  null
]

unlocked >>> 
 get_object 2.15.0 
unlocked >>>  get_object 2.15.0 
[{
    "id": "2.15.0",
    "witness_max_votes": 9,
    "committee_max_votes": 7,
    "contract_private_data_size": 3072,
    "contract_total_data_size": 10485760,
    "contract_max_data_size": 2147483648
  }
]
```  

# 2. 修改完最大投票数后，测试投票  
**测试过程和结果：**  
```  text  
ck@ubuntu:~/xukang/CocosBCX/feature_test/release1.1.5/proposal$ python3 vote_for.py 
# 1. test cli_wallet api: get_global_extensions_properties
>> get_global_extensions_properties []
{'id': 1, 'jsonrpc': '2.0', 'result': {'witness_max_votes': 9, 'contract_total_data_size': 10485760, 'id': '2.15.0', 'committee_max_votes': 7, 'contract_private_data_size': 3072, 'contract_max_data_size': 2147483648}}


# 2. test vote for witness
>> get_object ['2.15.0']
{'id': 1, 'jsonrpc': '2.0', 'result': [{'witness_max_votes': 9, 'contract_total_data_size': 10485760, 'id': '2.15.0', 'committee_max_votes': 7, 'contract_private_data_size': 3072, 'contract_max_data_size': 2147483648}]}

>> get_object 2.15.0
 [{'witness_max_votes': 9, 'contract_total_data_size': 10485760, 'id': '2.15.0', 'committee_max_votes': 7, 'contract_private_data_size': 3072, 'contract_max_data_size': 2147483648}]

[{'witness_max_votes': 9, 'contract_total_data_size': 10485760, 'id': '2.15.0', 'committee_max_votes': 7, 'contract_private_data_size': 3072, 'contract_max_data_size': 2147483648}]
>> list_witnesses ['', 10]
{'id': 1, 'jsonrpc': '2.0', 'result': [['init0', '1.6.1'], ['init1', '1.6.2'], ['init10', '1.6.11'], ['init2', '1.6.3'], ['init3', '1.6.4'], ['init4', '1.6.5'], ['init5', '1.6.6'], ['init6', '1.6.7'], ['init7', '1.6.8'], ['init8', '1.6.9']]}

witnesses: [['init0', '1.6.1'], ['init1', '1.6.2'], ['init10', '1.6.11'], ['init2', '1.6.3'], ['init3', '1.6.4'], ['init4', '1.6.5'], ['init5', '1.6.6'], ['init6', '1.6.7'], ['init7', '1.6.8'], ['init8', '1.6.9']]
>> list_account_balances ['nicotest']
{'id': 1, 'jsonrpc': '2.0', 'result': [{'amount': '9780000000000000', 'asset_id': '1.3.0'}]}

[{'amount': '9780000000000000', 'asset_id': '1.3.0'}]
>> vote_for_witness ['nicotest', 'init0', 7, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['b4c4519145e72893a9379828762d3c7cc548f7686dfab9edf3ca28cb2648a725', {'ref_block_prefix': 1583349037, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': ['1:0']}, 'account': '1.2.16', 'lock_with_vote': [1, {'amount': 7, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:08', 'extensions': [], 'signatures': ['1f757c240c7fdc5d722eee87ac93db1d0458346b4dcdda0a3238ba0449de8dc2070736c090ee91c8421e0973cf5218d9ffc114a1aec38a6625ea16b99dd5926baf'], 'ref_block_num': 431}]}

>> vote_for_witness ['nicotest', 'init1', 1, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['caf4c23450493da04bca4fd9b527c115224c14667a2ea594e95be660d97236f5', {'ref_block_prefix': 1583349037, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': ['1:0', '1:1']}, 'account': '1.2.16', 'lock_with_vote': [1, {'amount': 1, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:08', 'extensions': [], 'signatures': ['2023681f3c92f6b54e7d2751c395f684f41d11ee8973b1bfa9dc7d2969346520e676fa33da91e6fa60796b89769b72705f2d606e66f12b1505990bcd9fd7ba023f'], 'ref_block_num': 431}]}

>> vote_for_witness ['nicotest', 'init10', 13, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['a4798f8ceebcd634e3eb49629c926fd01fdcad098f1691a4291d3c3bff0f859d', {'ref_block_prefix': 1583349037, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': ['1:0', '1:1', '1:10']}, 'account': '1.2.16', 'lock_with_vote': [1, {'amount': 13, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:08', 'extensions': [], 'signatures': ['1f2e6eb39d31bc8bd3379e740f19d9de2e7958a639b5eea391e38b240fbb03b6d74fc750d8ccc148173425a795a3d91dfccd67a1225aff4bb2c85a01450c811aa4'], 'ref_block_num': 431}]}

>> vote_for_witness ['nicotest', 'init2', 18, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['3d3dac1452b305c3b6a9a5ceab8738dbd56a9b3e909a0076912a26410ee73425', {'ref_block_prefix': 1583349037, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': ['1:0', '1:1', '1:2', '1:10']}, 'account': '1.2.16', 'lock_with_vote': [1, {'amount': 18, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:08', 'extensions': [], 'signatures': ['1f2a153fe48c99809d2e76569c46963727f84e12219f588a9797d6b58148cc4b80064fd74316403b68daddb5aaa3e6ad3dce104f52330f435ec93e0926317f80f0'], 'ref_block_num': 431}]}

>> vote_for_witness ['nicotest', 'init3', 10, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['3fd2333eb9690c30b16038afc04c557704bbf19a32fb0a6e3782c6fafc51bac3', {'ref_block_prefix': 1583349037, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': ['1:0', '1:1', '1:2', '1:3', '1:10']}, 'account': '1.2.16', 'lock_with_vote': [1, {'amount': 10, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:08', 'extensions': [], 'signatures': ['1f5fdcbb36fb47b4c5e75e89fb58b6c32772a6373328a1f6b8dc3007e4cf06e076508d808fdffd102fd7c982639ecf809aa024a23ad37f8ec3a5ff683ab210af62'], 'ref_block_num': 431}]}

>> vote_for_witness ['nicotest', 'init4', 1, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['c93790813ad65aaa7c81076904af720dfebc707059a975983a8afac64e54283b', {'ref_block_prefix': 1583349037, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': ['1:0', '1:1', '1:2', '1:3', '1:4', '1:10']}, 'account': '1.2.16', 'lock_with_vote': [1, {'amount': 1, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:08', 'extensions': [], 'signatures': ['200ba738232e75b79b45b0c4c80b2c4ea7b5dd62c7394785da33e616c551505b27658f54d2cfb8a9af9fa49da10fed9d5184f001edf4760d352ced8695b2c5e2b6'], 'ref_block_num': 431}]}

>> vote_for_witness ['nicotest', 'init5', 19, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['b5c760f1300a51a18e0cd48240cd2abe28d7bbbe7ebf82812791163b664beaf7', {'ref_block_prefix': 1583349037, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': ['1:0', '1:1', '1:2', '1:3', '1:4', '1:5', '1:10']}, 'account': '1.2.16', 'lock_with_vote': [1, {'amount': 19, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:08', 'extensions': [], 'signatures': ['1f587ac4e860e62adee7af912e68ae7c5830b2715a824b947d344a99c440bf75aa2957b64334773d6739b6966e533bfab2c8715d24ce35823d97a28ba93098da4e'], 'ref_block_num': 431}]}

>> vote_for_witness ['nicotest', 'init6', 4, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['cbc7375e35f1dbe4ab0df3487cdce2bb68c20f555a234fe07e78939dc84c85aa', {'ref_block_prefix': 1583349037, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': ['1:0', '1:1', '1:2', '1:3', '1:4', '1:5', '1:6', '1:10']}, 'account': '1.2.16', 'lock_with_vote': [1, {'amount': 4, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:08', 'extensions': [], 'signatures': ['205732dbcca32829fe3eb864f2b5c12361c1719ad5bf617e8aa7637a8bf6011f1908b47cae6b1fff69153989d3668e55492f6cc7e64e3ad545b98a582a5599b7e4'], 'ref_block_num': 431}]}

>> vote_for_witness ['nicotest', 'init7', 20, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['f1a0380c4cd49ef90487ff00dac83e91ffd8e6e5955f43b1161bb88233c400db', {'ref_block_prefix': 1583349037, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': ['1:0', '1:1', '1:2', '1:3', '1:4', '1:5', '1:6', '1:7', '1:10']}, 'account': '1.2.16', 'lock_with_vote': [1, {'amount': 20, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:08', 'extensions': [], 'signatures': ['1f30474b051e373fc989c6501161facfc58b35b97b55442054b34d72b6035ef0c01eb59d45b07c64c5a4090917237e3dbcc934e8ca169b6090f24b6e8489227dc8'], 'ref_block_num': 431}]}

>> vote_for_witness ['nicotest', 'init8', 13, True]
{'error': {'code': 1, 'message': 'unspecified: Assert Exception: num_witness <= witness_number_of_vote: Voted for more witnesses than currently allowed (9)'}, 'id': 1, 'jsonrpc': '2.0'}

KeyError('result',)

# 3. test vote for committee
>> get_object ['2.15.0']
{'id': 1, 'jsonrpc': '2.0', 'result': [{'witness_max_votes': 9, 'contract_total_data_size': 10485760, 'id': '2.15.0', 'committee_max_votes': 7, 'contract_private_data_size': 3072, 'contract_max_data_size': 2147483648}]}

>> get_object 2.15.0
 [{'witness_max_votes': 9, 'contract_total_data_size': 10485760, 'id': '2.15.0', 'committee_max_votes': 7, 'contract_private_data_size': 3072, 'contract_max_data_size': 2147483648}]

[{'witness_max_votes': 9, 'contract_total_data_size': 10485760, 'id': '2.15.0', 'committee_max_votes': 7, 'contract_private_data_size': 3072, 'contract_max_data_size': 2147483648}]
>> list_committee_members ['', 8]
{'id': 1, 'jsonrpc': '2.0', 'result': [['init0', '1.5.0'], ['init1', '1.5.1'], ['init10', '1.5.10'], ['init2', '1.5.2'], ['init3', '1.5.3'], ['init4', '1.5.4'], ['init5', '1.5.5'], ['init6', '1.5.6']]}

committees: [['init0', '1.5.0'], ['init1', '1.5.1'], ['init10', '1.5.10'], ['init2', '1.5.2'], ['init3', '1.5.3'], ['init4', '1.5.4'], ['init5', '1.5.5'], ['init6', '1.5.6']]
>> list_account_balances ['nicotest']
{'id': 1, 'jsonrpc': '2.0', 'result': [{'amount': '9779999981922622', 'asset_id': '1.3.0'}]}

[{'amount': '9779999981922622', 'asset_id': '1.3.0'}]
>> vote_for_committee_member ['nicotest', 'init0', 11, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['7181dd64f3777ad157521afa86a676418c95e851baabfd8d0d64d0c344a42fe6', {'ref_block_prefix': 1583349037, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': ['0:11']}, 'account': '1.2.16', 'lock_with_vote': [0, {'amount': 11, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:08', 'extensions': [], 'signatures': ['207d0edea985757ca2a05a9c8115042e37968b93156b9e7f4a08cc9860b57594ee77adffcee1f3fee8112ee8b67a09a45b8f5aea10bea8ef26616ab7057e241bb0'], 'ref_block_num': 431}]}

>> vote_for_committee_member ['nicotest', 'init1', 17, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['7af024770c29bfa079ca5cfe3b9cdb34ed2179c1f719b7e408f0019a1ad014f5', {'ref_block_prefix': 1583349037, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': ['0:11', '0:12']}, 'account': '1.2.16', 'lock_with_vote': [0, {'amount': 17, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:08', 'extensions': [], 'signatures': ['203b991d9a6d7c299d379afc177092181a415ac7bd1f37da8c4e69f3f967ff614253dabe622dc065708eac62e300dafb0f38fb1732f9e49ed929d5adb1b4ca2302'], 'ref_block_num': 431}]}

>> vote_for_committee_member ['nicotest', 'init10', 18, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['c6c6fe429c98279bc87ebcfa7e05edcf460b77a8dc8c59ec7ebf952e81021ad1', {'ref_block_prefix': 1583349037, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': ['0:11', '0:12', '0:21']}, 'account': '1.2.16', 'lock_with_vote': [0, {'amount': 18, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:08', 'extensions': [], 'signatures': ['201c203c18be8f8fb823ca5c2009a9da2db1c84195ea2294ec2499bddc06f52cf7324a9722b0e84ee9e400bb2e7388e2ba6fd40791583e10c39c097b2aab1e6438'], 'ref_block_num': 431}]}

>> vote_for_committee_member ['nicotest', 'init2', 18, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['dc9eab8a6b903080c1a2ddd38b92f160f009e91a3e5814206e10b55fd52c057e', {'ref_block_prefix': 1583349037, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': ['0:11', '0:12', '0:13', '0:21']}, 'account': '1.2.16', 'lock_with_vote': [0, {'amount': 18, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:08', 'extensions': [], 'signatures': ['2007e2ca13932bc594766b6d162d44da09776d42994c2678cd25520ce8fe8c7eb45d056d2021fef38182ca3ab1216ff87d7fe5ebb63a34ff88702d3d682e796b05'], 'ref_block_num': 431}]}

>> vote_for_committee_member ['nicotest', 'init3', 3, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['fc2d202ed6b30c4e332f25b5d6e5f764258c83b1f6fd0736c73545b8ac99e275', {'ref_block_prefix': 1583349037, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': ['0:11', '0:12', '0:13', '0:14', '0:21']}, 'account': '1.2.16', 'lock_with_vote': [0, {'amount': 3, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:08', 'extensions': [], 'signatures': ['1f72af5ab97429f118c34513bb6734de1227c18202d4dca641c4d072d1b7cf9b9b2c16415a4838bcfd46db5f6a8e8e3d71c6320da9c2f22eddcba789df2a8a9dd5'], 'ref_block_num': 431}]}

>> vote_for_committee_member ['nicotest', 'init4', 11, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['f00f95ab913b19408a59a7fea25b1aa6a312943c37a33524806a81d2cd014304', {'ref_block_prefix': 1583349037, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': ['0:11', '0:12', '0:13', '0:14', '0:15', '0:21']}, 'account': '1.2.16', 'lock_with_vote': [0, {'amount': 11, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:08', 'extensions': [], 'signatures': ['1f27df9054294daf500fa7619caf424c5c7ca976b27ce2375142ec5eb5797e1fee5fefee86eb3365f6e5b03401375171461a8bd82347cb53781e486ae2aee34a13'], 'ref_block_num': 431}]}

>> vote_for_committee_member ['nicotest', 'init5', 20, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['dc3002382aa6e99c15d76df0c0c490a7577210fee677ec0f8c48a7a2b9a29fd3', {'ref_block_prefix': 1583349037, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': ['0:11', '0:12', '0:13', '0:14', '0:15', '0:16', '0:21']}, 'account': '1.2.16', 'lock_with_vote': [0, {'amount': 20, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:08', 'extensions': [], 'signatures': ['20542a6daa77b7a149bec614e9ba0f0f730bf1ff098714927087b2520bc5ee64d762f82276274d2b952b93731e39acd983098c8460677cb52f0f6a3ad38127f14a'], 'ref_block_num': 431}]}

>> vote_for_committee_member ['nicotest', 'init6', 5, True]
{'error': {'code': 1, 'message': 'unspecified: Assert Exception: num_committee <= committee_number_of_vote: Voted for more committee members than currently allowed (7)'}, 'id': 1, 'jsonrpc': '2.0'}

KeyError('result',)

# 4. test cancle vote for witness
>> vote_for_witness ['nicotest', 'init0', 0, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['03e50dffd08b94d945b76ef0f249f6a2249adefcb8a691877f29fc719f156de7', {'ref_block_prefix': 2167441650, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:18', 'extensions': [], 'signatures': ['1f4a4625310275a83d2ec7644cc6d961eff1fd791f6d671884938b273230612a0376c6869d91fb21d04ae3377ef023a848b64c3bf15a460df3b5af07de50d801b5'], 'ref_block_num': 432}]}

>> vote_for_witness ['nicotest', 'init1', 0, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['c9f72bb4d363810e96cd7290e1772bb3526d657c893a7de9187b25a33c7d7c05', {'ref_block_prefix': 2167441650, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:19', 'extensions': [], 'signatures': ['20710b3efa4937690b19ee97d19e6b9cc5db744e9e7246ce3ef16f7453a82b77f440f7846b9ecfb0baf714e9b478b27d68a26461e7e810864fc47f2676f0611b3c'], 'ref_block_num': 432}]}

>> vote_for_witness ['nicotest', 'init10', 0, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['f08a1a9c43760cd80a2b45fa5d03bcf4dc4c3c6e3791c14abcf9b8b2d01156b0', {'ref_block_prefix': 2167441650, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:20', 'extensions': [], 'signatures': ['1f5c6c20410459f4d133b418808e3acca7fba53c13dfc050c768a4e997940bc8ef4f4208caa1b2cc790c765a4db5d583c26ac26e7ac7afa9ccd1cc6e15440ba9b3'], 'ref_block_num': 432}]}

>> vote_for_witness ['nicotest', 'init2', 0, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['f10aca65017f790d4fd5a95d7005822ea0e2b5115b865ded73e07423f668bfbc', {'ref_block_prefix': 2167441650, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:21', 'extensions': [], 'signatures': ['20122ea6365f0254cef0520b5476a0173be26d1d063a47d3ae7bf164f0dfe9526a3ef9f54f0d8162f1cb9659689a34c8d62e49884639a3fdaa489d3e2ec03b12a0'], 'ref_block_num': 432}]}

>> vote_for_witness ['nicotest', 'init3', 0, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['2fa84192fada31f90f12c4fef42d73676e1d07e09faab1c7722edc7c56e454a8', {'ref_block_prefix': 2167441650, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:22', 'extensions': [], 'signatures': ['207a01bdf47f49630183643af04269d41067c9d1003187b598b399cdcfa0ad928b528bcb964abd806f46dde393d8ff88ffa014e71f53d1ba3361523d562f13ddb0'], 'ref_block_num': 432}]}

>> vote_for_witness ['nicotest', 'init4', 0, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['40623b4dd7a748f1fc1c26c19f405bd59f355379c8ed879ef3c7c71d44d35dcd', {'ref_block_prefix': 2167441650, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:23', 'extensions': [], 'signatures': ['20381c966cddd2f156ac887ab121a0f632c8768cc0dad4bf6c0af7b505e00cbf870bc0aaa7ab936c178b1c7b4185769ccdd30b56deb607c243ae509833facbe860'], 'ref_block_num': 432}]}

>> vote_for_witness ['nicotest', 'init5', 0, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['0640feb3ef026776372432f7b2cfe7e496e56a5539cd1fccd91bfeb34f9e19ce', {'ref_block_prefix': 2167441650, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:24', 'extensions': [], 'signatures': ['1f51b060f3c09e1e702a85f156e186f1ce8992fa09288ccfc11306aa97e376a6223254bd3dd7ceea147ae71a9228b1406ac2e808f9f0ac76efa87b2916e976c326'], 'ref_block_num': 432}]}

>> vote_for_witness ['nicotest', 'init6', 0, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['5d5eae2b5dc8202f2e9677e5c3d3f32c6fc047ec996320a3ccaa02bf3550e414', {'ref_block_prefix': 2167441650, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:25', 'extensions': [], 'signatures': ['1f4e3071fdfc74a21eb9512e58d621b264bc0ecfe2f9b965a2ce42d072dacbdb5a4d57713946d5b32ad1a0507d6861b8263c9c14fc597d0a0a9bf0d496e8ec30b4'], 'ref_block_num': 432}]}

>> vote_for_witness ['nicotest', 'init7', 0, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['4e8c49efb76e5650ecc2432ff4e55490623dd8ad4d08ee5f3fd2efeeb86941a4', {'ref_block_prefix': 2167441650, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:26', 'extensions': [], 'signatures': ['1f65f9b6c85f3f4fa22dc0677e4b42ccd2ac3dc118c5f64d81e2fd1966f9ddc2e22849bb884bb2a66e9fc872015a00bbe4ff09c67720e36a5e9ab57d22af1f6ff7'], 'ref_block_num': 432}]}

>> vote_for_witness ['nicotest', 'init8', 0, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['2d078bce30221f143b9dd0585353bde231b177bd470692397780c7cf11cc1048', {'ref_block_prefix': 2167441650, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': []}, 'account': '1.2.16', 'lock_with_vote': [1, {'amount': 0, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:27', 'extensions': [], 'signatures': ['1f0193c051aec3fda32c461c824b1d4ed21de5979398307513c7d7154711412ffc074f2e4b76c92672e35474be76a332004ac3f9d98f816977e865f01779c9f136'], 'ref_block_num': 432}]}


# 5. test  cancle vote for committee
>> vote_for_committee_member ['nicotest', 'init0', 0, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['a257f98cc4bd5b617721f16744de0d1bb2ab2dc2523833a3ff150bff840cad07', {'ref_block_prefix': 2167441650, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:18', 'extensions': [], 'signatures': ['1f1f356423dbe49aee301886f705665c0257d052ed13fd97d2bc3e5b73b6f7254d0dd2779da62818c5b3fa5b38f56edc450b56b1ca4353bc1ad7c0ccd96dd9fbe7'], 'ref_block_num': 432}]}

>> vote_for_committee_member ['nicotest', 'init1', 0, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['1b19260e5b9351fbb44414f4b46b6b8647dbdeb29696b2f7d95666746ca1393d', {'ref_block_prefix': 2167441650, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:19', 'extensions': [], 'signatures': ['2047e55477a30cdcdf0d6c29874ee6eab70abc9369aaf8d83bee85ddc4619847fd3a24e5188faad8fc65e091b02d471f90da7b5a5185bd12e9bd24c7966fdd7b74'], 'ref_block_num': 432}]}

>> vote_for_committee_member ['nicotest', 'init10', 0, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['e9b74ea09a62f0b2cfcf4230a2ade5f83c7fda9d5398e5cf787126e217975894', {'ref_block_prefix': 2167441650, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:20', 'extensions': [], 'signatures': ['1f15c0970c4e605f5c7747044ec15a08656f007abc80f3985d186c898ae449beb26f6021c73b7b2af4589e4a091573c47cc87ee75569f3f40acbb7d5ed1930419d'], 'ref_block_num': 432}]}

>> vote_for_committee_member ['nicotest', 'init2', 0, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['7bc2c6061e418a035184e07f556c03af252d5871341d36ac36dd1afdbb7c760b', {'ref_block_prefix': 2167441650, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:21', 'extensions': [], 'signatures': ['204abc9ec0ad860a8debaeb6b69142cfe214d08835b9833ae96ab7a3d627d9d9d50f9b9f9c54ce1a794dae9e99a7f0e08d4b065be11b586c7fe863fc7d7a0a92d7'], 'ref_block_num': 432}]}

>> vote_for_committee_member ['nicotest', 'init3', 0, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['d50dc7280d71c8eb08c0576974233e779c01e0dcbd61518d7c680b9b371b0984', {'ref_block_prefix': 2167441650, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:22', 'extensions': [], 'signatures': ['2002c7db911896d7aab243e9cddef91aa89da158b4feacf1b03e0f84a601d6921a21c210353c33657d709341fd8e9f580a1cb1a0e3bc431e33a838a1582dfdbe21'], 'ref_block_num': 432}]}

>> vote_for_committee_member ['nicotest', 'init4', 0, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['9dd2816206cb13c3b96e7bafade6c3198712a02dc20c4b5dfe8355c4be120d7f', {'ref_block_prefix': 2167441650, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:23', 'extensions': [], 'signatures': ['1f1fa6e99c7dfc9ceb991734736df58014c822a5351e89877172cc0666523a323c6342f188f383a58ab8d580b8d15c3024d00b3f1446f6966f792d500a3e7f0092'], 'ref_block_num': 432}]}

>> vote_for_committee_member ['nicotest', 'init5', 0, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['3a0196e9999725099a5171cf634305e677c6f2d8afbabe10a6f3830de9bc5377', {'ref_block_prefix': 2167441650, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:24', 'extensions': [], 'signatures': ['207873b681e70e2270f2354c2808f6aca975a019b595a8487f4de5ff1a16d36a287583ebc3a1bc5d6970d628e6dade7aee56b4fea31f2bf5301665765f219b2d37'], 'ref_block_num': 432}]}

>> vote_for_committee_member ['nicotest', 'init6', 0, True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['7a9e4f34cc2c1acf4af37267b38a7e1df5d4a74fa6d260958bdabadf3ef03623', {'ref_block_prefix': 2167441650, 'operations': [[6, {'extensions': {}, 'new_options': {'memo_key': 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 'extensions': [], 'votes': []}, 'account': '1.2.16', 'lock_with_vote': [0, {'amount': 0, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-07-23T06:54:25', 'extensions': [], 'signatures': ['1f7e93b631aa610e5b2d4297a9c9af5d7bcb74f15807b51e0e0294332a6e06f1a30fbc9a3f14092e19745aa6744f277db6f18d842c4aa91f7aee391dbae05170db'], 'ref_block_num': 432}]}

test vote for xxx done
ck@ubuntu:~/xukang/CocosBCX/feature_test/release1.1.5/proposal$ 
```  
功能验证完成  
