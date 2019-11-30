#-*- coding: utf-8  -*-

import unittest
from utils import request_unittest, request_post
from config import *

class test_wallet_info_api(request_unittest):
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

    @classmethod
    def tearDownClass(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "lock",
            "params": [],
            "id":1
        }
        request_post(req_data)

    def test_is_new(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "is_new",
            "params": [],
            "id":1
        }
        # self.request_post(req_data)
        self.request_post_result_asset_false(req_data)

    def test_is_locked(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "is_locked",
            "params": [],
            "id":1
        }
        self.request_post_result_asset_false(req_data)

    def test_lock(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "lock",
            "params": [],
            "id":1
        }
        # self.request_post(req_data)
        self.request_post_result_asset_is_none(req_data)
    
    def test_unlock(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "unlock",
            "params": [wallet_password],
            "id":1
        }
        # self.request_post(req_data)
        self.request_post_result_asset_is_none(req_data)

    def test_set_password(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "set_password",
            "params": [wallet_password],
            "id":1
        }
        # self.request_post(req_data)
        self.request_post_result_asset_is_none(req_data)

    def test_dump_private_keys(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "dump_private_keys",
            "params": [wallet_password],
            "id":1
        }
        keys = [test_account_public_key, test_account_private_key]
        self.request_post_result_asset_in(req_data, keys)

    def test_import_key(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "import_key",
            "params": [test_account, test_account_private_key],
            "id":1
        }
        # self.request_post(req_data)
        self.request_post_result_asset_true(req_data)

    def test_import_balance(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "import_balance",
            "params": [test_account, [test_balance_address], 'true'],
            "id":1
        }
        value = [] # 链初始化时已经执行过import_balance, 再次执行result = []
        self.request_post_result_asset_equal(req_data, value)

    def test_suggest_brain_key(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "suggest_brain_key",
            "params": [],
            "id":1
        }
        # self.request_post(req_data)
        self.request_post_error_asset_false(req_data)

    @unittest.skipIf(True, 'test other')
    def test_get_transaction_id(self):
        transfer_req_data = {
            "jsonrpc": "2.0",
            "method": "transfer",
            "params": [test_account, test_witness_account, 100, 'COCOS', 'get_transaction_id test', 'false'],
            "id":1
        }
        response = self.request_post(transfer_req_data)
        result = response['result']
        # print('result: {}'.format(result))
        transaction_id = result[0]
        transaction = result[1]
        # print('trx_id: {}, trx: {}'.format(transaction_id, transaction))

        req_data = {
            "jsonrpc": "2.0",
            "method": "get_transaction_id",
            "params": [transaction],
            "id":1
        }
        # self.request_post(req_data)
        self.request_post_result_asset_in(req_data, transaction_id, False)

    def test_get_private_key(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "get_private_key",
            "params": [test_account_public_key],
            "id":1
        }
        # self.request_post(req_data)
        self.request_post_result_asset_equal(req_data, test_account_private_key)

    def test_normalize_brain_key(self):
        test_brain_key = "  test   wallet API    NORMALIZE BRAIN  key by python unit TEST  "
        normalize_brain_key = "TEST WALLET API NORMALIZE BRAIN KEY BY PYTHON UNIT TEST"
        req_data = {
            "jsonrpc": "2.0",
            "method": "normalize_brain_key",
            "params": [test_brain_key],
            "id":1
        }
        # self.request_post(req_data)
        self.request_post_result_asset_equal(req_data, normalize_brain_key)

    def test_save_wallet_file(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "save_wallet_file",
            "params": ["test_wallet.json"],
            "id":1
        }
        # self.request_post(req_data)
        self.request_post_result_asset_is_none(req_data)

    def test_load_wallet_file(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "load_wallet_file",
            "params": [""],
            "id":1
        }
        # self.request_post(req_data)
        self.request_post_result_asset_true(req_data)

    def test_derive_owner_keys_from_brain_key(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "suggest_brain_key",
            "params": [],
            "id":1
        }
        suggest_brain_key = self.request_post(req_data)['result']
        brain_key = suggest_brain_key['brain_priv_key']
        private_key = suggest_brain_key['wif_priv_key']
        public_key =  suggest_brain_key['pub_key']
        
        req_data = {
            "jsonrpc": "2.0",
            "method": "derive_owner_keys_from_brain_key",
            "params": [brain_key, 1],
            "id":1
        }
        result = self.request_post(req_data)['result'][0]
        self.assertTrue(private_key, result['wif_priv_key'])
        self.assertTrue(public_key, result['pub_key'])

    def test_suggest_brain_address_key(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "suggest_brain_address_key",
            "params": [],
            "id":1
        }
        self.request_post(req_data)
        # self.request_post_error_asset_false(req_data)

if __name__ == '__main__':
    unittest.main()

