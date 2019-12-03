#-*- coding: utf-8  -*-

import unittest
from utils import *
from config import *
import sys
from websocket import create_connection

class test_asset_api(websocket_unittest):
    @classmethod
    def setUpClass(self):
        self.ws = create_connection(node_ws_url)
        req_data = {
            "id":1,
            "method":"call",
            "params":[1, "network_node", []]
        }
        self.handle = ws_post(self.ws, req_data)['result']
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @classmethod
    def tearDownClass(self):
        self.ws.close()
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    # (get_info)(add_node)(get_connected_peers)(get_potential_peers)
    # (get_advanced_node_parameters)(set_advanced_node_parameters)
    # (set_message_send_cache_size)(set_deduce_in_verification_mode))
    def test_get_info(self):
        req_data = {
            "id":1,
            "method":"call",
            "params":[self.handle, "get_info", []]
        }
        self.ws_post(self.ws, req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_get_connected_peers(self):
        req_data = {
            "id":1,
            "method":"call",
            "params":[self.handle, "get_connected_peers", []]
        }
        self.ws_post(self.ws, req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_get_advanced_node_parameters(self):
        req_data = {
            "id":1,
            "method":"call",
            "params":[self.handle, "get_advanced_node_parameters", []]
        }
        self.ws_post(self.ws, req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_get_potential_peers(self):
        req_data = {
            "id":1,
            "method":"call",
            "params":[self.handle, "get_potential_peers", []]
        }
        self.ws_post(self.ws, req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    # @unittest.skipIf(True, 'test other')
    def test_set_deduce_in_verification_mode(self):
        is_deduce = 'true'
        params = [is_deduce]
        req_data = {
            "id":1,
            "method":"call",
            "params":[self.handle, "set_deduce_in_verification_mode", params]
        }
        # self.ws_post(self.ws, req_data)
        response = ws_post(self.ws, req_data, is_assert=False)
        self.assertTrue('error' in response)
        self.assertTrue(response['error']['message'].find('No permission') != -1)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_set_message_send_cache_size(self):
        resize = 4000
        params = [resize]
        req_data = {
            "id":1,
            "method":"call",
            "params":[self.handle, "set_message_send_cache_size", params]
        }
        # self.ws_post(self.ws, req_data)
        response = ws_post(self.ws, req_data, is_assert=False)
        self.assertTrue('error' in response)
        self.assertTrue(response['error']['message'].find('No permission') != -1)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    # @unittest.skipIf(True, 'test other')
    def test_add_node(self):
        endpoint = '127.0.0.1:8051'
        params = [endpoint]
        req_data = {
            "id":1,
            "method":"call",
            "params":[self.handle, "add_node", params]
        }
        response = ws_post(self.ws, req_data, is_assert=False)
        self.assertTrue('error' in response)
        self.assertTrue(response['error']['message'].find('No permission') != -1)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_set_advanced_node_parameters(self):
        params = {
            "peer_connection_retry_timeout": 60,
            "desired_number_of_connections": 1000,
            "maximum_number_of_connections": 3000,
            "maximum_number_of_blocks_to_handle_at_one_time": 800,
            "maximum_number_of_sync_blocks_to_prefetch": 120,
            "maximum_blocks_per_peer_during_syncing": 240
        }
        req_data = {
            "id":1,
            "method":"call",
            "params":[self.handle, "set_advanced_node_parameters", [params]]
        }
        response = ws_post(self.ws, req_data, is_assert=False)
        self.assertTrue('error' in response)
        self.assertTrue(response['error']['message'].find('No permission') != -1)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

if __name__ == '__main__':
    unittest.main()




