#!/usr/bin/python
# -*- coding: utf-8 -*- 

import os
import sys
import json
import requests
from time import sleep

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

test_account = 'nicotest'
test_account_key = '5J2SChqa9QxrCkdMor9VC2k9NT4R4ctRrJA6odQCPkb3yL89vxo'
test_balance_address = '5KAUeN3Yv51FzpLGGf4S1ByKpMqVFNzXTJK7euqc3NnaaLz1GJm'

headers = {"content-type": "application/json"}
# config end

def cmd_exec(cmd, is_log=True):
    if is_log:
        print('>>> {}'.format(cmd))
    os.system(cmd)

def node_clean():
    cmd = 'pkill {}; sleep 2'.format(node_bin_filename)
    cmd_exec(cmd)
    cmd = 'rm -rf {} *.log {}'.format(node_data_dir, node_bin_filename)
    cmd_exec(cmd)
    print('node clean done.')

def cli_wallet_clean():
    cmd = 'pkill {}; sleep 2'.format(wallet_bin_filename)
    cmd_exec(cmd)
    cmd = 'rm -rf {} '.format(wallet_bin_path)
    cmd_exec(cmd)
    print('wallet clean done.')

def chain_id_init():
    global chain_id
    with open('chain_id.log', 'r') as f:
        for line in f:
            tokens = line.split('is')
            chain_id = tokens[1].strip()
            print('chain id: {}'.format(chain_id))
            break
        f.close()

def node_init():
    node_clean()
    cmd = 'tar -zxvf {}.tar.gz; chmod +x {}'.format(node_bin_filename, node_bin_filename)
    cmd_exec(cmd)
    cmd = 'mkdir {}; cp config.ini {}/'.format(node_data_dir, node_data_dir)
    cmd_exec(cmd)
    cmd = 'nohup ./{} --genesis-json genesis.json -d {} >> {}.log 2>&1 &'.format(node_bin_filename, node_data_dir, node_bin_filename)
    cmd_exec(cmd)
    cmd = 'sleep 2; grep -n "Chain ID is" {}.log >> chain_id.log'.format(node_bin_filename)
    cmd_exec(cmd)
    chain_id_init()

def node_restart():
    cmd = 'pkill {}; sleep 2'.format(node_bin_filename)
    cmd_exec(cmd)
    cmd = 'nohup ./{} --genesis-json genesis.json -d {} >> {}.log 2>&1 &'.format(
        node_bin_filename, node_data_dir, node_bin_filename)
    cmd_exec(cmd)
    chain_id_init()

def generate_wallet_start():
    ws = 'ws://{}:{}'.format(host, node_rpc_port)
    cmd = './{} --chain-id {} -s {} -r 0.0.0.0:{} '.format(
        wallet_bin_filename, chain_id, ws, '8047')
    start_file = './{}/start.sh'.format(wallet_bin_path)
    cmd_exec('echo {} >> {} && chmod +x {}'.format(cmd, start_file, start_file))

def cli_wallet_start():
    chain_id_init()
    ws = 'ws://{}:{}'.format(host, node_rpc_port)
    global chain_id
    cmd = 'cd {}; pkill {}; nohup ./{} --chain-id {} -s {} -r 0.0.0.0:{} -d >> {}.log  2>&1 &'.format(
        wallet_bin_path, wallet_bin_filename, wallet_bin_filename, chain_id, ws, wallet_rpc_port, wallet_bin_filename)
    cmd_exec(cmd)

def cli_wallet_start2():
    cli_wallet_start()
    sleep(2)
    unlock(wallet_password)

def cli_wallet_init():
    cmd = 'pkill {}; sleep 2; rm -rf {}; mkdir {}; cp {}.tar.gz {}/; cd {}; tar -zxvf {}.tar.gz; chmod +x {}'.format(
        wallet_bin_filename, wallet_bin_path, wallet_bin_path, wallet_bin_filename, wallet_bin_path, 
        wallet_bin_path, wallet_bin_filename, wallet_bin_filename
    )
    cmd_exec(cmd)
    cli_wallet_start()
    sleep(2)
    cli_wallet_operate_init()
    generate_wallet_start()

def cli_wallet_operate_init():
    print('cli_wallet_url: {}'.format(cli_wallet_url))
    set_password(wallet_password)
    unlock(wallet_password)
    import_key(test_account, test_account_key)
    import_balance(test_account, test_balance_address)
    list_account_balances(test_account)


########## cli_wallet api 
def request_post(req_data):
    try:
       response = json.loads(requests.post(cli_wallet_url, data = json.dumps(req_data), headers = headers).text)
       print('>> {} {}\n{}\n'.format(req_data['method'], req_data['params'], response))
       #print('>> {} {}\n{}'.format(req_data['method'], req_data['params'], response['result']))
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
        account_info = json.loads(requests.post(cli_wallet_url, data = json.dumps(body_relay), headers = headers).text)
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
        response = json.loads(requests.post(cli_wallet_url, data = json.dumps(body_relay), headers = headers).text)
        brain_key = response['result']
        print('>> suggest_brain_key\n {}\n'.format(brain_key))
        return brain_key
    except Exception as e:
        print(repr(e))

########## cli_wallet api end

def wallet_api_test():
    #suggest_brain_key()
    account = get_account('nicotest')
    print(account)
    #list_account_balances('init1')
    list_account_balances('nicotest12')
    #cli_wallet_operate_init()

if __name__ == '__main__':
    print('>> {}'.format(sys.argv))
    if len(sys.argv) >= 2:
        if sys.argv[1] == 'init':
            node_init()
        elif sys.argv[1] == 'wallet':
            if len(sys.argv) >= 3:
                if sys.argv[2] == 'init':
                    cli_wallet_init()
                elif sys.argv[2] == 'clean':
                    cli_wallet_clean()
                elif sys.argv[2] == 'test':
                    wallet_api_test()
            else:
                cli_wallet_start2()
        elif sys.argv[1] == 'clean':
            node_clean()
        # else:
        #    node_restart()
    else:
        node_restart()

