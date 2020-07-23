#!/usr/bin/python
# -*- coding: utf-8 -*- 

import os
import sys
import json
import requests
from time import sleep
import datetime
import time
import random
import string

# config
host = "127.0.0.1"
node_rpc_port = 8049
wallet_rpc_port = 8047

wallet_password = 123456
chain_url = "http://127.0.0.1:{}".format(node_rpc_port)
cli_wallet_url = "http://{}:{}".format(host, wallet_rpc_port)

headers = {"content-type": "application/json"}
# config end

########## cli_wallet api 
# def request_post(req_data):
#     try:
#        response = json.loads(requests.post(cli_wallet_url, data = json.dumps(req_data), headers = headers).text)
#        print('>> {} {}\n{}\n'.format(req_data['method'], req_data['params'], response))
#        #print('>> {} {}\n{}'.format(req_data['method'], req_data['params'], response['result']))
#        return response
#     except Exception as e:
#         print(repr(e))

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

def call_contract(caller, contract, function, params=[], is_assert=True):
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
    time.sleep(4) # 保证合约已执行
    operation_results = get_transaction_by_id(tx_id)['result']['operation_results']
    print("tx_id: {}, result: {}".format(tx_id, operation_results))
    return operation_results
    # for op_result in operation_results:
    #     print(op_result)
    #     # print(op_result[1]['contract_affecteds'])

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

def unlock(pwd="123456"):
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
        return request_post(body_relay)["result"]
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
        # print('>> get_object {}\n {}\n'.format(id, result))
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


def list_witnesses(lowerbound="", limit=11):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "list_witnesses",
            "params": [lowerbound, limit],
            "id":1
        }
        response = request_post(body_relay)
        result = response['result']
        return result
    except Exception as e:
        print(repr(e))

def list_committee_members(lowerbound="", limit=11):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "list_committee_members",
            "params": [lowerbound, limit],
            "id":1
        }
        response = request_post(body_relay)
        result = response['result']
        return result
    except Exception as e:
        print(repr(e))


def vote_for_witness(vote_account, witness, votes, broadcast=True):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "vote_for_witness",
            "params": [vote_account, witness, votes, broadcast],
            "id":1
        }
        response = request_post(body_relay)
        result = response['result']
        return result
    except Exception as e:
        print(repr(e))

def chain_api_get_global_property_extensions():
    req_data = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": [0, "get_global_property_extensions", [[]]],
        "id":1
    }
    return request_post(req_data, is_assert=False, url=chain_url)['result']

def get_global_extensions_properties():
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "get_global_extensions_properties",
            "params": [],
            "id":1
        }
        response = request_post(body_relay)
        result = response['result']
        return result
    except Exception as e:
        print(repr(e))

def vote_for_committee_member(vote_account, committee, votes, broadcast=True):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "method": "vote_for_committee_member",
            "params": [vote_account, committee, votes, broadcast],
            "id":1
        }
        response = request_post(body_relay)
        result = response['result']
        return result
    except Exception as e:
        print(repr(e))

def vote_witness_test(vote_account = "nicotest"):
    # 1. get_object 2.15.0
    vote_chain_properties = get_object("2.15.0")
    print(vote_chain_properties)
    if not vote_chain_properties:
        print("No votes chain properties")
        return
    vote_chain_properties_obj = vote_chain_properties[0]
    witness_max_votes = vote_chain_properties_obj["witness_max_votes"]
    committee_max_votes = vote_chain_properties_obj["committee_max_votes"]

    # 2. fetch vote witnesses
    witnesses = list_witnesses(limit=witness_max_votes+1)
    print("witnesses: {}".format(witnesses))

    # 3. calc vote amount by account_balances
    # vote_account = "nicotest"
    account_balances = list_account_balances(vote_account)
    print(account_balances)
    cocos_balances = [ i for i in account_balances if i["asset_id"] == "1.3.0" ]
    if not cocos_balances:
        print("no COCOS balances")
        return
    cocos_amount = int(cocos_balances[0]["amount"])
    # print(cocos_amount)
    vote_amount_max = 20 if cocos_amount > 10 else cocos_amount 
    # print(vote_amount_max)

    # 4. vote for witness
    for witness in witnesses:
        witness_account = witness[0]
        witness_id = witness[1]
        random_vote_amount = random.randint(1, vote_amount_max)
        vote_for_witness(vote_account=vote_account, witness=witness_account, votes=random_vote_amount)
    return witnesses

def vote_committee_test(vote_account = "nicotest"):
    # 1. get_object 2.15.0
    vote_chain_properties = get_object("2.15.0")
    print(vote_chain_properties)
    if not vote_chain_properties:
        print("No votes chain properties")
        return
    vote_chain_properties_obj = vote_chain_properties[0]
    witness_max_votes = vote_chain_properties_obj["witness_max_votes"]
    committee_max_votes = vote_chain_properties_obj["committee_max_votes"]

    # 2. fetch vote witnesses
    committees = list_committee_members(limit=committee_max_votes+1)
    print("committees: {}".format(committees))

    # 3. calc vote amount by account_balances
    # vote_account = "nicotest"
    account_balances = list_account_balances(vote_account)
    print(account_balances)
    cocos_balances = [ i for i in account_balances if i["asset_id"] == "1.3.0" ]
    if not cocos_balances:
        print("no COCOS balances")
        return
    cocos_amount = int(cocos_balances[0]["amount"])
    # print(cocos_amount)
    vote_amount_max = 20 if cocos_amount > 10 else cocos_amount 
    # print(vote_amount_max)

    # 4. vote for witness
    for committee in committees:
        committee_account = committee[0]
        committee_id = committee[1]
        random_vote_amount = random.randint(1, vote_amount_max)
        vote_for_committee_member(vote_account=vote_account, committee=committee_account, votes=random_vote_amount)
    return committees

def cancle_vote_for_witness(vote_account, witnesses):
    for witness in witnesses:
        witness_account = witness[0]
        witness_id = witness[1]
        random_vote_amount = 0
        vote_for_witness(vote_account=vote_account, witness=witness_account, votes=random_vote_amount)


def cancle_vote_for_committees(vote_account, committees):
    for committee in committees:
        committee_account = committee[0]
        committee_id = committee[1]
        random_vote_amount = 0
        vote_for_committee_member(vote_account=vote_account, committee=committee_account, votes=random_vote_amount)

def release_vote_function(account="nicotest"):
    print("# 1. test cli_wallet api: get_global_extensions_properties")
    get_global_extensions_properties()

    print("# 2. test chain_api_get_global_property_extensions")
    chain_api_get_global_property_extensions()

    # vote_account = "nicotest"  # local test
    # vote_account = "release1142" # master
    vote_account = account

    print("\n# 3. test vote for witness")
    witnesses = vote_witness_test(vote_account)

    print("\n# 4. test vote for committee")
    committees = vote_committee_test(vote_account)

    time.sleep(10)
    print("\n# 5. test cancle vote for witness")
    cancle_vote_for_witness(vote_account, witnesses)

    print("\n# 6. test  cancle vote for committee")
    cancle_vote_for_committees(vote_account, committees)

    print("test vote for xxx done")

def create_contract_test(account, contract_name, contract_file, pub_key, function, params=[]):
    contract_create_if_not_exist(account, contract_name, pub_key, contract_file)
    
    time.sleep(2)

    result = call_contract(account, contract_name, function, params)['result']
    tx_id = result[0]
    get_contract_call_tx_result(tx_id)

def revise_contract_test(account, contract_name, contract_file, function, params=[]):
    # contract_create_if_not_exist(account, contract_name, pub_key, contract_file)
    revise_contract(account, contract_name, contract_file)
    
    time.sleep(2)

    result = call_contract(account, contract_name, function, params)['result']
    tx_id = result[0]
    get_contract_call_tx_result(tx_id)

def release_cli_wallet_api(account="nicotest"):
    # test_account = "nicotest"
    test_account = account
    pub_key = "COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz"

    contract_name = "contract.release115{}".format(random_lowercases(3))
    print("contract_name: {}, test account: {}".format(contract_name, test_account))

    print("1. create contract from file and call test")
    file_name = os.getcwd() + "/contract_create.lua"
    function = "contract_test"
    create_contract_test(test_account, contract_name, file_name, pub_key, function)

    print("2. contract revise from file and call test")
    file_name = os.getcwd() + "/contract_revise.lua"
    revise_contract_test(test_account, contract_name, file_name, function)
    
    print('{} done\n'.format(sys._getframe().f_code.co_name))

def test_contract_get_contract_public_data(account="nicotest"):
    # test_account = "nicotest"
    test_account = account
    pub_key = "COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz"

    contract_name = "contract.release115.gcpd{}".format(random_lowercases(3))
    print("contract_name: {}, test account: {}".format(contract_name, test_account))

    print("1. create contract from file and call test")
    file_name = os.getcwd() + "/contract_api_get_contract_public_data.lua"
    function = "init"
    create_contract_test(test_account, contract_name, file_name, pub_key, function)

    # 2. insert contract public data
    function = "insert"
    for index in range(1, 3):
        rand_index = random.randint(1,999)
        # num = "%05d"%rand_index
        num = str(rand_index).rjust(5, '0')
        name = "zhang_{}".format(rand_index)
        params = [[2, {"v":num}], [2, {"v":name}]]
        result = call_contract(test_account, contract_name, function, params)['result']
        tx_id = result[0]
        get_contract_call_tx_result(tx_id)
    time.sleep(4)
    contract_obj = get_contract(contract_name)['result']
    print(contract_obj)

    # test contract api get_contract_public_data
    function = "test"
    params = [[2, {"v":contract_name}]]
    result = call_contract(test_account, contract_name, function, params)['result']
    tx_id = result[0]
    get_contract_call_tx_result(tx_id)
    print('{} done\n'.format(sys._getframe().f_code.co_name))

def test_contract_api_integer_max_and_min(account="nicotest"):
    # test_account = "nicotest"
    test_account = account
    pub_key = "COCOS71VkaLtMrnx29GpLEuBFsksy3tVDRCbpkJH1Mu1bxe6bK1c1Wz"

    contract_name = "contract.release115.gcpd{}".format(random_lowercases(3))
    print("contract_name: {}, test account: {}".format(contract_name, test_account))

    print("### 1. create contract from file and call test")
    file_name = os.getcwd() + "/contract_api_integer_max_and_min.lua"
    function = "test_integer_max"
    create_contract_test(test_account, contract_name, file_name, pub_key, function)

    function = "test_integer_min"
    params = []
    result = call_contract(test_account, contract_name, function, params)['result']
    tx_id = result[0]
    get_contract_call_tx_result(tx_id)

def release_contract_api_test(account="nicotest"):
    test_contract_get_contract_public_data(account="nicotest")
    test_contract_api_integer_max_and_min(account="nicotest")

def main():
    unlock()

    test_account = "nicotest" # testnet
    # test_account = "release1142" # master

    print("# cli_wallet api test")
    release_cli_wallet_api(account=test_account)

    print("# vote function test")
    release_vote_function(account=test_account)

    print("# contract api test")
    release_contract_api_test(account=test_account)

if __name__ == '__main__':
    main()
