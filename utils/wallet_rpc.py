import re
import ssl
import websocket
import json
import time
import logging
from itertools import cycle

log = logging.getLogger(__name__)

class wallet_rpc(object):
    def __init__(self, urls, user="", password="", **kwargs):
        self._request_id = 0
        if isinstance(urls, list):
            self.urls = cycle(urls)
        else:
            self.urls = cycle([urls])
        self.user = user
        self.password = password
        self.num_retries = kwargs.get("num_retries", -1)

        self.wsconnect()

    def get_request_id(self):
        self._request_id += 1
        return self._request_id

    def wsconnect(self):
        cnt = 0
        while True:
            cnt += 1
            self.url = next(self.urls)
            log.debug("Trying to connect to node %s" % self.url)
            if self.url[:3] == "wss":
                sslopt_ca_certs = {'cert_reqs': ssl.CERT_NONE}
                self.ws = websocket.WebSocket(sslopt=sslopt_ca_certs)
            else:
                self.ws = websocket.WebSocket()
            try:
                self.ws.connect(self.url)
                break
            except KeyboardInterrupt:
                raise
            except:
                if (self.num_retries >= 0 and cnt > self.num_retries):
                    raise 

                sleeptime = (cnt - 1) * 2 if cnt < 10 else 10
                if sleeptime:
                    log.warning(
                        "Lost connection to node during wsconnect(): %s (%d/%d) "
                        % (self.url, cnt, self.num_retries) +
                        "Retrying in %d seconds" % sleeptime
                    )
                    time.sleep(sleeptime)


    """ RPC Calls
    """
    def rpc_exec(self, payload):
        """ Execute a call by sending the payload
            :param json payload: Payload data
        """
        log.debug(json.dumps(payload))
        cnt = 0
        while True:
            cnt += 1

            try:
                self.ws.send(json.dumps(payload, ensure_ascii=False).encode('utf8'))
                reply = self.ws.recv()
                break
            except KeyboardInterrupt:
                raise
            except:
                if (self.num_retries > -1 and
                        cnt > self.num_retries):
                    raise 
                sleeptime = (cnt - 1) * 2 if cnt < 10 else 10
                if sleeptime:
                    log.warning(
                        "Lost connection to node during rpc_exec(): %s (%d/%d) "
                        % (self.url, cnt, self.num_retries) +
                        "Retrying in %d seconds" % sleeptime
                    )
                    time.sleep(sleeptime)

                try:
                    self.ws.close()
                    time.sleep(sleeptime)
                    self.wsconnect()
                    self.register_apis()
                except:
                    pass

        ret = {}
        try:
            ret = json.loads(reply, strict=False)
        except ValueError:
            raise ValueError("Client returned invalid format. Expected JSON!")

        if 'error' in ret:
            raise Exception(ret["error"])
        else:
            return ret["result"]

    def __getattr__(self, name):
        """ Map all methods to RPC calls and pass through the arguments
        """
        def method(*args, **kwargs):

            query = {"method": name,
                     "params": list(args),
                     "jsonrpc": "2.0",
                     "id": self.get_request_id()}
            r = self.rpc_exec(query)
            print('>>>> {} {} \n {}'.format(query['method'], query['params'], r))
            return r
        return method

def test_wallet_api():
    # ws = "ws://127.0.0.1:8048" # 单节点
    ws = ["ws://127.0.0.1:8048"] # 多节点
    wallet_rpc_instance = wallet_rpc(ws)

    result = wallet_rpc_instance.info()
    print('info: {}\n'.format(result))

    result = wallet_rpc_instance.list_account_balances('nicotest')
    print('list_account_balances: {}\n'.format(result))

    result = wallet_rpc_instance.transfer('nicotest', 'test1', "100", "COCOS", ["test memo", 'false'], 'true')
    print('transfer: {}\n'.format(result))

    result = wallet_rpc_instance.get_account_history('nicotest', 3)
    print('get_account_history: {}\n'.format(result))
    
test_wallet_api()

'''
>>>> info [] 
 {'head_block_num': 35977, 'head_block_id': '00008c89e07b78f0e0fd23ebf17674c9c258c267', 'head_block_age': '9 seconds ago', 'next_maintenance_time': '41 minutes in the future', 'chain_id': '179db3c6a2e08d610f718f05e9cc2aabad62aff80305b9621b162b8b6f2fd79f', 'participation': '91.40625000000000000', 'active_witnesses': ['1.6.1', '1.6.2', '1.6.3', '1.6.4', '1.6.5', '1.6.6', '1.6.7', '1.6.8', '1.6.9', '1.6.10', '1.6.11'], 'active_committee_members': ['1.5.0', '1.5.1', '1.5.2', '1.5.3', '1.5.4', '1.5.5', '1.5.6', '1.5.7', '1.5.8', '1.5.9', '1.5.10']}
info: {'head_block_num': 35977, 'head_block_id': '00008c89e07b78f0e0fd23ebf17674c9c258c267', 'head_block_age': '9 seconds ago', 'next_maintenance_time': '41 minutes in the future', 'chain_id': '179db3c6a2e08d610f718f05e9cc2aabad62aff80305b9621b162b8b6f2fd79f', 'participation': '91.40625000000000000', 'active_witnesses': ['1.6.1', '1.6.2', '1.6.3', '1.6.4', '1.6.5', '1.6.6', '1.6.7', '1.6.8', '1.6.9', '1.6.10', '1.6.11'], 'active_committee_members': ['1.5.0', '1.5.1', '1.5.2', '1.5.3', '1.5.4', '1.5.5', '1.5.6', '1.5.7', '1.5.8', '1.5.9', '1.5.10']}

>>>> list_account_balances ['nicotest'] 
 [{'amount': '9677387512479481', 'asset_id': '1.3.0'}, {'amount': 742051714, 'asset_id': '1.3.1'}]
list_account_balances: [{'amount': '9677387512479481', 'asset_id': '1.3.0'}, {'amount': 742051714, 'asset_id': '1.3.1'}]

>>>> transfer ['nicotest', 'test1', '100', 'COCOS', ['test memo', 'false'], 'true'] 
 ['a2fd56961d5ed9cb92cd46af0be082df27613426591c89778fb7707968f3dddf', {'ref_block_num': 35969, 'ref_block_prefix': 3430375696, 'expiration': '2019-12-11T11:38:55', 'operations': [[0, {'from': '1.2.16', 'to': '1.2.17', 'amount': {'amount': 10000000, 'asset_id': '1.3.0'}, 'memo': [0, 'test memo'], 'extensions': []}]], 'extensions': [], 'signatures': ['1f308769e4685eae06b2d3c6567e2c5b64d194e83ddd1d6cb61ca50c03ff8282fd1e726e3462015aa854d90644b2a184b06cede93a8ad3ce5b044f91bcb644d6f2']}]
transfer: ['a2fd56961d5ed9cb92cd46af0be082df27613426591c89778fb7707968f3dddf', {'ref_block_num': 35969, 'ref_block_prefix': 3430375696, 'expiration': '2019-12-11T11:38:55', 'operations': [[0, {'from': '1.2.16', 'to': '1.2.17', 'amount': {'amount': 10000000, 'asset_id': '1.3.0'}, 'memo': [0, 'test memo'], 'extensions': []}]], 'extensions': [], 'signatures': ['1f308769e4685eae06b2d3c6567e2c5b64d194e83ddd1d6cb61ca50c03ff8282fd1e726e3462015aa854d90644b2a184b06cede93a8ad3ce5b044f91bcb644d6f2']}]

>>>> get_account_history ['nicotest', 3] 
 [{'memo': '', 'description': 'transfer_operation ', 'op': {'id': '1.11.1022', 'op': [0, {'from': '1.2.16', 'to': '1.2.17', 'amount': {'amount': 10000000, 'asset_id': '1.3.0'}, 'memo': [0, 'test memo'], 'extensions': []}], 'result': [1, {'fees': [{'amount': 2011718, 'asset_id': '1.3.1'}], 'real_running_time': 222}], 'block_num': 35960, 'trx_in_block': 0, 'op_in_trx': 0, 'virtual_op': 7}}, {'memo': '', 'description': 'update_collateral_for_gas_operation    result: 3.4.366', 'op': {'id': '1.11.1021', 'op': [54, {'mortgager': '1.2.16', 'beneficiary': '1.2.407', 'collateral': 4000000}], 'result': [2, {'fees': [{'amount': 100000, 'asset_id': '1.3.1'}], 'result': '3.4.366', 'real_running_time': 104}], 'block_num': 17108, 'trx_in_block': 2, 'op_in_trx': 0, 'virtual_op': 5}}, {'memo': '', 'description': 'transfer_operation ', 'op': {'id': '1.11.1020', 'op': [0, {'from': '1.2.16', 'to': '1.2.407', 'amount': {'amount': '10000000000', 'asset_id': '1.3.0'}, 'memo': [0, 'Welcome To COCOS Community!'], 'extensions': []}], 'result': [1, {'fees': [{'amount': 2029296, 'asset_id': '1.3.1'}], 'real_running_time': 74}], 'block_num': 17108, 'trx_in_block': 1, 'op_in_trx': 0, 'virtual_op': 4}}]
get_account_history: [{'memo': '', 'description': 'transfer_operation ', 'op': {'id': '1.11.1022', 'op': [0, {'from': '1.2.16', 'to': '1.2.17', 'amount': {'amount': 10000000, 'asset_id': '1.3.0'}, 'memo': [0, 'test memo'], 'extensions': []}], 'result': [1, {'fees': [{'amount': 2011718, 'asset_id': '1.3.1'}], 'real_running_time': 222}], 'block_num': 35960, 'trx_in_block': 0, 'op_in_trx': 0, 'virtual_op': 7}}, {'memo': '', 'description': 'update_collateral_for_gas_operation    result: 3.4.366', 'op': {'id': '1.11.1021', 'op': [54, {'mortgager': '1.2.16', 'beneficiary': '1.2.407', 'collateral': 4000000}], 'result': [2, {'fees': [{'amount': 100000, 'asset_id': '1.3.1'}], 'result': '3.4.366', 'real_running_time': 104}], 'block_num': 17108, 'trx_in_block': 2, 'op_in_trx': 0, 'virtual_op': 5}}, {'memo': '', 'description': 'transfer_operation ', 'op': {'id': '1.11.1020', 'op': [0, {'from': '1.2.16', 'to': '1.2.407', 'amount': {'amount': '10000000000', 'asset_id': '1.3.0'}, 'memo': [0, 'Welcome To COCOS Community!'], 'extensions': []}], 'result': [1, {'fees': [{'amount': 2029296, 'asset_id': '1.3.1'}], 'real_running_time': 74}], 'block_num': 17108, 'trx_in_block': 1, 'op_in_trx': 0, 'virtual_op': 4}}]
'''
