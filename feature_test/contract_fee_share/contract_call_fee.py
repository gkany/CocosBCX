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
    balances = None
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "list_account_balances",
            "params": [account],
            "id":1
        }
        result = request_post(body_relay)
        balances = result["result"]
    except Exception as e:
        print(repr(e))
    return balances

def accounts_balances(accounts=[]):
    if len(accounts) == 0:
        return None
    result = {}
    for account_name in accounts:
        balances = list_account_balances(account_name)
        result[account_name] = balances
    return result

def get_asset_balance(balances, asset="1.3.0"):
    for obj in balances:
        if obj["asset_id"] == asset:
            return int(obj["amount"])
    return 0

def delta_asset_balance(old, new, asset="1.3.0"):
    old_asset_amount = get_asset_balance(old, asset)
    new_asset_amount = get_asset_balance(new, asset)
    return old_asset_amount - new_asset_amount 

def delta_assets_balances(old, new, assets=["1.3.0", "1.3.1"]):
    result = {}
    for asset in assets:
        result[asset] = delta_asset_balance(old, new, asset)
    return result

# COCOS GAS
def delta_balances(old_balances, new_balances):
    delta_result = {}
    for account in old_balances.keys():
        old_balance = old_balances[account]
        new_balance = new_balances[account]
        delta_result[account] = delta_assets_balances(old_balance, new_balance)
    return delta_result

def calc_contract_call_operation_fee(func=None, accounts=[]):
    if not func or len(accounts) == 0:
        return
    
    old_balances = accounts_balances(accounts)
    func()
    current_balances = accounts_balances(accounts)
    delta = delta_balances(old_balances, current_balances)
    print("op before balances: {}\nop after  balances: {}\nbalances delta: {}".format(
        old_balances, current_balances, delta))

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


def test_helloworld(caller="nicotest", log_result=False):
    contract = "contract.testapi.contractfeeshare"
    func = "test_helloworld"
    params = []

    # caller = "nicotest" #owner
    call_result = call_contract(caller, contract, func, params, broadcast=True)

    # get block
    block = get_block_by_transaction_id(call_result[0])

    if log_result:
        print("-------------------- contract call fee result ------------------------")
        # print("block: {}\n".format(block))
        transactions = block["transactions"]
        for trx in transactions:
            # print("### operation_results: {}".format(trx[1]["operation_results"]))
            operation_results = trx[1]["operation_results"]
            for op_result in operation_results:
                if op_result[0] == 4:
                    total_fee = op_result[1]["fees"]
                    print("## total_fee: {}".format(total_fee))
                    contract_affecteds = op_result[1]["contract_affecteds"]
                    for contract_affected in contract_affecteds:
                        if contract_affected[0] == 5:
                            print("### {}".format(contract_affected[1]))
        print("-----------------------------------------------------------------------")

def test_helloworld_owner():
    test_helloworld(log_result=True)

def test_helloworld_not_owner():
    test_helloworld(caller="init1", log_result=True)

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

    # test_helloworld(log_result=True)
    # test_helloworld(caller="init1", log_result=True)

    # test_set_percent()

    # result = list_account_balances("init1")
    # print("result: {}".format(result))

    # result = accounts_balances(["init1", "nicotest"])
    # print("balances: {}".format(result))
    # print("============================================")
    # calc_contract_call_operation_fee(test_helloworld, ["nicotest"])
    calc_contract_call_operation_fee(test_helloworld_owner, ["nicotest"])

# tar -czvf file.tar.gz file
