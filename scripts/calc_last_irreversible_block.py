# -*- coding:utf-8 -*-
import math
import numpy as np
import json
import requests

#define
GRAPHENE_100_PERCENT                = 10000
GRAPHENE_1_PERCENT                  = (GRAPHENE_100_PERCENT/100)
GRAPHENE_IRREVERSIBLE_THRESHOLD     = (70 * GRAPHENE_1_PERCENT)

node_rpc_url = "https://api.cocosbcx.net"

headers = {"content-type": "application/json"}

def request_post(req_data, is_assert=True):
    response = json.loads(requests.post(node_rpc_url, data=json.dumps(req_data), headers=headers).text)
    # print('>>{} {}'.format(req_data['method'], req_data['params']))
    if is_assert:
        assert 'error' not in response
    return response

def get_objects(id):
    try:
        req_data = {
                "jsonrpc": "2.0",
                "method": "call",
                "params": [0, "get_objects", [[id]]],
                "id":1
                }
        return request_post(req_data)["result"]
    except Exception as e:
        print(repr(e))
    return None

def partition_arg_topK(matrix, K, axis=0):
    """
        perform topK based on np.argpartition
        :param matrix: to be sorted
        :param K: select and sort the top K items
        :param axis: 0 or 1. dimension to be sorted.
        :return:
    """
    a_part = np.argpartition(matrix, K, axis=axis)
    # print('axis: {}'.format(axis))
    if axis == 0:
        row_index = np.arange(matrix.shape[1 - axis])
        a_sec_argsort_K = np.argsort(matrix[a_part[0:K, :], row_index], axis=axis)
        return a_part[0:K, :][a_sec_argsort_K, row_index]
    else:
        column_index = np.arange(matrix.shape[1 - axis])[:, None]
        a_sec_argsort_K = np.argsort(matrix[column_index, a_part[:, 0:K]], axis=axis)
        return a_part[:, 0:K][column_index, a_sec_argsort_K]

def update_last_irreversible_block():
    witness_last_blocks = []
    gpo = get_objects("2.0.0")[0]
    dpo = get_objects("2.1.0")[0]
    print("id: {}, head_block_number: {}, last_irreversible_block_num: {}".format(
        dpo['id'],dpo['head_block_number'], dpo['last_irreversible_block_num']))
    active_witnesses = gpo['active_witnesses']
    for witness_id in active_witnesses:
        witness = get_objects(witness_id)[0]
        last_confirmed_block_num = witness['last_confirmed_block_num']
        witness_last_blocks.append(last_confirmed_block_num)

    witness_size = len(witness_last_blocks) 
    offset = math.floor(((GRAPHENE_100_PERCENT - GRAPHENE_IRREVERSIBLE_THRESHOLD) * witness_size / GRAPHENE_100_PERCENT))
    # print('>> witness size: {}, offset: {}'.format(witness_size, offset))

    block_nums = np.array(witness_last_blocks)
    print('witness size: {}, offset: {}, offset block_num: {}'.format(witness_size, offset, block_nums[offset]))
    part_numbers = np.partition(block_nums, offset)
    # print('\npartition sort: ', part_numbers)

    new_last_irreversible_block_num = part_numbers[offset]
    last_irreversible_block_num = dpo['last_irreversible_block_num']
    print('\nlast_irreversible_block_num    : {}'.format(last_irreversible_block_num))
    print('new_last_irreversible_block_num: {}'.format(new_last_irreversible_block_num))
    if new_last_irreversible_block_num > last_irreversible_block_num:
        print('>> [DB]update_last_irreversible_block: {}'.format(new_last_irreversible_block_num))
    else:
        print(">> Don't update_last_irreversible_block")

def main():
    update_last_irreversible_block()
    dpo = get_objects("2.1.0")[0]
    print("id: {}, head_block_number: {}, last_irreversible_block_num: {}".format(
        dpo['id'],dpo['head_block_number'], dpo['last_irreversible_block_num']))

if __name__ == '__main__':
    main()


'''
### test1
dev@ubuntu:~/data/CocosBCX/scripts$ python3 calc_last_irreversible_block.py 
id: 2.1.0, head_block_number: 12444885, last_irreversible_block_num: 12444865
witness size: 11, offset: 3, offset block_num: 12444882

last_irreversible_block_num    : 12444865
new_last_irreversible_block_num: 12444870
>> [DB]update_last_irreversible_block: 12444870
id: 2.1.0, head_block_number: 12444885, last_irreversible_block_num: 12444865
dev@ubuntu:~/data/CocosBCX/scripts$ 

### test2
dev@ubuntu:~/data/CocosBCX/scripts$ python3 calc_last_irreversible_block.py 
id: 2.1.0, head_block_number: 12444885, last_irreversible_block_num: 12444865
witness size: 11, offset: 3, offset block_num: 12444882

last_irreversible_block_num    : 12444865
new_last_irreversible_block_num: 12444870
>> [DB]update_last_irreversible_block: 12444870
id: 2.1.0, head_block_number: 12444885, last_irreversible_block_num: 12444865
dev@ubuntu:~/data/CocosBCX/scripts$ 
dev@ubuntu:~/data/CocosBCX/scripts$ 

### test3
dev@ubuntu:~/data/CocosBCX/scripts$ python3 calc_last_irreversible_block.py 
id: 2.1.0, head_block_number: 12452183, last_irreversible_block_num: 12450924
witness size: 11, offset: 3, offset block_num: 12452182

last_irreversible_block_num    : 12450924
new_last_irreversible_block_num: 12444867
>> Don't update_last_irreversible_block
id: 2.1.0, head_block_number: 12452184, last_irreversible_block_num: 12450924
dev@ubuntu:~/data/CocosBCX/scripts$ 
'''