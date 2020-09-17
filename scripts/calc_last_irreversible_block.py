# -*- coding:utf-8 -*-
import math
import numpy as np
from PythonMiddleware.graphene import Graphene

#define
GRAPHENE_100_PERCENT                = 10000
GRAPHENE_1_PERCENT                  = (GRAPHENE_100_PERCENT/100)
GRAPHENE_IRREVERSIBLE_THRESHOLD     = (70 * GRAPHENE_1_PERCENT)

#nodeaddress = "ws://test.cocosbcx.net"
nodeaddress = "wss://api.cocosbcx.net"

def partition_arg_topK(matrix, K, axis=0):
    """
    perform topK based on np.argpartition
    :param matrix: to be sorted
    :param K: select and sort the top K items
    :param axis: 0 or 1. dimension to be sorted.
    :return:
    """
    a_part = np.argpartition(matrix, K, axis=axis)
    print('axis: {}'.format(axis))
    if axis == 0:
        row_index = np.arange(matrix.shape[1 - axis])
        a_sec_argsort_K = np.argsort(matrix[a_part[0:K, :], row_index], axis=axis)
        return a_part[0:K, :][a_sec_argsort_K, row_index]
    else:
        column_index = np.arange(matrix.shape[1 - axis])[:, None]
        a_sec_argsort_K = np.argsort(matrix[column_index, a_part[:, 0:K]], axis=axis)
        return a_part[:, 0:K][column_index, a_sec_argsort_K]

def update_last_irreversible_block():
    #last_block_dict = {}
    witness_last_blocks = []
    gph = Graphene(node=nodeaddress)
    gpo = gph.rpc.get_object("2.0.0")
    dpo = gph.rpc.get_object("2.1.0")
    active_witnesses = gpo['active_witnesses']
    for witness_id in active_witnesses:
        witness = gph.rpc.get_object(witness_id)
        last_confirmed_block_num = witness['last_confirmed_block_num']
        #last_block_dict[witness_id] = last_confirmed_block_num
        witness_last_blocks.append(last_confirmed_block_num)

    witness_size = len(witness_last_blocks) 
    offset = math.floor(((GRAPHENE_100_PERCENT - GRAPHENE_IRREVERSIBLE_THRESHOLD) * witness_size / GRAPHENE_100_PERCENT))
    print('\nwitness size: {}, offset: {}'.format(witness_size, offset))

    block_nums = np.array(witness_last_blocks)
    print('np block_nums: ', block_nums)
    print('offset: {}, offset value: {}'.format(offset, block_nums[offset]))
    part_numbers = np.partition(block_nums, offset)
    print('partition sort: ', part_numbers)
    new_last_irreversible_block_num = part_numbers[offset]
    last_irreversible_block_num = dpo['last_irreversible_block_num']
    print('\nresult:')
    print('  last_irreversible_block_num: {}'.format(last_irreversible_block_num))
    print('  new_last_irreversible_block_num: {}'.format(new_last_irreversible_block_num))
    if new_last_irreversible_block_num > last_irreversible_block_num:
        print('update_last_irreversible_block')
    else:
        print('not update_last_irreversible_block')


def test():
    arr = [93, 91, 94, 87, 86, 85, 88, 89, 92, 45, 63]
    np_arr = np.array(arr)
    print('np_arr: ', np_arr)
    print('shape: ', np_arr.shape)
    print('shape arr: ', np_arr)
    sort_topk_arr = partition_arg_topK(matrix=np_arr, K=5)
    print('sort_topk_arr: ', sort_topk_arr)



def main():
    update_last_irreversible_block()

if __name__ == '__main__':
    main()
    #test()
