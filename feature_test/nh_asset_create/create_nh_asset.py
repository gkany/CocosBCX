#-*- coding: utf-8  -*-

import unittest
import os
import sys
import json
import requests
import time
import hashlib
import random
import string

cli_wallet_url = "http://127.0.0.1:8047"
headers = {"content-type": "application/json"}

chain_url = "http://127.0.0.1:8149" # 有些接口cli_wallet没有，使用chain api

# curl https://api.cocosbcx.net
# -d '{"id":1, "method":"call", "params":[0,"get_accounts",[["1.2.5", "1.2.100"]]]}'

def request_post(req_data, is_assert=True, response_log=True, url=cli_wallet_url):
    response = json.loads(requests.post(url, data = json.dumps(req_data), headers = headers).text)
    print('>> {} {}'.format(req_data['method'], req_data['params']))
    if response_log:
        print('\033[1;32;40m')
        print("{}\n".format(response))
        print('\033[0m')
    if is_assert:
        assert 'error' not in response
    return response

def random_uppercases(n):
    return ''.join([random.choice(string.ascii_uppercase) for i in range(n)])

def random_lowercases(n):
    return ''.join([random.choice(string.ascii_lowercase) for i in range(n)])

############# global var
g_owner = "nicotest"
# mainnet
#g_owner = "faucet1"

wallet_password = "123456"

def list_account_nh_asset(owner, world_view_name_or_ids, list_type=4):
    print(">>> list_account_nh_asset")
    default_pagesize = 5
    default_page = 1
    req_data = {
        "jsonrpc": "2.0",
        "method": "list_account_nh_asset",
        "params": [owner, world_view_name_or_ids, default_pagesize, default_page, list_type],
        "id":1
    }
    return request_post(req_data, response_log=True)

def list_account_balances(name_or_id):
    req_data = {
        "jsonrpc": "2.0",
        "method": "list_account_balances",
        "params": [name_or_id],
        "id":1
    }
    return request_post(req_data, response_log=True)

def get_contract(name_or_id):
    req_data = {
        "jsonrpc": "2.0",
        "method": "get_contract",
        "params": [name_or_id],
        "id":1
    }
    response = request_post(req_data)
    return response

def register_nh_asset_creator_if_not(account):
    req_data = {
        "jsonrpc": "2.0",
        "method": "register_nh_asset_creator",
        "params": [account, 'true'],
        "id":1
    }
    response = request_post(req_data, is_assert=False)
    if 'error' in response:
        err_message = response['error']['message']
        if err_message.find('You had registered to a nh asset creater') != -1:
            return True
        return False
    time.sleep(2)
    return True

def lookup_world_view(world_view):
    req_data = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": [0, "lookup_world_view", [[world_view]]],
        "id":1
    }
    return request_post(req_data, is_assert=False, url=chain_url)['result']

def create_nh_asset(creator, owner, world_view, base_desc, brodcast=True):
    req_data = {
        "jsonrpc": "2.0",
        "method": "create_nh_asset",
        "params": [creator, owner, world_view, base_desc, brodcast],
        "id":1
    }
    return self.request_post(req_data)["result"]

def create_world_view_if_not_exist(owner, world_view):
    result = lookup_world_view(world_view)
    if result == [None]:
        print("create_world_view")
        req_data = {
            "jsonrpc": "2.0",
            "method": "create_world_view",
            "params": [owner, world_view,'true'],
            "id":1
        }
        request_post(req_data)
        time.sleep(2)

def contract_create_if_not_exist(owner, contract_name, pub_key, file_name):
    req_data = {
        "jsonrpc": "2.0",
        "method": "get_contract",
        "params": [contract_name],
        "id":1
    }
    response = request_post(req_data, is_assert=False)
    if 'error' in response:
        req_data = {
            "jsonrpc": "2.0",
            "method": "create_contract_from_file",
            "params": [owner, contract_name, pub_key, file_name, 'true'],
            "id":1
        }
        request_post(req_data)
        time.sleep(2)

def revise_contract(owner, contract_name, file_name, revise=False):
    req_data = {
        "jsonrpc": "2.0",
        "method": "get_contract",
        "params": [contract_name],
        "id":1
    }
    response = request_post(req_data, is_assert=False)
    if 'error' not in response:
        req_data = {
            "jsonrpc": "2.0",
            "method": "revise_contract_from_file",
            "params": [owner, contract_name, file_name, 'true'],
            "id":1
        }
        request_post(req_data)
        time.sleep(2)

def call_contract(caller, contract, function, params, is_assert=True):
    # print('params: {}, type: {}'.format(params, type(params)))
    req_data = {
        "jsonrpc": "2.0",
        "method": "call_contract_function",
        "params": [caller, contract, function, params, 'true'],
        "id":1
    }
    return request_post(req_data, is_assert, response_log=True)

def import_key_if_not_exist(name, private_key):
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_my_accounts",
            "params": [],
            "id":1
        }
        accounts = request_post(req_data)['result']
        flag = True
        for account in accounts:
            if account['name'] == name or account['id'] == name:
                flag = False
                break
        if flag:
            req_data = {
                "jsonrpc": "2.0",
                "method": "import_key",
                "params": [name, private_key],
                "id":1
            }
            request_post(req_data)

def get_transaction_by_id(tx_id):
    req_data = {
        "jsonrpc": "2.0",
        "method": "get_transaction_by_id",
        "params": [tx_id],
        "id":1
    }
    return request_post(req_data)

def get_object(id):
    req_data = {
        "jsonrpc": "2.0",
        "method": "get_object",
        "params": [id],
        "id":1
    }
    return request_post(req_data)['result']

def get_contract_call_tx_result(tx_id):
    # time.sleep(2) # 保证合约已执行
    operation_results = get_transaction_by_id(tx_id)['result']['operation_results']
    print("tx_id: {}, result: {}".format(tx_id, operation_results))
    return operation_results
    # for op_result in operation_results:
    #     print(op_result)
    #     # print(op_result[1]['contract_affecteds'])


class contract_api_case_test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "unlock",
            "params": [wallet_password],
            "id":1
        }
        request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @classmethod
    def tearDownClass(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "lock",
            "params": [],
            "id":1
        }
        request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, "test other")
    def test_contract_16_create_nh_asset(self):
        # 1. register_nh_asset_creator
        status = register_nh_asset_creator_if_not(g_owner)
        assert status
        # time.sleep(2)

        # 2. create_world_view
        world_view = "test_wv" + random_lowercases(4)
        create_world_view_if_not_exist(g_owner, world_view)
        lookup_world_view(world_view)

        # 3. create_contract
        contract_name = self.contract_basic_name + "16.createnhasset"
        file_name = os.getcwd() + "/contract_16_create_nh_asset.lua"
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        revise_contract(g_owner, contract_name, file_name)
        time.sleep(2)

        # 4. create_nh_asset by contract
        function = "test_create_nh_asset"
        symbol = "COCOS"
        base_describe = "'nh_symbol': '{}'".format(random_uppercases(5))
        params = [
            [2,{"v":g_owner}],
            [2,{"v":symbol}],
            [2,{"v":world_view}],
            [2,{"v":base_describe}],
            [3,{"v":True}]
        ]
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(False, "test other")
    def test_create_nh_asset(self):
        # 1. register_nh_asset_creator
        status = register_nh_asset_creator_if_not(g_owner)
        assert status
        time.sleep(2)
        
        # 2. create_world_view
        world_view = "test_wv" + random_lowercases(4)
        create_world_view_if_not_exist(g_owner, world_view)
        lookup_world_view(world_view)

        # 3. create nh asset        
        base_describes = [
                "'nh_symbol': '{}'".format(random_uppercases(3)),
                "'nh_symbol': '{}'".format(random_uppercases(5)),
                "{'name':'ChinaJoy 2020 NFT门票','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy 首套NFT门票，仅供ChinaJoy Plus 2020上线期间使用，该门票不可进入ChinaJoy线下展会。'}",
                "{'name':'ChinaJoy 2020 NFT门票','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy 首套NFT门票，仅供ChinaJoy Plus 2020上线期间使用，该门票不可进入ChinaJoy线下展会'}",
                "{'name':'ChinaJoy 2020 NFT门票','icon':'https://jdi.cocosbcx.net/image/nft/shop-logo.png','intro':'ChinaJoy 首套NFT门票，仅供ChinaJoy Plus 2020上线期间使用，该门票不可进入ChinaJoy线下展会。。。。。。。。。。。。'}",
                "'nh_symbol': '{}'".format(random_uppercases(7))
        ]

        for base_describe in base_describes:
            result = create_nh_asset(g_owner, g_owner, world_view, base_describe)['result']
            tx_id = result[0]
            time.sleep(2)
            get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

