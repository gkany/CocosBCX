#-*- coding: utf-8  -*-

import unittest
import os
import sys
import json
import requests


cli_wallet_url = "http://127.0.0.1:8048"
headers = {"content-type": "application/json"}

def request_post(req_data, is_assert=True, response_log=False):
    response = json.loads(requests.post(cli_wallet_url, data = json.dumps(req_data), headers = headers).text)
    print('>> {} {}'.format(req_data['method'], req_data['params']))
    if response_log:
        print("{}\n".format(response))
    if is_assert:
        assert 'error' not in response
    return response


############# global var
g_owner = "nicotest"
g_pub_key = "COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx"
g_pri_key = "5J2SChqa9QxrCkdMor9VC2k9NT4R4ctRrJA6odQCPkb3yL89vxo"
g_contract_name = "contract.gastest100"
g_function_name = "collateral"
g_contract_lua_code = "function {}(to, amount) chainhelper:update_collateral_for_gas('',to,amount) end".format(
                        g_function_name)
wallet_password = "123456"

g_account2 = "init0"
g_pri_key2 = "5Kj5s6xAkjbFcsGXhP4ioWUk7dZm5aYyKDEWDbWAa5nwA8Paewc"

gas_precision = 100000

transfer_amount = 100000 # core asset
############ end

def contract_create_if_not_exist():
    req_data = {
        "jsonrpc": "2.0",
        "method": "get_contract",
        "params": [g_contract_name],
        "id":1
    }
    response = request_post(req_data, is_assert=False)
    if 'error' in response:
        req_data = {
            "jsonrpc": "2.0",
            "method": "create_contract",
            "params": [g_owner, g_contract_name, g_pub_key, g_contract_lua_code, 'true'],
            "id":1
        }
        request_post(req_data)

def list_account_balances(name_or_id):
    req_data = {
        "jsonrpc": "2.0",
        "method": "list_account_balances",
        "params": [name_or_id],
        "id":1
    }
    return request_post(req_data, response_log=True)

def call_contract(caller, to, amount, is_assert=True):
    params = [
        [2,{"v":to}],
        [0,{"v":amount}]
    ]
    req_data = {
        "jsonrpc": "2.0",
        "method": "call_contract_function",
        "params": [caller, g_contract_name, g_function_name, params, 'true'],
        "id":1
    }
    return request_post(req_data, is_assert)

class contract_api_collateral_gas(unittest.TestCase):
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
            "params": [g_owner, g_pri_key],
            "id":1
        }
        request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "import_key",
            "params": [g_account2, g_pri_key2],
            "id":1
        }
        request_post(req_data)
        contract_create_if_not_exist()
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @classmethod
    def tearDownClass(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "transfer",
            "params": [g_account2, g_owner, transfer_amount*2, 'COCOS', ['test account', 'false'], 'true'],
            "id":1
        }
        request_post(req_data)
        list_account_balances(g_account2)
        list_account_balances(g_owner)

        req_data = {
            "jsonrpc": "2.0",
            "method": "lock",
            "params": [],
            "id":1
        }
        request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(False, 'test other')
    def test_collateral_gas_self(self):
        list_account_balances(g_owner)

        call_contract(g_owner, g_owner, 100000*gas_precision)
        list_account_balances(g_owner)

        call_contract(g_owner, g_owner, 80000*gas_precision)
        list_account_balances(g_owner)

        call_contract(g_owner, g_owner, 0)
        list_account_balances(g_owner)

        response = call_contract(g_owner, g_owner, -100*gas_precision, is_assert=False)
        assert 'error' in response
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(False, 'test other')
    def test_collateral_gas_other(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "transfer",
            "params": [g_owner, g_account2, transfer_amount, 'COCOS', ['test account', 'false'], 'true'],
            "id":1
        }
        request_post(req_data)
        list_account_balances(g_account2)
        list_account_balances(g_owner)

        call_contract(g_account2, g_owner, transfer_amount*0.5*gas_precision)
        list_account_balances(g_owner)
        list_account_balances(g_account2)

        call_contract(g_account2, g_owner, transfer_amount*0.8*gas_precision)
        list_account_balances(g_owner)
        list_account_balances(g_account2)

        call_contract(g_account2, g_owner, 0)
        list_account_balances(g_owner)
        list_account_balances(g_account2)

        response = call_contract(g_account2, g_owner, -0.3*transfer_amount*gas_precision, is_assert=False)
        assert 'error' in response
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_collateral_gas_multi_accounts(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "transfer",
            "params": [g_owner, g_account2, transfer_amount, 'COCOS', ['test account', 'false'], 'true'],
            "id":1
        }
        request_post(req_data)
        list_account_balances(g_account2)
        list_account_balances(g_owner)

        call_contract(g_account2, g_owner, transfer_amount*0.5*gas_precision)
        list_account_balances(g_owner)
        list_account_balances(g_account2)

        call_contract(g_owner, g_owner, 80000*gas_precision)
        list_account_balances(g_owner)
        list_account_balances(g_account2)

        call_contract(g_owner, g_owner, 8000*gas_precision)
        list_account_balances(g_owner)
        list_account_balances(g_account2)

        call_contract(g_account2, g_owner, transfer_amount*0.8*gas_precision)
        list_account_balances(g_owner)
        list_account_balances(g_account2)

        call_contract(g_account2, g_owner, 0)
        call_contract(g_owner, g_owner, 0)
        list_account_balances(g_owner)
        list_account_balances(g_account2)

if __name__ == "__main__":
    unittest.main()

