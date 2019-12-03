#-*- coding: utf-8  -*-

import math
import unittest
from utils import *
from chain_param import *
from config import *
import sys
from time import sleep
# from requests

class test_login_api(websocket_unittest):
    @classmethod
    def setUpClass(self):
        self.ws = create_connection(node_ws_url)
        req_data = {
            "id":1,
            "method":"call",
            "params":[1, "login", []]
        }
        self.handle = ws_post(self.ws, req_data)['result']
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @classmethod
    def tearDownClass(self):
        print('{} done\n'.format(sys._getframe().f_code.co_name))


    def test_get_account_history(self):
        # session = request_session()
        # print('self.session: {}', self.session)
        # stop = "1.11.30"
        # limit = 10
        # start = "1.11.5"
        # for index in range(3, 20, 3):
        #     account_id = "1.2.{}".format(index)
        #     params = [account_id, stop, limit, start]
        #     req_data = {
        #         "id":1,
        #         "method":"call",
        #         "params":[self.handle, "get_account_history", params]
        #     }
        #     self.session_post(self.session, req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))


if __name__ == '__main__':
    unittest.main()
