#-*- coding: utf-8  -*-

import math
import unittest
from utils import request_unittest
from chain_param import operation_list
from config import *

class test_wallet_common_api(request_unittest):
    def test_help(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "help",
            "params": [],
            "id":1
        }
        self.request_post_error_asset_false(req_data)

    def test_gethelp(self):
        methods = ['transfer', 'register_account', 'about']
        for method in methods:
            req_data = {
                "jsonrpc": "2.0",
                "method": "gethelp",
                "params": [method],
                "id":1
            }
            self.request_post_error_asset_false(req_data)

    def test_info(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "info",
            "params": [],
            "id":1
        }
        self.request_post_error_asset_false(req_data)
    
    def test_about(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "about",
            "params": [],
            "id":1
        }
        self.request_post_error_asset_false(req_data)

    def test_network_add_nodes(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "network_add_nodes",
            "params": [["127.0.0.1:8090"]],
            "id":1
        }
        # self.request_post_error_asset_false(req_data)
        self.request_post_error_asset_true(req_data)

    def test_network_get_connected_peers(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "network_get_connected_peers",
            "params": [],
            "id":1
        }
        self.request_post_error_asset_false(req_data)

    def test_get_block(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "info",
            "params": [],
            "id":1
        }
        info = self.request_post(req_data)['result']
        num = math.ceil(info['head_block_num']/2)

        req_data = {
            "jsonrpc": "2.0",
            "method": "get_block",
            "params": [num],
            "id":1
        }
        self.request_post(req_data)

    def test_get_global_properties(self):
        req_data = {
            "jsonrpc": "1.2.0",
            "method": "get_global_properties",
            "params": [],
            "id":1
        }
        self.request_post(req_data)

    def test_get_dynamic_global_properties(self):
        req_data = {
            "jsonrpc": "1.2.0",
            "method": "get_dynamic_global_properties",
            "params": [],
            "id":1
        }
        self.request_post(req_data)

    def test_get_chain_properties(self):
        req_data = {
            "jsonrpc": "1.2.0",
            "method": "get_chain_properties",
            "params": [],
            "id":1
        }
        self.request_post(req_data)

    @unittest.skipIf(True, 'test other')
    def test_get_prototype_operation_by_name(self):
        for operation in operation_list:
            req_data = {
                "jsonrpc": "1.2.0",
                "method": "get_prototype_operation_by_name",
                "params": [operation],
                "id":1
            }
            self.request_post(req_data)

    @unittest.skipIf(True, 'test other')
    def test_get_prototype_operation_by_idx(self):
        for index in range(0, len(operation_list)):
            req_data = {
                "jsonrpc": "1.2.0",
                "method": "get_prototype_operation_by_idx",
                "params": [index],
                "id":1
            }
            self.request_post(req_data)
        
    def test_is_public_key_registered(self):
        pub_key = test_account_public_key
        req_data = {
            "jsonrpc": "1.2.0",
            "method": "is_public_key_registered",
            "params": [pub_key],
            "id":1
        }
        # self.request_post(req_data)
        self.request_post_result_asset_true(req_data)

if __name__ == '__main__':
    unittest.main()