#-*- coding: utf-8  -*-

import unittest
from utils import *
from config import *
import sys
from websocket import create_connection

class test_history_api(websocket_unittest):
    @classmethod
    def setUpClass(self):
        self.ws = create_connection(node_ws_url)
        req_data = {
            "id":1,
            "method":"call",
            "params":[1, "history", []]
        }
        self.handle = ws_post(self.ws, req_data)['result']
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @classmethod
    def tearDownClass(self):
        self.ws.close()
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    # (get_account_history)(get_account_history_operations)(get_relative_account_history)
    # (get_fill_order_history)(get_market_history)(get_market_history_buckets)

    # vector<operation_history_object> 
    # history_api::get_account_history(
    #     account_id_type account,
    #     operation_history_id_type stop,
    #     unsigned limit,
    #     operation_history_id_type start) const
    def test_get_account_history(self):
        stop = "1.11.30"
        limit = 10
        start = "1.11.5"
        for index in range(3, 20, 3):
            account_id = "1.2.{}".format(index)
            params = [account_id, stop, limit, start]
            req_data = {
                "id":1,
                "method":"call",
                "params":[self.handle, "get_account_history", params]
            }
            self.ws_post(self.ws, req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    # vector<operation_history_object> 
    # history_api::get_account_history_operations(
    #         account_id_type account,
    #         unsigned operation_id,
    #         operation_history_id_type start,
    #         operation_history_id_type stop,
    #         unsigned limit) const
    def test_get_account_history_operations(self):
        stop = "1.11.30"
        limit = 10
        start = "1.11.5"
        operation_id = 0 #transfer
        for index in range(3, 20, 3):
            account_id = "1.2.{}".format(index)
            params = [account_id, operation_id, start, stop, limit]
            req_data = {
                "id":1,
                "method":"call",
                "params":[self.handle, "get_account_history_operations", params]
            }
            self.ws_post(self.ws, req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

#   vector<operation_history_object> get_relative_account_history(account_id_type account,
#                                                                 uint32_t stop = 0,
#                                                                 unsigned limit = 100,
#                                                                 uint32_t start = 0) const;
    def test_get_relative_account_history(self):
        start = 2
        stop = 17
        limit = 10
        for index in range(3, 20, 3):
            account_id = "1.2.{}".format(index)
            params = [account_id, stop, limit, start]
            req_data = {
                "id":1,
                "method":"call",
                "params":[self.handle, "get_relative_account_history", params]
            }
            self.ws_post(self.ws, req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

#   vector<order_history_object> get_fill_order_history(asset_id_type a, asset_id_type b, uint32_t limit) const;
    def test_get_fill_order_history(self):
        a_asset_id = "1.3.0"  # core_asset
        limit = 10
        for index in range(1, 2):
            b_asset_id = "1.3.{}".format(index)
            params = [a_asset_id, b_asset_id, limit]
            req_data = {
                "id":1,
                "method":"call",
                "params":[self.handle, "get_fill_order_history", params]
            }
            self.ws_post(self.ws, req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

#   vector<bucket_object> get_market_history(asset_id_type a, asset_id_type b, uint32_t bucket_seconds,
#                                            fc::time_point_sec start, fc::time_point_sec end) const;
    def test_get_market_history(self):
        a_asset_id = "1.3.0"  # core_asset
        bucket_seconds = 300
        start = datetime_N_ago(10).strftime("%Y-%m-%dT%H:%M:%S")
        end = datetime_N_ago(0).strftime("%Y-%m-%dT%H:%M:%S")
        for index in range(1, 2):
            b_asset_id = "1.3.{}".format(index)
            params = [a_asset_id, b_asset_id, bucket_seconds, start, end]
            req_data = {
                "id":1,
                "method":"call",
                "params":[self.handle, "get_market_history", params]
            }
            self.ws_post(self.ws, req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

#   flat_set<uint32_t> get_market_history_buckets() const;
    def test_get_market_history_buckets(self):
        req_data = {
            "id":1,
            "method":"call",
            "params":[self.handle, "get_market_history_buckets", []]
        }
        self.ws_post(self.ws, req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))


    def test_get_account_history_operations(self):
        stop = "1.11.30"
        limit = 10
        start = "1.11.5"
        operation_id = 0 #transfer
        for index in range(3, 20, 3):
            account_id = "1.2.{}".format(index)
            params = [account_id, operation_id, start, stop, limit]
            req_data = {
                "id":1,
                "method":"call",
                "params":[self.handle, "get_account_history_operations", params]
            }
            self.ws_post(self.ws, req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))


if __name__ == '__main__':
    unittest.main()