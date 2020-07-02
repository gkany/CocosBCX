#!/usr/bin/python
# -*- coding: utf-8 -*- 

import os
import sys
import json
import requests
from time import sleep
import datetime
import time

# config
host = "127.0.0.1"
wallet_rpc_port = 8048

wallet_password = 123456
cli_wallet_url = "http://{}:{}".format(host, wallet_rpc_port)

headers = {"content-type": "application/json"}
# config end

########## cli_wallet api 
def request_post(req_data):
    try:
       response = json.loads(requests.post(cli_wallet_url, data = json.dumps(req_data), headers = headers).text)
       print('>> {} {}\n{}\n'.format(req_data['method'], req_data['params'], response))
       #print('>> {} {}\n{}'.format(req_data['method'], req_data['params'], response['result']))
       return response
    except Exception as e:
        print(repr(e))

def unlock(pwd):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "unlock",
            "params": [pwd],
            "id":1
        }
        request_post(body_relay)
    except Exception as e:
        print(repr(e))

def list_account_balances(account):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "list_account_balances",
            "params": [account],
            "id":1
        }
        request_post(body_relay)
    except Exception as e:
        print(repr(e))

def get_block(num):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "get_block",
            "params": [num],
            "id":1
        }
        # response = json.loads(requests.post(cli_wallet_url, data = json.dumps(body_relay), headers = headers).text)
        response = request_post(body_relay)
        block = response['result']
        # print('>> get_block {}\n {}\n'.format(num, block))
        return block
    except Exception as e:
        print(repr(e))

def get_tx_in_block_num(tx_id):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "get_transaction_in_block_info",
            "params": [tx_id],
            "id":1
        }
        # response = json.loads(requests.post(cli_wallet_url, data = json.dumps(body_relay), headers = headers).text)
        response = request_post(body_relay)
        result = response['result']
        print('>> get_transaction_in_block_info {}\n {}\n'.format(tx_id, result))
        return result
    except Exception as e:
        print(repr(e))

def get_object(id):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "get_object",
            "params": [id],
            "id":1
        }
        # response = json.loads(requests.post(cli_wallet_url, data = json.dumps(body_relay), headers = headers).text)
        response = request_post(body_relay)
        result = response['result']
        print('>> get_object {}\n {}\n'.format(id, result))
        return result
    except Exception as e:
        print(repr(e))

def transfer(from_account, to, amount, asset="COCOS", memo="", broadcast=True):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "transfer",
            "params": [from_account, to, amount, asset, [memo, False], broadcast],
            "id":1
        }
        # response = json.loads(requests.post(cli_wallet_url, data = json.dumps(body_relay), headers = headers).text)
        response = request_post(body_relay)
        result = response['result']
        return result
    except Exception as e:
        print(repr(e))


def begin_builder_transaction():
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "begin_builder_transaction",
            "params": [],
            "id":1
        }
        response = request_post(body_relay)
        result = response['result']
        return result
    except Exception as e:
        print(repr(e))

def add_operation_to_builder_transaction(id, op):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "add_operation_to_builder_transaction",
            "params": [id, op],
            "id":1
        }
        response = request_post(body_relay)
        result = response['result']
        return result
    except Exception as e:
        print(repr(e))

def preview_builder_transaction(id):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "preview_builder_transaction",
            "params": [id],
            "id":1
        }
        response = request_post(body_relay)
        result = response['result']
        return result
    except Exception as e:
        print(repr(e))

def sign_builder_transaction(id, broadcast=True):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "sign_builder_transaction",
            "params": [id, broadcast],
            "id":1
        }
        response = request_post(body_relay)
        result = response['result']
        return result
    except Exception as e:
        print(repr(e))

def call_contract(caller, contract, function, params=[], broadcast=True):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "call_contract_function",
            "params": [caller, contract, function, params, broadcast],
            "id":1
        }
        response = request_post(body_relay)
        result = response['result']
        return result
    except Exception as e:
        print(repr(e))

def get_transfer_op(from_account, to, amount, broadcast=False):
    result = transfer(from_account=from_account, to=to, amount=amount, broadcast=broadcast)
    # tx_id = result[0]
    tx = result[1]
    operations = tx["operations"]
    op = operations[0]
    return op

def get_contract_function_call_op(caller, contract, function, params=[], broadcast=False):
    result = call_contract(caller, contract, function, params, broadcast)
    # tx_id = result[0]
    tx = result[1]
    operations = tx["operations"]
    op = operations[0]
    return op

def get_block_by_transaction_id(tx_id):
    times = 3
    while times >= 0:
        times = times - 1 
        time.sleep(2)
        result = get_tx_in_block_num(tx_id)
        if not result:
            continue
        block = get_block(result["block_num"])
        if not block:
            continue
        # print("block: {}".format(block))
        return block
    return None

def main_build_tx():
    # 1. begin_builder_transaction
    id = begin_builder_transaction()
    # print("begin_builder_transaction id: {}".format(id))

    # 2. add_operation_to_builder_transaction
    # 2.1 add transfer op
    op = get_transfer_op(from_account="nicotest", to="init0", amount=23)
    add_op_result = add_operation_to_builder_transaction(id, op)
    # print("add_op_result: {}".format(add_op_result))

    # 2.2 add call contract
    contract = "contract.testapi.contractfeeshare"
    func = "test_helloworld"
    params = []

    caller = "nicotest" #owner
    op = get_contract_function_call_op(caller, contract, func, params)
    add_op_result = add_operation_to_builder_transaction(id, op)

    # 2.3 add call contract
    caller = "init1"
    op = get_contract_function_call_op(caller, contract, func, params)
    add_op_result = add_operation_to_builder_transaction(id, op)

    # 2.4 add transfer op
    op = get_transfer_op(from_account="nicotest", to="init1", amount=78)
    add_op_result = add_operation_to_builder_transaction(id, op)
    # print("add_op_result: {}".format(add_op_result))

    # 3. preview_builder_transaction
    result = preview_builder_transaction(id)
    # print("preview result: {}".format(result))

    # 4. sign_builder_transaction
    sign_result = sign_builder_transaction(id)
    # print("sign result: {}".format(sign_result))

    # 5. get block
    block = get_block_by_transaction_id(sign_result[0])

def test_set_percent(owner="nicotest", percent=30):
    contract = "contract.testapi.contractfeeshare"
    func = "test_set_percent"
    params = [[1, {"v":percent}]]

    # caller = "nicotest" #owner
    call_result = call_contract(owner, contract, func, params, broadcast=True)

    # get block
    block = get_block_by_transaction_id(call_result[0])

def test_helloworld(caller="nicotest"):
    contract = "contract.testapi.contractfeeshare"
    func = "test_helloworld"
    params = []

    # caller = "nicotest" #owner
    call_result = call_contract(caller, contract, func, params, broadcast=True)

    # get block
    block = get_block_by_transaction_id(call_result[0])


def get_contract_function_call_op_test():
    caller = "nicotest"
    contract = "contract.testapi.contractfeeshare"
    func = "test_helloworld"
    params = []
    get_contract_function_call_op(caller, contract, func, params)

if __name__ == '__main__':
    # print('>> {}'.format(sys.argv))
    unlock("123456")

    # main_build_tx()
    # get_contract_function_call_op_test()

    # test_helloworld()
    test_helloworld(caller="init1")

    # test_set_percent()

# tar -czvf file.tar.gz file

'''
## 1. test_helloworld
### 1.1 caller = owner
>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'result': ['afba96943360480fd69dd329a060e31b4fdd5290eb29d6ba039a61ed557a4ff5', {'expiration': '2020-07-02T07:25:14', 'signatures': ['207f7875f12f7721cf61b3b32a7cf7df51cb8308f8cefb711f7aee24b6efd150360fd3ccae75ba6bb123d963f46caf68233d4135da34bcd7b2d23e30dff64bd275'], 'operations': [[35, {'function_name': 'test_helloworld', 'extensions': [], 'caller': '1.2.16', 'value_list': [], 'contract_id': '1.16.1'}]], 'ref_block_num': 994, 'ref_block_prefix': 3197526302, 'extensions': []}], 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info ['afba96943360480fd69dd329a060e31b4fdd5290eb29d6ba039a61ed557a4ff5']
{'result': {'trx_hash': 'afba96943360480fd69dd329a060e31b4fdd5290eb29d6ba039a61ed557a4ff5', 'trx_in_block': 0, 'block_num': 1004, 'id': '3.1.2'}, 'jsonrpc': '2.0', 'id': 1}

>> get_transaction_in_block_info afba96943360480fd69dd329a060e31b4fdd5290eb29d6ba039a61ed557a4ff5
 {'trx_hash': 'afba96943360480fd69dd329a060e31b4fdd5290eb29d6ba039a61ed557a4ff5', 'trx_in_block': 0, 'block_num': 1004, 'id': '3.1.2'}

>> get_block [1004]
{'result': {'transactions': [['afba96943360480fd69dd329a060e31b4fdd5290eb29d6ba039a61ed557a4ff5', {'expiration': '2020-07-02T07:25:14', 'signatures': ['207f7875f12f7721cf61b3b32a7cf7df51cb8308f8cefb711f7aee24b6efd150360fd3ccae75ba6bb123d963f46caf68233d4135da34bcd7b2d23e30dff64bd275'], 'operations': [[35, {'function_name': 'test_helloworld', 'extensions': [], 'caller': '1.2.16', 'value_list': [], 'contract_id': '1.16.1'}]], 'ref_block_num': 994, 'ref_block_prefix': 3197526302, 'extensions': [], 'operation_results': [[4, {'relevant_datasize': 35, 'fees': [{'asset_id': '1.3.0', 'amount': 2448757}], 'process_value': '', 'existed_pv': False, 'contract_affecteds': [[3, {'message': 'Hi, Cocos-BCX contract', 'affected_account': '1.2.16'}], [5, {'message': '100%', 'fees': [{'asset_id': '1.3.0', 'amount': 2448757}], 'affected_account': '1.2.16'}]], 'contract_id': '1.16.1', 'real_running_time': 397}]]}]], 'transaction_merkle_root': 'd808694bea99fb764f4f8f4e1d91cdad082907e3', 'witness': '1.6.7', 'previous': '000003eb8b2f4742e4993e105fd276db26e53f05', 'timestamp': '2020-07-02T07:04:46', 'witness_signature': '2023b2ea4d6e7a2b12c7d91793e1ead112a0ecabccd9dba1997cf3e86afaa370c37b004023af2e8dfc7f1d32ffc1c058d8f9709b7ab0df11d86843e2346ea51465', 'block_id': '000003ecd11fc1b1de71dc864148d16839fa37ed'}, 'jsonrpc': '2.0', 'id': 1}

### 1.2 caller != owner
>> call_contract_function ['init1', 'contract.testapi.contractfeeshare', 'test_helloworld', [], True]
{'id': 1, 'jsonrpc': '2.0', 'result': ['32f248b786e88fcfc64c100254aeb77d378363e48c6669ec0b4aef56b965867f', {'ref_block_prefix': 2352907040, 'extensions': [], 'signatures': ['20235416da2073c564e3bd3b557591184d27a061ee0c1b71bf8366986d730c518a42ad8d8e74b08af97c6a0e94a72fb6bfb0a1ac06db369dcd17ee0e813c15b514'], 'expiration': '2020-07-02T07:37:12', 'operations': [[35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'extensions': [], 'value_list': [], 'contract_id': '1.16.1'}]], 'ref_block_num': 1320}]}

>> get_transaction_in_block_info ['32f248b786e88fcfc64c100254aeb77d378363e48c6669ec0b4aef56b965867f']
{'id': 1, 'jsonrpc': '2.0', 'result': {'id': '3.1.4', 'trx_hash': '32f248b786e88fcfc64c100254aeb77d378363e48c6669ec0b4aef56b965867f', 'trx_in_block': 0, 'block_num': 1329}}

>> get_transaction_in_block_info 32f248b786e88fcfc64c100254aeb77d378363e48c6669ec0b4aef56b965867f
 {'id': '3.1.4', 'trx_hash': '32f248b786e88fcfc64c100254aeb77d378363e48c6669ec0b4aef56b965867f', 'trx_in_block': 0, 'block_num': 1329}

>> get_block [1329]
{'id': 1, 'jsonrpc': '2.0', 'result': {'transactions': [['32f248b786e88fcfc64c100254aeb77d378363e48c6669ec0b4aef56b965867f', {'ref_block_prefix': 2352907040, 'extensions': [], 'signatures': ['20235416da2073c564e3bd3b557591184d27a061ee0c1b71bf8366986d730c518a42ad8d8e74b08af97c6a0e94a72fb6bfb0a1ac06db369dcd17ee0e813c15b514'], 'expiration': '2020-07-02T07:37:12', 'operations': [[35, {'function_name': 'test_helloworld', 'caller': '1.2.6', 'extensions': [], 'value_list': [], 'contract_id': '1.16.1'}]], 'operation_results': [[4, {'contract_id': '1.16.1', 'relevant_datasize': 35, 'existed_pv': False, 'process_value': '', 'fees': [{'amount': 2497757, 'asset_id': '1.3.0'}], 'real_running_time': 446, 'contract_affecteds': [[3, {'affected_account': '1.2.6', 'message': 'Hi, Cocos-BCX contract'}], [5, {'affected_account': '1.2.6', 'message': '30%', 'fees': [{'amount': 749328, 'asset_id': '1.3.0'}]}], [5, {'affected_account': '1.2.16', 'message': '70%', 'fees': [{'amount': 1748429, 'asset_id': '1.3.0'}]}]]}]], 'ref_block_num': 1320}]], 'transaction_merkle_root': 'a9a22bfbcf4ee35485a8620bfa1357cc6898db8d', 'block_id': '00000531c2982d63962e55fda04f0b3d9c493baa', 'timestamp': '2020-07-02T07:16:44', 'witness': '1.6.5', 'witness_signature': '1f3bcba2db2d90a25d7f50c2f74c3929e233878c01ce8a933a8bc5393a6a0a4d612203e2172b97f16d7a8ba6c0e7c7524f8cc325e698eedee27d374bf8b0b12c41', 'previous': '00000530c1217f626830349e0c2b01b052e5f5bb'}}


## test_set_percent
>> call_contract_function ['nicotest', 'contract.testapi.contractfeeshare', 'test_set_percent', [[1, {'v': 30}]], True]
{'result': ['a8f1d10f1475d0559cc50f6a6738d71d81c3357d7de9203b7460c1fc33a54d64', {'ref_block_num': 1246, 'extensions': [], 'ref_block_prefix': 124217732, 'operations': [[35, {'value_list': [[1, {'v': '30.00000000000000000'}]], 'contract_id': '1.16.1', 'function_name': 'test_set_percent', 'extensions': [], 'caller': '1.2.16'}]], 'signatures': ['2044aaa1328c9379fcf759fb08a9855f33a34ba6fb4b6f21455f3e7f4204d5e3967015a0825dc1efbe535480304c5c2d7c8e1b1baa260a95948fd361c20641c3ea'], 'expiration': '2020-07-02T07:34:36'}], 'id': 1, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info ['a8f1d10f1475d0559cc50f6a6738d71d81c3357d7de9203b7460c1fc33a54d64']
{'result': None, 'id': 1, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info a8f1d10f1475d0559cc50f6a6738d71d81c3357d7de9203b7460c1fc33a54d64
 None

>> get_transaction_in_block_info ['a8f1d10f1475d0559cc50f6a6738d71d81c3357d7de9203b7460c1fc33a54d64']
{'result': {'trx_in_block': 0, 'trx_hash': 'a8f1d10f1475d0559cc50f6a6738d71d81c3357d7de9203b7460c1fc33a54d64', 'id': '3.1.3', 'block_num': 1258}, 'id': 1, 'jsonrpc': '2.0'}

>> get_transaction_in_block_info a8f1d10f1475d0559cc50f6a6738d71d81c3357d7de9203b7460c1fc33a54d64
 {'trx_in_block': 0, 'trx_hash': 'a8f1d10f1475d0559cc50f6a6738d71d81c3357d7de9203b7460c1fc33a54d64', 'id': '3.1.3', 'block_num': 1258}

>> get_block [1258]
{'result': {'timestamp': '2020-07-02T07:14:10', 'witness_signature': '1f298a7d3b29100d1f486b4143061044d0ec0f01eff7cae54e66e53723ffbac46515dd07958425c39ae674394069ac595f24f7bf0c6b8aac6de9f5cfddf7997ee4', 'transaction_merkle_root': '8957169c4204c703292cf1533dbfcc36ced28fab', 'witness': '1.6.8', 'previous': '000004e93454b2b701b5f06298b2d6cd2410c018', 'block_id': '000004eab8a260239a8ec7ff1252d523eb4759df', 'transactions': [['a8f1d10f1475d0559cc50f6a6738d71d81c3357d7de9203b7460c1fc33a54d64', {'ref_block_num': 1246, 'extensions': [], 'ref_block_prefix': 124217732, 'operation_results': [[4, {'real_running_time': 352, 'relevant_datasize': 37, 'contract_id': '1.16.1', 'existed_pv': False, 'fees': [{'amount': 2415475, 'asset_id': '1.3.0'}], 'contract_affecteds': [[3, {'affected_account': '1.2.16', 'message': 'set_invoke_share_percent'}], [5, {'affected_account': '1.2.16', 'fees': [{'amount': 2415475, 'asset_id': '1.3.0'}], 'message': '100%'}]], 'process_value': ''}]], 'operations': [[35, {'value_list': [[1, {'v': '30.00000000000000000'}]], 'contract_id': '1.16.1', 'function_name': 'test_set_percent', 'extensions': [], 'caller': '1.2.16'}]], 'signatures': ['2044aaa1328c9379fcf759fb08a9855f33a34ba6fb4b6f21455f3e7f4204d5e3967015a0825dc1efbe535480304c5c2d7c8e1b1baa260a95948fd361c20641c3ea'], 'expiration': '2020-07-02T07:34:36'}]]}, 'id': 1, 'jsonrpc': '2.0'}

'''