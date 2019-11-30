#-*- coding: utf-8  -*-

import unittest
from config import *
from utils import *
import os

class test_wallet_contract_api(request_unittest):
    @classmethod
    def setUpClass(self):
        self.owner = test_account
        self.pub_key = test_account_public_key
        self.contract_name = "contract.debug.hello"
        # self.contract_name = "contract.debug.world"
        self.function_name = "hello"
        self.contract_data = "function {}() chainhelper:log('create contract test') end".format(self.function_name)

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

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unittest.skipIf(True, 'test other')
    def test_create_contract(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "create_contract",
            "params": [self.owner, self.contract_name, self.pub_key, self.contract_data, 'true'],
            "id":1
        }
        self.request_post(req_data)

    @unittest.skipIf(True, 'filename need cli_wallet abspath')
    def test_create_contract_from_file(self):
        #generate random contract_name by suggest_brain_key
        tokens = generate_random_words()
        owner = test_account
        contract_name = "test.contract." + tokens[0].lower()
        contract_authority = test_account_public_key
        current_path = os.path.abspath(os.path.dirname(__file__))
        filename = current_path + '/' + "contract_hello.lua"
        print('filename: {}'.format(filename))
        req_data = {
            "jsonrpc": "2.0",
            "method": "create_contract_from_file",
            "params": [owner, contract_name, contract_authority, filename, 'true'],
            "id":1
        }
        self.request_post(req_data)

    def test_get_contract(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "get_contract",
            "params": [self.contract_name],
            "id":1
        }
        self.request_post(req_data)

    def test_call_contract_function(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "call_contract_function",
            "params": [self.owner, self.contract_name, self.function_name, [], 'true'],
            "id":1
        }
        self.request_post(req_data)

    def test_revise_contract(self):
        contract_data = "function {}() chainhelper:log('revise_contract test') end".format(self.function_name)
        req_data = {
            "jsonrpc": "2.0",
            "method": "revise_contract",
            "params": [self.owner, self.contract_name, contract_data, 'true'],
            "id":1
        }
        self.request_post(req_data)

    def test_get_account_contract_data(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "get_account_contract_data",
            "params": [self.owner, self.contract_name],
            "id":1
        }
        self.request_post(req_data)

    def test_get_contract_public_data(self):
        filter = [[]]
        req_data = {
            "jsonrpc": "2.0",
            "method": "get_contract_public_data",
            "params": [self.contract_name, filter],
            "id":1
        }
        self.request_post(req_data)

if __name__ == "__main__":
    unittest.main()

