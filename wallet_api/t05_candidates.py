#-*- coding: utf-8  -*-

import unittest
from config import *
from utils import *
import os

class test_wallet_candidates_api(request_unittest):
    @classmethod
    def setUpClass(self):
        # self.new_witness = "test.witness"
        # self.new_committee = "test.committee"
        # self.new_witness_pub_key = test_witness_account_public_key
        self.new_witness = ""
        self.new_committee = ""

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

        #register_account new_witness_account
        tokens = generate_random_words()
        size = len(tokens[0])+len(tokens[1])+len(tokens[2])
        new_witness_account_name = tokens[0].lower() + str(size)
        # pub_key = suggest_brain_key['pub_key']
        pub_key = test_witness_account_public_key
        register = test_account
        req_data = {
            "jsonrpc": "2.0",
            "method": "register_account",
            "params": [new_witness_account_name, pub_key, pub_key, register, 'true'],
            "id":1
        }
        request_post(req_data)
        self.new_witness = new_witness_account_name
        req_data = {
            "jsonrpc": "2.0",
            "method": "import_key",
            "params": [new_witness_account_name, test_witness_account_private_key],
            "id":1
        }
        request_post(req_data)

        #register_account new_committee_account
        size = len(tokens[0])+len(tokens[3])+len(tokens[4])
        new_committee_account_name = tokens[1].lower() + str(size)
        # pub_key = suggest_brain_key['pub_key']
        pub_key = test_committee_account_public_key
        register = test_account
        req_data = {
            "jsonrpc": "2.0",
            "method": "register_account",
            "params": [new_committee_account_name, pub_key, pub_key, register, 'true'],
            "id":1
        }
        request_post(req_data)
        self.new_committee = new_committee_account_name
        req_data = {
            "jsonrpc": "2.0",
            "method": "import_key",
            "params": [new_committee_account_name, test_committee_account_private_key],
            "id":1
        }
        request_post(req_data)
        print('setUpClass done')

    @classmethod
    def tearDownClass(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "lock",
            "params": [],
            "id":1
        }
        request_post(req_data)
        print('tearDownClass done')

    def setUp(self):
        print('setUp done')

    def tearDown(self):
        print('tearDown done')

    # @unittest.skipIf(True, 'test other')
    def test_get_witness(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "get_witness",
            "params": [test_witness_account],
            "id":1
        }
        self.request_post(req_data)

    def test_get_committee_member(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "get_committee_member",
            "params": [test_committee_account],
            "id":1
        }
        self.request_post(req_data)

    def test_list_witnesses(self):
        lowerbound = ""
        limit = 3
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_witnesses",
            "params": [lowerbound, limit],
            "id":1
        }
        self.request_post(req_data)

    def test_list_committee_members(self):
        lowerbound = ""
        limit = 3
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_committee_members",
            "params": [lowerbound, limit],
            "id":1
        }
        self.request_post(req_data)

    @unittest.skipIf(True, 'test other')
    def test_vote_for_witness(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "vote_for_witness",
            "params": [test_account, test_witness_account, 10000, 'true'],
            "id":1
        }
        self.request_post(req_data)

    @unittest.skipIf(True, 'test other')
    def test_vote_for_committee_member(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "vote_for_committee_member",
            "params": [test_account, test_committee_account, 10000, 'true'],
            "id":1
        }
        self.request_post(req_data)

    @unittest.skipIf(True, 'test other')
    def test_create_witness(self):
        # fee
        req_data = {
            "jsonrpc": "2.0",
            "method": "transfer",
            "params": [test_account, self.new_witness, 80000000, 'COCOS', 'test account', 'true'],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "upgrade_account",
            "params": [self.new_witness, 'true'],
            "id":1
        }
        self.request_post(req_data)

        url = "www.create_witness-test.org"
        req_data = {
            "jsonrpc": "2.0",
            "method": "create_witness",
            "params": [self.new_witness, url, 'true'],
            "id":1
        }
        self.request_post(req_data)
        req_data = {
            "jsonrpc": "2.0",
            "method": "get_witness",
            "params": [self.new_witness],
            "id":1
        }
        self.request_post(req_data)

    @unittest.skipIf(True, 'test other')
    def test_create_committee_member(self):
        # fee
        req_data = {
            "jsonrpc": "2.0",
            "method": "transfer",
            "params": [test_account, self.new_committee, 80000000, 'COCOS', 'test account', 'true'],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "upgrade_account",
            "params": [self.new_committee, 'true'],
            "id":1
        }
        self.request_post(req_data)

        url = "www.create_committee-test.org"
        req_data = {
            "jsonrpc": "2.0",
            "method": "create_committee_member",
            "params": [self.new_committee, url, 'true'],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "get_committee_member",
            "params": [self.new_committee],
            "id":1
        }
        self.request_post(req_data)

    def test_update_witness(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "update_witness",
            "params": [test_witness_account, "www.update_witness.org", test_witness_account_public_key, 'true', 'true'],
            "id":1
        }
        self.request_post(req_data)

    def test_update_committee_member(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "update_committee_member",
            "params": [test_committee_account, "www.update_committee_member.org", 'true', 'true'],
            "id":1
        }
        self.request_post(req_data)


if __name__ == "__main__":
    unittest.main()

