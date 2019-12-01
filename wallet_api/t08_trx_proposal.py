#-*- coding: utf-8  -*-

import unittest
from config import *
from utils import *
import os
import sys

class test_wallet_transaction_proposal_api(request_unittest):
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


# (begin_builder_transaction)(add_operation_to_builder_transaction)
# (replace_operation_in_builder_transaction)(preview_builder_transaction)
# (sign_builder_transaction)(propose_builder_transaction)(remove_builder_transaction)
# (get_transaction_by_id)(get_transaction_in_block_info)(get_account_top_transaction)

# (get_account_transaction)

# (serialize_transaction)(sign_transaction)(validate_transaction)

# (propose_parameter_change)(propose_fee_change)(approve_proposal)

    def test_get_account_top_transaction(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "get_account_top_transaction",
            "params": [test_account],
            "id":1
        }
        self.request_post(req_data)['result']
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    # pair<pair<tx_hash_type, pair<object_id_type, account_transaction_history_id_type>>, processed_transaction> wallet_api::get_account_top_transaction(const string account_id_or_name)
    def test_get_transaction(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "get_account_top_transaction",
            "params": [test_account],
            "id":1
        }
        transactions = self.request_post(req_data)['result']
        pair_trx = transactions[0]
        trx_id = pair_trx[0]
        print("trx_id: {}".format(trx_id))
        req_data = {
            "jsonrpc": "2.0",
            "method": "get_transaction_by_id",
            "params": [trx_id],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "get_transaction_in_block_info",
            "params": [trx_id],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    def test_builder_transaction(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "begin_builder_transaction",
            "params": [],
            "id":1
        }
        transaction_handle = self.request_post(req_data)['result']

        req_data = {
            "jsonrpc": "2.0",
            "method": "transfer",
            "params": [test_account, test_witness_account, "20", "COCOS", ["test builder trx", 'false'], 'false'],
            "id":1
        }
        transfer_result = self.request_post(req_data)['result']
        transfer_operation = transfer_result[1]["operations"][0]
        # transfer_operation_index = transfer_operation[0]
        print("transfer_operations: {}".format(transfer_operation))

        # void wallet_api::add_operation_to_builder_transaction(transaction_handle_type transaction_handle, const operation &op)
        req_data = {
            "jsonrpc": "2.0",
            "method": "add_operation_to_builder_transaction",
            "params": [transaction_handle, transfer_operation],
            "id":1
        }
        self.request_post(req_data)

        #preview_builder_transaction
        req_data = {
            "jsonrpc": "2.0",
            "method": "preview_builder_transaction",
            "params": [transaction_handle],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "sign_builder_transaction",
            "params": [transaction_handle, 'true'],
            "id":1
        }
        self.request_post(req_data)

        #replace_operation_in_builder_transaction
        ref_block_num = transfer_result[1]['ref_block_num']
        filename = 'ref_' + str(ref_block_num)
        file_content = 'build transaction transfer ref_block_num = ' + str(ref_block_num)
        req_data = {
            "jsonrpc": "2.0",
            "method": "create_file",
            "params": [test_account, filename, file_content, 'false'],
            "id":1
        }
        create_file_result = self.request_post(req_data)['result']
        create_file_operation = create_file_result['operations'][0]
        create_file_operation_index = create_file_operation[0]
        print('create_file_operation_index: {}'.format(create_file_operation_index))

        req_data = {
            "jsonrpc": "2.0",
            "method": "add_operation_to_builder_transaction",
            "params": [transaction_handle, create_file_operation],
            "id":1
        }
        self.request_post(req_data)

        filename = 'r_' + str(ref_block_num)
        file_content = '[replace_operation_in_builder_transaction] build transaction transfer ref_block_num = ' + str(ref_block_num)
        # replace_create_file_operations = create_file_operations
        req_data = {
            "jsonrpc": "2.0",
            "method": "create_file",
            "params": [test_account, filename, file_content, 'false'],
            "id":1
        }
        create_file_result = self.request_post(req_data)['result']
        replace_create_file_operation = create_file_result['operations'][0]

        # void wallet_api::replace_operation_in_builder_transaction(transaction_handle_type handle, unsigned operation_index, const operation &new_op)
        req_data = {
            "jsonrpc": "2.0",
            "method": "replace_operation_in_builder_transaction",
            "params": [transaction_handle, create_file_operation_index, replace_create_file_operation],
            "id":1
        }
        # self.request_post(req_data)

#>> replace_operation_in_builder_transaction [12, 46, [46, {u'file_owner': u'1.2.16', u'file_name': u'r_13590', u'file_content': u'[replace_operation_in_builder_transaction]
#  build transaction transfer ref_block_num = 13590'}]]
# {u'jsonrpc': u'2.0', u'id': 1, u'error': {u'message': u'Assert Exception: operation_index < trx.operations.size(): ', u'code': 1}}
# 之前就遇到的问题，没修复。


        #preview_builder_transaction
        req_data = {
            "jsonrpc": "2.0",
            "method": "preview_builder_transaction",
            "params": [transaction_handle],
            "id":1
        }
        self.request_post(req_data)

        #propose_builder_transaction
        expiration_time = datetime_N_ago(-1).strftime("%Y-%m-%dT%H:%M:%S")
        req_data = {
            "jsonrpc": "2.0",
            "method": "propose_builder_transaction",
            "params": [transaction_handle, test_account, expiration_time, "600", 'true'],
            "id":1
        }
        self.request_post(req_data)

        # sign_builder_transaction
        req_data = {
            "jsonrpc": "2.0",
            "method": "sign_builder_transaction",
            "params": [transaction_handle, 'true'],
            "id":1
        }
        self.request_post(req_data)

        # remove_builder_transaction
        req_data = {
            "jsonrpc": "2.0",
            "method": "remove_builder_transaction",
            "params": [transaction_handle],
            "id":1
        }
        self.request_post(req_data)

        print('{} done\n'.format(sys._getframe().f_code.co_name))



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

>> begin_builder_transaction []
{u'jsonrpc': u'2.0', u'id': 1, u'result': 13}

>> transfer ['nicotest', 'init1', '20', 'COCOS', ['test builder trx', 'false'], 'false']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [u'4c2a89d795ff88b7204a98201ad3d6bbb511ddab39d5594393e51978edf057ef', {u'ref_block_prefix': 2936364321, u'operations': [[0, {u'to'
: u'1.2.6', u'amount': {u'asset_id': u'1.3.0', u'amount': 2000000}, u'from': u'1.2.16', u'memo': [0, u'test builder trx'], u'extensions': []}]], u'signatures': [u'2072f48fb
1519d5fb69eaa7bb9793bb63abb3d156e92da5b5c7aebae4a8a098515105502106f549b2124608c4361c6fbc8aab865053e6a0719b889caabf262a90c'], u'ref_block_num': 14542, u'extensions': [], u'e
xpiration': u'2019-12-01T12:45:56'}]}

transfer_operations: [0, {u'to': u'1.2.6', u'amount': {u'asset_id': u'1.3.0', u'amount': 2000000}, u'from': u'1.2.16', u'memo': [0, u'test builder trx'], u'extensions': []}
]
>> add_operation_to_builder_transaction [13, [0, {u'to': u'1.2.6', u'amount': {u'asset_id': u'1.3.0', u'amount': 2000000}, u'from': u'1.2.16', u'memo': [0, u'test builder t
rx'], u'extensions': []}]]
{u'jsonrpc': u'2.0', u'id': 1, u'result': None}

>> preview_builder_transaction [13]
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'ref_block_prefix': 0, u'ref_block_num': 0, u'extensions': [], u'expiration': u'1970-01-01T00:00:00', u'operations': [[0, {u'to'
: u'1.2.6', u'amount': {u'asset_id': u'1.3.0', u'amount': 2000000}, u'from': u'1.2.16', u'memo': [0, u'test builder trx'], u'extensions': []}]]}}

>> sign_builder_transaction [13, 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [u'cde93cdbd5c8bafe3e78560746b0c6edb5b322a5ee7f58bea021193f089d3723', {u'ref_block_prefix': 2936364321, u'operations': [[0, {u'to'
: u'1.2.6', u'amount': {u'asset_id': u'1.3.0', u'amount': 2000000}, u'from': u'1.2.16', u'memo': [0, u'test builder trx'], u'extensions': []}]], u'signatures': [u'205d8f9c3
4accc3f81701ab3eb5826ea1f6f7069d20dac8f0e5c22bd5cf68a23fd1430a9727245dd9ab025dd1726055a418e335546e5768336c7456186381e38c4'], u'ref_block_num': 14542, u'extensions': [], u'e
xpiration': u'2019-12-01T12:45:57'}]}

>> create_file ['nicotest', 'ref_14542', 'build transaction transfer ref_block_num = 14542', 'false']
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'ref_block_prefix': 2936364321, u'operations': [[46, {u'file_owner': u'1.2.16', u'file_name': u'ref_14542', u'file_content': u'b
uild transaction transfer ref_block_num = 14542'}]], u'signatures': [u'2040fc96b10abed5873f3de892f5c07f1fba655094c766456905a2452c9a1b62ea235d7d86c4e068ea987ca7522b4c6592aee
28f187622f67075f3b06711925b4e'], u'ref_block_num': 14542, u'extensions': [], u'expiration': u'2019-12-01T12:45:56'}}

create_file_operation_index: 46
>> add_operation_to_builder_transaction [13, [46, {u'file_owner': u'1.2.16', u'file_name': u'ref_14542', u'file_content': u'build transaction transfer ref_block_num = 14542
'}]]
{u'jsonrpc': u'2.0', u'id': 1, u'result': None}

>> create_file ['nicotest', 'r_14542', '[replace_operation_in_builder_transaction] build transaction transfer ref_block_num = 14542', 'false']
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'ref_block_prefix': 2936364321, u'operations': [[46, {u'file_owner': u'1.2.16', u'file_name': u'r_14542', u'file_content': u'[re
place_operation_in_builder_transaction] build transaction transfer ref_block_num = 14542'}]], u'signatures': [u'1f4d3811600fb60195db8c44176dead86709217990a376aec18f14098658
423d704521789fb107c12a00b90d1f774b06c85a9879b484fdff1227156aee2a4be6ef'], u'ref_block_num': 14542, u'extensions': [], u'expiration': u'2019-12-01T12:45:56'}}

>> preview_builder_transaction [13]
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'ref_block_prefix': 2936364321, u'ref_block_num': 14542, u'extensions': [], u'expiration': u'2019-12-01T12:45:57', u'operations'
: [[0, {u'to': u'1.2.6', u'amount': {u'asset_id': u'1.3.0', u'amount': 2000000}, u'from': u'1.2.16', u'memo': [0, u'test builder trx'], u'extensions': []}], [46, {u'file_ow
ner': u'1.2.16', u'file_name': u'ref_14542', u'file_content': u'build transaction transfer ref_block_num = 14542'}]]}}

>> propose_builder_transaction [13, 'nicotest', '2019-12-02T12:25:27', '600', 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [u'1d5c67ede7932978b3a7fb0ec4ee9fa41cc7d70c695153fb1218dfbdbf6e0dad', {u'ref_block_prefix': 2936364321, u'operations': [[20, {u'ex
piration_time': u'2019-12-02T12:25:27', u'proposed_ops': [{u'op': [0, {u'to': u'1.2.6', u'amount': {u'asset_id': u'1.3.0', u'amount': 2000000}, u'from': u'1.2.16', u'memo':
 [0, u'test builder trx'], u'extensions': []}]}, {u'op': [46, {u'file_owner': u'1.2.16', u'file_name': u'ref_14542', u'file_content': u'build transaction transfer ref_block
_num = 14542'}]}], u'extensions': [], u'review_period_seconds': 600, u'fee_paying_account': u'1.2.16'}]], u'signatures': [u'1f025557805b08464ffb3bc1f4b9a84421ba101f7dbb5233
7a8e7b64b202034df827d738eb042311b174ca9166576dc56440eb481da41f9aa6ea9e0a158bc4bd88'], u'ref_block_num': 14542, u'extensions': [], u'expiration': u'2019-12-01T12:45:56'}]}

>> sign_builder_transaction [13, 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [u'14e9f69cbb50135a8be810e5833a5f094676ca8d073a8a1c4357c60101acaff3', {u'ref_block_prefix': 2936364321, u'operations': [[0, {u'to'
: u'1.2.6', u'amount': {u'asset_id': u'1.3.0', u'amount': 2000000}, u'from': u'1.2.16', u'memo': [0, u'test builder trx'], u'extensions': []}], [46, {u'file_owner': u'1.2.1
6', u'file_name': u'ref_14542', u'file_content': u'build transaction transfer ref_block_num = 14542'}]], u'signatures': [u'201e356349dda5775f89ab15164339341e4d98391f627553d
85a3f022ad51a80c31870ffa052303f506aa1e475e969cc13692904302a4105dd0ef7c5fc188be710'], u'ref_block_num': 14542, u'extensions': [], u'expiration': u'2019-12-01T12:45:56'}]}

>> remove_builder_transaction [13]
{u'jsonrpc': u'2.0', u'id': 1, u'result': None}

test_builder_transaction done

.>> get_account_top_transaction ['nicotest']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [[u'ff67723c995be4b37606462f01b81297f9ace558e473b5270374bd3189aaf194', [u'2.9.268', u'2.9.266']], {u'ref_block_prefix': 1274356783
, u'operations': [[0, {u'to': u'1.2.6', u'amount': {u'asset_id': u'1.3.0', u'amount': 2000000}, u'from': u'1.2.16', u'memo': [0, u'test builder trx'], u'extensions': []}]],
 u'signatures': [u'20157db71c854278a78c092d5035e2e7375973b26c944220615b5ecc20308f168a128207ec5f0dc3780bbfbf6f97945e52f7ae70ad8e29dc9621eb88bd37f0dc99'], u'operation_results
': [[1, {u'real_running_time': 115, u'fees': [{u'asset_id': u'1.3.0', u'amount': 2018554}]}]], u'ref_block_num': 13590, u'extensions': [], u'expiration': u'2019-12-01T12:10
:59'}]}

test_get_account_top_transaction done

.>> get_account_top_transaction ['nicotest']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [[u'ff67723c995be4b37606462f01b81297f9ace558e473b5270374bd3189aaf194', [u'2.9.268', u'2.9.266']], {u'ref_block_prefix': 1274356783
, u'operations': [[0, {u'to': u'1.2.6', u'amount': {u'asset_id': u'1.3.0', u'amount': 2000000}, u'from': u'1.2.16', u'memo': [0, u'test builder trx'], u'extensions': []}]],
 u'signatures': [u'20157db71c854278a78c092d5035e2e7375973b26c944220615b5ecc20308f168a128207ec5f0dc3780bbfbf6f97945e52f7ae70ad8e29dc9621eb88bd37f0dc99'], u'operation_results
': [[1, {u'real_running_time': 115, u'fees': [{u'asset_id': u'1.3.0', u'amount': 2018554}]}]], u'ref_block_num': 13590, u'extensions': [], u'expiration': u'2019-12-01T12:10
:59'}]}

trx_id: ff67723c995be4b37606462f01b81297f9ace558e473b5270374bd3189aaf194
>> get_transaction_by_id [u'ff67723c995be4b37606462f01b81297f9ace558e473b5270374bd3189aaf194']
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'ref_block_prefix': 1274356783, u'operations': [[0, {u'to': u'1.2.6', u'amount': {u'asset_id': u'1.3.0', u'amount': 2000000}, u'
from': u'1.2.16', u'memo': [0, u'test builder trx'], u'extensions': []}]], u'signatures': [u'20157db71c854278a78c092d5035e2e7375973b26c944220615b5ecc20308f168a128207ec5f0dc
3780bbfbf6f97945e52f7ae70ad8e29dc9621eb88bd37f0dc99'], u'operation_results': [[1, {u'real_running_time': 115, u'fees': [{u'asset_id': u'1.3.0', u'amount': 2018554}]}]], u'r
ef_block_num': 13590, u'extensions': [], u'expiration': u'2019-12-01T12:10:59'}}

>> get_transaction_in_block_info [u'ff67723c995be4b37606462f01b81297f9ace558e473b5270374bd3189aaf194']
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'trx_hash': u'ff67723c995be4b37606462f01b81297f9ace558e473b5270374bd3189aaf194', u'trx_in_block': 0, u'id': u'3.1.217', u'block_
num': 13600}}

test_get_transaction done

.>> lock []
{u'jsonrpc': u'2.0', u'id': 1, u'result': None}

tearDownClass done


----------------------------------------------------------------------
Ran 3 tests in 2.537s

OK
'''