#-*- coding: utf-8  -*-

import unittest
from config import *
from utils import *
import os
import sys

class test_wallet_file_api(request_unittest):
    @classmethod
    def setUpClass(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "unlock",
            "params": [wallet_password],
            "id":1
        }
        request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "import_key",
            "params": [test_account, test_account_private_key],
            "id":1
        }
        request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "import_key",
            "params": [test_witness_account, test_witness_account_private_key],
            "id":1
        }
        request_post(req_data)

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

    # def setUp(self):
    #     print('setUp done')

    # def tearDown(self):
    #     print('tearDown done')

    def test_create_file(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "info",
            "params": [],
            "id":1
        }
        info = self.request_post(req_data)['result']
        head_block_num = info['head_block_num']
        head_block_id = info['head_block_id']

        filename = 'block_num_' + str(head_block_num)
        file_content = 'block id = ' + head_block_id
        req_data = {
            "jsonrpc": "2.0",
            "method": "create_file",
            "params": [test_account, filename, file_content, 'true'],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "lookup_file",
            "params": [filename],
            "id":1
        }
        file = self.request_post(req_data)['result']
        file_id = file['id']

        req_data = {
            "jsonrpc": "2.0",
            "method": "add_file_relate_account",
            "params": [test_account, file_id, [test_witness_account], 'true'],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "file_signature",
            "params": [test_witness_account, file_id, "relate accout signature", 'true'],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "list_account_created_file",
            "params": [test_account],
            "id":1
        }
        self.request_post(req_data)


    # signed_transaction propose_relate_parent_file(const string &file_creator, 
    #       const string &parent_file_name_or_id, const string &sub_file_name_or_id,
    #       fc::time_point_sec expiration_time, bool broadcast = false)
    def test_propose_relate_parent_file(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "info",
            "params": [],
            "id":1
        }
        info = self.request_post(req_data)['result']
        head_block_num = info['head_block_num']
        head_block_id = info['head_block_id']

        parent_filename = 'p_block_num_' + str(head_block_num) 
        sub_filename = 's_block_num_' + str(head_block_num)
        size = len(head_block_id)
        parent_file_content = 'block id : ' + head_block_id
        sub_file_content = 'part block id: ' + head_block_id[0:int(size/2)]
        req_data = {
            "jsonrpc": "2.0",
            "method": "create_file",
            "params": [test_account, parent_filename, parent_file_content, 'true'],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "create_file",
            "params": [test_account, sub_filename, sub_file_content, 'true'],
            "id":1
        }
        self.request_post(req_data)

        expiration_time = datetime_N_ago(-1).strftime("%Y-%m-%dT%H:%M:%S")
        req_data = {
            "jsonrpc": "2.0",
            "method": "propose_relate_parent_file",
            "params": [test_account, parent_filename, sub_filename, expiration_time, 'true'],
            "id":1
        }
        self.request_post(req_data)

if __name__ == "__main__":
    unittest.main()


'''
>> unlock ['123456']
{u'jsonrpc': u'2.0', u'id': 1, u'result': None}

>> import_key ['nicotest', '5J2SChqa9QxrCkdMor9VC2k9NT4R4ctRrJA6odQCPkb3yL89vxo']
{u'jsonrpc': u'2.0', u'id': 1, u'result': True}

>> import_key ['init1', '5K5fqjvMrH5UtUisCgSZHQjiQf9BvtZ5vsKPhCErDy7P2gnLQmw']
{u'jsonrpc': u'2.0', u'id': 1, u'result': True}

setUpClass done

>> info []
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'active_committee_members': [u'1.5.0', u'1.5.1', u'1.5.2', u'1.5.3', u'1.5.4', u'1.5.5', u'1.5.6', u'1.5.7', u'1.5.8', u'1.5.9',
 u'1.5.10'], u'head_block_age': u'0 second ago', u'chain_id': u'c1ac4bb7bd7d94874a1cb98b39a8a582421d03d022dfa4be8c70567076e03ad0', u'active_witnesses': [u'1.6.1', u'1.6.2',
 u'1.6.3', u'1.6.4', u'1.6.5', u'1.6.6', u'1.6.7', u'1.6.8', u'1.6.9', u'1.6.10', u'1.6.11'], u'head_block_id': u'000007cbf009cc7583d9dbcbaffcc1989caf54bb', u'next_maintena
nce_time': u'13 minutes in the future', u'participation': u'90.62500000000000000', u'head_block_num': 1995}}

>> create_file ['nicotest', 'block_num_1995', u'block id = 000007cbf009cc7583d9dbcbaffcc1989caf54bb', 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'ref_block_prefix': 678620151, u'operations': [[46, {u'file_owner': u'1.2.16', u'file_name': u'block_num_1995', u'file_content':
 u'block id = 000007cbf009cc7583d9dbcbaffcc1989caf54bb'}]], u'signatures': [u'1f3be4a084cf38fde521e45028b32ee32720a561405a2aa63234f57575da0d5acd1d4d3aa29130e470eb41656affa9
12b825d8a2cfc67cbd8d958c6c35e906fd08'], u'ref_block_num': 1986, u'extensions': [], u'expiration': u'2019-11-30T18:07:12'}}

>> lookup_file ['block_num_1995']
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'file_owner': u'1.2.16', u'file_content': u'block id = 000007cbf009cc7583d9dbcbaffcc1989caf54bb', u'file_name': u'block_num_1995
', u'create_time': u'2019-11-30T17:46:42', u'signature': [], u'sub_file': [], u'id': u'1.18.9', u'related_account': []}}

>> add_file_relate_account ['nicotest', u'1.18.9', ['init1'], 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'ref_block_prefix': 678620151, u'operations': [[47, {u'file_owner': u'1.2.16', u'file_id': u'1.18.9', u'related_account': [u'1.2
.6']}]], u'signatures': [u'1f05badb9da90d02d52cf07d0c07413efc91e7aabf5c8b75a2c49661ad779ed3b928736d10c6df6fa67afdb0e9b8bc4d6733669159224cf872459bc90734201c2f'], u'ref_block
_num': 1986, u'extensions': [], u'expiration': u'2019-11-30T18:07:12'}}

>> file_signature ['init1', u'1.18.9', 'relate accout signature', 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'ref_block_prefix': 678620151, u'operations': [[48, {u'signature': u'relate accout signature', u'file_id': u'1.18.9', u'signatur
e_account': u'1.2.6'}]], u'signatures': [u'207513eb23c18f06712dd5746e307b243c0fa2db239a08dd5ed787dd5ed5a5a6da19b756cad70ed2eae2976f1200c9506d450bc43e2ce4f0ce44c384a7cc9b326
0'], u'ref_block_num': 1986, u'extensions': [], u'expiration': u'2019-11-30T18:07:12'}}

>> list_account_created_file ['nicotest']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [[u'block_num_1200', u'1.18.0'], [u'block_num_1433', u'1.18.1'], [u'block_num_1881', u'1.18.2'], [u'block_num_1898', u'1.18.3'], [
u'block_num_1927', u'1.18.4'], [u'block_num_1951', u'1.18.5'], [u'block_num_1975', u'1.18.6'], [u'block_num_1995', u'1.18.9'], [u'p_block_num_1975', u'1.18.7'], [u's_block_
num_1975', u'1.18.8']]}

.>> info []
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'active_committee_members': [u'1.5.0', u'1.5.1', u'1.5.2', u'1.5.3', u'1.5.4', u'1.5.5', u'1.5.6', u'1.5.7', u'1.5.8', u'1.5.9',
 u'1.5.10'], u'head_block_age': u'0 second ago', u'chain_id': u'c1ac4bb7bd7d94874a1cb98b39a8a582421d03d022dfa4be8c70567076e03ad0', u'active_witnesses': [u'1.6.1', u'1.6.2',
 u'1.6.3', u'1.6.4', u'1.6.5', u'1.6.6', u'1.6.7', u'1.6.8', u'1.6.9', u'1.6.10', u'1.6.11'], u'head_block_id': u'000007cbf009cc7583d9dbcbaffcc1989caf54bb', u'next_maintena
nce_time': u'13 minutes in the future', u'participation': u'90.62500000000000000', u'head_block_num': 1995}}

>> create_file ['nicotest', 'p_block_num_1995', u'block id : 000007cbf009cc7583d9dbcbaffcc1989caf54bb', 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'ref_block_prefix': 678620151, u'operations': [[46, {u'file_owner': u'1.2.16', u'file_name': u'p_block_num_1995', u'file_content
': u'block id : 000007cbf009cc7583d9dbcbaffcc1989caf54bb'}]], u'signatures': [u'1f2dfedf823b4eeadff6c0e1fa7beaaca9a55e39f53ee363ffc6369f47502224fd7f520b232117075993f1d562bf
704244e1696d0968e963dba917a8e539c6682a'], u'ref_block_num': 1986, u'extensions': [], u'expiration': u'2019-11-30T18:07:12'}}

>> create_file ['nicotest', 's_block_num_1995', u'part block id: 000007cbf009cc7583d9', 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'ref_block_prefix': 678620151, u'operations': [[46, {u'file_owner': u'1.2.16', u'file_name': u's_block_num_1995', u'file_content
': u'part block id: 000007cbf009cc7583d9'}]], u'signatures': [u'200cabb937e09ecd7e23b99e83895706351b29aba8a9cfcd398e44fb2ef14e0efd5ab8fb5e887091d9e7d2d1f10e9fe5593e82c0a0cf
8081d3c1550c2137284060'], u'ref_block_num': 1986, u'extensions': [], u'expiration': u'2019-11-30T18:07:12'}}

>> propose_relate_parent_file ['nicotest', 'p_block_num_1995', 's_block_num_1995', '2019-12-01T17:46:42', 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'ref_block_prefix': 678620151, u'operations': [[20, {u'expiration_time': u'2019-12-01T17:46:42', u'proposed_ops': [{u'op': [49,
{u'parent_file_owner': u'1.2.16', u'sub_file_owner': u'1.2.16', u'parent_file': u'1.18.10', u'sub_file': u'1.18.11'}]}], u'extensions': [], u'fee_paying_account': u'1.2.16'
}]], u'signatures': [u'1f01c045e5051d803f55b2a0145fe7aee8c748a4ac68b89e3c4ac0a7ba011e788f38ff5afcf4a5ab85bd35c3ce6bd42739608d7e9008734120877baf38367854dd'], u'ref_block_num
': 1986, u'extensions': [], u'expiration': u'2019-11-30T18:07:12'}}

.>> lock []
{u'jsonrpc': u'2.0', u'id': 1, u'result': None}

tearDownClass done


----------------------------------------------------------------------
Ran 2 tests in 0.143s

OK
'''