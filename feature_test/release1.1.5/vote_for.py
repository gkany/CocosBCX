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
wallet_rpc_port = 8047

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

def main():
    print("# 1. test cli_wallet api: get_global_extensions_properties")
    get_global_extensions_properties()

    vote_account = "nicotest"
    # vote_account = "release1142"

    print("\n# 2. test vote for witness")
    witnesses = vote_witness_test(vote_account)

    print("\n# 3. test vote for committee")
    committees = vote_committee_test(vote_account)

    time.sleep(10)
    print("\n# 4. test cancle vote for witness")
    cancle_vote_for_witness(vote_account, witnesses)

    print("\n# 5. test  cancle vote for committee")
    cancle_vote_for_committees(vote_account, committees)

    print("test vote for xxx done")


if __name__ == '__main__':
    # print('>> {}'.format(sys.argv))
    main()

# tar -czvf file.tar.gz file
