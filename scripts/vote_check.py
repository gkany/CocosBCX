#-*- coding: utf-8  -*-

import sys
import json
import requests
import operator

node_rpc_urls = {
    "mainnet-fn": "https://api.cocosbcx.net", #
    "test-node-release8543": "http://127.0.0.1:8543",
    "test-node-release8249": "http://127.0.0.1:8249"
}

headers = {"content-type": "application/json"}

def request_post(url, req_data, is_assert=True):
    response = json.loads(requests.post(url, data = json.dumps(req_data), headers = headers).text)
    # print('>> {} {}\n{}\n'.format(req_data['method'], req_data['params'], response))
    print('>>{} {} from {}\n'.format(req_data['method'], req_data['params'], url))
    if is_assert:
        assert 'error' not in response
    return response

###################### class Vote Object
class VoteObj(object):
    def __init__(self, obj, is_witness):
        self.id = obj["id"]
        self.url = obj["url"]
        self.vote_id = obj["vote_id"]
        self.supporters = {}
        for supporter in obj["supporters"]:
            self.supporters[supporter[0]] = supporter[1]

        if is_witness:
            self.account = obj["witness_account"]
        else:
            self.account = obj["committee_member_account"]
        self.total_votes = obj["total_votes"]
        self.work_status = obj["work_status"]

    def __eq__(self, other):
        return operator.eq(self.__dict__, other.__dict__)

    def show_supporters_different(self, other):
        print("basic data: \n{}\n{}".format(self, other))
        other_supporters = other.supporters
        different = {}
        for id, vote in self.supporters.items():
            other_vote = None
            if id in other_supporters.keys():
                other_vote = other_supporters[id]
            if not operator.eq(vote, other_vote):
                different[id] = [vote, other_vote]
        print("votes detail different: \n", different)

    def __str__(self):
        #return "id:{}, url:{}, vote_id:{}, account:{}, total_votes:{}, work_status:{}, supporters:{}".format(
        #        self.id, self.url, self.vote_id, self.account, self.total_votes, self.work_status, self.supporters)
        return "id:{}, url:{}, vote_id:{}, account:{}, total_votes:{}, work_status:{}".format(
                self.id, self.url, self.vote_id, self.account, self.total_votes, self.work_status)

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
    url = None
    for value in node_rpc_urls.values():
        url = value
        break
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
        votes[witness["id"]] = VoteObj(witness, True)
        #if witness["id"] == "1.6.23":
        #    print(url, witness)
    return votes

def get_committee_members_votes(url, members=[]):
    witnesses_data = get_node_committee_members(url, members)
    votes = {}
    for committee in witnesses_data:
        votes[committee["id"]] = VoteObj(committee, False)
    return votes

def compare_witness_vote():
    active_witnesses = get_global_properties()["active_witnesses"]
    results = {}
    for key, url in node_rpc_urls.items():
        results[key] = get_witnesses_votes(url, active_witnesses)
    last_key = None
    last_votes = None
    diffent = {}
    for key, votes in results.items():
        if not last_votes:
            last_key = key
            last_votes = votes
            continue
        diffent_ids = []
        for id, vote_obj in votes.items():
            last_vote = last_votes[id]
            if not vote_obj == last_vote:
                print("\n>>> node {} and {} witness {} votes diffenent: ".format(last_key, key, id))
                vote_obj.show_supporters_different(last_vote)
                diffent_ids.append(id)
        if diffent_ids:
            diffent_key = last_key + "--" + key
            diffent[diffent_key] = diffent_ids
        print("\ncompare node active_witness votes: {} and {} done.".format(last_key, key))
        last_key = key
        last_votes = votes
    print("\ncompare witnesses votes done. diffent witness: {}\n".format(diffent))

def compare_committee_members_vote():
    active_committee_members = get_global_properties()["active_committee_members"]
    results = {}
    for key, url in node_rpc_urls.items():
        results[key] = get_committee_members_votes(url, active_committee_members)
    last_key = None
    last_votes = None
    diffent = {}
    for key, votes in results.items():
        if not last_votes:
            last_key = key
            last_votes = votes
            continue
        diffent_ids = []
        for id, vote_obj in votes.items():
            last_vote = last_votes[id]
            if not vote_obj == last_vote:
                print("\n>>> node {} and {} committee_members {} votes diffenent: ".format(last_key, key, id))
                vote_obj.show_supporters_different(last_vote)
                diffent_ids.append(id)
        if diffent_ids:
            diffent_key = last_key + "--" + key
            diffent[diffent_key] = diffent_ids
        print("\ncompare node {} and {} active_committee votes done. ".format(last_key, key))
        last_key = key
        last_votes = votes
    print("\ncompare committee members votes done. diffent committee: {}\n".format(diffent))
        
def vote_check():
    compare_witness_vote()
    compare_committee_members_vote()
    print("vote check done.")

def main():
    vote_check()

if __name__ == '__main__':
    print('>> {}\n'.format(sys.argv))
    main()


