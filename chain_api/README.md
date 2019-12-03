# chain api

# 链api
## 链支持的api
``` text
       ["login",0],
       ["block",1],
       ["network_broadcast",2],
       ["database",3],
       ["history",4],
       ["network_node",5],
       ["asset",6],
       ["debug",7]
``` 
### api-access 
1. api-access 在config.ini中配置。默认为空。  

2. api-access若为空，login时: user="", password=""。这种模式下，节点只开发如下几种接口：  
``` text
        database_api
        network_broadcast_api
        history_api
        network_node_api
```

3. api-access配置

## api支持的接口
### 1. database_api  
``` text
       // Objects
       (get_objects)

       // Subscriptions
       (set_subscribe_callback)(set_pending_transaction_callback)(set_block_applied_callback)(cancel_all_subscriptions)

       // Blocks and transactions
       (get_block_header)(get_block_header_batch)(get_block)(get_transaction)(get_recent_transaction_by_id)

       // Globals
       (get_chain_properties)(get_global_properties)(get_config)(get_chain_id)(get_dynamic_global_properties)

       // Keys
       (get_key_references)(is_public_key_registered)(get_signature_keys)

       // Accounts
       (get_accounts)(get_full_accounts)(get_account_by_name)(get_account_references)(lookup_account_names)(lookup_accounts)(get_account_count)

       // Balances
       (get_account_balances)(get_named_account_balances)(get_balance_objects)(get_vested_balances)(get_vesting_balances)(get_prototype_operation_by_idx)

       // Lua contract
       (list_account_contracts)(get_account_contract_data)(get_contract_public_data)(get_contract)(get_transaction_by_id)(get_transaction_in_block_info)

       //nh asset
       (lookup_world_view)(lookup_nh_asset)(list_nh_asset_by_creator)(list_account_nh_asset)(get_nh_creator)(list_nh_asset_order)(list_new_nh_asset_order)(list_account_nh_asset_order)

       //file
       (lookup_file)(list_account_created_file)
       
       // crontab
       (list_account_crontab)
       
       // Assets
       (get_assets)(list_assets)(lookup_asset_symbols)(list_asset_restricted_objects)

       // Markets / feeds
       (get_order_book)(estimation_gas)(get_limit_orders)(get_call_orders)(get_settle_orders)(get_margin_positions)(get_collateral_bids)(subscribe_to_market)(unsubscribe_from_market)(get_ticker)(get_24_volume)(get_trade_history)(get_trade_history_by_sequence)

       // Witnesses
       (get_witnesses)(get_witness_by_account)(lookup_witness_accounts)(get_witness_count)

       // Committee members
       (get_committee_members)(get_committee_member_by_account)(lookup_committee_member_accounts)(get_committee_count)

       // workers
       (get_all_workers)

       // Votes
       (lookup_vote_ids)

       // Authority / validation
       (get_transaction_hex)(get_required_signatures)(get_potential_signatures)(get_potential_address_signatures)(verify_authority)(verify_account_authority)(validate_transaction)

       // Proposed transactions
       (get_proposed_transactions))
```

### 2. history_api  
``` text  
    (get_account_history)
    (get_account_history_operations)
    (get_relative_account_history)
    (get_fill_order_history)
    (get_market_history)
    (get_market_history_buckets)
```


### 3. block_api
``` text
       (get_blocks))

```


### 4. network_broadcast_api
``` text  
       (broadcast_transaction)
       (broadcast_transaction_with_callback)
       (broadcast_transaction_synchronous)
       (broadcast_block)
```

### 5. network_node_api
``` text  
       (get_info)
       (add_node)
       (get_connected_peers)
       (get_potential_peers)
       (get_advanced_node_parameters)

       # need permission
       (set_advanced_node_parameters)
       (set_message_send_cache_size)
       (set_deduce_in_verification_mode))
```

### 6. asset_api
``` text  
FC_API(graphene::app::asset_api,
       (get_asset_holders)(get_asset_holders_count)(get_all_asset_holders))

```

### 7. login_api
``` text  
FC_API(graphene::app::login_api,
       (login)(block)(network_broadcast)(database)(history)(network_node)(asset)(debug))
```



