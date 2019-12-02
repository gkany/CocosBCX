# -*- coding: utf-8 -*-

host = '127.0.0.1'
port = 8048
cli_wallet_url = "http://{}:{}".format(host, port)

rpc_host = '127.0.0.1'
rpc_port = 8049
node_rpc_url = "http://{}:{}".format(rpc_host, rpc_port)

wallet_password = "123456"

headers = {"content-type": "application/json"}

test_account = 'nicotest'
test_account_private_key = '5J2SChqa9QxrCkdMor9VC2k9NT4R4ctRrJA6odQCPkb3yL89vxo'
test_account_public_key = 'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx'

test_balance_address = '5KAUeN3Yv51FzpLGGf4S1ByKpMqVFNzXTJK7euqc3NnaaLz1GJm' # 链启动后已经导入过

test_witness_account = 'init1'
test_witness_account_public_key = 'COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7'
test_witness_account_private_key = '5K5fqjvMrH5UtUisCgSZHQjiQf9BvtZ5vsKPhCErDy7P2gnLQmw'


test_committee_account = 'init5'
test_committee_account_public_key = 'COCOS8LQSvCgZvwW44iJuCBkVmpR3uUh6J2VFkBJScA3vJq3gXTLCLr'
test_committee_account_private_key = '5KVEqMvCQf5CP4Stkd9CW479uwQnDbhCiFxbdRLXgkxS3RchZ6X'

test_nh_creator = "creator2"

core_asset = "COCOS"
asset_gas = "GAS"
test_default_asset = "AAAA"
test_default_bitasset = "BBBB"


#   {"id":1,"method":"call","params":[1,"network_broadcast",[]]}
#   {"id":1,"method":"call","params":[1,"network_node",[]]}
#   {"id":1,"method":"call","params":[1,"network_broadcast",[]]}
#   {"id":1,"method":"call","params":[1,"database",[]]}
#   {"id":1,"method":"call","params":[1,"history",[]]}
chain_api = [
    "database",
    "network_broadcast",
    "network_node",
    "history"
]