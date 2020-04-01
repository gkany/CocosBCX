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

def get_contract_public_data_size(contract_id):
    req_data = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": [0, "get_contract_public_data_size", [contract_id]],
        "id":1
    }
    return request_post(req_data, is_assert=False, url=chain_url)['result']

def get_contract_private_data_size(account_id, contract_id):
    req_data = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": [0, "get_contract_private_data_size", [account_id, contract_id]],
        "id":1
    }
    return request_post(req_data, is_assert=False, url=chain_url)['result']

def get_contract_data_size(contract_id):
    req_data = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": [0, "get_contract_data_size", [contract_id]],
        "id":1
    }
    return request_post(req_data, is_assert=False, url=chain_url)['result']

def get_contract_data_size_by_cli_wallet(contract_id):
    req_data = {
        "jsonrpc": "2.0",
        "method": "get_contract_data_size",
        "params": [contract_id],
        "id":1
    }
    return request_post(req_data, is_assert=False)['result']

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

def get_account_contract_data(account, contract):
    req_data = {
        "jsonrpc": "2.0",
        "method": "get_account_contract_data",
        "params": [account, contract],
        "id":1
    }
    return request_post(req_data)['result']

def get_account(id_or_name):
    req_data = {
        "jsonrpc": "2.0",
        "method": "get_account",
        "params": [id_or_name],
        "id":1
    }
    return request_post(req_data)['result']

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
        account_obj = get_account(g_owner)
        print(account_obj)
        self.g_owner_id = account_obj['id']

        import_key_if_not_exist(g_owner, g_pri_key)
        self.contract_basic_name = "contract.testapi"
        self.contract_name = self.contract_basic_name + "01.privatedata"
        self.file_name = os.getcwd() + "/contract_private_data.lua"

        contract_create_if_not_exist(g_owner, self.contract_name, g_pub_key, self.file_name)
        # revise_contract(g_owner, self.contract_name, self.file_name)
        time.sleep(2)

        contract_obj = get_contract(self.contract_name)['result']
        print(contract_obj)
        self.contract_id = contract_obj['id']

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

    def test_contract_private_data(self):
        # function = "init"
        # params = []
        # result = call_contract(g_owner, self.contract_name, function, params)['result']
        # tx_id = result[0]
        # get_contract_call_tx_result(tx_id)

        for index in range(1, 10):
            if index % 2 == 0:
                flag = "private"
            else:
                flag = "public"
            function = "insert_{}".format(flag)
            rand_index = random.randint(1,999)
            num = str(rand_index).rjust(5, '0')
            name = "{}_zhang_{}".format(flag, rand_index)
            params = [[2, {"v":num}], [2, {"v":name}]]
            result = call_contract(g_owner, self.contract_name, function, params)['result']
            time.sleep(0.1)
        time.sleep(2)
        print(">>>>>>>>> private data: ")
        private_data_obj = get_account_contract_data(g_owner, self.contract_name)
        print(private_data_obj)

        print(">>>>>>>>> [chain_api] private data size: ")
        private_size = get_contract_private_data_size(self.g_owner_id, self.contract_id)

        print(">>>>>>>>> [chain_api] public data size: ")
        private_size = get_contract_public_data_size(self.contract_id)

        print(">>>>>>>>> [chain_api] data size: ")
        data_size = get_contract_data_size(self.contract_id)

        print(">>>>>>>>>> cli_wallet data size: ")
        data_size = get_contract_data_size_by_cli_wallet(self.contract_id)

        print('{} done\n'.format(sys._getframe().f_code.co_name))


if __name__ == "__main__":
    unittest.main()

