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
## witness_node
node_bin_path = "./" # node work_dir
node_bin_filename = "witness_node"
node_data_dir = "witness_node_data_dir"
node_p2p_port = 8050
node_rpc_port = 8049

balance_address = ''
chain_id = '725fdc4a727a6aa84aea37376bb51e419febbf0f59830c05f3e82f607631e5fc'


wallet_bin_path = "wallet" # cli_wallet work_dir
wallet_bin_filename = "cli_wallet"
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

def set_password(pwd):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "set_password",
            "params": [pwd],
            "id":1
        }
        request_post(body_relay)
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

def import_key(account, key):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "import_key",
            "params": [account, key],
            "id":1
        }
        request_post(body_relay)
    except Exception as e:
        print(repr(e))

def import_key2(params):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "import_key",
            "params": params,
            "id":1
        }
        request_post(body_relay)
    except Exception as e:
        print(repr(e))

def import_balance(account, address):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "import_balance",
            "params": [account, [address], 'true'],
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

def get_account(name):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "get_account",
            "params": [name],
            "id":1
        }
        # account_info = json.loads(requests.post(cli_wallet_url, data = json.dumps(body_relay), headers = headers).text)
        account_info = request_post(body_relay)
        account_object = account_info['result']
        return account_object
    except Exception as e:
        print(repr(e))

def suggest_brain_key():
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "suggest_brain_key",
            "params": [],
            "id":1
        }
        # response = json.loads(requests.post(cli_wallet_url, data = json.dumps(body_relay), headers = headers).text)
        response = request_post(body_relay)
        brain_key = response['result']
        # print('>> suggest_brain_key\n {}\n'.format(brain_key))
        return brain_key
    except Exception as e:
        print(repr(e))

########## cli_wallet api end

# propose_extensions_parameter_change init0 "2020-05-21T05:55:00" {"witness_max_votes": 7} true
# approve_proposal nicotest 1.10.0 {"active_approvals_to_add" : ["init0"]} true
def propose_extension_parameter(account, expire_time, changed_param):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "propose_extensions_parameter_change",
            "params": [account, expire_time, changed_param, True],
            "id":1
        }
        # data = json.dumps(body_relay)
        # print(data)
        # response = json.loads(requests.post(cli_wallet_url, data = data, headers = headers).text)
        response = request_post(body_relay)
        result = response['result']
        # print('>> propose_extensions_parameter_change\n {}\n'.format(result))
        return result
    except Exception as e:
        print(repr(e))

def info():
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "info",
            "params": [],
            "id":1
        }
        # response = json.loads(requests.post(cli_wallet_url, data = json.dumps(body_relay), headers = headers).text)
        response = request_post(body_relay)
        info = response['result']
        # print('>> info\n {}\n'.format(info))
        return info
    except Exception as e:
        print(repr(e))

def get_dynamic_global_properties():
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "get_dynamic_global_properties",
            "params": [],
            "id":1
        }
        # response = json.loads(requests.post(cli_wallet_url, data = json.dumps(body_relay), headers = headers).text)
        response = request_post(body_relay)
        result = response['result']
        # print('>> get_dynamic_global_properties\n {}\n'.format(result))
        return result
    except Exception as e:
        print(repr(e))

def get_global_properties():
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "get_global_properties",
            "params": [],
            "id":1
        }
        # response = json.loads(requests.post(cli_wallet_url, data = json.dumps(body_relay), headers = headers).text)
        response = request_post(body_relay)
        result = response['result']
        # print('>> get_global_properties\n {}\n'.format(result))
        return result
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

def transfer(from_account, to, amount, asset="COCOS", memo=""):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "transfer",
            "params": [from_account, to, amount, asset, [memo, False], True],
            "id":1
        }
        # response = json.loads(requests.post(cli_wallet_url, data = json.dumps(body_relay), headers = headers).text)
        response = request_post(body_relay)
        result = response['result']
        return result
    except Exception as e:
        print(repr(e))

def time_mktime(utc_str_time):
    return time.mktime(time.strptime(utc_str_time, "%Y-%m-%dT%H:%M:%S"))

def proposal(account):
    dgp = get_dynamic_global_properties()
    next_maintenance_time = dgp["next_maintenance_time"]
    now_time = dgp["time"]
    print("next_maintenance_time: {}, now time: {}".format(next_maintenance_time, now_time))
    time_delta = int(time_mktime(next_maintenance_time) - time_mktime(now_time))
    print("time_delta: {}".format(time_delta))

    gp = get_global_properties()
    parameters = gp["parameters"]
    committee_proposal_review_period = int(parameters["committee_proposal_review_period"])
    print("committee_proposal_review_period: {}".format(committee_proposal_review_period))
    if time_delta <= committee_proposal_review_period:
        print("Please wait for the next maintenance")
        return ""
        # print("Please wait for the next maintenance: {} seconds".format(time_delta+30))
        # time.sleep(time_delta+30)

    #  将字符串转化为时间戳
    maint_time = time.mktime(time.strptime(next_maintenance_time, "%Y-%m-%dT%H:%M:%S"))
    #  将时间戳转换为字符串
    expire_time = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(maint_time - 300))
    print("expire_time: {}".format(expire_time))

    changed = {'witness_max_votes': 7, "committee_max_votes": 9}
    # changed = {'witness_max_votes': 11, "committee_max_votes": 7}
    result = propose_extension_parameter(account=account, expire_time=expire_time, changed_param=changed)
    tx_id = result[0]
    print("tx_id: {}".format(tx_id))

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
        print("block: {}".format(block))
        tx_pair = block["transactions"][0]
        print("\ntx_pair: {}".format(tx_pair))
        print("[0]: {}".format(tx_pair[0]))
        if tx_pair[0] == tx_id:
            tx = tx_pair[1]
            print("\ntx: {}".format(tx))
            operation_results = tx["operation_results"]
            print("\noperation_results: {}".format(operation_results))
            propose_id = operation_results[0][1]["result"]
            print("propose_id: {}".format(propose_id))

            result = get_object(propose_id)
            if not result:
                continue
            print("propose object: {}".format(result))
            # break
            return propose_id
    return ""

# approve_proposal nicotest 1.10.0 {"active_approvals_to_add" : ["init0"]} true

def approve_proposal(propose_id, account):
    try:
        approve = {"active_approvals_to_add" : [account]}
        body_relay = {
            "jsonrpc": "2.0",
            "method": "approve_proposal",
            "params": [account, propose_id, approve, True],
            "id":1
        }
        response = json.loads(requests.post(cli_wallet_url, data = json.dumps(body_relay), headers = headers).text)
        result = response['result']
        print('>> approve_proposal {}\n {}\n'.format(body_relay["params"], result))
        return result
    except Exception as e:
        print(repr(e))

def main():
    account = "init0"
    # 1. propose
    propose_id = proposal(account)
    if propose_id == "":
        return

    # 2. transfer to committee-account
    proposal_fee = 3
    transfer(account, "committee-account", proposal_fee)

    # 3. approve propose
    committees = ["init0", "init1", "init2", "init3", "init4", "init5", "init6", "init7", "init8", "init9", "init10"]
    # committees = ["init8", "init9", "init10"]
    for committee in committees:
        approve_proposal(propose_id, committee)
    time.sleep(5)
    get_object(propose_id)

if __name__ == '__main__':
    # print('>> {}'.format(sys.argv))
    main()

# tar -czvf file.tar.gz file
