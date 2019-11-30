#-*- coding: utf-8  -*-

import json
import requests
import unittest

import time
import sys
import datetime

from config import *

def request_post(req_data, is_assert=True):
    response = json.loads(requests.post(cli_wallet_url, data = json.dumps(req_data), headers = headers).text)
    print('>> {} {}\n{}\n'.format(req_data['method'], req_data['params'], response))
    if is_assert:
        assert 'error' not in response
    return response

#default:
# user issuer asset: AAAA
# bit asset        : BBBB
def get_asset_if_not_create(symbol, is_bitasset=False):
    print('[{}] symbol: {}'.format(sys._getframe().f_code.co_name, symbol))
    req_data = {
        "jsonrpc": "2.0",
        "method": "get_asset",
        "params": [symbol],
        "id":1
    }
    # response = json.loads(requests.post(cli_wallet_url, data = json.dumps(req_data), headers = headers).text)
    response = request_post(req_data, False)
    if 'error' in response:
        precision = 5
        asset_opts = {
            "max_supply":"2100000000000000",
            "market_fee_percent":0,
            "max_market_fee":0,
            "flags":0,
            "core_exchange_rate":{
                "base":{"amount":1,"asset_id":"1.3.3"},
                "quote":{"amount":1,"asset_id":"1.3.0"}
            },
            "description":"",
            "extensions":[]
        }
        bitasset_opts = None
        if is_bitasset:
            asset_opts = {
                "issuer_permissions": 511,
                "flags": 0,
                "core_exchange_rate":{
                    "base":{"amount":1,"asset_id":"1.3.4"},
                    "quote":{"amount":1,"asset_id":"1.3.0"}
                }
            }
            bitasset_opts = {
                "new_feed_producers":[],
                "feed_lifetime_sec":120
            }
        req_data = {
            "jsonrpc": "2.0",
            "method": "create_asset",
            "params": [test_account, symbol, precision, asset_opts, bitasset_opts, 'true'],
            "id":1
        }
        # response = json.loads(requests.post(cli_wallet_url, data = json.dumps(req_data), headers = headers).text)
        response = request_post(req_data)
        # assert 'bitasset_data_id' in response
        return response['result']
    return response['result']

#generate random words by suggest_brain_key
def generate_random_words():
    req_data = {
        "jsonrpc": "2.0",
        "method": "suggest_brain_key",
        "params": [],
        "id":1
    }
    suggest_brain_key = json.loads(requests.post(cli_wallet_url, data = json.dumps(req_data), headers = headers).text)['result']
    brain_key = suggest_brain_key['brain_priv_key']
    return brain_key.split()


class request_unittest(unittest.TestCase):
    def request_post(self, req_data):
        response = json.loads(requests.post(cli_wallet_url, data = json.dumps(req_data), headers = headers).text)
        print('>> {} {}\n{}\n'.format(req_data['method'], req_data['params'], response))
        self.assertFalse('error' in response)
        return response

    def request_post_error_asset_false(self, req_data):
        response = json.loads(requests.post(cli_wallet_url, data = json.dumps(req_data), headers = headers).text)
        #print('>> {} {}\n{}\n'.format(req_data['method'], req_data['params'], response))
        self.assertFalse('error' in response, '{} {} error'.format(req_data['method'], req_data['params']))

    def request_post_error_asset_true(self, req_data):
        response = json.loads(requests.post(cli_wallet_url, data = json.dumps(req_data), headers = headers).text)
        self.assertTrue('error' in response, '{} {} error'.format(req_data['method'], req_data['params']))

    def request_post_result_asset_false(self, req_data):
        response = json.loads(requests.post(cli_wallet_url, data = json.dumps(req_data), headers = headers).text)
        self.assertFalse('error' in response)
        self.assertFalse(response['result'])

    def request_post_result_asset_true(self, req_data):
        response = json.loads(requests.post(cli_wallet_url, data = json.dumps(req_data), headers = headers).text)
        self.assertFalse('error' in response)
        self.assertTrue(response['result'])

    def request_post_result_asset_is_none(self, req_data):
        response = json.loads(requests.post(cli_wallet_url, data = json.dumps(req_data), headers = headers).text)
        self.assertFalse('error' in response)
        self.assertIsNone(response['result'])

    def request_post_result_asset_in(self, req_data, first_or_second, is_first=True):
        response = json.loads(requests.post(cli_wallet_url, data = json.dumps(req_data), headers = headers).text)
        self.assertFalse('error' in response)
        if is_first:
            self.assertIn(first_or_second, response['result'])
        else:
            self.assertIn(response['result'], first_or_second)

    def request_post_result_asset_equal(self, req_data, value):
        response = json.loads(requests.post(cli_wallet_url, data = json.dumps(req_data), headers = headers).text)
        self.assertFalse('error' in response)
        self.assertEqual(value, response['result'])


def datetime_N_ago(n):
    n_ago = (datetime.datetime.now() - datetime.timedelta(days = n))
    # return n_ago.strftime("%Y-%m-%d %H:%M:%S")
    return n_ago
