import re
import ssl
import websocket
import json
import time
import logging
from itertools import cycle

log = logging.getLogger(__name__)

class websocket_rpc(object):
    def __init__(self, urls, user="", password="", **kwargs):
        self.api_id = {}
        self._request_id = 0
        if isinstance(urls, list):
            self.urls = cycle(urls)
        else:
            self.urls = cycle([urls])
        self.user = user
        self.password = password
        self.num_retries = kwargs.get("num_retries", -1)

        self.wsconnect()
        self.register_apis()

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
        self.login(self.user, self.password, api_id=1)

    def register_apis(self):
        self.api_id["database"] = self.database(api_id=1)
        self.api_id["history"] = self.history(api_id=1)
        self.api_id["network_broadcast"] = self.network_broadcast(api_id=1)
        self.api_id["network_node"] = self.network_node(api_id=1)
        #network_node

        # self.ws = create_connection(node_ws_url)
        # req_data = {
        #     "id":1,
        #     "method":"call",
        #     "params":[1, "network_node", []]
        # }
        # # handle = ws_post(self.ws, req_data)['result']
        # response = self.rpc_exec(req_data)
        # self.api_id["network_node"] = self.rpc_exec(req_data)

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
            if "api_id" not in kwargs:
                if ("api" in kwargs):
                    if (kwargs["api"] in self.api_id and
                            self.api_id[kwargs["api"]]):
                        api_id = self.api_id[kwargs["api"]]
                    else:
                        raise ValueError(
                            "Unknown API! "
                            "Verify that you have registered to %s"
                            % kwargs["api"]
                        )
                else:
                    api_id = 0
            else:
                api_id = kwargs["api_id"]

            self.num_retries = kwargs.get("num_retries", self.num_retries)

            query = {"method": "call",
                     "params": [api_id, name, list(args)],
                     "jsonrpc": "2.0",
                     "id": self.get_request_id()}
            r = self.rpc_exec(query)
            # print('>>>> {} {} \n {}'.format(query['method'], query['params'], r))
            return r
        return method


class node_rpc(websocket_rpc):
    def __init__(self, *args, **kwargs):
        super(node_rpc, self).__init__(*args, **kwargs)

    def register_apis(self):
        self.api_id["database"] = self.database(api_id=1)
        self.api_id["history"] = self.history(api_id=1)
        self.api_id["network_broadcast"] = self.network_broadcast(api_id=1)
        self.api_id["network_node"] = self.network_node(api_id=1)

    def rpc_exec(self, payload):
        """ Execute a call by sending the payload.
            It makes use of the GrapheneRPC library.
            In here, we mostly deal with Graphene specific error handling
            :param json payload: Payload data
        """
        try:
            return super(node_rpc, self).rpc_exec(payload)
        except Exception as e:
            raise e

    def get_account(self, name, **kwargs):
        """ Get full account details from account name or id
            :param str name: Account name or account id
        """
        if len(name.split(".")) == 3:
            return self.get_objects([name])[0]
        else:
            return self.get_account_by_name(name, **kwargs)

    def get_asset(self, name, **kwargs):
        """ Get full asset from name of id
            :param str name: Symbol name or asset id (e.g. 1.3.0)
        """
        if len(name.split(".")) == 3:
            return self.get_objects([name], **kwargs)[0]
        else:
            return self.lookup_asset_symbols([name], **kwargs)[0]

    def get_object(self, o, **kwargs):
        """ Get object with id ``o``
            :param str o: Full object id
        """
        return self.get_objects([o], **kwargs)[0]
    

def test():
    # ws = "ws://127.0.0.1:8049"
    ws = "ws://test.cocosbcx.net"
    # ws = "wss://api.cocosbcx.net"
    node_rpc_instance = node_rpc(ws)

    result = node_rpc_instance.get_object('1.2.0')
    print('get_object: {}\n'.format(result))

    result = node_rpc_instance.get_account('test1')
    print('get_account: {}\n'.format(result))

    result = node_rpc_instance.get_asset('1.3.0')
    print('get_asset: {}\n'.format(result))

    result = node_rpc_instance.get_asset('GAS')
    print('get_asset: {}\n'.format(result))

    result = node_rpc_instance.get_block('100')
    print('get_block: {}\n'.format(result))

    result = node_rpc_instance.get_dynamic_global_properties()
    print('get_dynamic_global_properties: {}\n'.format(result))

    result = node_rpc_instance.get_account_balances("1.2.15", ["1.3.1", "1.3.0"])
    print('get_account_balances: {}\n'.format(result))

    #get_account_history
    stop = "1.11.500"
    limit = 10
    start = "1.11.5"
    result = node_rpc_instance.get_account_history("1.2.15", stop, limit, start, api="history")
    print('get_account_history: {}\n'.format(result))

    result = node_rpc_instance.get_info(api="network_node")
    print('get_info: {}\n'.format(result))

    result = node_rpc_instance.get_connected_peers(api="network_node")
    print('get_connected_peers: {}\n'.format(result))

test()

