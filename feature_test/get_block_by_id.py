#-*- coding: utf-8  -*-

import unittest
import os
import sys
import json
import requests
import random


cli_wallet_url = "http://127.0.0.1:8048"
chain_api_url = "http://127.0.0.1:8049"

headers = {"content-type": "application/json"}

############ global var
g_is_cli_wallet = True # False -- chain api
############

def request_post(req_data, is_assert=True, response_log=False):
    url = cli_wallet_url
    if not g_is_cli_wallet:
        url = chain_api_url
    response = json.loads(requests.post(url, data = json.dumps(req_data), headers = headers).text)
    print('>> {} {}'.format(req_data['method'], req_data['params']))
    if response_log:
        print("{}\n".format(response))
    if is_assert:
        assert 'error' not in response
    return response


def get_dynamic_global_properties():
    req_data = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": [0, "get_dynamic_global_properties", []],
        "id":1
    }
    if g_is_cli_wallet:
        req_data["method"] = "get_dynamic_global_properties"
        req_data["params"] = []
    return request_post(req_data, response_log=True)

def get_block(method, num_or_id):
    req_data = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": [0, method, [num_or_id]],
        "id":1
    }
    if g_is_cli_wallet:
        req_data["method"] = method
        req_data["params"] = [num_or_id]
    return request_post(req_data)


def test_get_block_by_id():
    head_block_number = get_dynamic_global_properties()['result']['head_block_number']
    print(head_block_number)
    for i in range(1, int(head_block_number)%100):
        random_num = random.randint(1, head_block_number)
        block1 = get_block("get_block", random_num)['result']
        block2 = get_block("get_block_by_id", block1['block_id'])['result']
        assert block1['witness_signature'] == block2['witness_signature']
    print('{} done\n'.format(sys._getframe().f_code.co_name))

class api_get_block(unittest.TestCase):
    @unittest.skipIf(False, 'test other')
    def test_cli_wallet_get_block_by_id(self):
        test_get_block_by_id()
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(False, 'test other')
    def test_chain_get_block_by_id(self):
        global g_is_cli_wallet
        g_is_cli_wallet = False
        test_get_block_by_id()
        print('{} done\n'.format(sys._getframe().f_code.co_name))

if __name__ == "__main__":
    unittest.main()

