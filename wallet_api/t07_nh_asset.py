#-*- coding: utf-8  -*-

import unittest
from config import *
from utils import *
# import os
import sys
from chain_param import *

class test_wallet_nh_asset_api(request_unittest):
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
            "method": "upgrade_account",
            "params": [test_account, 'true'],
            "id":1
        }
        # request_post(req_data)
        response = request_post(req_data, False)

        req_data = {
            "jsonrpc": "2.0",
            "method": "load_wallet_file",
            "params": [""],
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

        #get_nh_creator
        req_data = {
            "jsonrpc": "2.0",
            "method": "get_nh_creator",
            "params": [test_account],
            "id":1
        }
        response = request_post(req_data, False)
        if 'error' in response:
            #register nh creator
            req_data = {
                "jsonrpc": "2.0",
                "method": "register_nh_asset_creator",
                "params": [test_account, 'true'],
                "id":1
            }
            request_post(req_data)
        self.nh_creator = test_account
        self.nh_creator_account_id = response['result']['creator']
        print('creator_account_id: {}'.format(self.nh_creator_account_id))

        req_data = {
            "jsonrpc": "2.0",
            "method": "get_account",
            "params": [test_nh_creator],
            "id":1
        }
        response = request_post(req_data, False)
        if 'error' in response:
            #register account
            req_data = {
                "jsonrpc": "2.0",
                "method": "register_account",
                "params": [test_nh_creator, test_account_public_key, test_account_public_key, test_account, 'true'],
                "id":1
            }
            request_post(req_data)
            req_data = {
                "jsonrpc": "2.0",
                "method": "import_key",
                "params": [test_nh_creator, test_account_private_key],
                "id":1
            }
            request_post(req_data)

            req_data = {
                "jsonrpc": "2.0",
                "method": "transfer",
                "params": [test_account, test_nh_creator, 1000000, "COCOS", ["nh asset api test", "false"], 'true'],
                "id":1
            }
            request_post(req_data)

            req_data = {
                "jsonrpc": "2.0",
                "method": "upgrade_account",
                "params": [test_nh_creator, 'true'],
                "id":1
            }
            request_post(req_data)

            req_data = {
                "jsonrpc": "2.0",
                "method": "get_nh_creator",
                "params": [test_nh_creator],
                "id":1
            }
            response = request_post(req_data, False)
            if 'error' in response:
                #register nh creator
                req_data = {
                    "jsonrpc": "2.0",
                    "method": "register_nh_asset_creator",
                    "params": [test_nh_creator, 'true'],
                    "id":1
                }
                request_post(req_data)

        # create world view
        tokens = generate_random_words()
        world_view = 'test_' + tokens[0].lower()
        req_data = {
            "jsonrpc": "2.0",
            "method": "create_world_view",
            "params": [test_account, world_view, 'true'],
            "id":1
        }
        request_post(req_data)
        self.world_view = world_view
        self.relate_world_view = 'test_' + tokens[1].lower()

        self.core_asset = core_asset
        self.core_asset_id = "1.3.0"

        # create world view
        tokens = generate_random_words()
        world_view = 'test_common'
        req_data = {
            "jsonrpc": "2.0",
            "method": "create_world_view",
            "params": [test_account, world_view, 'true'],
            "id":1
        }
        request_post(req_data, False)
        self.test_world_view_common = world_view

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


    # signed_transaction propose_relate_world_view(
    #     const string &proposing_account, fc::time_point_sec expiration_time,
    #     const string &world_view_owner, const string &world_view, bool broadcast = false)
    @unittest.skipIf(True, 'test other')
    def test_propose_relate_world_view(self):
        expiration_time = datetime_N_ago(-1).strftime("%Y-%m-%dT%H:%M:%S")
        req_data = {
            "jsonrpc": "2.0",
            "method": "propose_relate_world_view",
            "params": [test_nh_creator, expiration_time, test_account, self.world_view, 'true'],
            "id":1
        }
        info = self.request_post(req_data)['result']
        print('{} done\n'.format(sys._getframe().f_code.co_name))


    #   signed_transaction create_nh_asset(
    #       const string &creator, const string &owner, 
    #       const string &asset_id, const string &world_view,
    #       const string &base_describe, bool broadcast = false)
    def test_create_nh_asset(self):
        base_describe = "{k1:v1, k2:v2}"
        req_data = {
            "jsonrpc": "2.0",
            "method": "create_nh_asset",
            "params": [self.nh_creator, test_account, self.core_asset_id,
                        self.test_world_view_common, base_describe, 'true'],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

# std::pair<vector<nh_asset_object>, uint32_t> wallet_api::list_nh_asset_by_creator(
#     const string &nh_asset_creator,
#     uint32_t pagesize,
#     uint32_t page)

    @unittest.skipIf(True, "test other")
    def test_list_nh_asset_by_creator(self):
        pagesize = 5
        page = 1
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_nh_asset_by_creator",
            "params": [self.nh_creator, self.test_world_view_common, pagesize, page],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

# std::pair<vector<nh_asset_object>, uint32_t> wallet_api::list_account_nh_asset(
#     const string &nh_asset_owner,
#     const vector<string> &world_view_name_or_ids,
#     uint32_t pagesize,
#     uint32_t page,
#     nh_asset_list_type list_type)
    @unittest.skipIf(True, "test other")
    def test_list_account_nh_asset(self):
        pagesize = 5
        page = 1
        # list_type = nh_asset_list_type['owner_and_active']
        for index in range(0, len(nh_asset_list_type)):
            req_data = {
                "jsonrpc": "2.0",
                "method": "list_account_nh_asset",
                "params": [test_account, [self.world_view], pagesize, page, index],
                "id":1
            }
            self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

# pair<tx_hash_type, signed_transaction> wallet_api::transfer_nh_asset(
#     const string &from,
#     const string &to,
#     const string &nh_asset,
#     bool broadcast)
    @unittest.skipIf(True, "test other")
    def test_transfer_nh_asset(self):
        base_describe = "{k1:v1, k2:v2}"
        req_data = {
            "jsonrpc": "2.0",
            "method": "create_nh_asset",
            "params": [self.nh_creator, test_account, self.core_asset_id,
                        self.test_world_view_common, base_describe, 'true'],
            "id":1
        }
        for _ in range(0, 3):
            self.request_post(req_data)

        pagesize = 5
        page = 1
        index = 4       # owner_and_active
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_account_nh_asset",
            "params": [test_account, [self.test_world_view_common], pagesize, page, index],
            "id":1
        }
        page_nh_assets = self.request_post(req_data)['result']
        # page_nh_assets: [[obj1, obj2, obj3...], size]            
        index = 0
        for nh_asset in page_nh_assets[0]:
            # print('nh_asset: {}'.format(nh_asset))            
            asset_id = nh_asset['id']
            if index == 0:
                #transfer
                req_data = {
                    "jsonrpc": "2.0",
                    "method": "transfer_nh_asset",
                    "params": [nh_asset['nh_asset_owner'], test_witness_account, asset_id, 'true'],
                    "id":1
                }
                request_post(req_data)
            # elif index == 1:
            elif index % 100 == 1:
                #delete
                req_data = {
                    "jsonrpc": "2.0",
                    "method": "delete_nh_asset",
                    "params": [self.nh_creator, asset_id, 'true'],
                    "id":1
                }
                self.request_post(req_data)
            index = index + 1
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, "test other")
    def test_list_account_nh_asset_order(self):
        pagesize = 5
        page = 1
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_account_nh_asset_order",
            "params": [self.nh_creator, pagesize, page],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

# std::pair<vector<nh_asset_order_object>, uint32_t> wallet_api::list_nh_asset_order(
#     const string &asset_symbols_or_id,
#     const string &world_view_name_or_id,
#     const string &base_describe,
#     uint32_t pagesize,
#     uint32_t page,
#     bool is_ascending_order)
    def test_list_nh_asset_order(self):
        base_describe = "{k1:v1, k2:v2}"
        pagesize = 5
        page = 1
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_nh_asset_order",
            "params": [self.core_asset_id, self.test_world_view_common, 
                    base_describe, pagesize, page, 'true'],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

# pair<tx_hash_type, signed_transaction> wallet_api::create_nh_asset_order(
#     const string &seller,
#     const string &otcaccount,
#     const string &pending_fee_amount,
#     const string &pending_fee_symbol,
#     const string &nh_asset,
#     const string &price_amount,
#     const string &price_symbol,
#     const string &memo,
#     fc::time_point_sec expiration_time,
#     bool broadcast)

    def test_nh_assert_order(self):
        pagesize = 5
        page = 1
        index = 4       # owner_and_active
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_account_nh_asset",
            "params": [test_account, [self.test_world_view_common], pagesize, page, index],
            "id":1
        }
        page_nh_assets = self.request_post(req_data)['result']
        # page_nh_assets: [[obj1, obj2, obj3...], size]            
        index = 0
        for nh_asset in page_nh_assets[0]:
            # asset_id = nh_asset['id']
            # if index % 2 == 0:
            seller = nh_asset['nh_asset_owner']
            otcaccount = test_witness_account
            pending_fee_amount = "500"
            pending_fee_symbol = core_asset
            nh_asset_id = nh_asset['id']
            price_amount = "1500"
            price_symbol = core_asset
            memo = "create_nh_asset_order test"
            expiration_time = datetime_N_ago(-1).strftime("%Y-%m-%dT%H:%M:%S")
            req_data = {
                "jsonrpc": "2.0",
                "method": "create_nh_asset_order",
                "params": [seller, otcaccount, pending_fee_amount, pending_fee_symbol,
                        nh_asset_id, price_amount, price_symbol, memo, expiration_time, 'true'],
                "id":1
            }
            request_post(req_data)
            index = index + 1
        print('{} done\n'.format(sys._getframe().f_code.co_name))


# pair<tx_hash_type, signed_transaction> wallet_api::cancel_nh_asset_order(
    # object_id_type order_id, bool broadcast)
    def test_cancel_nh_asset_order(self):
        pagesize = 5
        page = 1
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_account_nh_asset_order",
            "params": [self.nh_creator, pagesize, page],
            "id":1
        }
        nh_asset_orders = self.request_post(req_data)['result']
        index = 0
        for order in nh_asset_orders[0]:
            if index == 0:
                req_data = {
                    "jsonrpc": "2.0",
                    "method": "cancel_nh_asset_order",
                    "params": [order['id'], 'true'],
                    "id":1
                }
                request_post(req_data)
            index = index + 1
        print('{} done\n'.format(sys._getframe().f_code.co_name))

# pair<tx_hash_type, signed_transaction> wallet_api::fill_nh_asset_order(
#     const string &fee_paying_account,
#     nh_asset_order_id_type order_id,
#     bool broadcast)
    def test_fill_nh_asset_order(self):
        pagesize = 5
        page = 1
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_account_nh_asset_order",
            "params": [self.nh_creator, pagesize, page],
            "id":1
        }
        nh_asset_orders = self.request_post(req_data)['result']
        index = 0
        for order in nh_asset_orders[0]:
            if index == 0:
                req_data = {
                    "jsonrpc": "2.0",
                    "method": "fill_nh_asset_order",
                    "params": [test_account, order['id'], 'true'],
                    "id":1
                }
                request_post(req_data)
            index = index + 1
        print('{} done\n'.format(sys._getframe().f_code.co_name))

if __name__ == "__main__":
    unittest.main()

'''
>> unlock ['123456']
{u'jsonrpc': u'2.0', u'id': 1, u'result': None}

>> import_key ['nicotest', '5J2SChqa9QxrCkdMor9VC2k9NT4R4ctRrJA6odQCPkb3yL89vxo']
{u'jsonrpc': u'2.0', u'id': 1, u'result': True}

>> upgrade_account ['nicotest', 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'error': {u'message': u'Assert Exception: !account_obj.is_lifetime_member(): ', u'code': 1}}

>> load_wallet_file ['']
{u'jsonrpc': u'2.0', u'id': 1, u'result': True}

>> import_key ['init1', '5K5fqjvMrH5UtUisCgSZHQjiQf9BvtZ5vsKPhCErDy7P2gnLQmw']
{u'jsonrpc': u'2.0', u'id': 1, u'result': True}

>> get_nh_creator ['nicotest']
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'id': u'4.0.0', u'world_view': [u'test_veruled', u'test_stew', u'test_hushel', u'test_quizzer', u'test_mallow', u'test_katydid',
 u'test_aition', u'test_aflaunt', u'test_common', u'test_chordal', u'test_privily', u'test_uncheck', u'test_undry', u'test_closure', u'test_unrhyme', u'test_glaver', u'test
_cig', u'test_page', u'test_pipy', u'test_limbeck', u'test_foamer', u'test_roughet', u'test_freak', u'test_logman', u'test_drab', u'test_excite', u'test_pyrexia', u'test_re
gimen', u'test_sicsac', u'test_askance', u'test_cursus', u'test_grobian', u'test_alchimy', u'test_nuzzle', u'test_courlan', u'test_revend', u'test_unfiber', u'test_unionic'
, u'test_sorroa', u'test_feower', u'test_disturb', u'test_smeary', u'test_verve', u'test_tutoyer', u'test_unfar', u'test_infidel', u'test_shyly', u'test_midwise', u'test_jo
bber'], u'creator': u'1.2.16'}}

creator_account_id: 1.2.16
>> get_account ['creator2']
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'statistics': u'2.6.17', u'name': u'creator2', u'options': {u'memo_key': u'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mX
px', u'extensions': [], u'votes': []}, u'active': {u'weight_threshold': 1, u'account_auths': [], u'key_auths': [[u'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx',
 1]], u'address_auths': []}, u'registrar': u'1.2.16', u'asset_locked': {u'contract_lock_details': [], u'locked_total': []}, u'owner': {u'weight_threshold': 1, u'account_aut
hs': [], u'key_auths': [[u'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]], u'address_auths': []}, u'membership_expiration_date': u'1969-12-31T23:59:59', u'id
': u'1.2.17'}}

>> create_world_view ['nicotest', u'test_slung', 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [u'a474eda2f5ab902ee0eca85e4e01d07980aba2af4590dae7e546dea8f834b406', {u'ref_block_prefix': 294711135, u'operations': [[38, {u'wor
ld_view': u'test_slung', u'fee_paying_account': u'1.2.16'}]], u'signatures': [u'1f59e869de1ccac5d2b2cffde6b0929e7a60b4c2c321bec86ce6c65546dd7a7f01758d7616293c704746a82e2dea
ae079ab12c32e95932b427199b5cf7b00c009e'], u'ref_block_num': 9472, u'extensions': [], u'expiration': u'2019-12-01T04:12:58'}]}

>> create_world_view ['nicotest', 'test_common', 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'error': {u'message': u'unspecified: Assert Exception: insert_result.second: Could not create object! Most likely a uniqueness constraint is
 violated.', u'code': 1}}

setUpClass done

>> list_account_nh_asset_order ['nicotest', 5, 1]
{u'jsonrpc': u'2.0', u'id': 1, u'result': [[{u'base_describe': u'{k1:v1, k2:v2}', u'nh_asset_id': u'4.2.38', u'price': {u'asset_id': u'1.3.0', u'amount': 150000000}, u'memo
': u'create_nh_asset_order test', u'nh_hash': u'2600000000000000274c0c8a9173c4f7c282a31a790ca301e4f954c163f5f305', u'seller': u'1.2.16', u'asset_qualifier': u'COCOS', u'exp
iration': u'2019-12-02T03:52:22', u'otcaccount': u'1.2.6', u'id': u'4.3.9', u'world_view': u'test_common'}, {u'base_describe': u'{k1:v1, k2:v2}', u'nh_asset_id': u'4.2.36',
 u'price': {u'asset_id': u'1.3.0', u'amount': 150000000}, u'memo': u'create_nh_asset_order test', u'nh_hash': u'2400000000000000274c0c8a9173c4f7c282a31a790ca301e4f954c163f5
f305', u'seller': u'1.2.16', u'asset_qualifier': u'COCOS', u'expiration': u'2019-12-02T03:52:22', u'otcaccount': u'1.2.6', u'id': u'4.3.8', u'world_view': u'test_common'},
{u'base_describe': u'{k1:v1, k2:v2}', u'nh_asset_id': u'4.2.34', u'price': {u'asset_id': u'1.3.0', u'amount': 150000000}, u'memo': u'create_nh_asset_order test', u'nh_hash'
: u'2200000000000000274c0c8a9173c4f7c282a31a790ca301e4f954c163f5f305', u'seller': u'1.2.16', u'asset_qualifier': u'COCOS', u'expiration': u'2019-12-02T03:52:22', u'otcaccou
nt': u'1.2.6', u'id': u'4.3.7', u'world_view': u'test_common'}, {u'base_describe': u'{k1:v1, k2:v2}', u'nh_asset_id': u'4.2.31', u'price': {u'asset_id': u'1.3.0', u'amount'
: 150000000}, u'memo': u'create_nh_asset_order test', u'nh_hash': u'1f00000000000000274c0c8a9173c4f7c282a31a790ca301e4f954c163f5f305', u'seller': u'1.2.16', u'asset_qualifi
er': u'COCOS', u'expiration': u'2019-12-02T03:52:22', u'otcaccount': u'1.2.6', u'id': u'4.3.6', u'world_view': u'test_common'}, {u'base_describe': u'{k1:v1, k2:v2}', u'nh_a
sset_id': u'4.2.29', u'price': {u'asset_id': u'1.3.0', u'amount': 150000000}, u'memo': u'create_nh_asset_order test', u'nh_hash': u'1d00000000000000274c0c8a9173c4f7c282a31a
790ca301e4f954c163f5f305', u'seller': u'1.2.16', u'asset_qualifier': u'COCOS', u'expiration': u'2019-12-02T03:52:22', u'otcaccount': u'1.2.6', u'id': u'4.3.5', u'world_view
': u'test_common'}], 5]}

>> cancel_nh_asset_order [u'4.3.9', 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [u'b59bc6146d9d1be9dd399177e1d80a10ba40a543e4af81c6bc06f6b761ad6174', {u'ref_block_prefix': 294711135, u'operations': [[44, {u'ext
ensions': [], u'order': u'4.3.9', u'fee_paying_account': u'1.2.16'}]], u'signatures': [u'1f258fba634e1ab9d11891097592ddd39523e4fe74dddb8f08d7fe4213c0970cfd7a200d4acdf641f2b
8022130123dffd93a3595b02c025aa832ec5b1deeef2bb9'], u'ref_block_num': 9472, u'extensions': [], u'expiration': u'2019-12-01T04:12:58'}]}

test_cancel_nh_asset_order done

.>> create_nh_asset ['nicotest', 'nicotest', '1.3.0', 'test_common', '{k1:v1, k2:v2}', 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [u'7815698ebd5e5db2a4f86c386bc856f8f91aaa34b26353943978c2d992f6aefe', {u'ref_block_prefix': 294711135, u'operations': [[40, {u'own
er': u'1.2.16', u'asset_id': u'COCOS', u'base_describe': u'{k1:v1, k2:v2}', u'world_view': u'test_common', u'fee_paying_account': u'1.2.16'}]], u'signatures': [u'1f3913b992
e448b97d8382a02c1adf94d9111e6f803203a101883e60f31291e562465b62aaae170efac986856b67f94c55a02561c233f546a7fc3f69b8066c5638'], u'ref_block_num': 9472, u'extensions': [], u'exp
iration': u'2019-12-01T04:12:58'}]}

test_create_nh_asset done

.>> list_account_nh_asset_order ['nicotest', 5, 1]
{u'jsonrpc': u'2.0', u'id': 1, u'result': [[{u'base_describe': u'{k1:v1, k2:v2}', u'nh_asset_id': u'4.2.36', u'price': {u'asset_id': u'1.3.0', u'amount': 150000000}, u'memo
': u'create_nh_asset_order test', u'nh_hash': u'2400000000000000274c0c8a9173c4f7c282a31a790ca301e4f954c163f5f305', u'seller': u'1.2.16', u'asset_qualifier': u'COCOS', u'exp
iration': u'2019-12-02T03:52:22', u'otcaccount': u'1.2.6', u'id': u'4.3.8', u'world_view': u'test_common'}, {u'base_describe': u'{k1:v1, k2:v2}', u'nh_asset_id': u'4.2.34',
 u'price': {u'asset_id': u'1.3.0', u'amount': 150000000}, u'memo': u'create_nh_asset_order test', u'nh_hash': u'2200000000000000274c0c8a9173c4f7c282a31a790ca301e4f954c163f5
f305', u'seller': u'1.2.16', u'asset_qualifier': u'COCOS', u'expiration': u'2019-12-02T03:52:22', u'otcaccount': u'1.2.6', u'id': u'4.3.7', u'world_view': u'test_common'},
{u'base_describe': u'{k1:v1, k2:v2}', u'nh_asset_id': u'4.2.31', u'price': {u'asset_id': u'1.3.0', u'amount': 150000000}, u'memo': u'create_nh_asset_order test', u'nh_hash'
: u'1f00000000000000274c0c8a9173c4f7c282a31a790ca301e4f954c163f5f305', u'seller': u'1.2.16', u'asset_qualifier': u'COCOS', u'expiration': u'2019-12-02T03:52:22', u'otcaccou
nt': u'1.2.6', u'id': u'4.3.6', u'world_view': u'test_common'}, {u'base_describe': u'{k1:v1, k2:v2}', u'nh_asset_id': u'4.2.29', u'price': {u'asset_id': u'1.3.0', u'amount'
: 150000000}, u'memo': u'create_nh_asset_order test', u'nh_hash': u'1d00000000000000274c0c8a9173c4f7c282a31a790ca301e4f954c163f5f305', u'seller': u'1.2.16', u'asset_qualifi
er': u'COCOS', u'expiration': u'2019-12-02T03:52:22', u'otcaccount': u'1.2.6', u'id': u'4.3.5', u'world_view': u'test_common'}], 4]}

>> fill_nh_asset_order ['nicotest', u'4.3.8', 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [u'ce20cd706f2907c9cf6058db5bfa1f7e1aac925e622c4045c517506c5416f6d7', {u'ref_block_prefix': 294711135, u'operations': [[45, {u'pri
ce_amount': u'1500', u'fee_paying_account': u'1.2.16', u'price_asset_symbol': u'COCOS', u'seller': u'1.2.16', u'price_asset_id': u'1.3.0', u'extensions': [], u'nh_asset': u
'4.2.36', u'order': u'4.3.8'}]], u'signatures': [u'20534850da054cf3d8f2d9750ec29c6c653a304f00906a809901ab0c9db8671179503ab6f64b09e4627aa1f9c38f2b2d38614cd902bb6e7af18784f79
9027eff09'], u'ref_block_num': 9472, u'extensions': [], u'expiration': u'2019-12-01T04:12:58'}]}

test_fill_nh_asset_order done

.sss>> list_nh_asset_order ['1.3.0', 'test_common', '{k1:v1, k2:v2}', 5, 1, 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [[{u'base_describe': u'{k1:v1, k2:v2}', u'nh_asset_id': u'4.2.29', u'price': {u'asset_id': u'1.3.0', u'amount': 150000000}, u'memo
': u'create_nh_asset_order test', u'nh_hash': u'1d00000000000000274c0c8a9173c4f7c282a31a790ca301e4f954c163f5f305', u'seller': u'1.2.16', u'asset_qualifier': u'COCOS', u'exp
iration': u'2019-12-02T03:52:22', u'otcaccount': u'1.2.6', u'id': u'4.3.5', u'world_view': u'test_common'}, {u'base_describe': u'{k1:v1, k2:v2}', u'nh_asset_id': u'4.2.31',
 u'price': {u'asset_id': u'1.3.0', u'amount': 150000000}, u'memo': u'create_nh_asset_order test', u'nh_hash': u'1f00000000000000274c0c8a9173c4f7c282a31a790ca301e4f954c163f5
f305', u'seller': u'1.2.16', u'asset_qualifier': u'COCOS', u'expiration': u'2019-12-02T03:52:22', u'otcaccount': u'1.2.6', u'id': u'4.3.6', u'world_view': u'test_common'},
{u'base_describe': u'{k1:v1, k2:v2}', u'nh_asset_id': u'4.2.34', u'price': {u'asset_id': u'1.3.0', u'amount': 150000000}, u'memo': u'create_nh_asset_order test', u'nh_hash'
: u'2200000000000000274c0c8a9173c4f7c282a31a790ca301e4f954c163f5f305', u'seller': u'1.2.16', u'asset_qualifier': u'COCOS', u'expiration': u'2019-12-02T03:52:22', u'otcaccou
nt': u'1.2.6', u'id': u'4.3.7', u'world_view': u'test_common'}], 3]}

test_list_nh_asset_order done

.>> list_account_nh_asset ['nicotest', ['test_common'], 5, 1, 4]
{u'jsonrpc': u'2.0', u'id': 1, u'result': [[{u'base_describe': u'{k1:v1, k2:v2}', u'parent': [], u'limit_type': u'black_list', u'nh_asset_owner': u'1.2.16', u'nh_hash': u'2
800000000000000274c0c8a9173c4f7c282a31a790ca301e4f954c163f5f305', u'nh_asset_active': u'1.2.16', u'asset_qualifier': u'COCOS', u'dealership': u'1.2.16', u'create_time': u'2
019-12-01T03:00:08', u'limit_list': [], u'nh_asset_creator': u'1.2.16', u'child': [], u'describe_with_contract': [], u'id': u'4.2.40', u'world_view': u'test_common'}, {u'ba
se_describe': u'{k1:v1, k2:v2}', u'parent': [], u'limit_type': u'black_list', u'nh_asset_owner': u'1.2.16', u'nh_hash': u'2a00000000000000274c0c8a9173c4f7c282a31a790ca301e4
f954c163f5f305', u'nh_asset_active': u'1.2.16', u'asset_qualifier': u'COCOS', u'dealership': u'1.2.16', u'create_time': u'2019-12-01T03:00:52', u'limit_list': [], u'nh_asse
t_creator': u'1.2.16', u'child': [], u'describe_with_contract': [], u'id': u'4.2.42', u'world_view': u'test_common'}, {u'base_describe': u'{k1:v1, k2:v2}', u'parent': [], u
'limit_type': u'black_list', u'nh_asset_owner': u'1.2.16', u'nh_hash': u'2c00000000000000274c0c8a9173c4f7c282a31a790ca301e4f954c163f5f305', u'nh_asset_active': u'1.2.16', u
'asset_qualifier': u'COCOS', u'dealership': u'1.2.16', u'create_time': u'2019-12-01T03:04:52', u'limit_list': [], u'nh_asset_creator': u'1.2.16', u'child': [], u'describe_w
ith_contract': [], u'id': u'4.2.44', u'world_view': u'test_common'}, {u'base_describe': u'{k1:v1, k2:v2}', u'parent': [], u'limit_type': u'black_list', u'nh_asset_owner': u
'1.2.16', u'nh_hash': u'2e00000000000000274c0c8a9173c4f7c282a31a790ca301e4f954c163f5f305', u'nh_asset_active': u'1.2.16', u'asset_qualifier': u'COCOS', u'dealership': u'1.2
.16', u'create_time': u'2019-12-01T03:05:36', u'limit_list': [], u'nh_asset_creator': u'1.2.16', u'child': [], u'describe_with_contract': [], u'id': u'4.2.46', u'world_view
': u'test_common'}, {u'base_describe': u'{k1:v1, k2:v2}', u'parent': [], u'limit_type': u'black_list', u'nh_asset_owner': u'1.2.16', u'nh_hash': u'3000000000000000274c0c8a9
173c4f7c282a31a790ca301e4f954c163f5f305', u'nh_asset_active': u'1.2.16', u'asset_qualifier': u'COCOS', u'dealership': u'1.2.16', u'create_time': u'2019-12-01T03:13:58', u'l
imit_list': [], u'nh_asset_creator': u'1.2.16', u'child': [], u'describe_with_contract': [], u'id': u'4.2.48', u'world_view': u'test_common'}], 33]}

>> create_nh_asset_order [u'1.2.16', 'init1', '500', 'COCOS', u'4.2.40', '1500', 'COCOS', 'create_nh_asset_order test', '2019-12-02T03:52:29', 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [u'a34b30cb740844083ffcdba603017ac4f921a68156790b3f88aa46911d9cfd12', {u'ref_block_prefix': 294711135, u'operations': [[43, {u'pen
ding_orders_fee': {u'asset_id': u'1.3.0', u'amount': 50000000}, u'memo': u'create_nh_asset_order test', u'nh_asset': u'4.2.40', u'seller': u'1.2.16', u'expiration': u'2019-
12-02T03:52:29', u'otcaccount': u'1.2.6', u'price': {u'asset_id': u'1.3.0', u'amount': 150000000}}]], u'signatures': [u'1f6e78bc300f805aa0b8cfd6f6976054f1a394cf2e646d91c7af
f3e4f925c38c742a96f9750cfb389379446f1d9fbbcab8302a899547b60c08d5a7bf2c5ea5484d'], u'ref_block_num': 9472, u'extensions': [], u'expiration': u'2019-12-01T04:12:58'}]}

>> create_nh_asset_order [u'1.2.16', 'init1', '500', 'COCOS', u'4.2.42', '1500', 'COCOS', 'create_nh_asset_order test', '2019-12-02T03:52:29', 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [u'd957d945c355205622984e14010a9cfc7cd698cbb50d36cbf50ab7f2bf5beeed', {u'ref_block_prefix': 294711135, u'operations': [[43, {u'pen
ding_orders_fee': {u'asset_id': u'1.3.0', u'amount': 50000000}, u'memo': u'create_nh_asset_order test', u'nh_asset': u'4.2.42', u'seller': u'1.2.16', u'expiration': u'2019-
12-02T03:52:29', u'otcaccount': u'1.2.6', u'price': {u'asset_id': u'1.3.0', u'amount': 150000000}}]], u'signatures': [u'20278be23667dc749376db130fcd07322b3e2b8bcfdd7749e0fe
4a488a46d7e9fe136e4980a106f6125fa4af32017d42e0f5a0965946e582f19e71912dd061efee'], u'ref_block_num': 9472, u'extensions': [], u'expiration': u'2019-12-01T04:12:58'}]}

>> create_nh_asset_order [u'1.2.16', 'init1', '500', 'COCOS', u'4.2.44', '1500', 'COCOS', 'create_nh_asset_order test', '2019-12-02T03:52:29', 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [u'7c087865aae362db6a6d7d69982915b95e1a7a6090e4c68adddd9ee5cf1f0cb1', {u'ref_block_prefix': 294711135, u'operations': [[43, {u'pen
ding_orders_fee': {u'asset_id': u'1.3.0', u'amount': 50000000}, u'memo': u'create_nh_asset_order test', u'nh_asset': u'4.2.44', u'seller': u'1.2.16', u'expiration': u'2019-
12-02T03:52:29', u'otcaccount': u'1.2.6', u'price': {u'asset_id': u'1.3.0', u'amount': 150000000}}]], u'signatures': [u'2046df088ce2c5d93664c4ca6315b0594790a35a92f7564afae4
7fda75c58cd86416c95b139d13b0d7064b267f1571862b08901acc8164211d711e8fbff05a3b73'], u'ref_block_num': 9472, u'extensions': [], u'expiration': u'2019-12-01T04:12:58'}]}

>> create_nh_asset_order [u'1.2.16', 'init1', '500', 'COCOS', u'4.2.46', '1500', 'COCOS', 'create_nh_asset_order test', '2019-12-02T03:52:29', 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [u'767346864fd58bfd70cdd71e55ee6787ad2bb8095381f0618ca12420713f7b80', {u'ref_block_prefix': 294711135, u'operations': [[43, {u'pen
ding_orders_fee': {u'asset_id': u'1.3.0', u'amount': 50000000}, u'memo': u'create_nh_asset_order test', u'nh_asset': u'4.2.46', u'seller': u'1.2.16', u'expiration': u'2019-
12-02T03:52:29', u'otcaccount': u'1.2.6', u'price': {u'asset_id': u'1.3.0', u'amount': 150000000}}]], u'signatures': [u'2019607b49c1498bf1b84f2170e1477dc75542417717c7e57e8e
f2c8d422b97e3206f68883b838de4f93daf333e10bce097c8cc290b623747ae4ef11390104b867'], u'ref_block_num': 9472, u'extensions': [], u'expiration': u'2019-12-01T04:12:58'}]}

>> create_nh_asset_order [u'1.2.16', 'init1', '500', 'COCOS', u'4.2.48', '1500', 'COCOS', 'create_nh_asset_order test', '2019-12-02T03:52:29', 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [u'edc52fdf6d4cf1588f8503e2405a8aa7985ad6e26ef91fc46728fc3bc14cd0ca', {u'ref_block_prefix': 294711135, u'operations': [[43, {u'pen
ding_orders_fee': {u'asset_id': u'1.3.0', u'amount': 50000000}, u'memo': u'create_nh_asset_order test', u'nh_asset': u'4.2.48', u'seller': u'1.2.16', u'expiration': u'2019-
12-02T03:52:29', u'otcaccount': u'1.2.6', u'price': {u'asset_id': u'1.3.0', u'amount': 150000000}}]], u'signatures': [u'202234f5f63f78edfd78be4839d960d3c9c85c9274780b165ce2
52043cb6c5237850880bc088c71db6e52aaf5670c47d846b16a6da4453228f42425ae837c2667e'], u'ref_block_num': 9472, u'extensions': [], u'expiration': u'2019-12-01T04:12:58'}]}

test_nh_assert_order done

.ss>> lock []
{u'jsonrpc': u'2.0', u'id': 1, u'result': None}

tearDownClass done


----------------------------------------------------------------------
Ran 10 tests in 0.331s

OK (skipped=5)

'''