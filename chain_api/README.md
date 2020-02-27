# chain api

# 链api
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

2. api-access若为空，login时: user="", password=""。这种模式下，节点只开放如下4种接口：  
``` text
        database_api
        network_broadcast_api
        history_api
        network_node_api
```

3. api-access配置示例和ws连接测试      
> apiaccess.json    

``` json  
{
    "permission_map":[
        [
            "root", {
                "password_hash_b64":"iHLgVGD7iiZXrFLRNH9GAF4mNqLO6OwvK0b2XZ6U1VI=",
                "password_salt_b64":"DXobg1wQ0Lg=",
                "allowed_apis":[
                    "database_api",
                    "network_broadcast_api",
                    "history_api",
                    "network_node_api",
                    "block_api",
                    "asset_api",
                    "debug_api",
                    "login_api"
                ]
            }
        ],
        [
            "*", {
                "password_hash_b64":"*",
                "password_salt_b64":"*",
                "allowed_apis":[
                    "database_api",
                    "network_broadcast_api",
                    "history_api",
                    "network_node_api"
                ]
            }
        ]
    ]
}
```

启动节点示例：  

```shell
./witness_node --genesis-json genesis.json -d witness_node_data_dir --plugins "debug_witness account_history market_history" --api-access "apiaccess.json"
```

使用cli_wallet测试连接：  

``` shell
./cli_wallet --chain-id 9f487f4cca8ababac23d3806a901e9044ab4d82be33cf2abb5cc3185e04fbafd -s ws://127.0.0.1:8052 -u root -p 123456

./cli_wallet --chain-id 9f487f4cca8ababac23d3806a901e9044ab4d82be33cf2abb5cc3185e04fbafd -s ws://127.0.0.1:8052 
```



​a. user="root", password="123456"测试  

```json  
Logging RPC to file: logs/rpc/rpc.log
850251ms th_a       main.cpp:131                  main                 ] key_to_wif( committee_private_key ): 5KCBDTcyDqzsqehcb52tW5nU6pXife6V2rX9Yf7c3saYSzbDZ5W 
850251ms th_a       main.cpp:135                  main                 ] nico_pub_key: COCOS7yE9skpBAirth3eSNMRtwq1jYswEE3uSbbuAtXTz88HtbpQsZf 
850251ms th_a       main.cpp:136                  main                 ] key_to_wif( nico_private_key ): 5KAUeN3Yv51FzpLGGf4S1ByKpMqVFNzXTJK7euqc3NnaaLz1GJm 
850253ms th_a       main.cpp:183                  main                 ] wdata.ws_server: ws://127.0.0.1:8052 
850256ms th_a       main.cpp:188                  main                 ] wdata.ws_user: root wdata.ws_password: 123456 
Please use the set_password method to initialize a new wallet before continuing
new >>> info
info
{
  "head_block_num": 0,
  "head_block_id": "0000000000000000000000000000000000000000",
  "head_block_age": "48 weeks ago",
  "next_maintenance_time": "50 years ago",
  "chain_id": "9f487f4cca8ababac23d3806a901e9044ab4d82be33cf2abb5cc3185e04fbafd",
  "participation": "100.00000000000000000",
  "active_witnesses": [
    "1.6.1",
    "1.6.2",
    "1.6.3",
    "1.6.4",
    "1.6.5",
    "1.6.6",
    "1.6.7",
    "1.6.8",
    "1.6.9",
    "1.6.10",
    "1.6.11"
  ],
  "active_committee_members": []
}
new >>> 
```  

b. user="", password=""测试    

```json
Logging RPC to file: logs/rpc/rpc.log
825920ms th_a       main.cpp:131                  main                 ] key_to_wif( committee_private_key ): 5KCBDTcyDqzsqehcb52tW5nU6pXife6V2rX9Yf7c3saYSzbDZ5W 
825920ms th_a       main.cpp:135                  main                 ] nico_pub_key: COCOS7yE9skpBAirth3eSNMRtwq1jYswEE3uSbbuAtXTz88HtbpQsZf 
825920ms th_a       main.cpp:136                  main                 ] key_to_wif( nico_private_key ): 5KAUeN3Yv51FzpLGGf4S1ByKpMqVFNzXTJK7euqc3NnaaLz1GJm 
825922ms th_a       main.cpp:183                  main                 ] wdata.ws_server: ws://127.0.0.1:8052 
825925ms th_a       main.cpp:188                  main                 ] wdata.ws_user:  wdata.ws_password:  
Please use the set_password method to initialize a new wallet before continuing
new >>> info
info
{
  "head_block_num": 0,
  "head_block_id": "0000000000000000000000000000000000000000",
  "head_block_age": "48 weeks ago",
  "next_maintenance_time": "50 years ago",
  "chain_id": "9f487f4cca8ababac23d3806a901e9044ab4d82be33cf2abb5cc3185e04fbafd",
  "participation": "100.00000000000000000",
  "active_witnesses": [
    "1.6.1",
    "1.6.2",
    "1.6.3",
    "1.6.4",
    "1.6.5",
    "1.6.6",
    "1.6.7",
    "1.6.8",
    "1.6.9",
    "1.6.10",
    "1.6.11"
  ],
  "active_committee_members": []
}
new >>> 
```  

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



