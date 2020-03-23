#-*- coding: utf-8  -*-

import unittest
import os
import sys
import json
import requests
import time
import hashlib
import random

cli_wallet_url = "http://127.0.0.1:8048"
headers = {"content-type": "application/json"}

def request_post(req_data, is_assert=True, response_log=True):
    response = json.loads(requests.post(cli_wallet_url, data = json.dumps(req_data), headers = headers).text)
    print('>> {} {}'.format(req_data['method'], req_data['params']))
    if response_log:
        print('\033[1;32;40m')
        print("{}\n".format(response))
        print('\033[0m')
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

def get_contract_call_tx_result(tx_id):
    # time.sleep(2) # 保证合约已执行
    operation_results = get_transaction_by_id(tx_id)['result']['operation_results']
    print("tx_id: {}, result: {}".format(tx_id, operation_results))
    return operation_results
    # for op_result in operation_results:
    #     print(op_result)
    #     # print(op_result[1]['contract_affecteds'])


def hash256(src):
    sha256 = hashlib.sha256()
    sha256.update(src.encode('utf-8'))
    return sha256.hexdigest()

def hash512(src):
    sha512 = hashlib.sha512()
    sha512.update(src.encode('utf-8'))
    return sha512.hexdigest()

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
        import_key_if_not_exist(g_owner, g_pri_key)
        self.contract_basic_name = "contract.testapi"
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
    def test_contract_helloworld(self):
        contract_name = self.contract_basic_name + ".helloworld"
        file_name = os.getcwd() + '/contract_helloworld.lua'
        function = "test_helloworld"
        params = []
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        time.sleep(2)
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, "test other")
    def test_contract_01_is_owner(self):
        contract_name = self.contract_basic_name + "01.isowner"
        file_name = os.getcwd() + '/contract_01_is_owner.lua'
        function = "test_is_owner"
        params = []
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        time.sleep(2)
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, "test other")
    def test_contract_02_log(self):
        contract_name = self.contract_basic_name + "02.testlog"
        file_name = os.getcwd() + "/contract_02_log.lua"
        function = "test_log"
        params = [[2,{"v":"WELCOME TO COCOS CONTRACT"}]]
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        time.sleep(2)
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))



    @unittest.skipIf(True, "test other")
    def test_contract_03_contract_random(self):
        contract_name = self.contract_basic_name + "03.contractrandom"
        file_name = os.getcwd() + "/contract_03_contract_random.lua"
        function = "test_contract_random"
        params = []
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)
        time.sleep(2)
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, "test other")
    def test_contract_03_contract_random(self):
        contract_name = self.contract_basic_name + "03.contractrandom"
        file_name = os.getcwd() + "/contract_03_contract_random.lua"
        function = "test_contract_random"
        params = []
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)
        time.sleep(2)
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))


    @unittest.skipIf(True, "test other")
    def test_contract_04_set_permissions_flag(self):
        contract_name = self.contract_basic_name + "04.permissionsflag"
        file_name = os.getcwd() + "/contract_04_set_permissions_flag.lua"
        function = "test_set_permissions_flag"
        params = [[3,{"v":True}]]
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)
        time.sleep(2)
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        get_contract_call_tx_result(tx_id)

        params = [[3,{"v":False}]]
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, "test other")
    def test_contract_05_set_invoke_percent(self):
        contract_name = self.contract_basic_name + "05.invokepercent"
        file_name = os.getcwd() + "/contract_05_set_invoke_percent.lua"
        function = "test_set_invoke_percent"
        params = [[1,{"v":12.5}]]
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)
        time.sleep(2)
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, "test other")
    def test_contract_06_set_invoke_share_percent(self):
        contract_name = self.contract_basic_name + "06.invokesharepercent"
        file_name = os.getcwd() + "/contract_06_set_invoke_share_percent.lua"
        function = "test_set_invoke_share_percent"
        params = [[1,{"v":12.5}]]
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)
        time.sleep(2)

        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        get_contract_call_tx_result(tx_id)

        params = [[1,{"v":-3.14}]]
        response = call_contract(g_owner, contract_name, function, params, is_assert=False)
        assert 'error' in response

        params = [[1,{"v":106.75}]]
        response = call_contract(g_owner, contract_name, function, params, is_assert=False)
        assert 'error' in response
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, "test other")
    def test_contract_07_read_write_chain(self):
        contract_name = self.contract_basic_name + "07.readwritechain"
        file_name = os.getcwd() + "/contract_07_read_chain.lua"
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)
        function = "init"
        params = []
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        get_contract_call_tx_result(tx_id)

        function = "insert"
        for index in range(1, 3):
            rand_index = random.randint(1,999)
            # num = "%05d"%rand_index
            num = str(rand_index).rjust(5, '0')
            name = "zhang_{}".format(rand_index)
            params = [[2, {"v":num}], [2, {"v":name}]]
            result = call_contract(g_owner, contract_name, function, params)['result']
            tx_id = result[0]
            get_contract_call_tx_result(tx_id)
        time.sleep(2)
        constract_obj = get_contract(contract_name)['result']
        print(constract_obj)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, "test other")
    def test_contract_09_test_number_min(self):
        contract_name = self.contract_basic_name + "09.numbermin"
        file_name = os.getcwd() + "/contract_09_number_min.lua"
        function = "test_number_min"
        params = []
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)
        time.sleep(2)

        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, "test other")
    def test_contract_10_test_number_max(self):
        contract_name = self.contract_basic_name + "10.numbermax"
        file_name = os.getcwd() + "/contract_10_number_max.lua"
        function = "test_number_max"
        params = []
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)
        time.sleep(2)

        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, "test other")
    def test_contract_11_test_hash256(self):
        contract_name = self.contract_basic_name + "11.hash256"
        file_name = os.getcwd() + "/contract_11_hash256.lua"
        function = "test_hash256"
        hash_src = "hash256 random number {}".format(random.randint(1,1000))
        params = [[2,{"v": hash_src}]]
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        tx_result = get_contract_call_tx_result(tx_id)
        py_hash256 = hash256(hash_src)
        print("python hash256 result: {}".format(py_hash256))
        result_str = json.dumps(tx_result)
        assert result_str.find(py_hash256) != -1
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, "test other")
    def test_contract_12_test_hash512(self):
        contract_name = self.contract_basic_name + "12.hash512"
        file_name = os.getcwd() + "/contract_12_hash512.lua"
        function = "test_hash512"
        hash_src = "hash512 random number {}".format(random.randint(1,1000))
        params = [[2,{"v": hash_src}]]
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        tx_result = get_contract_call_tx_result(tx_id)
        py_hash512 = hash512(hash_src)
        print("python hash512 result: {}".format(py_hash512))
        result_str = json.dumps(tx_result)
        assert result_str.find(py_hash512) != -1
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, "test other")
    def test_contract_13_head_block_time(self):
        contract_name = self.contract_basic_name + "13.headblocktime"
        file_name = os.getcwd() + "/contract_13_head_block_time.lua"
        function = "test_head_block_time"
        params = []
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, "test other")
    def test_contract_14_real_time(self):
        contract_name = self.contract_basic_name + "14.realtime"
        file_name = os.getcwd() + "/contract_14_real_time.lua"
        function = "test_real_time"
        params = []
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, "test other")
    def test_contract_15_adjust_lock_asset(self):
        contract_name = self.contract_basic_name + "15.adjustlockasset"
        file_name = os.getcwd() + "/contract_15_adjust_lock_asset.lua"
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)
        function = "test_adjust_lock_asset"
        params = [[2,{"v":"COCOS"}], [1,{"v":200000}]]
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)

        params = [[2,{"v":"1.3.0"}], [1,{"v":100000}]]
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(False, 'test other')
    def test_contract_22_collateral_gas_self(self):
        contract_name = self.contract_basic_name + "22.collateralgas"
        file_name = os.getcwd() + "/contract_22_update_collateral_for_gas.lua"
        # contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        revise_contract(g_owner, contract_name, file_name)

        function = "test_colllateral_gas"
        print("### collateral_gas_self test")
        list_account_balances(g_owner)
        params = [[2,{"v":g_owner}], [1,{"v":1000*gas_precision}]]
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)
        list_account_balances(g_owner)

        params = [[2,{"v":g_owner}], [1,{"v":800*gas_precision}]]
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)
        list_account_balances(g_owner)

        params = [[2,{"v":g_owner}], [1,{"v":0}]]
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)
        list_account_balances(g_owner)

        response = call_contract(g_owner, contract_name, function, params, is_assert=False)
        assert 'error' in response
        print('{} done\n'.format(sys._getframe().f_code.co_name))

if __name__ == "__main__":
    unittest.main()

