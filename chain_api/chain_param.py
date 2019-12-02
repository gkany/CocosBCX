#-*- coding: utf-8  -*-

operation_list = [
        "transfer_operation",                                      #0     static_variant  operation
        "limit_order_create_operation",                            #1   #自动检测是否有相符的订单，自动调用fill_order_operation撮合
        "limit_order_cancel_operation",                            #2    
        "call_order_update_operation",                             #3   #调整抵押单
        "fill_order_operation",                                    #4  # 系统私有op
        "account_create_operation",                                #5
        "account_update_operation",                                #6
        "account_upgrade_operation",                               #7  
        "asset_create_operation",                                  #8
        "asset_update_operation",                                  #9
        "asset_update_restricted_operation",                       #10
        "asset_update_bitasset_operation",                         #11     #/更新智能资产
        "asset_update_feed_producers_operation",                   #12     #/ 修改智能资产喂价账户
        "asset_issue_operation",                                   #13    #/定向发行资产
        "asset_reserve_operation",                                 #14    ##放弃部分资产，指定资产将被回收，流通量减少，总量不变
        "asset_settle_operation",                                  #15    ## 清算bitasset资产
        "asset_global_settle_operation",                           #16    #/ 在global_settle允许的情况下清算货币交易市场
        "asset_publish_feed_operation",                            #17
        "witness_create_operation",                                #18 见证人
        "witness_update_operation",                                #19
        "proposal_create_operation",                               #20
        "proposal_update_operation",                               #21
        "proposal_delete_operation",                               #22 #提议
        "committee_member_create_operation",                       #23 #理事会成员创建
        "committee_member_update_operation",                       #24 #理事会成员更新
        "committee_member_update_global_parameters_operation",     #25 #理事会更新链上运行参数
        "vesting_balance_create_operation",                        #26 #保留资金 ，锁定资金
        "vesting_balance_withdraw_operation",                      #27  #领取解冻的保留资金
        "worker_create_operation",                                 #28
        "balance_claim_operation",                                 #29  取回链初始化时分配的资产
        "asset_settle_cancel_operation",   # VIRTUAL               #30 #未有实体的清算取消操作
        "asset_claim_fees_operation",                              #31  #资产发行人从资产累计池中取回资产
        "bid_collateral_operation",                                #32  #智能货币抵押投标
        "execute_bid_operation",            # VIRTUAL              #33    # 内部私有op
        "contract_create_operation",                               #34
        "call_contract_function_operation",                        #35
        "temporary_authority_change_operation",                    #36
        "register_nh_asset_creator_operation",                     #37
        "create_world_view_operation",                             #38
        "relate_world_view_operation",                             #39
        "create_nh_asset_operation",                               #40
        "delete_nh_asset_operation",                               #41
        "transfer_nh_asset_operation",                             #42
        "create_nh_asset_order_operation",                         #43
        "cancel_nh_asset_order_operation",                         #44
        "fill_nh_asset_order_operation",                           #45
        "create_file_operation",                                   #46
        "add_file_relate_account_operation",                       #47
        "file_signature_operation",                                #48
        "relate_parent_file_operation",                            #49
        "revise_contract_operation",                               #50
        "crontab_create_operation",                                #51
        "crontab_cancel_operation",                                #52
        "crontab_recover_operation",                               #53
        "update_collateral_for_gas_operation",                     #54
        "account_authentication_operation"                         #55 
]


restricted_enum = [
        "all_restricted",                      #0,
        "whitelist_authorities",               #1,
        "blacklist_authorities",               #2,
        "whitelist_markets",                   #3,
        "blacklist_markets",                   #4
]


# enum class nh_asset_list_type
nh_asset_list_type = [
    "only_active"         ,                    # = 0,  // target with NHA active permission only 
    "only_owner"          ,                    # = 1,  // target with NHA owner permission only 
    "all_active"          ,                    # = 2,  // target with NHA active permission
    "all_owner"           ,                    # = 3,  // target with NHA active permission
    "owner_and_active"    ,                    # = 4   // target with NHA both active and owner permission
]