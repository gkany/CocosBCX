# -*- coding:utf-8 -*-
from PythonMiddleware.graphene import Graphene

import sys
import datetime
import time

nodeaddress = "wss://api.cocosbcx.net"

interval_blocks = 10000
block_count_result = {}

def check_block(start_block, end_block=-1):
    global interval_blocks, block_count_result
    print("interval_blocks: {}".format(interval_blocks))

    gph = Graphene(node=nodeaddress)
    if end_block == -1:
        info = gph.info()
        print("info: {}".format(info))
        end_block = info['head_block_number']

    key_block_num = str(start_block)
    for i in range(int(start_block), int(end_block)):
        try:
            block = gph.rpc.get_block(i)
            # print("block: {}".format(block))
            timestamp = block["timestamp"]
            block_date = timestamp.split("T")[0]
            
            if i % interval_blocks == 0 or key_block_num == str(i):
                # print("start_block: {}, end_block: {}, block_id: {}".format(key_block_num, i, block["block_id"]))
                if key_block_num in block_count_result.keys():
                    print(">>>> {}: {}".format(key_block_num, block_count_result[key_block_num]))
                key_block_num = i
                block_count_result[key_block_num] = {
                    "start_block": int(key_block_num),
                    "block_total": 0,
                    "trx_total": 0,
                    "ops_total": 0
                }

            block_data = block_count_result[key_block_num]
            block_data["block_total"] += 1
            block_data["end_block"] = i

            transactions = block["transactions"]
            if transactions:
                block_data["trx_total"] += len(transactions)
                for trx in transactions:
                    block_data["ops_total"] += len(trx[1]["operations"])
            block_count_result[key_block_num] = block_data
        except Exception as e:
            print('get_object exception. block {}, error {}'.format(block_num, repr(e)))
    print("\n\n>>>> total result: \n{}".format(block_count_result))

def compare_time(time1, time2):
    s_time = time.mktime(time.strptime(time1,'%Y-%m-%d'))
    e_time = time.mktime(time.strptime(time2,'%Y-%m-%d'))
    return int(s_time) - int(e_time)

def compare_time_test():
    result = compare_time('2020-04-17', '2020-04-19')
    print("result: {}".format(result))

if __name__ == '__main__':
    print('args: {}'.format(sys.argv))
    if len(sys.argv) < 2:
        print('Usage: python3 check.py start_block end_block')
        sys.exit(1)
    start_block = sys.argv[1]
    end_block = -1
    if len(sys.argv) >= 2:
        end_block = sys.argv[2]
    check_block(start_block, end_block)

'''
1. 功能
统计一段区块范围的的链上区块、交易和operation的总数。

2. 使用
依赖： python-sdk

python3 check_blocks_count.py start_block end_block 

3. 测试
dev@ubuntu:~/data/mrepo/CocosBCX/feature_test/bugfix_cpu/mainnet_test_data$ python3 check_blocks_count.py 123 1450
args: ['check_blocks_count.py', '123', '1450']
interval_blocks: 100
chain_params {'prefix': 'COCOS', 'chain_id': '6057d856c398875cac2650fe33caef3d5f6b403d184c5154abbff526ec1143c4', 'core_symbol': 'COCOS'}
>>>> 123: {'trx_total': 0, 'ops_total': 0, 'end_block': 199, 'start_block': 123, 'block_total': 77}
>>>> 200: {'trx_total': 1, 'ops_total': 1, 'end_block': 299, 'start_block': 200, 'block_total': 100}
>>>> 300: {'trx_total': 12, 'ops_total': 12, 'end_block': 399, 'start_block': 300, 'block_total': 100}
>>>> 400: {'trx_total': 0, 'ops_total': 0, 'end_block': 499, 'start_block': 400, 'block_total': 100}
>>>> 500: {'trx_total': 0, 'ops_total': 0, 'end_block': 599, 'start_block': 500, 'block_total': 100}
>>>> 600: {'trx_total': 1, 'ops_total': 1, 'end_block': 699, 'start_block': 600, 'block_total': 100}
>>>> 700: {'trx_total': 0, 'ops_total': 0, 'end_block': 799, 'start_block': 700, 'block_total': 100}
>>>> 800: {'trx_total': 0, 'ops_total': 0, 'end_block': 899, 'start_block': 800, 'block_total': 100}
>>>> 900: {'trx_total': 0, 'ops_total': 0, 'end_block': 999, 'start_block': 900, 'block_total': 100}
>>>> 1000: {'trx_total': 0, 'ops_total': 0, 'end_block': 1099, 'start_block': 1000, 'block_total': 100}
>>>> 1100: {'trx_total': 1, 'ops_total': 1, 'end_block': 1199, 'start_block': 1100, 'block_total': 100}
>>>> 1200: {'trx_total': 6, 'ops_total': 6, 'end_block': 1299, 'start_block': 1200, 'block_total': 100}
>>>> 1300: {'trx_total': 0, 'ops_total': 0, 'end_block': 1399, 'start_block': 1300, 'block_total': 100}


>>>> total result: 
{800: {'trx_total': 0, 'ops_total': 0, 'end_block': 899, 'start_block': 800, 'block_total': 100}, 1200: {'trx_total': 6, 'ops_total': 6, 'end_block': 1299, 'start_block': 1200, 'block_total': 100}, 900: {'trx_total': 0, 'ops_total': 0, 'end_block': 999, 'start_block': 900, 'block_total': 100}, 1400: {'trx_total': 0, 'ops_total': 0, 'end_block': 1449, 'start_block': 1400, 'block_total': 50}, 1000: {'trx_total': 0, 'ops_total': 0, 'end_block': 1099, 'start_block': 1000, 'block_total': 100}, 300: {'trx_total': 12, 'ops_total': 12, 'end_block': 399, 'start_block': 300, 'block_total': 100}, 1100: {'trx_total': 1, 'ops_total': 1, 'end_block': 1199, 'start_block': 1100, 'block_total': 100}, 400: {'trx_total': 0, 'ops_total': 0, 'end_block': 499, 'start_block': 400, 'block_total': 100}, 200: {'trx_total': 1, 'ops_total': 1, 'end_block': 299, 'start_block': 200, 'block_total': 100}, 500: {'trx_total': 0, 'ops_total': 0, 'end_block': 599, 'start_block': 500, 'block_total': 100}, 600: {'trx_total': 1, 'ops_total': 1, 'end_block': 699, 'start_block': 600, 'block_total': 100}, 1300: {'trx_total': 0, 'ops_total': 0, 'end_block': 1399, 'start_block': 1300, 'block_total': 100}, 123: {'trx_total': 0, 'ops_total': 0, 'end_block': 199, 'start_block': 123, 'block_total': 77}, 700: {'trx_total': 0, 'ops_total': 0, 'end_block': 799, 'start_block': 700, 'block_total': 100}}

'''
