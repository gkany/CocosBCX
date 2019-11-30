#-*- coding: utf-8  -*-

import unittest
from utils import *
from chain_param import restricted_enum
from config import *

import sys

class test_wallet_asset_api(request_unittest):
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

        #init new_asset_symbol
        tokens = generate_random_words()
        self.new_asset_symbol = tokens[0]
        self.new_bitasset_symbol = tokens[1]
        print('new_asset_symbol: {}, new_bitasset_symbol: {}'.format(self.new_asset_symbol, self.new_bitasset_symbol))

        # register feeder account
        new_account = "feeder"
        req_data = {
            "jsonrpc": "2.0",
            "method": "get_account",
            "params": [new_account],
            "id":1
        }
        response = request_post(req_data, is_assert=False)
        if  'error' in response:
            print('### register feeder account: {}'.format(new_account))
            register = test_account
            req_data = {
                "jsonrpc": "2.0",
                "method": "register_account",
                "params": [new_account, test_account_public_key, test_account_public_key, register, 'true'],
                "id":1
            }
            request_post(req_data)
            # request_post(req_data, False)
            req_data = {
                "jsonrpc": "2.0",
                "method": "import_key",
                "params": [new_account, test_account_private_key],
                "id":1
            }
            request_post(req_data)
            req_data = {
                "jsonrpc": "2.0",
                "method": "transfer",
                "params": [test_account, new_account, 1000000, core_asset, "init feeder balance", 'true'],
                "id":1
            }
            request_post(req_data)
        self.feeder = new_account

        #feed asset
        self.feed_asset = "STEEM"
        # result = get_asset_if_not_create(self.feed_asset, True)
        # print('###### asset: {}'.format(result))
        get_asset_if_not_create(self.feed_asset, True)
        req_data = {
            "jsonrpc": "2.0",
            "method": "get_asset",
            "params": [self.feed_asset],
            "id":1
        }
        asset = request_post(req_data)['result']
        self.feed_asset_id = asset['id']
        self.feed_asset_dynamic_asset_data_id = asset['dynamic_asset_data_id']
        self.feed_asset_bitasset_data_id = asset['bitasset_data_id']
        print('####feed asset| symbol: {}, asset_id: {}, dynamic_asset_data_id: {} bitasset_data_id: {}'.format(
            self.feed_asset, self.feed_asset_id, self.feed_asset_dynamic_asset_data_id, 
            self.feed_asset_bitasset_data_id))

        print('setUpClass done.')

    @classmethod
    def tearDownClass(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "lock",
            "params": [],
            "id":1
        }
        request_post(req_data)
        print('tearDownClass done.')

    @unittest.skipIf(True, 'test other')
    def test_list_assets(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_assets",
            "params": ["", 3],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    @unittest.skipIf(True, 'test other')
    def test_get_asset(self):
        symbols = ["COCOS", "GAS"]
        for symbol in symbols:
            req_data = {
                "jsonrpc": "2.0",
                "method": "get_asset",
                "params": [symbol],
                "id":1
            }
            self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))  

    @unittest.skipIf(True, 'test other')
    def test_list_asset_restricted_objects(self):
        asset_id_list = []
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_assets",
            "params": ["", 3],
            "id":1
        }
        assets = self.request_post(req_data)['result']
        for asset in assets:
            asset_id_list.append(asset['id'])
        print('asset_id_list: {}'.format(asset_id_list))

        for asset in asset_id_list:
            for index in range(0, len(restricted_enum)):
                req_data = {
                    "jsonrpc": "2.0",
                    "method": "list_asset_restricted_objects",
                    "params": [asset, index],
                    "id":1
                }
                self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    # # create_asset nicotest NODE 8  {"max_supply":"2100000000000000","market_fee_percent":0,"max_market_fee":0,"flags":0,"core_exchange_rate":{"base":{"amount":1,"asset_id":"1.3.4"},"quote":{"amount":1,"asset_id":"1.3.0"}},"description":"","extensions":[]} null true
    # # create asset: params: [issuer, symbol, precision, asset_options, bitasset_opts, broadcast]

    # >> get_asset [u'AUTONYM']
    # {u'jsonrpc': u'2.0', u'id': 1, u'result': {u'symbol': u'AUTONYM', u'precision': 5, u'id': u'1.3.2', u'options': {u'issuer_permissions': 15, u'description': u'', u'max_market_fee': 0, u'max_supply': u'2100000000000000', u'flags': 0, u'extensions': [], u'market_fee_percent': 0, u'core_exchange_rate': {u'quote': {u'asset_id': u'1.3.0', u'amount': 1}, u'base': {u'asset_id': u'1.3.2', u'amount': 1}}}, u'dynamic_asset_data_id': u'2.3.2', u'issuer': u'1.2.16'}}
    @unittest.skipIf(True, 'test other')
    def test_create_asset(self):
        precision = 5
        asset_opts = {
            "max_supply":"2100000000000000",
            "market_fee_percent":0,
            "max_market_fee":0,
            "flags":0,
            "core_exchange_rate":{
                "base":{"amount":1,"asset_id":"1.3.3"},
                "quote":{"amount":1,"asset_id":"1.3.0"}
            },
            "description":"",
            "extensions":[]
        }
        req_data = {
            "jsonrpc": "2.0",
            "method": "create_asset",
            "params": [test_account, self.new_asset_symbol, precision, asset_opts, None, 'true'],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
                "jsonrpc": "2.0",
                "method": "get_asset",
                "params": [self.new_asset_symbol],
                "id":1
            }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    # create asset: params: [issuer, symbol, precision, asset_options, bitasset_opts, broadcast]
    # create_asset testbit STEEM 5 {"issuer_permissions": 511,"flags": 0,"core_exchange_rate":{"base":{"amount":1,"asset_id":"1.3.10"},"quote":{"amount":1,"asset_id":"1.3.0"}}} {"new_feed_producers":[],"feed_lifetime_sec":120} true
    #     >> get_asset [u'NOXIOUS']
    # {u'jsonrpc': u'2.0', u'id': 1, u'result': {u'symbol': u'NOXIOUS', u'precision': 5, u'id': u'1.3.3', u'bitasset_data_id': u'2.4.0', u'options': {u'issuer_permissions': 511, u'description': u'', u'max_market_fee': u'1000000000000000000', u'max_supply': u'1000000000000000000', u'flags': 0, u'extensions': [], u'market_fee_percent': 0, u'core_exchange_rate': {u'quote': {u'asset_id': u'1.3.0', u'amount': 1}, u'base': {u'asset_id': u'1.3.3', u'amount': 1}}}, u'dynamic_asset_data_id': u'2.3.3', u'issuer': u'1.2.16'}}

    @unittest.skipIf(True, 'test other')
    def test_create_bitasset(self):
        precision = 5
        asset_opts = {
            "issuer_permissions": 511,
            "flags": 0,
            "core_exchange_rate":{
                "base":{"amount":1,"asset_id":"1.3.4"},
                "quote":{"amount":1,"asset_id":"1.3.0"}
            }
        }
        bitasset_opts = {
            "new_feed_producers":[],
            "feed_lifetime_sec":120
        }
        req_data = {
            "jsonrpc": "2.0",
            "method": "create_asset",
            "params": [test_account, self.new_bitasset_symbol, precision, asset_opts, bitasset_opts, 'true'],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
                "jsonrpc": "2.0",
                "method": "get_asset",
                "params": [self.new_bitasset_symbol],
                "id":1
            }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))

    #get_market_history(string symbol1, string symbol2, uint32_t bucket, fc::time_point_sec start, fc::time_point_sec end)
    @unittest.skipIf(True, 'test other')
    def test_get_market_history(self):
        base_quote_list = []  #base:quote
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_assets",
            "params": ["", 10],
            "id":1
        }
        assets = self.request_post(req_data)['result']
        for asset in assets:
            options = asset['options']
            if 'core_exchange_rate' in options:
                base_asset_id = options['core_exchange_rate']['base']['asset_id']
                quote_asset_id = options['core_exchange_rate']['quote']['asset_id']
                base_quote_list.append([base_asset_id, quote_asset_id])
        print('asset_id_list: {}'.format(base_quote_list))

        bucket = 86400
        start = datetime_N_ago(14).strftime("%Y-%m-%dT%H:%M:%S")
        # end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        end = datetime_N_ago(0).strftime("%Y-%m-%dT%H:%M:%S")
        for base_quote in base_quote_list:
            req_data = {
                "jsonrpc": "2.0",
                "method": "get_market_history",
                "params": [base_quote[0], base_quote[1], bucket, start, end],
                "id":1
            }
            self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))  

    # get_order_book(const string &base, const string &quote, unsigned limit)
    @unittest.skipIf(True, 'test other')
    def test_get_order_book(self):
        base_quote_list = []  #base:quote
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_assets",
            "params": ["", 10],
            "id":1
        }
        assets = self.request_post(req_data)['result']
        for asset in assets:
            options = asset['options']
            if 'core_exchange_rate' in options:
                base_asset_id = options['core_exchange_rate']['base']['asset_id']
                quote_asset_id = options['core_exchange_rate']['quote']['asset_id']
                base_quote_list.append([base_asset_id, quote_asset_id])
        print('asset_id_list: {}'.format(base_quote_list))

        limit = 20
        for base_quote in base_quote_list:
            req_data = {
                "jsonrpc": "2.0",
                "method": "get_order_book",
                "params": [base_quote[0], base_quote[1], 20],
                "id":1
            }
            self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))  

    @unittest.skipIf(False, 'test other')
    def test_get_limit_orders(self):
        base_quote_list = []  #base:quote
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_assets",
            "params": ["", 10],
            "id":1
        }
        assets = self.request_post(req_data)['result']
        for asset in assets:
            options = asset['options']
            if 'core_exchange_rate' in options:
                base_asset_id = options['core_exchange_rate']['base']['asset_id']
                quote_asset_id = options['core_exchange_rate']['quote']['asset_id']
                base_quote_list.append([base_asset_id, quote_asset_id])
        print('asset_id_list: {}'.format(base_quote_list))

        limit = 10
        for base_quote in base_quote_list:
            req_data = {
                "jsonrpc": "2.0",
                "method": "get_limit_orders",
                "params": [base_quote[0], base_quote[1], 20],
                "id":1
            }
            self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))  

    @unittest.skipIf(True, 'test other')
    def test_get_call_orders(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_assets",
            "params": ["", 10],
            "id":1
        }
        assets = self.request_post(req_data)['result']
        limit = 10
        for asset in assets:
            if 'bitasset_data_id' in asset:
                req_data = {
                    "jsonrpc": "2.0",
                    "method": "get_call_orders",
                    "params": [asset['symbol'], limit],
                    "id":1
                }
                self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))  

    @unittest.skipIf(True, 'test other')
    def test_get_settle_orders(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_assets",
            "params": ["", 10],
            "id":1
        }
        assets = self.request_post(req_data)['result']
        limit = 10
        for asset in assets:
            req_data = {
                "jsonrpc": "2.0",
                "method": "get_settle_orders",
                "params": [asset['symbol'], limit],
                "id":1
            }
            self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))  

    def test_get_bitasset_data(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "list_assets",
            "params": ["", 10],
            "id":1
        }
        assets = self.request_post(req_data)['result']
        for asset in assets:
            if 'bitasset_data_id' in asset:
                req_data = {
                    "jsonrpc": "2.0",
                    "method": "get_bitasset_data",
                    "params": [asset['symbol']],
                    "id":1
                }
                self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))  

# (get_limit_orders)(get_call_orders)(get_settle_orders)
# (get_market_history) (get_order_book)
# (list_assets)(list_asset_restricted_objects)
# (get_asset)(get_bitasset_data)
# (create_asset)(update_asset)(update_bitasset)(issue_asset)(reserve_asset)
#(borrow_asset)(update_asset_feed_producers)(publish_asset_feed)(global_settle_asset)


# (asset_update_restricted_list)

# (sell_asset)(sell)(buy)(cancel_order)

# (settle_asset)(bid_collateral)

# update_asset(symbol, new_issuer, new_options, broadcast)
# update_asset 1.3.4 test1 {"core_exchange_rate":{"base":{"amount":1,"asset_id":"1.3.4"},"quote":{"amount":1,"asset_id":"1.3.0"}}} true
    @unittest.skipIf(True, 'test other')
    def test_update_asset(self):
        asset = get_asset_if_not_create(test_default_asset)
        # print('###### asset: {}'.format(asset))
        asset_opts = asset['options']
        asset_opts['core_exchange_rate']['quote']['amount'] = 8
        req_data = {
            "jsonrpc": "2.0",
            "method": "update_asset",
            "params": [asset['symbol'], None, asset_opts, 'true'],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))  

    # update_bitasset(symbol, new_options, broadcast)
    @unittest.skipIf(True, 'test other')
    def test_update_bitasset(self):
        asset = get_asset_if_not_create(test_default_bitasset, True)
        print('###### asset: {}'.format(asset))
        req_data = {
            "jsonrpc": "2.0",
            "method": "get_object",
            "params": [asset['bitasset_data_id']],
            "id":1
        }
        response = self.request_post(req_data)
        bitasset_data = response['result']
        # print('##### bitasset_data: {}'.format(bitasset_data))
        bitasset_opts = bitasset_data[0]['options']
        # print('##### bitasset_opts: {}'.format(bitasset_opts))
        bitasset_opts["feed_lifetime_sec"] = bitasset_opts["feed_lifetime_sec"] + 30
        req_data = {
            "jsonrpc": "2.0",
            "method": "update_bitasset",
            "params": [asset['symbol'], bitasset_opts, 'true'],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))  

    #issue_asset nicotest  10000 NODE "test issue asset" true
    def test_issue_asset(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "issue_asset",
            "params": [test_account, 100, test_default_asset, "issue_asset test", 'true'],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "list_account_balances",
            "params": [test_account],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))  

    @unittest.skipIf(True, 'test other')
    def test_reserve_asset(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "reserve_asset",
            "params": [test_account, 20, test_default_asset, 'true'],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "list_account_balances",
            "params": [test_account],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))  

    @unittest.skipIf(True, 'need feed price')
    def test_borrow_asset(self):
        req_data = {
            "jsonrpc": "2.0",
            "method": "borrow_asset",
            "params": [test_account, 20, test_default_bitasset, 'true'],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "list_account_balances",
            "params": [test_account],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))  

    # sell_asset nicotest 100 NODE 1000 COCOS  1800 false true
    @unittest.skipIf(False, 'test other')
    def test_sell_asset(self):
        amount = 20
        timeout = 3600
        fill_or_kill = 'false'
        req_data = {
            "jsonrpc": "2.0",
            "method": "sell_asset",
            "params": [test_account, amount, test_default_asset, amount*2, core_asset, timeout, fill_or_kill, 'true'],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
                "jsonrpc": "2.0",
                "method": "get_limit_orders",
                "params": [test_default_asset, core_asset, 20],
                "id":1
            }
        orders = self.request_post(req_data)['result']

        index = 0
        for order in orders:
            if index % 2 == 0:
                # print('### settle_asset: {}'.format(order))
                # req_data = {
                #     "jsonrpc": "2.0",
                #     "method": "settle_asset",
                #     "params": [order['id'], 'true'],
                #     "id":1
                # }
                # self.request_post(req_data)
                pass
            else:
                print("### cancel_order: {}".format(order))
                req_data = {
                    "jsonrpc": "2.0",
                    "method": "cancel_order",
                    "params": [order['id'], 'true'],
                    "id":1
                }
                self.request_post(req_data)
            index = index+1

        print('{} done\n'.format(sys._getframe().f_code.co_name))  

    @unittest.skipIf(True, 'test other')
    def test_feed(self):
        #update_asset_feed_producers 1.3.10 ["feeder"] true
        req_data = {
            "jsonrpc": "2.0",
            "method": "update_asset_feed_producers",
            "params": [self.feed_asset_id, [self.feeder], 'true'],
            "id":1
        }
        self.request_post(req_data)

        feed_price =  {
            "settlement_price":{ 
                "base":{"amount":5,"asset_id": self.feed_asset_id},
                "quote":{"amount":10,"asset_id":"1.3.0"}
            },
            "core_exchange_rate":{
                "base":{"amount":100,"asset_id":self.feed_asset_id},
                "quote":{"amount":2,"asset_id":"1.3.0"}
            }
        }
        req_data = {
            "jsonrpc": "2.0",
            "method": "publish_asset_feed",
            "params": [self.feeder, self.feed_asset_id, feed_price, 'true'],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "get_bitasset_data",
            "params": [self.feed_asset],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "get_object",
            "params": [self.feed_asset_dynamic_asset_data_id],
            "id":1
        }
        self.request_post(req_data)

        # borrow_asset nicotest  50 STEEM  1500 true
        req_data = {
            "jsonrpc": "2.0",
            "method": "borrow_asset",
            "params": [test_witness_account, 100, self.feed_asset, 1000, 'true'],
            "id":1
        }
        self.request_post(req_data)

        req_data = {
            "jsonrpc": "2.0",
            "method": "get_object",
            "params": [self.feed_asset_dynamic_asset_data_id],
            "id":1
        }
        self.request_post(req_data)

        settle_price = {
            "base":{"amount":5,"asset_id": self.feed_asset_id},
            "quote":{"amount":20,"asset_id":"1.3.0"}
        }
        req_data = {
            "jsonrpc": "2.0",
            "method": "global_settle_asset",
            "params": [self.feed_asset, settle_price, 'true'],
            "id":1
        }
        self.request_post(req_data)
        print('{} done\n'.format(sys._getframe().f_code.co_name))  

if __name__ == "__main__":
    unittest.main()


'''
##### test_feed的一次测试数据:

root@7ef1cba5083e:~/data/repo/scripts/chain/wallet_api_test# python t06_asset.py 
>> unlock ['123456']
{u'jsonrpc': u'2.0', u'id': 1, u'result': None}

>> import_key ['nicotest', '5J2SChqa9QxrCkdMor9VC2k9NT4R4ctRrJA6odQCPkb3yL89vxo']
{u'jsonrpc': u'2.0', u'id': 1, u'result': True}

>> import_key ['init1', '5K5fqjvMrH5UtUisCgSZHQjiQf9BvtZ5vsKPhCErDy7P2gnLQmw']
{u'jsonrpc': u'2.0', u'id': 1, u'result': True}

new_asset_symbol: BALE, new_bitasset_symbol: BASIFY
>> get_account ['feeder']
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'statistics': u'2.6.65', u'name': u'feeder', u'options': {u'memo_key': u'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', u'extensions': [], u'votes': []}, u'active': {u'weight_threshold': 1, u'account_auths': [], u'key_auths': [[u'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]], u'address_auths': []}, u'registrar': u'1.2.16', u'asset_locked': {u'contract_lock_details': [], u'locked_total': []}, u'owner': {u'weight_threshold': 1, u'account_auths': [], u'key_auths': [[u'COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx', 1]], u'address_auths': []}, u'membership_expiration_date': u'1970-01-01T00:00:00', u'id': u'1.2.65'}}

[get_asset_if_not_create] symbol: STEEM
>> get_asset ['STEEM']
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'symbol': u'STEEM', u'precision': 5, u'id': u'1.3.6', u'bitasset_data_id': u'2.4.2', u'options': {u'issuer_permissions': 511, u'description': u'', u'max_market_fee': u'1000000000000000000', u'max_supply': u'1000000000000000000', u'flags': 0, u'extensions': [], u'market_fee_percent': 0, u'core_exchange_rate': {u'quote': {u'asset_id': u'1.3.0', u'amount': 1}, u'base': {u'asset_id': u'1.3.6', u'amount': 1}}}, u'dynamic_asset_data_id': u'2.3.6', u'issuer': u'1.2.16'}}

>> get_asset ['STEEM']
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'symbol': u'STEEM', u'precision': 5, u'id': u'1.3.6', u'bitasset_data_id': u'2.4.2', u'options': {u'issuer_permissions': 511, u'description': u'', u'max_market_fee': u'1000000000000000000', u'max_supply': u'1000000000000000000', u'flags': 0, u'extensions': [], u'market_fee_percent': 0, u'core_exchange_rate': {u'quote': {u'asset_id': u'1.3.0', u'amount': 1}, u'base': {u'asset_id': u'1.3.6', u'amount': 1}}}, u'dynamic_asset_data_id': u'2.3.6', u'issuer': u'1.2.16'}}

####feed asset| symbol: STEEM, asset_id: 1.3.6, dynamic_asset_data_id: 2.3.6 bitasset_data_id: 2.4.2
setUpClass done.
sss>> update_asset_feed_producers [u'1.3.6', ['feeder'], 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [u'98b82b99ec399e3467b875d9f3008b090130e241e442626c02eb9661abec012a', {u'ref_block_prefix': 3918618374, u'operations': [[12, {u'new_feed_producers': [u'1.2.65'], u'asset_to_update': u'1.3.6', u'extensions': [], u'issuer': u'1.2.16'}]], u'signatures': [u'2011b60de6cf691bc72a9b97bcc71c55cc0f53f9cd274a110908539c8ba348d24d0a83050cc23e4f871e67bcfd7ed012d641dfab2eeb3d85df43cb96a6f04c1061'], u'ref_block_num': 42951, u'extensions': [], u'expiration': u'2019-11-29T12:10:26'}]}

>> publish_asset_feed ['feeder', u'1.3.6', {'settlement_price': {'quote': {'asset_id': '1.3.0', 'amount': 10}, 'base': {'asset_id': u'1.3.6', 'amount': 5}}, 'core_exchange_rate': {'quote': {'asset_id': '1.3.0', 'amount': 2}, 'base': {'asset_id': u'1.3.6', 'amount': 100}}}, 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [u'2240c914ddbce1b1c86ef1c641f9ce970877a786b9b7719c4ff49728f67e3816', {u'ref_block_prefix': 3918618374, u'operations': [[17, {u'asset_id': u'1.3.6', u'publisher': u'1.2.65', u'extensions': [], u'feed': {u'maximum_short_squeeze_ratio': 1500, u'settlement_price': {u'quote': {u'asset_id': u'1.3.0', u'amount': 10}, u'base': {u'asset_id': u'1.3.6', u'amount': 5}}, u'maintenance_collateral_ratio': 1750}}]], u'signatures': [u'1f4a2d759d08c1b3b982e585e814e94cca03ddf4fb6f58c9a01ad36022c7763d7379d2803b14085ede9406c931c2971d9011f93aeb572d455fa1a9c191e20103a2'], u'ref_block_num': 42951, u'extensions': [], u'expiration': u'2019-11-29T12:10:26'}]}

>> get_bitasset_data ['STEEM']
{u'jsonrpc': u'2.0', u'id': 1, u'result': {u'current_feed_publication_time': u'2019-11-29T11:49:56', u'settlement_price': {u'quote': {u'asset_id': u'1.3.0', u'amount': 0}, u'base': {u'asset_id': u'1.3.0', u'amount': 0}}, u'force_settled_volume': 0, u'settlement_fund': 0, u'options': {u'minimum_feeds': 1, u'force_settlement_delay_sec': 86400, u'force_settlement_offset_percent': 0, u'extensions': [], u'feed_lifetime_sec': 120, u'maximum_force_settlement_volume': 2000, u'short_backing_asset': u'1.3.0'}, u'feeds': [[u'1.2.65', [u'2019-11-29T11:49:56', {u'maximum_short_squeeze_ratio': 1500, u'settlement_price': {u'quote': {u'asset_id': u'1.3.0', u'amount': 10}, u'base': {u'asset_id': u'1.3.6', u'amount': 5}}, u'maintenance_collateral_ratio': 1750}]]], u'id': u'2.4.2', u'current_feed': {u'maximum_short_squeeze_ratio': 1500, u'settlement_price': {u'quote': {u'asset_id': u'1.3.0', u'amount': 10}, u'base': {u'asset_id': u'1.3.6', u'amount': 5}}, u'maintenance_collateral_ratio': 1750}}}

>> get_object [u'2.3.6']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [{u'current_supply': 10000000, u'accumulated_fees': 0, u'id': u'2.3.6'}]}

>> borrow_asset ['init1', 100, 'STEEM', 1000, 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [u'4cb2bc9725b79a5c3cfc648510d2994feb9ff420ea01377da85055d001579a5a', {u'ref_block_prefix': 3918618374, u'operations': [[3, {u'funding_account': u'1.2.6', u'delta_debt': {u'asset_id': u'1.3.6', u'amount': 10000000}, u'extensions': [], u'delta_collateral': {u'asset_id': u'1.3.0', u'amount': 100000000}}]], u'signatures': [u'207311002d80981a208128dee5c66aa533f66ae720006a8c2ef7ea18df654d75927cb4135d94cc6d731493b19f5435d2102c11dbddd9df20e3f0506dd32a0ee9f7'], u'ref_block_num': 42951, u'extensions': [], u'expiration': u'2019-11-29T12:10:26'}]}

>> get_object [u'2.3.6']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [{u'current_supply': 20000000, u'accumulated_fees': 0, u'id': u'2.3.6'}]}

>> global_settle_asset ['STEEM', {'quote': {'asset_id': '1.3.0', 'amount': 20}, 'base': {'asset_id': u'1.3.6', 'amount': 5}}, 'true']
{u'jsonrpc': u'2.0', u'id': 1, u'result': [u'282a9b75558dfd596f15559f8772b3bb096c2e5b3d815a54826d56bdaa87f54d', {u'ref_block_prefix': 3918618374, u'operations': [[16, {u'settle_price': {u'quote': {u'asset_id': u'1.3.0', u'amount': 20}, u'base': {u'asset_id': u'1.3.6', u'amount': 5}}, u'extensions': [], u'asset_to_settle': u'1.3.6', u'issuer': u'1.2.16'}]], u'signatures': [u'1f6366c7b25fb85dde073024239d4a76ca6485eabeac6160d8a6d6a5b7591c4a0b047e0a03981833c08c9c83f868839b308e6c2a139262eb103d6a8aec70ee75ea'], u'ref_block_num': 42951, u'extensions': [], u'expiration': u'2019-11-29T12:10:26'}]}
'''

