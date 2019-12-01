# cli_wallet api
## 1. 一般命令  
``` text
(help)(gethelp)(info)(about)

(network_add_nodes)(network_get_connected_peers)

(get_block)(get_object)       

(get_global_properties)(get_dynamic_global_properties)(get_chain_properties)

(get_prototype_operation_by_name)(get_prototype_operation_by_idx)

(is_public_key_registered)
```

## 2. 钱包相关  
``` text  
(is_new)(is_locked)(lock)(unlock)(set_password)(dump_private_keys)

(import_key)(import_balance)(suggest_brain_key)(derive_owner_keys_from_brain_key)(suggest_brain_address_key)

(get_transaction_id)(get_private_key)(normalize_brain_key)

(load_wallet_file)(save_wallet_file)(add_extern_sign_key)
```


## 3. 账号相关
``` text
(list_my_accounts)(list_accounts)(list_account_balances)

(register_account)(upgrade_account)(create_account_with_brain_key)

(transfer)(transfer2)(get_account)(get_account_id)

(get_account_count)(get_account_history)(get_relative_account_history)

(get_vesting_balances)(withdraw_vesting)

(update_collateral_for_gas)
```


## 4. 合约
``` text  
(create_contract)(create_contract_from_file)(call_contract_function)(revise_contract)

(get_contract)(get_account_contract_data)(get_contract_public_data)

```

## 5. 理事会和见证人
``` text  
# (get_witness)(get_committee_member)(list_witnesses)(list_committee_members)

# (create_committee_member)(update_committee_member)(create_witness)(update_witness)

# (vote_for_committee_member)(vote_for_witness)
```


## 6. 同质资产
``` text  
(get_limit_orders)(get_call_orders)(get_settle_orders)

(list_assets)(list_asset_restricted_objects)(asset_update_restricted_list)

(sell_asset)(sell)(buy)(borrow_asset)(cancel_order)

(create_asset)(update_asset)(update_bitasset)(update_asset_feed_producers)

(publish_asset_feed)(issue_asset)(get_asset)(get_bitasset_data)(reserve_asset)

(global_settle_asset)(settle_asset)(bid_collateral)

(get_market_history) (get_order_book)
```

## 7. 非同质资产
``` text  
(register_nh_asset_creator)(create_world_view)(propose_relate_world_view)(create_nh_asset)

(list_nh_asset_by_creator)(list_account_nh_asset)(transfer_nh_asset)(get_nh_creator)

(delete_nh_asset)(create_nh_asset_order)(list_nh_asset_order)(cancel_nh_asset_order)

(fill_nh_asset_order)(list_account_nh_asset_order)
```

## 8. 事物和提议
``` text  
(begin_builder_transaction)(add_operation_to_builder_transaction)

(replace_operation_in_builder_transaction)(preview_builder_transaction)

(sign_builder_transaction)(propose_builder_transaction)(remove_builder_transaction)

(get_transaction_by_id)(get_transaction_in_block_info)(get_account_top_transaction)

(get_account_transaction)(get_signature_keys)

(serialize_transaction)(sign_transaction)(validate_transaction)

(propose_parameter_change)(propose_fee_change)(approve_proposal)
```  

## 9. 文件
``` text         
(create_file)(add_file_relate_account)(file_signature)

(list_account_created_file)(lookup_file)

(propose_relate_parent_file)
```


## 10. 其他
``` text  
(set_node_message_send_cache_size)(set_node_deduce_in_verification_mode)

(get_collateral_bids)(adjustment_temporary_authorization)

(sign_memo)(read_memo)(set_key_label)(get_key_label)(get_public_key)

(create_crontab)(cancel_crontab)(list_account_crontab)(crontab_builder_transaction)(recover_crontab)

(dbg_push_blocks)(dbg_generate_blocks)(dbg_stream_json_objects)(dbg_update_object)
```

