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

cli_wallet_url = "http://127.0.0.1:8048"
headers = {"content-type": "application/json"}

chain_url = "http://127.0.0.1:8049" # 有些接口cli_wallet没有，使用chain api

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

# std::pair<vector<nh_asset_object>, uint32_t> wallet_api::list_account_nh_asset(
#     const string &nh_asset_owner,
#     const vector<string> &world_view_name_or_ids,
#     uint32_t pagesize,
#     uint32_t page,
#     nh_asset_list_type list_type)
# {
#       return my->_remote_db->list_account_nh_asset(get_account(nh_asset_owner).id, world_view_name_or_ids, pagesize, page, list_type);
# }

#default list_type = owner_and_active
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
        contract_obj = get_contract(contract_name)['result']
        print(contract_obj)
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

    @unittest.skipIf(True, "test other")
    def test_contract_16_create_nh_asset(self):
        # 1. register_nh_asset_creator
        status = register_nh_asset_creator_if_not(g_owner)
        assert status
        # time.sleep(2)

        # 2. create_world_view
        world_view = "test_wv" + random_lowercases(4)
        world_view = self.world_view
        create_world_view_if_not_exist(g_owner, world_view)
        lookup_world_view(world_view)

        # 3. create_contract
        contract_name = self.contract_basic_name + "16.createnhasset"
        file_name = os.getcwd() + "/contract_16_create_nh_asset.lua"
        # contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        revise_contract(g_owner, contract_name, file_name)
        # time.sleep(2)

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

    @unittest.skipIf(True, "test other")
    def test_contract_17_nht_describe_change(self):
        # 1. register_nh_asset_creator
        status = register_nh_asset_creator_if_not(g_owner)
        assert status

        # 2. create_world_view
        world_view = "test_wv" + random_lowercases(4) #随机世界观其他test_case操作不方便，使用全局world_view
        # world_view = self.world_view
        create_world_view_if_not_exist(g_owner, world_view)
        lookup_world_view(world_view)

        # 3. create_contract
        contract_name = self.contract_basic_name + "17.nhtdescchange"
        file_name = os.getcwd() + "/contract_17_nht_describe_change.lua"
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)

        contract_object = get_contract(contract_name)['result']
        contract_id = contract_object['id']
        print("contract_name: {}, contract_id: {}".format(contract_name, contract_id))

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

        # 5. list_account_nh_asset
        # list_account_nh_asset
        nh_assets_pair = list_account_nh_asset(g_owner, [world_view])['result']
        assert nh_assets_pair[1] > 0
        nh_asset = nh_assets_pair[0][0]
        nh_asset_id = nh_asset['id']

        '''
            [
                [{
                    'dealership': '1.2.16',
                    'base_describe': "'nh_symbol': 'NCSTC'",
                    'limit_type': 'black_list',
                    'id': '4.2.6',
                    'asset_qualifier': 'COCOS',
                    'nh_asset_owner': '1.2.16',
                    'child': [],
                    'nh_hash': '06000000000000006ea3f251af0b0b6e8165872e6858174ac31fdd56bc35c840',
                    'limit_list': [],
                    'nh_asset_creator': '1.2.16',
                    'describe_with_contract': [],
                    'parent': [],
                    'world_view': 'test_wvcplc',
                    'nh_asset_active': '1.2.16',
                    'create_time': '2020-03-24T10:54:38'
                }], 1
            ]
        '''
        # 6. change nh asset contract desc
        function = "test_nht_describe_change"
        verf_result = []
        for index in range(1, 3):
            key = "random_str{}".format(index)
            value = random_lowercases(10)
            verf_result.append([key, value])
            params = [
                [2,{"v":nh_asset_id}],
                [2,{"v":key}],
                [2,{"v":value}],
                [3,{"v":True}]
            ]
            call_contract(g_owner, contract_name, function, params)['result']
        time.sleep(2)

        # 7. get_nh_asset object 结果验证
        nh_asset_object = get_object(nh_asset_id)[0]
        describe_with_contract = nh_asset_object['describe_with_contract']
        flag = False
        for desc in describe_with_contract:
            print("desc: {}".format(desc)) # ['1.16.26', [['random_str1', 'uatnoupyjk'], ['random_str2', 'bltkxsrxlt']]]
            if desc[0] == contract_id:
                flag = True
                this_contract_desc = desc[1]
                assert verf_result == this_contract_desc
                break
        assert flag
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    # suggest_brain_key
    # {
    #   "brain_priv_key": "TRITE RULLION NASHGAB PERKILY DUCAT DOMITIC PALOLO TILTUP MUM DEUCED PINITE VERSANT CLOUGH UNGLEE PATINE SCANTLY",
    #   "wif_priv_key": "5Ka9Kb6yYRLZ1rBREV4c1dxXVPoeHdZJMouz4d3vvzSqcw4XoQq",
    #   "address_info": "COCOSDz8YQwfse71tMEB6W5aFK2C2P4h6CJRgb",
    #   "pub_key": "COCOS5LjcsExdE2ZEUgpjjKSQNNDsxKjeA5kDvJNCE9F7H3EeD47bMe"
    # }
    # locked >>>
    @unittest.skipIf(True, "test other")
    def test_contract_18_change_contract_authority(self):
        contract_name = self.contract_basic_name + "18.changcontractauthority"
        file_name = os.getcwd() + "/contract_18_change_contract_authority.lua"
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)

        new_contract_authority = "COCOS5LjcsExdE2ZEUgpjjKSQNNDsxKjeA5kDvJNCE9F7H3EeD47bMe"
        contract_obj = get_contract(contract_name)['result']
        if contract_obj['contract_authority'] == new_contract_authority:
            new_contract_authority = g_pub_key
        function = "test_change_contract_authority"
        params = [[2,{"v":new_contract_authority}]]
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)

        contract_obj = get_contract(contract_name)['result']
        assert contract_obj['contract_authority'] == new_contract_authority
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, "test other")
    def test_contract_19_make_memo(self):
        contract_name = self.contract_basic_name + "19.makememo"
        file_name = os.getcwd() + "/contract_19_make_memo.lua"
        # contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        revise_contract(g_owner, contract_name, file_name)

        function = "test_make_memo"
        params = [
            [2,{"v":"nicotest"}],
            [2,{"v":"test_key"}],
            [2,{"v":"test make_memo by contract api"}],
            [0,{"v":2020}],
            [3,{"v":True}],
        ]
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, "test other")
    def test_contract_20_invoke_contract_function(self):
        # test contract
        contract_name = self.contract_basic_name + "20.testlog"
        file_name = os.getcwd() + "/contract_02_log.lua"
        function = "test_log"
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        time.sleep(2)

        params = [
            [2, {"v":contract_name}],
            [2, {"v":function}],
            [2, {"v":'[[2,{"v":"invoke_contract_function by cli_wallet"}]]'}]
        ]

        contract_name = self.contract_basic_name + "20.invokecontractfunc"
        file_name = os.getcwd() + "/contract_20_invoke_contract_function.lua"
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)

        function = "test_invoke_contract_function"
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)

        contract_obj = get_contract(contract_name)['result']
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, "test other")
    def test_contract_21_make_release(self):
        contract_name = self.contract_basic_name + "21.makerelease"
        file_name = os.getcwd() + "/contract_21_make_release.lua"
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)
        function = "test_make_release"
        params = []
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)

        contract_obj = get_contract(contract_name)['result']
        assert contract_obj['is_release']
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, 'test other')
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

    @unittest.skipIf(True, 'test other')
    def test_contract_23_transfer_from_owner(self):
        contract_name = self.contract_basic_name + "23.transferfromowner"
        file_name = os.getcwd() + "/contract_23_transfer_from_owner.lua"
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)

        function = "test_transfer_from_owner"
        params = [
            [2,{"v":"1.2.5"}],
            [1,{"v":1523.78}],
            [2,{"v":"COCOS"}],
            [3,{"v":True}]
        ]
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, 'test other')
    def test_contract_24_transfer_from_caller(self):
        contract_name = self.contract_basic_name + "24.transferfromcaller"
        file_name = os.getcwd() + "/contract_24_transfer_from_caller.lua"
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)

        function = "test_transfer_from_caller"
        params = [
            [2,{"v":"1.2.5"}],
            [1,{"v":1523.78}],
            [2,{"v":"COCOS"}],
            [3,{"v":True}]
        ]
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))


    @unittest.skipIf(True, 'test other')
    def test_contract_27_get_account_balance(self):
        contract_name = self.contract_basic_name + "27.getaccountbalance"
        file_name = os.getcwd() + "/contract_27_get_account_balance.lua"
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)

        function = "test_get_account_balance"
        params = [[2,{"v":g_owner}], [2,{"v":"COCOS"}]]
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)

        params = [[2,{"v":"1.2.5"}], [2,{"v":"1.3.0"}]]
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))


    @unittest.skipIf(True, 'test other')
    def test_contract_25_transfer_nht_from_caller(self):
        # 1. register_nh_asset_creator
        status = register_nh_asset_creator_if_not(g_owner)
        assert status

        # 2. create_world_view
        world_view = "test_wv" + random_lowercases(4) #随机世界观其他test_case操作不方便，使用全局world_view
        # world_view = self.world_view
        create_world_view_if_not_exist(g_owner, world_view)
        lookup_world_view(world_view)

        # 3. create_contract
        contract_name = self.contract_basic_name + "25.transfernhtfromcaller"
        file_name = os.getcwd() + "/contract_25_transfer_nht_from_owner.lua"
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        revise_contract(g_owner, contract_name, file_name)

        contract_object = get_contract(contract_name)['result']
        contract_id = contract_object['id']
        print("contract_name: {}, contract_id: {}".format(contract_name, contract_id))

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

        # 5. list_account_nh_asset
        nh_assets_pair = list_account_nh_asset(g_owner, [world_view])['result']
        assert nh_assets_pair[1] > 0
        nh_asset = nh_assets_pair[0][0]
        nh_asset_id = nh_asset['id']

        # 6. transfer nht by contract
        function = "test_transfer_nht_from_owner"
        params = [
            [2,{"v":"1.2.5"}],
            [2,{"v":nh_asset_id}],
            [3,{"v":True}]
        ]
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, 'test other')
    def test_contract_26_transfer_nht_from_caller(self):
        # 1. register_nh_asset_creator
        status = register_nh_asset_creator_if_not(g_owner)
        assert status

        # 2. create_world_view
        world_view = "test_wv" + random_lowercases(4) #随机世界观其他test_case操作不方便，使用全局world_view
        # world_view = self.world_view
        create_world_view_if_not_exist(g_owner, world_view)
        lookup_world_view(world_view)

        # 3. create_contract
        contract_name = self.contract_basic_name + "26.transfernhtfromcaller"
        file_name = os.getcwd() + "/contract_26_transfer_nht_from_caller.lua"
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        revise_contract(g_owner, contract_name, file_name)

        contract_object = get_contract(contract_name)['result']
        contract_id = contract_object['id']
        print("contract_name: {}, contract_id: {}".format(contract_name, contract_id))

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

        # 5. list_account_nh_asset
        nh_assets_pair = list_account_nh_asset(g_owner, [world_view])['result']
        assert nh_assets_pair[1] > 0
        nh_asset = nh_assets_pair[0][0]
        nh_asset_id = nh_asset['id']

        # 6. transfer nht by contract
        function = "test_transfer_nht_from_caller"
        params = [
            [2,{"v":"1.2.5"}],
            [2,{"v":nh_asset_id}],
            [3,{"v":True}]
        ]
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(False, 'test other')
    def test_contract_28_change_nht_active_by_owner(self):
        # 1. register_nh_asset_creator
        status = register_nh_asset_creator_if_not(g_owner)
        assert status

        # 2. create_world_view
        world_view = "test_wv" + random_lowercases(4) #随机世界观其他test_case操作不方便，使用全局world_view
        # world_view = self.world_view
        create_world_view_if_not_exist(g_owner, world_view)
        lookup_world_view(world_view)

        # 3. create_contract
        contract_name = self.contract_basic_name + "28.changenhtactivebyowner"
        file_name = os.getcwd() + "/contract_28_change_nht_active_by_owner.lua"
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        revise_contract(g_owner, contract_name, file_name)

        contract_object = get_contract(contract_name)['result']
        contract_id = contract_object['id']
        print("contract_name: {}, contract_id: {}".format(contract_name, contract_id))

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

        # 5. list_account_nh_asset
        nh_assets_pair = list_account_nh_asset(g_owner, [world_view])['result']
        assert nh_assets_pair[1] > 0
        nh_asset = nh_assets_pair[0][0]
        nh_asset_id = nh_asset['id']

        # 6. transfer nht by contract
        function = "test_change_nht_active_by_owner"
        params = [
            [2,{"v":"1.2.5"}],
            [2,{"v":nh_asset_id}],
            [3,{"v":True}]
        ]
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(False, 'test other')
    def test_contract_29_change_nht_active_by_caller(self):
        # 1. register_nh_asset_creator
        status = register_nh_asset_creator_if_not(g_owner)
        assert status

        # 2. create_world_view
        world_view = "test_wv" + random_lowercases(4) #随机世界观其他test_case操作不方便，使用全局world_view
        # world_view = self.world_view
        create_world_view_if_not_exist(g_owner, world_view)
        lookup_world_view(world_view)

        # 3. create_contract
        contract_name = self.contract_basic_name + "29.changenhtactivebycaller"
        file_name = os.getcwd() + "/contract_29_change_nht_active_by_caller.lua"
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        revise_contract(g_owner, contract_name, file_name)

        contract_object = get_contract(contract_name)['result']
        contract_id = contract_object['id']
        print("contract_name: {}, contract_id: {}".format(contract_name, contract_id))

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

        # 5. list_account_nh_asset
        nh_assets_pair = list_account_nh_asset(g_owner, [world_view])['result']
        assert nh_assets_pair[1] > 0
        nh_asset = nh_assets_pair[0][0]
        nh_asset_id = nh_asset['id']

        # 6. transfer nht by contract
        function = "test_change_nht_active_by_caller"
        params = [
            [2,{"v":"1.2.5"}],
            [2,{"v":nh_asset_id}],
            [3,{"v":True}]
        ]
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(False, 'test other')
    def test_contract_30_transfer_nht_dealership_from_owner(self):
        # 1. register_nh_asset_creator
        status = register_nh_asset_creator_if_not(g_owner)
        assert status

        # 2. create_world_view
        world_view = "test_wv" + random_lowercases(4) #随机世界观其他test_case操作不方便，使用全局world_view
        # world_view = self.world_view
        create_world_view_if_not_exist(g_owner, world_view)
        lookup_world_view(world_view)

        # 3. create_contract
        contract_name = self.contract_basic_name + "30.transfernhtdealershipfromowner"
        file_name = os.getcwd() + "/contract_30_transfer_nht_dealership_from_owner.lua"
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        revise_contract(g_owner, contract_name, file_name)

        contract_object = get_contract(contract_name)['result']
        contract_id = contract_object['id']
        print("contract_name: {}, contract_id: {}".format(contract_name, contract_id))

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

        # 5. list_account_nh_asset
        nh_assets_pair = list_account_nh_asset(g_owner, [world_view])['result']
        assert nh_assets_pair[1] > 0
        nh_asset = nh_assets_pair[0][0]
        nh_asset_id = nh_asset['id']

        # 6. transfer nht by contract
        function = "test_transfer_nht_dealership_from_owner"
        params = [
            [2,{"v":"1.2.5"}],
            [2,{"v":nh_asset_id}],
            [3,{"v":True}]
        ]
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(False, 'test other')
    def test_contract_31_transfer_nht_dealership_from_caller(self):
        # 1. register_nh_asset_creator
        status = register_nh_asset_creator_if_not(g_owner)
        assert status

        # 2. create_world_view
        world_view = "test_wv" + random_lowercases(4) #随机世界观其他test_case操作不方便，使用全局world_view
        # world_view = self.world_view
        create_world_view_if_not_exist(g_owner, world_view)
        lookup_world_view(world_view)

        # 3. create_contract
        contract_name = self.contract_basic_name + "31.transfernhtdealershipfromcaller"
        file_name = os.getcwd() + "/contract_31_transfer_nht_dealership_from_caller.lua"
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        revise_contract(g_owner, contract_name, file_name)

        contract_object = get_contract(contract_name)['result']
        contract_id = contract_object['id']
        print("contract_name: {}, contract_id: {}".format(contract_name, contract_id))

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

        # 5. list_account_nh_asset
        nh_assets_pair = list_account_nh_asset(g_owner, [world_view])['result']
        assert nh_assets_pair[1] > 0
        nh_asset = nh_assets_pair[0][0]
        nh_asset_id = nh_asset['id']

        # 6. transfer nht by contract
        function = "test_transfer_nht_dealership_from_caller"
        params = [
            [2,{"v":"1.2.5"}],
            [2,{"v":nh_asset_id}],
            [3,{"v":True}]
        ]
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, "test other")
    def test_contract_params_lua_map_by_cli_wallet(self):
        contract_name = self.contract_basic_name + "00.invokecontractfunc"
        file_name = os.getcwd() + "/contract_lua_map_by_cli_wallet.lua"
        contract_create_if_not_exist(g_owner, contract_name, g_pub_key, file_name)
        # revise_contract(g_owner, contract_name, file_name)

        function = "test_params_lua_map"
        params = [
            [2, {"v":"name"}],
            [2, {"v":"address"}],
            [4, {
                  "v":[
                        [ {"key":[2,{"v":"name"}]},
                          [2,{"v":"zhang3"}]
                        ],
                        [ {"key":[2,{"v":"age"}]},
                          [0,{"v":22}]
                        ],
                        [ {"key":[2,{"v":"sex"}]},
                          [2,{"v":"man"}]
                        ],
                        [ {"key":[2,{"v":"height"}]},
                          [0,{"v":170}]
                        ],
                        [ {"key":[2,{"v":"weight"}]},
                          [1,{"v":65.3}]
                        ],
                        [ {"key":[2,{"v":"address"}]},
                          [2,{"v":"beijing chaoyang wangjing"}]
                        ],
                        [ {"key":[2,{"v":"is_student"}]},
                          [3,{"v":False}]
                        ],
                    ]
                }
            ]
        ]
        result = call_contract(g_owner, contract_name, function, params)['result']
        tx_id = result[0]
        time.sleep(2)
        get_contract_call_tx_result(tx_id)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

if __name__ == "__main__":
    unittest.main()

