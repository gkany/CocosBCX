#-*- coding: utf-8  -*-

import unittest
from utils import request_unittest, request_post
from config import *

class test_wallet_account_api(request_unittest):
    @classmethod
    def setUpClass(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "unlock",
            "params": [wallet_password],
            "id":1
        }
        request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "import_key",
            "params": [test_account, test_account_private_key],
            "id":1
        }
        request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "import_key",
            "params": [test_witness_account, test_witness_account_private_key],
            "id":1
        }
        request_post(req_data)

    @classmethod
    def tearDownClass(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "lock",
            "params": [],
            "id":1
        }
        request_post(req_data)

    def test_list_my_accounts(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_my_accounts",
            "params": [],
            "id":1
        }
        # self.request_post(req_data)
        self.request_post_error_asset_false(req_data)

    def test_list_accounts(self):
        committee_account = ["committee-account", "1.2.0"]
        committee_relaxed = ["committee-relaxed", "1.2.1"]
        lowerbound = ""
        limit = 10
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_accounts",
            "params": [lowerbound, limit],
            "id":1
        }
        self.request_post_result_asset_in(req_data, committee_account)
        self.request_post_result_asset_in(req_data, committee_relaxed)

    def test_list_account_balances(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_account_balances",
            "params": [test_account],
            "id":1
        }
        # self.request_post(req_data)
        self.request_post_error_asset_false(req_data)

    @unittest.skipIf(True, 'test other')
    def test_register_account(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "suggest_brain_key",
            "params": [],
            "id":1
        }
        suggest_brain_key = self.request_post(req_data)['result']
        brain_priv_key = suggest_brain_key['brain_priv_key']
        # print('suggest_brain_key: {}'.format(brain_priv_key))
        tokens = brain_priv_key.split()
        # print('token: {}'.format(tokens))
        # new_account_name = tokens[0].lower() + tokens[1].lower()
        size = len(tokens[0])+len(tokens[1])+len(tokens[2])
        new_account_name = tokens[0].lower() + str(size)
        pub_key = suggest_brain_key['pub_key']
        register = test_account
        req_data = {
            "jsonrpc": "2.0",
            "method": "register_account",
            "params": [new_account_name, pub_key, pub_key, register, 'true'],
            "id":1
        }
        self.request_post(req_data)

        # upgrade_account fee
        req_data = {
            "jsonrpc": "2.0",
            "method": "transfer",
            "params": [test_account, new_account_name, 10000*2, 'COCOS', 'test account', 'true'],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "import_key",
            "params": [new_account_name, suggest_brain_key['wif_priv_key']],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "upgrade_account",
            "params": [new_account_name, 'true'],
            "id":1
        }
        self.request_post(req_data)
    
    @unittest.skipIf(True, 'test other')
    def test_create_account_with_brain_key(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "suggest_brain_key",
            "params": [],
            "id":1
        }
        suggest_brain_key = self.request_post(req_data)['result']
        brain_key = suggest_brain_key['brain_priv_key']
        # print('suggest_brain_key: {}'.format(brain_priv_key))

        tokens = brain_key.split()
        size = len(tokens[0])+len(tokens[3])+len(tokens[4])
        new_account_name = tokens[0].lower() + str(size)
        register = test_account
        req_data = {
            "jsonrpc": "2.0",
            "method": "create_account_with_brain_key",
            "params": [brain_key, new_account_name, register, 'true'],
            "id":1
        }
        self.request_post(req_data)


    def test_get_vesting_balances(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "get_vesting_balances",
            "params": [test_witness_account],
            "id":1
        }
        # self.request_post(req_data)
        self.request_post_error_asset_false(req_data)


    @unittest.skipIf(True, 'test other')
    def test_withdraw_vesting(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "get_vesting_balances",
            "params": [test_witness_account],
            "id":1
        }
        response = self.request_post(req_data)
        # self.request_post_error_asset_false(req_data)
        for withdraw in response['result']:
            print('withdraw: {}'.format(withdraw))
            withdraw = withdraw['allowed_withdraw']
            # amount = int(withdraw['amount']/1000)
            amount = 1000
            asset_id = withdraw['asset_id']

            req_data = {
                "jsonrpc": "2.0",
                "method": "withdraw_vesting",
                "params": [test_witness_account, amount, asset_id, 'true'],
                "id":1
            }
            self.request_post(req_data)

    def test_get_account(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "get_account",
            "params": [test_account],
            "id":1
        }
        self.request_post(req_data)


    def test_get_account_id(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "get_account_id",
            "params": [test_account],
            "id":1
        }
        self.request_post(req_data)


    def test_get_account_history(self):
        limit = 3
        req_data = {
        "jsonrpc": "2.0",
        "method": "get_account_history",
        "params": [test_account, limit],
        "id":1
        }
        self.request_post(req_data)

    def test_transfer(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "transfer",
            "params": [test_account, test_witness_account, 10, 'COCOS', 'test transfer', 'true'],
            "id":1
        }
        self.request_post(req_data)

    def test_transfer2(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "transfer2",
            "params": [test_account, test_witness_account, 10, 'COCOS', 'test transfer2'],
            "id":1
        }
        self.request_post(req_data)

    def test_get_account_count(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "get_account_count",
            "params": [],
            "id":1
        }
        self.request_post(req_data)

    def test_get_relative_account_history(self):
        stop = 0
        limit = 12
        start = 3
        req_data = {
        "jsonrpc": "2.0",
        "method": "get_relative_account_history",
        "params": [test_account, stop, limit, start],
        "id":1
        }
        self.request_post(req_data)

    def test_update_collateral_for_gas(self):
        amount = 10*10**5
        req_data = {
        "jsonrpc": "2.0",
        "method": "update_collateral_for_gas",
        "params": [test_account, test_witness_account, amount, 'true'],
        "id":1
        }
        self.request_post(req_data)

if __name__ == "__main__":
    unittest.main()

