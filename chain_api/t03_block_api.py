#-*- coding: utf-8  -*-

import unittest
from utils import *
from config import *
import sys
from websocket import create_connection

class test_block_api(websocket_unittest):
    @classmethod
    def setUpClass(self):
        self.ws = create_connection(node_ws_url)
        req_data = {
            "id":1,
            "method":"call",
            "params":[1, "login", ["", ""]]
        }
        ws_post(self.ws, req_data)

        req_data = {
            "id":1,
            "method":"call",
            # "params":[1, "block_api", []]
            "params":[1, "block", []]
        }
        self.handle = ws_post(self.ws, req_data)['result']
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @classmethod
    def tearDownClass(self):
        self.ws.close()
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    # vector<optional<signed_block>> block_api::get_blocks(uint32_t block_num_from, uint32_t block_num_to) const
    def test_get_blocks(self):
        block_num_from = 10
        block_num_to = 48
        req_data = {
            "id":1,
            "method":"call",
            "params":[self.handle, "get_blocks", [block_num_from, block_num_to]]
        }
        self.ws_post(self.ws, req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))



if __name__ == '__main__':
    unittest.main()