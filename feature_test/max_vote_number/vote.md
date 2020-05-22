
## 启动节点  
参考README.md

## 测试

### 接口测试
#### cli_wallet api
``` shell
curl http://127.0.0.1:8048 -d '{"id":1, "method":"get_global_extensions_properties", "params":[]}' && echo ""
```

#### chain api
``` shell
curl http://127.0.0.1:8059 -d '{"id":1, "method":"call", "params":[0, "get_global_property_extensions", []]}' && echo ""
```

### 发起修改参数提案, 批准  
``` shell
python3 vote.py

```

**注意** : 提案review时间应该大于当前时间到链维护的间隔，否则提案失败，这种情况执行会有提示，`Please wait for the next maintenance`, 可以根据需要修改vote.py逻辑，`sleep(delta_time)`

**执行结果**
``` text
dev@ubuntu:~$ python3 vote.py 
>> ['vote.py']
>> get_dynamic_global_properties
 {'current_witness': '1.6.8', 'next_maintenance_time': '2020-05-22T07:40:00', 'last_budget_time': '2020-05-22T07:30:00', 'head_block_number': 23, 'accounts_registered_this_interval': 0, 'recently_missed_count': 1, 'dynamic_flags': 0, 'time': '2020-05-22T07:30:42', 'current_aslot': 18324468, 'recent_slots_filled': '16252919', 'last_irreversible_block_num': 16, 'witness_budget': 166438931, 'id': '2.1.0', 'head_block_id': '000000173a001878d8ec94fc293690cf4d731376', 'current_transaction_count': 0}

next_maintenance_time: 2020-05-22T07:40:00, now time: 2020-05-22T07:30:42
time_delta: 558
committee_proposal_review_period: 120
expire_time: 2020-05-22T07:35:00
{"id": 1, "params": ["init0", "2020-05-22T07:35:00", {"committee_max_votes": 9, "witness_max_votes": 7}, true], "method": "propose_extensions_parameter_change", "jsonrpc": "2.0"}
>> propose_extensions_parameter_change
 ['75dea1e3507e7f8e51d0aac801008a8c52485604f93c2d616e0130310be9e8df', {'signatures': ['1f7b613d0f34a643ca1a17232ab94a18da9017454bf6f955b1d2b768a5b7d90f211cad475e53b8388ea0587fb516421088cf80c87ef6fe21ad699cca4aff267d9e'], 'expiration': '2020-05-22T07:51:12', 'ref_block_prefix': 1712984885, 'operations': [[20, {'fee_paying_account': '1.2.5', 'proposed_ops': [{'op': [57, {'committee_max_votes': 9, 'contract_max_data_size': 2147483648, 'contract_private_data_size': 3072, 'contract_total_data_size': 10485760, 'witness_max_votes': 7}]}], 'review_period_seconds': 120, 'extensions': [], 'expiration_time': '2020-05-22T07:35:00'}]], 'ref_block_num': 15, 'extensions': []}]

tx_id: 75dea1e3507e7f8e51d0aac801008a8c52485604f93c2d616e0130310be9e8df
>> get_transaction_in_block_info 75dea1e3507e7f8e51d0aac801008a8c52485604f93c2d616e0130310be9e8df
 {'trx_in_block': 0, 'id': '3.1.1', 'block_num': 24, 'trx_hash': '75dea1e3507e7f8e51d0aac801008a8c52485604f93c2d616e0130310be9e8df'}

>> get_block 24
 {'witness_signature': '1f3334d3bc8fbbb05e905efbcd3c0acbab91477a0950ea78d8efad5babde08653f414c9596d5860253aa6d6da1649b128a7f5a1564a33cb8afe1a9e89e1e273ded', 'witness': '1.6.1', 'transactions': [['75dea1e3507e7f8e51d0aac801008a8c52485604f93c2d616e0130310be9e8df', {'signatures': ['1f7b613d0f34a643ca1a17232ab94a18da9017454bf6f955b1d2b768a5b7d90f211cad475e53b8388ea0587fb516421088cf80c87ef6fe21ad699cca4aff267d9e'], 'operation_results': [[2, {'real_running_time': 239, 'result': '1.10.0', 'fees': [{'amount': 2000000, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-05-22T07:51:12', 'ref_block_prefix': 1712984885, 'operations': [[20, {'fee_paying_account': '1.2.5', 'proposed_ops': [{'op': [57, {'committee_max_votes': 9, 'contract_max_data_size': 2147483648, 'contract_private_data_size': 3072, 'contract_total_data_size': 10485760, 'witness_max_votes': 7}]}], 'review_period_seconds': 120, 'extensions': [], 'expiration_time': '2020-05-22T07:35:00'}]], 'ref_block_num': 15, 'extensions': []}]], 'block_id': '0000001879e7f67092534a3c07ca19609840dc8d', 'previous': '000000173a001878d8ec94fc293690cf4d731376', 'transaction_merkle_root': 'fa9e57631c09a4c4d57f7dd3ef6d4846fe9824e2', 'timestamp': '2020-05-22T07:30:44'}

block: {'witness_signature': '1f3334d3bc8fbbb05e905efbcd3c0acbab91477a0950ea78d8efad5babde08653f414c9596d5860253aa6d6da1649b128a7f5a1564a33cb8afe1a9e89e1e273ded', 'witness': '1.6.1', 'transactions': [['75dea1e3507e7f8e51d0aac801008a8c52485604f93c2d616e0130310be9e8df', {'signatures': ['1f7b613d0f34a643ca1a17232ab94a18da9017454bf6f955b1d2b768a5b7d90f211cad475e53b8388ea0587fb516421088cf80c87ef6fe21ad699cca4aff267d9e'], 'operation_results': [[2, {'real_running_time': 239, 'result': '1.10.0', 'fees': [{'amount': 2000000, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-05-22T07:51:12', 'ref_block_prefix': 1712984885, 'operations': [[20, {'fee_paying_account': '1.2.5', 'proposed_ops': [{'op': [57, {'committee_max_votes': 9, 'contract_max_data_size': 2147483648, 'contract_private_data_size': 3072, 'contract_total_data_size': 10485760, 'witness_max_votes': 7}]}], 'review_period_seconds': 120, 'extensions': [], 'expiration_time': '2020-05-22T07:35:00'}]], 'ref_block_num': 15, 'extensions': []}]], 'block_id': '0000001879e7f67092534a3c07ca19609840dc8d', 'previous': '000000173a001878d8ec94fc293690cf4d731376', 'transaction_merkle_root': 'fa9e57631c09a4c4d57f7dd3ef6d4846fe9824e2', 'timestamp': '2020-05-22T07:30:44'}

tx_pair: ['75dea1e3507e7f8e51d0aac801008a8c52485604f93c2d616e0130310be9e8df', {'signatures': ['1f7b613d0f34a643ca1a17232ab94a18da9017454bf6f955b1d2b768a5b7d90f211cad475e53b8388ea0587fb516421088cf80c87ef6fe21ad699cca4aff267d9e'], 'operation_results': [[2, {'real_running_time': 239, 'result': '1.10.0', 'fees': [{'amount': 2000000, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-05-22T07:51:12', 'ref_block_prefix': 1712984885, 'operations': [[20, {'fee_paying_account': '1.2.5', 'proposed_ops': [{'op': [57, {'committee_max_votes': 9, 'contract_max_data_size': 2147483648, 'contract_private_data_size': 3072, 'contract_total_data_size': 10485760, 'witness_max_votes': 7}]}], 'review_period_seconds': 120, 'extensions': [], 'expiration_time': '2020-05-22T07:35:00'}]], 'ref_block_num': 15, 'extensions': []}]
[0]: 75dea1e3507e7f8e51d0aac801008a8c52485604f93c2d616e0130310be9e8df

tx: {'signatures': ['1f7b613d0f34a643ca1a17232ab94a18da9017454bf6f955b1d2b768a5b7d90f211cad475e53b8388ea0587fb516421088cf80c87ef6fe21ad699cca4aff267d9e'], 'operation_results': [[2, {'real_running_time': 239, 'result': '1.10.0', 'fees': [{'amount': 2000000, 'asset_id': '1.3.0'}]}]], 'expiration': '2020-05-22T07:51:12', 'ref_block_prefix': 1712984885, 'operations': [[20, {'fee_paying_account': '1.2.5', 'proposed_ops': [{'op': [57, {'committee_max_votes': 9, 'contract_max_data_size': 2147483648, 'contract_private_data_size': 3072, 'contract_total_data_size': 10485760, 'witness_max_votes': 7}]}], 'review_period_seconds': 120, 'extensions': [], 'expiration_time': '2020-05-22T07:35:00'}]], 'ref_block_num': 15, 'extensions': []}

operation_results: [[2, {'real_running_time': 239, 'result': '1.10.0', 'fees': [{'amount': 2000000, 'asset_id': '1.3.0'}]}]]
propose_id: 1.10.0
>> get_object 1.10.0
 [{'available_owner_approvals': [], 'review_period_time': '2020-05-22T07:33:00', 'required_owner_approvals': [], 'trx_hash': '75dea1e3507e7f8e51d0aac801008a8c52485604f93c2d616e0130310be9e8df', 'proposed_transaction': {'operations': [[57, {'committee_max_votes': 9, 'contract_max_data_size': 2147483648, 'contract_private_data_size': 3072, 'contract_total_data_size': 10485760, 'witness_max_votes': 7}]], 'ref_block_num': 0, 'expiration': '2020-05-22T07:35:00', 'ref_block_prefix': 0, 'extensions': ['1.10.0']}, 'id': '1.10.0', 'available_active_approvals': [], 'allow_execution': False, 'required_active_approvals': ['1.2.0'], 'available_key_approvals': [], 'expiration_time': '2020-05-22T07:35:00'}]

propose object: [{'available_owner_approvals': [], 'review_period_time': '2020-05-22T07:33:00', 'required_owner_approvals': [], 'trx_hash': '75dea1e3507e7f8e51d0aac801008a8c52485604f93c2d616e0130310be9e8df', 'proposed_transaction': {'operations': [[57, {'committee_max_votes': 9, 'contract_max_data_size': 2147483648, 'contract_private_data_size': 3072, 'contract_total_data_size': 10485760, 'witness_max_votes': 7}]], 'ref_block_num': 0, 'expiration': '2020-05-22T07:35:00', 'ref_block_prefix': 0, 'extensions': ['1.10.0']}, 'id': '1.10.0', 'available_active_approvals': [], 'allow_execution': False, 'required_active_approvals': ['1.2.0'], 'available_key_approvals': [], 'expiration_time': '2020-05-22T07:35:00'}]
>> approve_proposal ['init0', '1.10.0', {'active_approvals_to_add': ['init0']}, True]
 ['b68c856fe535878bbe6c5238b2193dcb8ae5dba5c53f2c78d9774d65a349ec5d', {'signatures': ['205b09a9693e85ca9552124a3abc7c5541f20ea666ff23c4a19443a7f9a2c61e192f2d39783fa5c95cc88b63c27d88f7c9ec13b488a97e783fa420273b2f852500'], 'expiration': '2020-05-22T07:51:14', 'ref_block_prefix': 1712984885, 'operations': [[21, {'active_approvals_to_add': ['1.2.5'], 'fee_paying_account': '1.2.5', 'key_approvals_to_remove': [], 'proposal': '1.10.0', 'key_approvals_to_add': [], 'extensions': [], 'owner_approvals_to_remove': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': []}]], 'ref_block_num': 15, 'extensions': []}]

>> approve_proposal ['init1', '1.10.0', {'active_approvals_to_add': ['init1']}, True]
 ['ca59863353b1ec7dca7b26c20d27fc44a2ce6938c3357bdba36601cec73ed7b2', {'signatures': ['1f7311453cbfdf3ad6eb533aa0a7603a05875a4a1d691470d252cdbf4e575e4f300625e0ec289ab2a4194ec2bbf5a1801ccdc97cd3cc0f4d79d9178e0d3cd57811'], 'expiration': '2020-05-22T07:51:14', 'ref_block_prefix': 1712984885, 'operations': [[21, {'active_approvals_to_add': ['1.2.6'], 'fee_paying_account': '1.2.6', 'key_approvals_to_remove': [], 'proposal': '1.10.0', 'key_approvals_to_add': [], 'extensions': [], 'owner_approvals_to_remove': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': []}]], 'ref_block_num': 15, 'extensions': []}]

>> approve_proposal ['init2', '1.10.0', {'active_approvals_to_add': ['init2']}, True]
 ['7a6deffaece7667e79a45c3ea46f8a204655840d43982711ab1365e78539438d', {'signatures': ['200b7d5b0748a8ffd0f900372b182c060c050da55474cddc949b54aae26d4194e106cfaeb5766e22e4b8431aa3ec6dd6e0c28de411edb4954c504db4ad84bbcfa9'], 'expiration': '2020-05-22T07:51:14', 'ref_block_prefix': 1712984885, 'operations': [[21, {'active_approvals_to_add': ['1.2.7'], 'fee_paying_account': '1.2.7', 'key_approvals_to_remove': [], 'proposal': '1.10.0', 'key_approvals_to_add': [], 'extensions': [], 'owner_approvals_to_remove': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': []}]], 'ref_block_num': 15, 'extensions': []}]

>> approve_proposal ['init3', '1.10.0', {'active_approvals_to_add': ['init3']}, True]
 ['9f111bdb699bc6547cde8f581dae788fd88b7c1e9bdedfdd16549bf5e088f2c9', {'signatures': ['2024370b878d23f912a533693de6e3f85313e785aca2d664ef822aafaf5225ae623a5dfacd1e1858c769abad3322e9bd893a8f32ff47e5d5178ef912ba8e07d60a'], 'expiration': '2020-05-22T07:51:14', 'ref_block_prefix': 1712984885, 'operations': [[21, {'active_approvals_to_add': ['1.2.8'], 'fee_paying_account': '1.2.8', 'key_approvals_to_remove': [], 'proposal': '1.10.0', 'key_approvals_to_add': [], 'extensions': [], 'owner_approvals_to_remove': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': []}]], 'ref_block_num': 15, 'extensions': []}]

>> approve_proposal ['init4', '1.10.0', {'active_approvals_to_add': ['init4']}, True]
 ['cbbe6a37f405e757b786d1747e13ddd983a36a31fa563590a60a158c496acd15', {'signatures': ['1f7f818cb68a5869817adcbf06434b309ba05e66d5b4cfa1dcb7e6b35652918427766b067e6f2c75c8e1b87a23ca1b0fe6aeba9e31d3063cf7f4fec5391d488c09'], 'expiration': '2020-05-22T07:51:14', 'ref_block_prefix': 1712984885, 'operations': [[21, {'active_approvals_to_add': ['1.2.9'], 'fee_paying_account': '1.2.9', 'key_approvals_to_remove': [], 'proposal': '1.10.0', 'key_approvals_to_add': [], 'extensions': [], 'owner_approvals_to_remove': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': []}]], 'ref_block_num': 15, 'extensions': []}]

>> approve_proposal ['init5', '1.10.0', {'active_approvals_to_add': ['init5']}, True]
 ['fa73c90f59366b9fe4ebcc3b06efd3f114c2da1be19eab2875585f250fdbf67a', {'signatures': ['20297246a3ca7c2d409af79bf0d2e48c4c93970f915d91572c3fef16b8225b292c66bbf73a0bffb2b25fb5543f0c2bbf9a638317fbe2840bc418a85213acb08d65'], 'expiration': '2020-05-22T07:51:14', 'ref_block_prefix': 1712984885, 'operations': [[21, {'active_approvals_to_add': ['1.2.10'], 'fee_paying_account': '1.2.10', 'key_approvals_to_remove': [], 'proposal': '1.10.0', 'key_approvals_to_add': [], 'extensions': [], 'owner_approvals_to_remove': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': []}]], 'ref_block_num': 15, 'extensions': []}]

>> approve_proposal ['init6', '1.10.0', {'active_approvals_to_add': ['init6']}, True]
 ['fde734e689d985356b11f239d752e3e454357e94a7584beea1887eba9727bab3', {'signatures': ['2058b62167e101aa7292b74347eb85ea9748ee1c61553a45b4dd6d85641925519c313406255cff8a53d66efd9796d704dc854cc199c8bcfb2d71088cde4a3e713e'], 'expiration': '2020-05-22T07:51:14', 'ref_block_prefix': 1712984885, 'operations': [[21, {'active_approvals_to_add': ['1.2.11'], 'fee_paying_account': '1.2.11', 'key_approvals_to_remove': [], 'proposal': '1.10.0', 'key_approvals_to_add': [], 'extensions': [], 'owner_approvals_to_remove': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': []}]], 'ref_block_num': 15, 'extensions': []}]

>> approve_proposal ['init7', '1.10.0', {'active_approvals_to_add': ['init7']}, True]
 ['7df7f5d88f40d0112835b5465f28d807a51b06a901734e455c2592e7002d727e', {'signatures': ['204a9cda8b966adb9d7ace5c983e047f1fd8d350c8640389a7495db8e694dbcbfc3b8bcbd0c5ba95730073617e2231ce1ed58a4a5a4f6055f4f3d82f7a647c5ffa'], 'expiration': '2020-05-22T07:51:14', 'ref_block_prefix': 1712984885, 'operations': [[21, {'active_approvals_to_add': ['1.2.12'], 'fee_paying_account': '1.2.12', 'key_approvals_to_remove': [], 'proposal': '1.10.0', 'key_approvals_to_add': [], 'extensions': [], 'owner_approvals_to_remove': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': []}]], 'ref_block_num': 15, 'extensions': []}]

>> approve_proposal ['init8', '1.10.0', {'active_approvals_to_add': ['init8']}, True]
 ['abd5667f15ded8af394e1a4091a6e57471efaa0be86f656e965edd12e7bbef14', {'signatures': ['20708c76ba22f233e63ff94ebb82dec76b9450ef4e6cb9b3280e274a6cb3ce82e234b78007a7d75e8b11f67081847e9f06ff866f916efcc30f9900f5299c824e13'], 'expiration': '2020-05-22T07:51:14', 'ref_block_prefix': 1712984885, 'operations': [[21, {'active_approvals_to_add': ['1.2.13'], 'fee_paying_account': '1.2.13', 'key_approvals_to_remove': [], 'proposal': '1.10.0', 'key_approvals_to_add': [], 'extensions': [], 'owner_approvals_to_remove': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': []}]], 'ref_block_num': 15, 'extensions': []}]

>> approve_proposal ['init9', '1.10.0', {'active_approvals_to_add': ['init9']}, True]
 ['b23a2fc2c4baa42b21387fc5c8f0f3281f6325e56d3f51110def6fa66b011caa', {'signatures': ['207a8cfe5e75964d0371a0f416c4db9198c6a852b10450a81ee1e7d9951f1e589849767fc3e2a2b4366e0ad015c4d26c86c71df7972be9cf66d0d8c53d3bff26a3'], 'expiration': '2020-05-22T07:51:14', 'ref_block_prefix': 1712984885, 'operations': [[21, {'active_approvals_to_add': ['1.2.14'], 'fee_paying_account': '1.2.14', 'key_approvals_to_remove': [], 'proposal': '1.10.0', 'key_approvals_to_add': [], 'extensions': [], 'owner_approvals_to_remove': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': []}]], 'ref_block_num': 15, 'extensions': []}]

>> approve_proposal ['init10', '1.10.0', {'active_approvals_to_add': ['init10']}, True]
 ['1a5787802b87974af74868def54afe420859c8845769e34c6b9ab2e73626326a', {'signatures': ['207c172be6646fd0be05495170677933e8e46df42e95a6fa24eaccd0eff69ed0f569d381d7047684bdb1a8d544ac175334d4fb47f4e1ce98aa574b9f7f73ea3989'], 'expiration': '2020-05-22T07:51:14', 'ref_block_prefix': 1712984885, 'operations': [[21, {'active_approvals_to_add': ['1.2.15'], 'fee_paying_account': '1.2.15', 'key_approvals_to_remove': [], 'proposal': '1.10.0', 'key_approvals_to_add': [], 'extensions': [], 'owner_approvals_to_remove': [], 'active_approvals_to_remove': [], 'owner_approvals_to_add': []}]], 'ref_block_num': 15, 'extensions': []}]

>> get_object 1.10.0
 [{'available_owner_approvals': [], 'review_period_time': '2020-05-22T07:33:00', 'required_owner_approvals': [], 'trx_hash': '75dea1e3507e7f8e51d0aac801008a8c52485604f93c2d616e0130310be9e8df', 'proposed_transaction': {'operations': [[57, {'committee_max_votes': 9, 'contract_max_data_size': 2147483648, 'contract_private_data_size': 3072, 'contract_total_data_size': 10485760, 'witness_max_votes': 7}]], 'ref_block_num': 24, 'expiration': '2020-05-22T07:40:00', 'ref_block_prefix': 1895229305, 'extensions': ['1.10.0']}, 'id': '1.10.0', 'available_active_approvals': ['1.2.5', '1.2.6', '1.2.7', '1.2.8', '1.2.9', '1.2.10', '1.2.11', '1.2.12', '1.2.13', '1.2.14', '1.2.15'], 'allow_execution': True, 'required_active_approvals': ['1.2.0'], 'available_key_approvals': [], 'expiration_time': '2020-05-22T07:35:00'}]

[{'available_owner_approvals': [], 'review_period_time': '2020-05-22T07:33:00', 'required_owner_approvals': [], 'trx_hash': '75dea1e3507e7f8e51d0aac801008a8c52485604f93c2d616e0130310be9e8df', 'proposed_transaction': {'operations': [[57, {'committee_max_votes': 9, 'contract_max_data_size': 2147483648, 'contract_private_data_size': 3072, 'contract_total_data_size': 10485760, 'witness_max_votes': 7}]], 'ref_block_num': 24, 'expiration': '2020-05-22T07:40:00', 'ref_block_prefix': 1895229305, 'extensions': ['1.10.0']}, 'id': '1.10.0', 'available_active_approvals': ['1.2.5', '1.2.6', '1.2.7', '1.2.8', '1.2.9', '1.2.10', '1.2.11', '1.2.12', '1.2.13', '1.2.14', '1.2.15'], 'allow_execution': True, 'required_active_approvals': ['1.2.0'], 'available_key_approvals': [], 'expiration_time': '2020-05-22T07:35:00'}]

```
