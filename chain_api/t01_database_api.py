#-*- coding: utf-8  -*-

import math
import unittest
from utils import *
from chain_param import *
from config import *
import sys
from time import sleep

class test_database_api(request_unittest):
    @classmethod
    def setUpClass(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "unlock",
            "params": [wallet_password],
            "id":1
        }
        request_post(req_data, is_wallet_rpc=True)

        req_data = {
            "jsonrpc": "2.0",
            "method": "import_key",
            "params": [test_account, test_account_private_key],
            "id":1
        }
        request_post(req_data, is_wallet_rpc=True)

        # req_data = {
        #     "jsonrpc": "2.0",
        #     "method": "import_key",
        #     "params": [test_witness_account, test_witness_account_private_key],
        #     "id":1
        # }
        # request_post(req_data, is_wallet_rpc=True)
        print('{} done\n'.format(sys._getframe().f_code.co_name))


    @classmethod
    def tearDownClass(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "lock",
            "params": [],
            "id":1
        }
        request_post(req_data, is_wallet_rpc=True)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    #    // Objects
    #    (get_objects)
    #   fc::variants get_objects(const vector<object_id_type> &ids) const;
    def test_get_objects(self):
        req_data = {
            "method": "get_objects",
            "params": [["1.2.0", "1.3.0"]],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    #    // Subscriptions
    #    (set_subscribe_callback)(set_pending_transaction_callback)(set_block_applied_callback)(cancel_all_subscriptions)

    #    // Blocks and transactions
    #    (get_block_header)(get_block_header_batch)(get_block)(get_transaction)(get_recent_transaction_by_id)

    #   optional<block_header> get_block_header(uint32_t block_num) const;
    def test_get_block_header(self):
        for block_num in range(10, 100, 20):
            req_data = {
                "method": "get_block_header",
                "params": [block_num],
                "id":1
            }
            self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    #   map<uint32_t, optional<block_header>> get_block_header_batch(const vector<uint32_t> block_nums) const;
    def test_get_block_header_batch(self):
        req_data = {
            "method": "get_block_header_batch",
            "params": [[10, 17, 35, 374]],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    #   optional<signed_block> get_block(uint32_t block_num) const;
    def test_get_block(self):
        for block_num in range(10, 100, 20):
            req_data = {
                "method": "get_block",
                "params": [block_num],
                "id":1
            }
            self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    #   processed_transaction get_transaction(uint32_t block_num, uint32_t trx_in_block) const;
    def test_get_transaction(self):
        req_data = {
            "method": "transfer",
            "params": [test_account, test_witness_account, "0.1", core_asset, ["node_rpc test get_transaction", 'false'], 'true'],
            "id":1
        }
        result = request_post(req_data, is_wallet_rpc=True)['result']
        transaction_id = result[0]
        sleep(3)  
        req_data = {
            "method": "get_transaction_in_block_info",
            "params": [transaction_id],
            "id":1
        }
        result = request_post(req_data, is_wallet_rpc=True)['result']
        self.assertIsNotNone(result)
        block_num = result['block_num']
        trx_in_block = 0
        req_data = {
            "method": "get_transaction",
            "params": [block_num, trx_in_block],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))


    #   optional<signed_transaction> get_recent_transaction_by_id(const string &id) const;
    def test_get_recent_transaction_by_id(self):
        req_data = {
            "method": "transfer",
            "params": [test_account, test_witness_account, "0.1", core_asset, ["node_rpc test get_transaction", 'false'], 'true'],
            "id":1
        }
        result = request_post(req_data, is_wallet_rpc=True)['result']
        transaction_id = result[0]
        sleep(2)  

        req_data = {
            "method": "get_recent_transaction_by_id",
            "params": [transaction_id],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    #    // Globals
    #    (get_chain_properties)(get_global_properties)(get_config)(get_chain_id)(get_dynamic_global_properties)
    def test_get_chain_properties(self):
        req_data = {
            "method": "get_chain_properties",
            "params": [],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_get_global_properties(self):
        req_data = {
            "method": "get_global_properties",
            "params": [],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_get_config(self):
        req_data = {
            "method": "get_config",
            "params": [],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_get_chain_id(self):
        req_data = {
            "method": "get_chain_id",
            "params": [],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_get_dynamic_global_properties(self):
        req_data = {
            "method": "get_dynamic_global_properties",
            "params": [],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    #    // Keys
    #    (get_key_references)(is_public_key_registered)(get_signature_keys)
    #   vector<vector<account_id_type>> get_key_references(vector<public_key_type> key) const;
    def test_get_key_references(self):
        req_data = {
            "method": "get_key_references",
            "params": [[test_account_public_key, test_witness_account_public_key]],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_is_public_key_registered(self):
        req_data = {
            "method": "is_public_key_registered",
            "params": [test_account_public_key],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_get_signature_keys(self):
        req_data = {
            "method": "transfer",
            "params": [test_account, test_witness_account, "0.1", core_asset, ["node_rpc test get_transaction", 'false'], 'false'],
            "id":1
        }
        trx = request_post(req_data, is_wallet_rpc=True)['result']

        req_data = {
            "method": "get_signature_keys",
            "params": [trx[1]],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    #    // Accounts  
    #    (get_accounts)(get_full_accounts)(get_account_by_name)(get_account_references)(lookup_account_names)(lookup_accounts)(get_account_count)

    def test_get_accounts(self):
        account_ids = []
        for index in range(0, 10, 2):
            account_id = "1.2.{}".format(index)
            account_ids.append(account_id)
        req_data = {
            "method": "get_accounts",
            "params": [account_ids],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_get_full_accounts(self):
        req_data = {
            "method": "get_full_accounts",
            "params": [[test_account, test_witness_account], 'true'],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_get_account_by_name(self):
        req_data = {
            "method": "get_account_by_name",
            "params": [test_account_public_key],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_get_account_references(self):
        for index in range(0, 10, 2):
            account_id = "1.2.{}".format(index)
            req_data = {
                "method": "get_account_references",
                "params": [account_id],
                "id":1
            }
            self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_lookup_account_names(self):
        req_data = {
            "method": "lookup_account_names",
            "params": [[test_account, test_witness_account]],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_lookup_accounts(self):
        req_data = {
            "method": "lookup_accounts",
            "params": ["", 5],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    #    // Balances
    #    (get_account_balances)(get_named_account_balances)(get_balance_objects)(get_vested_balances)(get_vesting_balances)(get_prototype_operation_by_idx)

    #   vector<asset> get_account_balances(account_id_type id, const flat_set<asset_id_type> &assets) const;
    def test_get_account_balances(self):
        assets = ["1.3.0", "1.3.1"]
        for index in range(0, 10, 2):
            account_id = "1.2.{}".format(index)
            req_data = {
                "method": "get_account_balances",
                "params": [account_id, assets],
                "id":1
            }
            self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_get_named_account_balances(self):
        assets = ["1.3.0", "1.3.1"]
        accounts = [test_account, test_witness_account, test_committee_account]
        for account_name in accounts:
            req_data = {
                "method": "get_named_account_balances",
                "params": [account_name, assets],
                "id":1
            }
            self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

#       vector<balance_object> get_balance_objects(const vector<address> &addrs) const;
    def test_get_balance_objects(self):
        addres_list = [test_balance_address]
        req_data = {
            "method": "get_balance_objects",
            "params": [addres_list],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    #   vector<asset> get_vested_balances(const vector<balance_id_type> &objs) const;
    def test_get_vested_balances(self):
        balance_ids = []
        for index in range(1, 10, 3):
            balance_id = "1.15.{}".format(index)
            balance_ids.append(balance_id)
        req_data = {
            "method": "get_vested_balances",
            "params": [balance_ids],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    #   vector<vesting_balance_object> get_vesting_balances(account_id_type account_id) const;
    def test_get_vesting_balances(self):
        accounts = [test_account, test_witness_account, test_committee_account]
        for account_name in accounts:
            req_data = {
                "method": "get_vesting_balances",
                "params": [account_name],
                "id":1
            }
            self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    #    // Lua contract
    #    (list_account_contracts)(get_account_contract_data)(get_contract_public_data)(get_contract)(get_transaction_by_id)(get_transaction_in_block_info)

    #    //nh asset
    #    (lookup_world_view)(lookup_nh_asset)(list_nh_asset_by_creator)(list_account_nh_asset)(get_nh_creator)(list_nh_asset_order)(list_new_nh_asset_order)(list_account_nh_asset_order)

    #    //file
    #    (lookup_file)(list_account_created_file)
       
    #    // crontab
    #    (list_account_crontab)
       
    #    // Assets
    #    (get_assets)(list_assets)(lookup_asset_symbols)(list_asset_restricted_objects)

    #    // Markets / feeds
    #    (get_order_book)(estimation_gas)(get_limit_orders)(get_call_orders)(get_settle_orders)(get_margin_positions)(get_collateral_bids)(subscribe_to_market)(unsubscribe_from_market)(get_ticker)(get_24_volume)(get_trade_history)(get_trade_history_by_sequence)

    #    // Witnesses
    #    (get_witnesses)(get_witness_by_account)(lookup_witness_accounts)(get_witness_count)
    def test_get_witnesses(self):
        committee_ids = []
        for index in range(1, 11, 3):
            committee_id = "1.5.{}".format(index)
            committee_ids.append(committee_id)
        req_data = {
            "method": "get_witnesses",
            "params": [committee_ids],
            "id":1
        }
        self.request_post(req_data)

    def test_get_witness_by_account(self):
        committee_accounts = [test_witness_account]
        for account in committee_accounts:
            req_data = {
                "method": "get_witness_by_account",
                "params": [account],
                "id":1
            }
            self.request_post(req_data)

    def test_lookup_witness_accounts(self):
        req_data = {
            "method": "lookup_witness_accounts",
            "params": ["", 5],
            "id":1
        }
        self.request_post(req_data)

    def test_get_witness_count(self):
        req_data = {
            "method": "get_witness_count",
            "params": [],
            "id":1
        }
        self.request_post(req_data)

    #    // Committee members
    #    (get_committee_members)(get_committee_member_by_account)(lookup_committee_member_accounts)(get_committee_count)
    # vector<optional<committee_member_object>> get_committee_members(const vector<committee_member_id_type> &committee_member_ids) const;
    # fc::optional<committee_member_object> get_committee_member_by_account(account_id_type account) const;
    # map<string, committee_member_id_type> lookup_committee_member_accounts(const string &lower_bound_name, uint32_t limit) const;
    # uint64_t get_committee_count() const;
    def test_get_committee_members(self):
        committee_ids = []
        for index in range(1, 11, 3):
            committee_id = "1.6.{}".format(index)
            committee_ids.append(committee_id)
        req_data = {
            "method": "get_committee_members",
            "params": [committee_ids],
            "id":1
        }
        self.request_post(req_data)

    def test_get_committee_member_by_account(self):
        committee_accounts = [test_committee_account]
        for account in committee_accounts:
            req_data = {
                "method": "get_committee_member_by_account",
                "params": [account],
                "id":1
            }
            self.request_post(req_data)

    def test_lookup_committee_member_accounts(self):
        req_data = {
            "method": "lookup_committee_member_accounts",
            "params": ["", 5],
            "id":1
        }
        self.request_post(req_data)

    def test_get_committee_count(self):
        req_data = {
            "method": "get_committee_count",
            "params": [],
            "id":1
        }
        self.request_post(req_data)

    #    // workers
    #    (get_all_workers)
    def test_get_all_workers(self):
        req_data = {
            "method": "get_all_workers",
            "params": [],
            "id":1
        }
        self.request_post(req_data)

    #    // Votes
    #    (lookup_vote_ids)
    def test_lookup_vote_ids(self):
        votes = ["1:0", "1:1"]
        req_data = {
            "method": "lookup_vote_ids",
            "params": [votes],
            "id":1
        }
        self.request_post(req_data)

    #    // Authority / validation
    #    (get_transaction_hex)(get_required_signatures)(get_potential_signatures)(get_potential_address_signatures)(verify_authority)(verify_account_authority)(validate_transaction)
    def test_get_transaction_hex(self):
        req_data = {
            "method": "transfer",
            "params": [test_account, test_witness_account, "0.1", core_asset, ["node_rpc test get_transaction_hex", 'false'], 'true'],
            "id":1
        }
        result = request_post(req_data, is_wallet_rpc=True)['result']
        trx = result[1]
        account_id = "1.2.{}".format(index)
        req_data = {
            "method": "get_transaction_hex",
            "params": [trx],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_get_required_signatures(self):
        req_data = {
            "method": "transfer",
            "params": [test_account, test_witness_account, "0.1", core_asset, ["node_rpc test get_required_signatures", 'false'], 'true'],
            "id":1
        }
        result = request_post(req_data, is_wallet_rpc=True)['result']
        trx = result[1]
        req_data = {
            "method": "get_required_signatures",
            "params": [trx, [test_witness_account_public_key]],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_get_potential_signatures(self):
        req_data = {
            "method": "transfer",
            "params": [test_account, test_witness_account, "0.1", core_asset, ["node_rpc test get_potential_signatures", 'false'], 'true'],
            "id":1
        }
        result = request_post(req_data, is_wallet_rpc=True)['result']
        trx = result[1]
        req_data = {
            "method": "get_potential_signatures",
            "params": [trx],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    # get_potential_address_signatures
    def test_get_potential_address_signatures(self):
        req_data = {
            "method": "transfer",
            "params": [test_account, test_witness_account, "0.1", core_asset, ["node_rpc test get_potential_address_signatures", 'false'], 'true'],
            "id":1
        }
        result = request_post(req_data, is_wallet_rpc=True)['result']
        trx = result[1]
        req_data = {
            "method": "get_potential_address_signatures",
            "params": [trx],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    # verify_authority
    def test_verify_authority(self):
        req_data = {
            "method": "transfer",
            "params": [test_account, test_witness_account, "0.1", core_asset, ["node_rpc test verify_authority", 'false'], 'true'],
            "id":1
        }
        result = request_post(req_data, is_wallet_rpc=True)['result']
        trx = result[1]
        req_data = {
            "method": "verify_authority",
            "params": [trx],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_verify_account_authority(self):
        req_data = {
            "method": "verify_account_authority",
            "params": [test_account, [test_account_public_key]],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
            "method": "verify_account_authority",
            "params": [test_account, [test_account_public_key, test_witness_account_public_key]],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    # validate_transaction
    def test_validate_transaction(self):
        req_data = {
            "method": "transfer",
            "params": [test_account, test_witness_account, "0.1", core_asset, ["node_rpc test verify_authority", 'false'], 'true'],
            "id":1
        }
        result = request_post(req_data, is_wallet_rpc=True)['result']
        trx = result[1]
        req_data = {
            "method": "validate_transaction",
            "params": [trx],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    #    // Proposed transactions
    #    (get_proposed_transactions))
    def test_get_proposed_transactions(self):
        for index in range(5, 16, 2):
            account_id = "1.2.{}".format(index)
            req_data = {
                "method": "get_proposed_transactions",
                "params": [account_id],
                "id":1
            }
            self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))



if __name__ == '__main__':
    unittest.main()