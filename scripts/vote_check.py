
#-*- coding: utf-8  -*-

import sys
import json
import requests

urls = {
    "default": "https://api.cocosbcx.net", #
    # "node1": "http://127.0.0.1:8049"
}

headers = {"content-type": "application/json"}

def request_post(url, req_data, is_assert=True):
    response = json.loads(requests.post(url, data = json.dumps(req_data), headers = headers).text)
    # print('>> {} {}\n{}\n'.format(req_data['method'], req_data['params'], response))
    print('>> {} {}\n'.format(req_data['method'], req_data['params']))
    if is_assert:
        assert 'error' not in response
    return response

###################### class Vote Object
class VoteObj(object):
    def __init__(self, obj, is_witness):
        self.id = obj["id"]
        self.url = obj["url"]
        self.vote_id = obj["vote_id"]
        self.supporters = obj["supporters"]
        if is_witness:
            self.account = obj["witness_account"]
        else:
            self.account = obj["committee_member_account"]
        self.total_votes = obj["total_votes"]
        self.work_status = obj["work_status"]

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

##########################

# curl https://api.cocosbcx.net -d '{"id":1, "method": "call", "params": [0, "get_witnesses", [["1.6.23"]]]}' && echo ""
# curl http://127.0.0.1:8049 -d '{"id":1, "method": "call", "params": [0, "get_witnesses", [["1.6.23"]]]}' && echo ""
def get_node_witness(url, witnesses=["1.6.1", "1.6.2"]):
    req_data = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": [0, "get_witnesses", [witnesses]],
        "id":1
    }
    return request_post(url, req_data)["result"]

def get_node_committee_members(url, members=["1.5.1", "1.5.2"]):
    req_data = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": [0, "get_committee_members", [members]],
        "id":1
    }
    return request_post(url, req_data)["result"]

# curl https://api.cocosbcx.net -d '{"id":1, "method":"call", "params":[0,"get_global_properties",[]]}' && echo ""
def get_global_properties():
    url = urls["default"]
    req_data = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": [0, "get_global_properties", []],
        "id":1
    }
    return request_post(url, req_data)["result"]

def get_witnesses_votes(url, witnesses=[]):
    witnesses_data = get_node_witness(url, witnesses)
    votes = {}
    for witness in witnesses_data:
        # print(witness)
        votes[witness["id"]] = VoteObj(witness, True)
    return votes

def get_committee_members_votes(url, members=[]):
    witnesses_data = get_node_committee_members(url, members)
    votes = {}
    for committee in witnesses_data:
        # print(committee)
        votes[committee["id"]] = VoteObj(committee, False)
    return votes

def compare_witness_vote():
    active_witnesses = get_global_properties()["active_witnesses"]
    results = {}
    for key, url in  urls.items():
        results[key] = get_witnesses_votes(url, active_witnesses)
    print(results)

def compare_committee_members_vote():
    active_committee_members = get_global_properties()["active_committee_members"]
    results = {}
    for key, url in urls.items():
        results[key] = get_committee_members_votes(url, active_committee_members)
    print(results)

def vote_check():
    compare_witness_vote()
    compare_committee_members_vote()

def main():
    vote_check()

if __name__ == '__main__':
    print('>> {}\n'.format(sys.argv))
    main()


