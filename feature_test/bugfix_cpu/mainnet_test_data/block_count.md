

# 1. 区块交易统计： 
``` text  
dev@ck-chain-slave-prod-001:~/CocosBCX/feature_test/bugfix_cpu/mainnet_test_data$ python3 check_blocks_count.py 8700000 9900000
args: ['check_blocks_count.py', '8700000', '9900000']
interval_blocks: 10000
chain_params {'chain_id': '6057d856c398875cac2650fe33caef3d5f6b403d184c5154abbff526ec1143c4', 'prefix': 'COCOS', 'core_symbol': 'COCOS'}

>>>> 8700000: {'end_block': 8709999, 'block_total': 10000, 'ops_total': 435, 'start_block': 8700000, 'trx_total': 435}
>>>> 8710000: {'end_block': 8719999, 'block_total': 10000, 'ops_total': 535, 'start_block': 8710000, 'trx_total': 535}
>>>> 8720000: {'end_block': 8729999, 'block_total': 10000, 'ops_total': 422, 'start_block': 8720000, 'trx_total': 422}
>>>> 8730000: {'end_block': 8739999, 'block_total': 10000, 'ops_total': 417, 'start_block': 8730000, 'trx_total': 417}
>>>> 8740000: {'end_block': 8749999, 'block_total': 10000, 'ops_total': 289, 'start_block': 8740000, 'trx_total': 289}
>>>> 8750000: {'end_block': 8759999, 'block_total': 10000, 'ops_total': 631, 'start_block': 8750000, 'trx_total': 631}
>>>> 8760000: {'end_block': 8769999, 'block_total': 10000, 'ops_total': 278, 'start_block': 8760000, 'trx_total': 278}
>>>> 8770000: {'end_block': 8779999, 'block_total': 10000, 'ops_total': 259, 'start_block': 8770000, 'trx_total': 259}
>>>> 8780000: {'end_block': 8789999, 'block_total': 10000, 'ops_total': 354, 'start_block': 8780000, 'trx_total': 354}
>>>> 8790000: {'end_block': 8799999, 'block_total': 10000, 'ops_total': 574, 'start_block': 8790000, 'trx_total': 574}
>>>> 8800000: {'end_block': 8809999, 'block_total': 10000, 'ops_total': 486, 'start_block': 8800000, 'trx_total': 486}
>>>> 8810000: {'end_block': 8819999, 'block_total': 10000, 'ops_total': 237, 'start_block': 8810000, 'trx_total': 237}
>>>> 8820000: {'end_block': 8829999, 'block_total': 10000, 'ops_total': 280, 'start_block': 8820000, 'trx_total': 280}
>>>> 8830000: {'end_block': 8839999, 'block_total': 10000, 'ops_total': 498, 'start_block': 8830000, 'trx_total': 498}
>>>> 8840000: {'end_block': 8849999, 'block_total': 10000, 'ops_total': 594, 'start_block': 8840000, 'trx_total': 594}
>>>> 8850000: {'end_block': 8859999, 'block_total': 10000, 'ops_total': 289, 'start_block': 8850000, 'trx_total': 289}
>>>> 8860000: {'end_block': 8869999, 'block_total': 10000, 'ops_total': 406, 'start_block': 8860000, 'trx_total': 406}
>>>> 8870000: {'end_block': 8879999, 'block_total': 10000, 'ops_total': 292, 'start_block': 8870000, 'trx_total': 292}
>>>> 8880000: {'end_block': 8889999, 'block_total': 10000, 'ops_total': 696, 'start_block': 8880000, 'trx_total': 696}
>>>> 8890000: {'end_block': 8899999, 'block_total': 10000, 'ops_total': 147, 'start_block': 8890000, 'trx_total': 147}
>>>> 8900000: {'end_block': 8909999, 'block_total': 10000, 'ops_total': 739, 'start_block': 8900000, 'trx_total': 739}
>>>> 8910000: {'end_block': 8919999, 'block_total': 10000, 'ops_total': 314, 'start_block': 8910000, 'trx_total': 314}
>>>> 8920000: {'end_block': 8929999, 'block_total': 10000, 'ops_total': 706, 'start_block': 8920000, 'trx_total': 706}
>>>> 8930000: {'end_block': 8939999, 'block_total': 10000, 'ops_total': 619, 'start_block': 8930000, 'trx_total': 619}
>>>> 8940000: {'end_block': 8949999, 'block_total': 10000, 'ops_total': 595, 'start_block': 8940000, 'trx_total': 595}
>>>> 8950000: {'end_block': 8959999, 'block_total': 10000, 'ops_total': 453, 'start_block': 8950000, 'trx_total': 453}
>>>> 8960000: {'end_block': 8969999, 'block_total': 10000, 'ops_total': 475, 'start_block': 8960000, 'trx_total': 475}
>>>> 8970000: {'end_block': 8979999, 'block_total': 10000, 'ops_total': 717, 'start_block': 8970000, 'trx_total': 717}
>>>> 8980000: {'end_block': 8989999, 'block_total': 10000, 'ops_total': 744, 'start_block': 8980000, 'trx_total': 744}
>>>> 8990000: {'end_block': 8999999, 'block_total': 10000, 'ops_total': 818, 'start_block': 8990000, 'trx_total': 818}
>>>> 9000000: {'end_block': 9009999, 'block_total': 10000, 'ops_total': 327, 'start_block': 9000000, 'trx_total': 327}
>>>> 9010000: {'end_block': 9019999, 'block_total': 10000, 'ops_total': 941, 'start_block': 9010000, 'trx_total': 941}
>>>> 9020000: {'end_block': 9029999, 'block_total': 10000, 'ops_total': 411, 'start_block': 9020000, 'trx_total': 411}
>>>> 9030000: {'end_block': 9039999, 'block_total': 10000, 'ops_total': 960, 'start_block': 9030000, 'trx_total': 960}
>>>> 9040000: {'end_block': 9049999, 'block_total': 10000, 'ops_total': 368, 'start_block': 9040000, 'trx_total': 368}
>>>> 9050000: {'end_block': 9059999, 'block_total': 10000, 'ops_total': 980, 'start_block': 9050000, 'trx_total': 980}
>>>> 9060000: {'end_block': 9069999, 'block_total': 10000, 'ops_total': 470, 'start_block': 9060000, 'trx_total': 470}
>>>> 9070000: {'end_block': 9079999, 'block_total': 10000, 'ops_total': 497, 'start_block': 9070000, 'trx_total': 497}
>>>> 9080000: {'end_block': 9089999, 'block_total': 10000, 'ops_total': 768, 'start_block': 9080000, 'trx_total': 768}
>>>> 9090000: {'end_block': 9099999, 'block_total': 10000, 'ops_total': 605, 'start_block': 9090000, 'trx_total': 605}
>>>> 9100000: {'end_block': 9109999, 'block_total': 10000, 'ops_total': 663, 'start_block': 9100000, 'trx_total': 663}
>>>> 9110000: {'end_block': 9119999, 'block_total': 10000, 'ops_total': 430, 'start_block': 9110000, 'trx_total': 430}
>>>> 9120000: {'end_block': 9129999, 'block_total': 10000, 'ops_total': 533, 'start_block': 9120000, 'trx_total': 533}

```  
**执行中断后再次继续：**  
``` text  
dev@ck-chain-slave-prod-001:~/CocosBCX/feature_test/bugfix_cpu/mainnet_test_data$ python3 check_blocks_count.py
args: ['check_blocks_count.py']
interval_blocks: 10000
chain_params {'chain_id': '6057d856c398875cac2650fe33caef3d5f6b403d184c5154abbff526ec1143c4', 'core_symbol': 'COCOS', 'prefix': 'COCOS'}
info: {'current_witness': '1.6.35', 'recent_slots_filled': '340282366920938463463374607431768211455', 'dynamic_flags': 0, 'recently_missed_count': 0, 'next_maintenance_time': '2020-07-30T00:00:00', 'id': '2.1.0', 'witness_budget': '203390000000', 'head_block_number': 10324957, 'head_block_id': '009d8bdd22fa64312a340095fd1c38e0994ac39b', 'last_budget_time': '2020-07-29T00:00:00', 'time': '2020-07-29T12:42:12', 'current_transaction_count': 0, 'accounts_registered_this_interval': 21, 'last_irreversible_block_num': 10324948, 'current_aslot': 10519316}
start block: 9120000, end_block: 10324957
>>>> 9120000: {'trx_total': 533, 'ops_total': 533, 'block_total': 10000, 'start_block': 9120000, 'end_block': 9129999}
>>>> 9130000: {'trx_total': 264, 'ops_total': 264, 'block_total': 10000, 'start_block': 9130000, 'end_block': 9139999}
>>>> 9140000: {'trx_total': 837, 'ops_total': 837, 'block_total': 10000, 'start_block': 9140000, 'end_block': 9149999}
>>>> 9150000: {'trx_total': 652, 'ops_total': 652, 'block_total': 10000, 'start_block': 9150000, 'end_block': 9159999}
>>>> 9160000: {'trx_total': 611, 'ops_total': 611, 'block_total': 10000, 'start_block': 9160000, 'end_block': 9169999}
>>>> 9170000: {'trx_total': 243, 'ops_total': 243, 'block_total': 10000, 'start_block': 9170000, 'end_block': 9179999}
>>>> 9180000: {'trx_total': 715, 'ops_total': 715, 'block_total': 10000, 'start_block': 9180000, 'end_block': 9189999}
>>>> 9190000: {'trx_total': 647, 'ops_total': 647, 'block_total': 10000, 'start_block': 9190000, 'end_block': 9199999}
>>>> 9200000: {'trx_total': 561, 'ops_total': 561, 'block_total': 10000, 'start_block': 9200000, 'end_block': 9209999}
>>>> 9210000: {'trx_total': 419, 'ops_total': 419, 'block_total': 10000, 'start_block': 9210000, 'end_block': 9219999}
>>>> 9220000: {'trx_total': 883, 'ops_total': 883, 'block_total': 10000, 'start_block': 9220000, 'end_block': 9229999}
>>>> 9230000: {'trx_total': 454, 'ops_total': 454, 'block_total': 10000, 'start_block': 9230000, 'end_block': 9239999}
>>>> 9240000: {'trx_total': 1170, 'ops_total': 1170, 'block_total': 10000, 'start_block': 9240000, 'end_block': 9249999}
>>>> 9250000: {'trx_total': 529, 'ops_total': 529, 'block_total': 10000, 'start_block': 9250000, 'end_block': 9259999}
>>>> 9260000: {'trx_total': 99, 'ops_total': 99, 'block_total': 10000, 'start_block': 9260000, 'end_block': 9269999}
>>>> 9270000: {'trx_total': 921, 'ops_total': 921, 'block_total': 10000, 'start_block': 9270000, 'end_block': 9279999}
>>>> 9280000: {'trx_total': 418, 'ops_total': 418, 'block_total': 10000, 'start_block': 9280000, 'end_block': 9289999}
>>>> 9290000: {'trx_total': 576, 'ops_total': 576, 'block_total': 10000, 'start_block': 9290000, 'end_block': 9299999}
>>>> 9300000: {'trx_total': 246, 'ops_total': 246, 'block_total': 10000, 'start_block': 9300000, 'end_block': 9309999}
>>>> 9310000: {'trx_total': 1272, 'ops_total': 1272, 'block_total': 10000, 'start_block': 9310000, 'end_block': 9319999}
>>>> 9320000: {'trx_total': 629, 'ops_total': 629, 'block_total': 10000, 'start_block': 9320000, 'end_block': 9329999}
>>>> 9330000: {'trx_total': 1208, 'ops_total': 1208, 'block_total': 10000, 'start_block': 9330000, 'end_block': 9339999}
>>>> 9340000: {'trx_total': 1502, 'ops_total': 1502, 'block_total': 10000, 'start_block': 9340000, 'end_block': 9349999}
>>>> 9350000: {'trx_total': 1396, 'ops_total': 1396, 'block_total': 10000, 'start_block': 9350000, 'end_block': 9359999}
>>>> 9360000: {'trx_total': 1277, 'ops_total': 1277, 'block_total': 10000, 'start_block': 9360000, 'end_block': 9369999}
>>>> 9370000: {'trx_total': 1081, 'ops_total': 1081, 'block_total': 10000, 'start_block': 9370000, 'end_block': 9379999}
>>>> 9380000: {'trx_total': 1368, 'ops_total': 1368, 'block_total': 10000, 'start_block': 9380000, 'end_block': 9389999}
>>>> 9390000: {'trx_total': 1171, 'ops_total': 1171, 'block_total': 10000, 'start_block': 9390000, 'end_block': 9399999}
>>>> 9400000: {'trx_total': 1438, 'ops_total': 1438, 'block_total': 10000, 'start_block': 9400000, 'end_block': 9409999}
>>>> 9410000: {'trx_total': 1171, 'ops_total': 1171, 'block_total': 10000, 'start_block': 9410000, 'end_block': 9419999}
>>>> 9420000: {'trx_total': 1337, 'ops_total': 1337, 'block_total': 10000, 'start_block': 9420000, 'end_block': 9429999}
>>>> 9430000: {'trx_total': 1039, 'ops_total': 1039, 'block_total': 10000, 'start_block': 9430000, 'end_block': 9439999}
>>>> 9440000: {'trx_total': 1742, 'ops_total': 1742, 'block_total': 10000, 'start_block': 9440000, 'end_block': 9449999}
>>>> 9450000: {'trx_total': 1129, 'ops_total': 1129, 'block_total': 10000, 'start_block': 9450000, 'end_block': 9459999}
>>>> 9460000: {'trx_total': 405, 'ops_total': 405, 'block_total': 10000, 'start_block': 9460000, 'end_block': 9469999}
>>>> 9470000: {'trx_total': 293, 'ops_total': 293, 'block_total': 10000, 'start_block': 9470000, 'end_block': 9479999}
>>>> 9480000: {'trx_total': 502, 'ops_total': 502, 'block_total': 10000, 'start_block': 9480000, 'end_block': 9489999}
>>>> 9490000: {'trx_total': 1169, 'ops_total': 1169, 'block_total': 10000, 'start_block': 9490000, 'end_block': 9499999}
>>>> 9500000: {'trx_total': 1558, 'ops_total': 1558, 'block_total': 10000, 'start_block': 9500000, 'end_block': 9509999}
>>>> 9510000: {'trx_total': 1612, 'ops_total': 1612, 'block_total': 10000, 'start_block': 9510000, 'end_block': 9519999}
>>>> 9520000: {'trx_total': 1125, 'ops_total': 1125, 'block_total': 10000, 'start_block': 9520000, 'end_block': 9529999}
>>>> 9530000: {'trx_total': 1515, 'ops_total': 1515, 'block_total': 10000, 'start_block': 9530000, 'end_block': 9539999}
>>>> 9540000: {'trx_total': 1375, 'ops_total': 1375, 'block_total': 10000, 'start_block': 9540000, 'end_block': 9549999}
>>>> 9550000: {'trx_total': 1385, 'ops_total': 1385, 'block_total': 10000, 'start_block': 9550000, 'end_block': 9559999}
>>>> 9560000: {'trx_total': 1101, 'ops_total': 1101, 'block_total': 10000, 'start_block': 9560000, 'end_block': 9569999}
>>>> 9570000: {'trx_total': 1812, 'ops_total': 1812, 'block_total': 10000, 'start_block': 9570000, 'end_block': 9579999}
>>>> 9580000: {'trx_total': 1459, 'ops_total': 1459, 'block_total': 10000, 'start_block': 9580000, 'end_block': 9589999}
>>>> 9590000: {'trx_total': 1356, 'ops_total': 1356, 'block_total': 10000, 'start_block': 9590000, 'end_block': 9599999}
>>>> 9600000: {'trx_total': 1432, 'ops_total': 1432, 'block_total': 10000, 'start_block': 9600000, 'end_block': 9609999}
>>>> 9610000: {'trx_total': 1423, 'ops_total': 1423, 'block_total': 10000, 'start_block': 9610000, 'end_block': 9619999}
>>>> 9620000: {'trx_total': 1268, 'ops_total': 1268, 'block_total': 10000, 'start_block': 9620000, 'end_block': 9629999}
>>>> 9630000: {'trx_total': 28663, 'ops_total': 130506, 'block_total': 10000, 'start_block': 9630000, 'end_block': 9639999}
>>>> 9640000: {'trx_total': 44382, 'ops_total': 88132, 'block_total': 10000, 'start_block': 9640000, 'end_block': 9649999}
>>>> 9650000: {'trx_total': 40223, 'ops_total': 80015, 'block_total': 10000, 'start_block': 9650000, 'end_block': 9659999}
>>>> 9660000: {'trx_total': 33908, 'ops_total': 52232, 'block_total': 10000, 'start_block': 9660000, 'end_block': 9669999}
>>>> 9670000: {'trx_total': 50495, 'ops_total': 59880, 'block_total': 10000, 'start_block': 9670000, 'end_block': 9679999}
>>>> 9680000: {'trx_total': 67302, 'ops_total': 77877, 'block_total': 10000, 'start_block': 9680000, 'end_block': 9689999}
>>>> 9690000: {'trx_total': 66438, 'ops_total': 80674, 'block_total': 10000, 'start_block': 9690000, 'end_block': 9699999}
>>>> 9700000: {'trx_total': 62200, 'ops_total': 71853, 'block_total': 10000, 'start_block': 9700000, 'end_block': 9709999}
>>>> 9710000: {'trx_total': 59803, 'ops_total': 68080, 'block_total': 10000, 'start_block': 9710000, 'end_block': 9719999}
>>>> 9720000: {'trx_total': 57033, 'ops_total': 64826, 'block_total': 10000, 'start_block': 9720000, 'end_block': 9729999}
>>>> 9730000: {'trx_total': 57923, 'ops_total': 65879, 'block_total': 10000, 'start_block': 9730000, 'end_block': 9739999}
>>>> 9740000: {'trx_total': 54198, 'ops_total': 61309, 'block_total': 10000, 'start_block': 9740000, 'end_block': 9749999}
>>>> 9750000: {'trx_total': 52299, 'ops_total': 58558, 'block_total': 10000, 'start_block': 9750000, 'end_block': 9759999}
>>>> 9760000: {'trx_total': 53359, 'ops_total': 59836, 'block_total': 10000, 'start_block': 9760000, 'end_block': 9769999}
>>>> 9770000: {'trx_total': 29259, 'ops_total': 29259, 'block_total': 10000, 'start_block': 9770000, 'end_block': 9779999}
>>>> 9780000: {'trx_total': 29103, 'ops_total': 29103, 'block_total': 10000, 'start_block': 9780000, 'end_block': 9789999}
>>>> 9790000: {'trx_total': 52939, 'ops_total': 52939, 'block_total': 10000, 'start_block': 9790000, 'end_block': 9799999}
>>>> 9800000: {'trx_total': 50318, 'ops_total': 50318, 'block_total': 10000, 'start_block': 9800000, 'end_block': 9809999}
>>>> 9810000: {'trx_total': 52524, 'ops_total': 52524, 'block_total': 10000, 'start_block': 9810000, 'end_block': 9819999}
>>>> 9820000: {'trx_total': 53274, 'ops_total': 53274, 'block_total': 10000, 'start_block': 9820000, 'end_block': 9829999}
>>>> 9830000: {'trx_total': 50198, 'ops_total': 50198, 'block_total': 10000, 'start_block': 9830000, 'end_block': 9839999}
>>>> 9840000: {'trx_total': 49111, 'ops_total': 49111, 'block_total': 10000, 'start_block': 9840000, 'end_block': 9849999}
>>>> 9850000: {'trx_total': 49395, 'ops_total': 49395, 'block_total': 10000, 'start_block': 9850000, 'end_block': 9859999}
>>>> 9860000: {'trx_total': 47928, 'ops_total': 47928, 'block_total': 10000, 'start_block': 9860000, 'end_block': 9869999}
>>>> 9870000: {'trx_total': 48052, 'ops_total': 48052, 'block_total': 10000, 'start_block': 9870000, 'end_block': 9879999}
>>>> 9880000: {'trx_total': 52666, 'ops_total': 52666, 'block_total': 10000, 'start_block': 9880000, 'end_block': 9889999}
>>>> 9890000: {'trx_total': 50458, 'ops_total': 50458, 'block_total': 10000, 'start_block': 9890000, 'end_block': 9899999}
>>>> 9900000: {'trx_total': 57005, 'ops_total': 57005, 'block_total': 10000, 'start_block': 9900000, 'end_block': 9909999}
>>>> 9910000: {'trx_total': 53796, 'ops_total': 53796, 'block_total': 10000, 'start_block': 9910000, 'end_block': 9919999}
>>>> 9920000: {'trx_total': 40857, 'ops_total': 40857, 'block_total': 10000, 'start_block': 9920000, 'end_block': 9929999}
>>>> 9930000: {'trx_total': 40983, 'ops_total': 40983, 'block_total': 10000, 'start_block': 9930000, 'end_block': 9939999}
>>>> 9940000: {'trx_total': 42253, 'ops_total': 42253, 'block_total': 10000, 'start_block': 9940000, 'end_block': 9949999}
>>>> 9950000: {'trx_total': 47147, 'ops_total': 47147, 'block_total': 10000, 'start_block': 9950000, 'end_block': 9959999}
>>>> 9960000: {'trx_total': 40542, 'ops_total': 40542, 'block_total': 10000, 'start_block': 9960000, 'end_block': 9969999}
>>>> 9970000: {'trx_total': 43797, 'ops_total': 43797, 'block_total': 10000, 'start_block': 9970000, 'end_block': 9979999}
>>>> 9980000: {'trx_total': 49889, 'ops_total': 49889, 'block_total': 10000, 'start_block': 9980000, 'end_block': 9989999}
>>>> 9990000: {'trx_total': 50592, 'ops_total': 50592, 'block_total': 10000, 'start_block': 9990000, 'end_block': 9999999}
>>>> 10000000: {'trx_total': 55234, 'ops_total': 55234, 'block_total': 10000, 'start_block': 10000000, 'end_block': 10009999}
>>>> 10010000: {'trx_total': 50030, 'ops_total': 50030, 'block_total': 10000, 'start_block': 10010000, 'end_block': 10019999}
>>>> 10020000: {'trx_total': 39859, 'ops_total': 39859, 'block_total': 10000, 'start_block': 10020000, 'end_block': 10029999}
>>>> 10030000: {'trx_total': 39884, 'ops_total': 39884, 'block_total': 10000, 'start_block': 10030000, 'end_block': 10039999}
>>>> 10040000: {'trx_total': 39486, 'ops_total': 39486, 'block_total': 10000, 'start_block': 10040000, 'end_block': 10049999}
>>>> 10050000: {'trx_total': 37039, 'ops_total': 37039, 'block_total': 10000, 'start_block': 10050000, 'end_block': 10059999}
>>>> 10060000: {'trx_total': 41900, 'ops_total': 41907, 'block_total': 10000, 'start_block': 10060000, 'end_block': 10069999}
>>>> 10070000: {'trx_total': 37672, 'ops_total': 37672, 'block_total': 10000, 'start_block': 10070000, 'end_block': 10079999}
>>>> 10080000: {'trx_total': 1892, 'ops_total': 1892, 'block_total': 10000, 'start_block': 10080000, 'end_block': 10089999}
>>>> 10090000: {'trx_total': 1814, 'ops_total': 1814, 'block_total': 10000, 'start_block': 10090000, 'end_block': 10099999}
>>>> 10100000: {'trx_total': 81510, 'ops_total': 81510, 'block_total': 10000, 'start_block': 10100000, 'end_block': 10109999}
>>>> 10110000: {'trx_total': 59347, 'ops_total': 59347, 'block_total': 10000, 'start_block': 10110000, 'end_block': 10119999}
>>>> 10120000: {'trx_total': 47505, 'ops_total': 47505, 'block_total': 10000, 'start_block': 10120000, 'end_block': 10129999}
>>>> 10130000: {'trx_total': 49244, 'ops_total': 49244, 'block_total': 10000, 'start_block': 10130000, 'end_block': 10139999}
>>>> 10140000: {'trx_total': 70139, 'ops_total': 70139, 'block_total': 10000, 'start_block': 10140000, 'end_block': 10149999}
>>>> 10150000: {'trx_total': 63431, 'ops_total': 63431, 'block_total': 10000, 'start_block': 10150000, 'end_block': 10159999}
>>>> 10160000: {'trx_total': 48554, 'ops_total': 48554, 'block_total': 10000, 'start_block': 10160000, 'end_block': 10169999}
>>>> 10170000: {'trx_total': 48838, 'ops_total': 48838, 'block_total': 10000, 'start_block': 10170000, 'end_block': 10179999}
>>>> 10180000: {'trx_total': 48317, 'ops_total': 48317, 'block_total': 10000, 'start_block': 10180000, 'end_block': 10189999}
>>>> 10190000: {'trx_total': 47892, 'ops_total': 47892, 'block_total': 10000, 'start_block': 10190000, 'end_block': 10199999}
>>>> 10200000: {'trx_total': 38661, 'ops_total': 38661, 'block_total': 10000, 'start_block': 10200000, 'end_block': 10209999}
>>>> 10210000: {'trx_total': 43210, 'ops_total': 43210, 'block_total': 10000, 'start_block': 10210000, 'end_block': 10219999}
>>>> 10220000: {'trx_total': 14991, 'ops_total': 14991, 'block_total': 10000, 'start_block': 10220000, 'end_block': 10229999}
>>>> 10230000: {'trx_total': 1502, 'ops_total': 1502, 'block_total': 10000, 'start_block': 10230000, 'end_block': 10239999}
>>>> 10240000: {'trx_total': 1447, 'ops_total': 1447, 'block_total': 10000, 'start_block': 10240000, 'end_block': 10249999}
>>>> 10250000: {'trx_total': 1454, 'ops_total': 1454, 'block_total': 10000, 'start_block': 10250000, 'end_block': 10259999}
>>>> 10260000: {'trx_total': 1735, 'ops_total': 1735, 'block_total': 10000, 'start_block': 10260000, 'end_block': 10269999}
>>>> 10270000: {'trx_total': 1806, 'ops_total': 1806, 'block_total': 10000, 'start_block': 10270000, 'end_block': 10279999}
>>>> 10280000: {'trx_total': 1900, 'ops_total': 1900, 'block_total': 10000, 'start_block': 10280000, 'end_block': 10289999}
>>>> 10290000: {'trx_total': 1912, 'ops_total': 1912, 'block_total': 10000, 'start_block': 10290000, 'end_block': 10299999}
>>>> 10300000: {'trx_total': 2397, 'ops_total': 2397, 'block_total': 10000, 'start_block': 10300000, 'end_block': 10309999}
>>>> 10310000: {'trx_total': 1890, 'ops_total': 1890, 'block_total': 10000, 'start_block': 10310000, 'end_block': 10319999}


>>>> total result:
{9120000: {'trx_total': 533, 'ops_total': 533, 'block_total': 10000, 'start_block': 9120000, 'end_block': 9129999}, 9360000: {'trx_total': 1277, 'ops_total': 1277, 'block_total': 10000, 'start_block': 9360000, 'end_block': 9369999}, 10030000: {'trx_total': 39884, 'ops_total': 39884, 'block_total': 10000, 'start_block': 10030000, 'end_block': 10039999}, 10240000: {'trx_total': 1447, 'ops_total': 1447, 'block_total': 10000, 'start_block': 10240000, 'end_block': 10249999}, 9300000: {'trx_total': 246, 'ops_total': 246, 'block_total': 10000, 'start_block': 9300000, 'end_block': 9309999}, 9510000: {'trx_total': 1612, 'ops_total': 1612, 'block_total': 10000, 'start_block': 9510000, 'end_block': 9519999}, 10290000: {'trx_total': 1912, 'ops_total': 1912, 'block_total': 10000, 'start_block': 10290000, 'end_block': 10299999}, 9930000: {'trx_total': 40983, 'ops_total': 40983, 'block_total': 10000, 'start_block': 9930000, 'end_block': 9939999}, 9770000: {'trx_total': 29259, 'ops_total': 29259, 'block_total': 10000, 'start_block': 9770000, 'end_block': 9779999}, 10140000: {'trx_total': 70139, 'ops_total': 70139, 'block_total': 10000, 'start_block': 10140000, 'end_block': 10149999}, 10180000: {'trx_total': 48317, 'ops_total': 48317, 'block_total': 10000, 'start_block': 10180000, 'end_block': 10189999}, 9620000: {'trx_total': 1268, 'ops_total': 1268, 'block_total': 10000, 'start_block': 9620000, 'end_block': 9629999}, 9830000: {'trx_total': 50198, 'ops_total': 50198, 'block_total': 10000, 'start_block': 9830000, 'end_block': 9839999}, 10040000: {'trx_total': 39486, 'ops_total': 39486, 'block_total': 10000, 'start_block': 10040000, 'end_block': 10049999}, 10250000: {'trx_total': 1454, 'ops_total': 1454, 'block_total': 10000, 'start_block': 10250000, 'end_block': 10259999}, 9460000: {'trx_total': 405, 'ops_total': 405, 'block_total': 10000, 'start_block': 9460000, 'end_block': 9469999}, 9310000: {'trx_total': 1272, 'ops_total': 1272, 'block_total': 10000, 'start_block': 9310000, 'end_block': 9319999}, 9520000: {'trx_total': 1125, 'ops_total': 1125, 'block_total': 10000, 'start_block': 9520000, 'end_block': 9529999}, 9730000: {'trx_total': 57923, 'ops_total': 65879, 'block_total': 10000, 'start_block': 9730000, 'end_block': 9739999}, 10150000: {'trx_total': 63431, 'ops_total': 63431, 'block_total': 10000, 'start_block': 10150000, 'end_block': 10159999}, 9630000: {'trx_total': 28663, 'ops_total': 130506, 'block_total': 10000, 'start_block': 9630000, 'end_block': 9639999}, 9150000: {'trx_total': 652, 'ops_total': 652, 'block_total': 10000, 'start_block': 9150000, 'end_block': 9159999}, 9840000: {'trx_total': 49111, 'ops_total': 49111, 'block_total': 10000, 'start_block': 9840000, 'end_block': 9849999}, 10050000: {'trx_total': 37039, 'ops_total': 37039, 'block_total': 10000, 'start_block': 10050000, 'end_block': 10059999}, 10260000: {'trx_total': 1735, 'ops_total': 1735, 'block_total': 10000, 'start_block': 10260000, 'end_block': 10269999}, 9970000: {'trx_total': 43797, 'ops_total': 43797, 'block_total': 10000, 'start_block': 9970000, 'end_block': 9979999}, 9530000: {'trx_total': 1515, 'ops_total': 1515, 'block_total': 10000, 'start_block': 9530000, 'end_block': 9539999}, 9740000: {'trx_total': 54198, 'ops_total': 61309, 'block_total': 10000, 'start_block': 9740000, 'end_block': 9749999}, 9950000: {'trx_total': 47147, 'ops_total': 47147, 'block_total': 10000, 'start_block': 9950000, 'end_block': 9959999}, 9320000: {'trx_total': 629, 'ops_total': 629, 'block_total': 10000, 'start_block': 9320000, 'end_block': 9329999}, 9420000: {'trx_total': 1337, 'ops_total': 1337, 'block_total': 10000, 'start_block': 9420000, 'end_block': 9429999}, 10160000: {'trx_total': 48554, 'ops_total': 48554, 'block_total': 10000, 'start_block': 10160000, 'end_block': 10169999}, 9220000: {'trx_total': 883, 'ops_total': 883, 'block_total': 10000, 'start_block': 9220000, 'end_block': 9229999}, 9430000: {'trx_total': 1039, 'ops_total': 1039, 'block_total': 10000, 'start_block': 9430000, 'end_block': 9439999}, 9640000: {'trx_total': 44382, 'ops_total': 88132, 'block_total': 10000, 'start_block': 9640000, 'end_block': 9649999}, 9850000: {'trx_total': 49395, 'ops_total': 49395, 'block_total': 10000, 'start_block': 9850000, 'end_block': 9859999}, 10060000: {'trx_total': 41900, 'ops_total': 41907, 'block_total': 10000, 'start_block': 10060000, 'end_block': 10069999}, 10270000: {'trx_total': 1806, 'ops_total': 1806, 'block_total': 10000, 'start_block': 10270000, 'end_block': 10279999}, 9330000: {'trx_total': 1208, 'ops_total': 1208, 'block_total': 10000, 'start_block': 9330000, 'end_block': 9339999}, 9540000: {'trx_total': 1375, 'ops_total': 1375, 'block_total': 10000, 'start_block': 9540000, 'end_block': 9549999}, 9750000: {'trx_total': 52299, 'ops_total': 58558, 'block_total': 10000, 'start_block': 9750000, 'end_block': 9759999}, 9960000: {'trx_total': 40542, 'ops_total': 40542, 'block_total': 10000, 'start_block': 9960000, 'end_block': 9969999}, 10170000: {'trx_total': 48838, 'ops_total': 48838, 'block_total': 10000, 'start_block': 10170000, 'end_block': 10179999}, 9230000: {'trx_total': 454, 'ops_total': 454, 'block_total': 10000, 'start_block': 9230000, 'end_block': 9239999}, 9440000: {'trx_total': 1742, 'ops_total': 1742, 'block_total': 10000, 'start_block': 9440000, 'end_block': 9449999}, 9180000: {'trx_total': 715, 'ops_total': 715, 'block_total': 10000, 'start_block': 9180000, 'end_block': 9189999}, 9370000: {'trx_total': 1081, 'ops_total': 1081, 'block_total': 10000, 'start_block': 9370000, 'end_block': 9379999}, 9160000: {'trx_total': 611, 'ops_total': 611, 'block_total': 10000, 'start_block': 9160000, 'end_block': 9169999}, 9860000: {'trx_total': 47928, 'ops_total': 47928, 'block_total': 10000, 'start_block': 9860000, 'end_block': 9869999}, 10070000: {'trx_total': 37672, 'ops_total': 37672, 'block_total': 10000, 'start_block': 10070000, 'end_block': 10079999}, 9130000: {'trx_total': 264, 'ops_total': 264, 'block_total': 10000, 'start_block': 9130000, 'end_block': 9139999}, 10280000: {'trx_total': 1900, 'ops_total': 1900, 'block_total': 10000, 'start_block': 10280000, 'end_block': 10289999}, 9340000: {'trx_total': 1502, 'ops_total': 1502, 'block_total': 10000, 'start_block': 9340000, 'end_block': 9349999}, 9550000: {'trx_total': 1385, 'ops_total': 1385, 'block_total': 10000, 'start_block': 9550000, 'end_block': 9559999}, 9760000: {'trx_total': 53359, 'ops_total': 59836, 'block_total': 10000, 'start_block': 9760000, 'end_block': 9769999}, 9350000: {'trx_total': 1396, 'ops_total': 1396, 'block_total': 10000, 'start_block': 9350000, 'end_block': 9359999}, 9800000: {'trx_total': 50318, 'ops_total': 50318, 'block_total': 10000, 'start_block': 9800000, 'end_block': 9809999}, 9240000: {'trx_total': 1170, 'ops_total': 1170, 'block_total': 10000, 'start_block': 9240000, 'end_block': 9249999}, 9450000: {'trx_total': 1129, 'ops_total': 1129, 'block_total': 10000, 'start_block': 9450000, 'end_block': 9459999}, 9660000: {'trx_total': 33908, 'ops_total': 52232, 'block_total': 10000, 'start_block': 9660000, 'end_block': 9669999}, 9820000: {'trx_total': 53274, 'ops_total': 53274, 'block_total': 10000, 'start_block': 9820000, 'end_block': 9829999}, 10080000: {'trx_total': 1892, 'ops_total': 1892, 'block_total': 10000, 'start_block': 10080000, 'end_block': 10089999}, 9140000: {'trx_total': 837, 'ops_total': 837, 'block_total': 10000, 'start_block': 9140000, 'end_block': 9149999}, 9200000: {'trx_total': 561, 'ops_total': 561, 'block_total': 10000, 'start_block': 9200000, 'end_block': 9209999}, 9720000: {'trx_total': 57033, 'ops_total': 64826, 'block_total': 10000, 'start_block': 9720000, 'end_block': 9729999}, 9980000: {'trx_total': 49889, 'ops_total': 49889, 'block_total': 10000, 'start_block': 9980000, 'end_block': 9989999}, 10190000: {'trx_total': 47892, 'ops_total': 47892, 'block_total': 10000, 'start_block': 10190000, 'end_block': 10199999}, 9250000: {'trx_total': 529, 'ops_total': 529, 'block_total': 10000, 'start_block': 9250000, 'end_block': 9259999}, 9210000: {'trx_total': 419, 'ops_total': 419, 'block_total': 10000, 'start_block': 9210000, 'end_block': 9219999}, 9880000: {'trx_total': 52666, 'ops_total': 52666, 'block_total': 10000, 'start_block': 9880000, 'end_block': 9889999}, 10090000: {'trx_total': 1814, 'ops_total': 1814, 'block_total': 10000, 'start_block': 10090000, 'end_block': 10099999}, 9650000: {'trx_total': 40223, 'ops_total': 80015, 'block_total': 10000, 'start_block': 9650000, 'end_block': 9659999}, 10300000: {'trx_total': 2397, 'ops_total': 2397, 'block_total': 10000, 'start_block': 10300000, 'end_block': 10309999}, 9780000: {'trx_total': 29103, 'ops_total': 29103, 'block_total': 10000, 'start_block': 9780000, 'end_block': 9789999}, 9380000: {'trx_total': 1368, 'ops_total': 1368, 'block_total': 10000, 'start_block': 9380000, 'end_block': 9389999}, 9670000: {'trx_total': 50495, 'ops_total': 59880, 'block_total': 10000, 'start_block': 9670000, 'end_block': 9679999}, 10200000: {'trx_total': 38661, 'ops_total': 38661, 'block_total': 10000, 'start_block': 10200000, 'end_block': 10209999}, 9260000: {'trx_total': 99, 'ops_total': 99, 'block_total': 10000, 'start_block': 9260000, 'end_block': 9269999}, 9470000: {'trx_total': 293, 'ops_total': 293, 'block_total': 10000, 'start_block': 9470000, 'end_block': 9479999}, 9680000: {'trx_total': 67302, 'ops_total': 77877, 'block_total': 10000, 'start_block': 9680000, 'end_block': 9689999}, 9890000: {'trx_total': 50458, 'ops_total': 50458, 'block_total': 10000, 'start_block': 9890000, 'end_block': 9899999}, 10100000: {'trx_total': 81510, 'ops_total': 81510, 'block_total': 10000, 'start_block': 10100000, 'end_block': 10109999}, 9870000: {'trx_total': 48052, 'ops_total': 48052, 'block_total': 10000, 'start_block': 9870000, 'end_block': 9879999}, 10310000: {'trx_total': 1890, 'ops_total': 1890, 'block_total': 10000, 'start_block': 10310000, 'end_block': 10319999}, 9580000: {'trx_total': 1459, 'ops_total': 1459, 'block_total': 10000, 'start_block': 9580000, 'end_block': 9589999}, 9790000: {'trx_total': 52939, 'ops_total': 52939, 'block_total': 10000, 'start_block': 9790000, 'end_block': 9799999}, 9990000: {'trx_total': 50592, 'ops_total': 50592, 'block_total': 10000, 'start_block': 9990000, 'end_block': 9999999}, 10000000: {'trx_total': 55234, 'ops_total': 55234, 'block_total': 10000, 'start_block': 10000000, 'end_block': 10009999}, 10210000: {'trx_total': 43210, 'ops_total': 43210, 'block_total': 10000, 'start_block': 10210000, 'end_block': 10219999}, 9560000: {'trx_total': 1101, 'ops_total': 1101, 'block_total': 10000, 'start_block': 9560000, 'end_block': 9569999}, 9940000: {'trx_total': 42253, 'ops_total': 42253, 'block_total': 10000, 'start_block': 9940000, 'end_block': 9949999}, 9690000: {'trx_total': 66438, 'ops_total': 80674, 'block_total': 10000, 'start_block': 9690000, 'end_block': 9699999}, 10110000: {'trx_total': 59347, 'ops_total': 59347, 'block_total': 10000, 'start_block': 10110000, 'end_block': 10119999}, 9170000: {'trx_total': 243, 'ops_total': 243, 'block_total': 10000, 'start_block': 9170000, 'end_block': 9179999}, 10320000: {'trx_total': 970, 'ops_total': 970, 'block_total': 4957, 'start_block': 10320000, 'end_block': 10324956}, 9590000: {'trx_total': 1356, 'ops_total': 1356, 'block_total': 10000, 'start_block': 9590000, 'end_block': 9599999}, 9410000: {'trx_total': 1171, 'ops_total': 1171, 'block_total': 10000, 'start_block': 9410000, 'end_block': 9419999}, 10010000: {'trx_total': 50030, 'ops_total': 50030, 'block_total': 10000, 'start_block': 10010000, 'end_block': 10019999}, 10220000: {'trx_total': 14991, 'ops_total': 14991, 'block_total': 10000, 'start_block': 10220000, 'end_block': 10229999}, 9280000: {'trx_total': 418, 'ops_total': 418, 'block_total': 10000, 'start_block': 9280000, 'end_block': 9289999}, 9490000: {'trx_total': 1169, 'ops_total': 1169, 'block_total': 10000, 'start_block': 9490000, 'end_block': 9499999}, 9700000: {'trx_total': 62200, 'ops_total': 71853, 'block_total': 10000, 'start_block': 9700000, 'end_block': 9709999}, 9910000: {'trx_total': 53796, 'ops_total': 53796, 'block_total': 10000, 'start_block': 9910000, 'end_block': 9919999}, 9900000: {'trx_total': 57005, 'ops_total': 57005, 'block_total': 10000, 'start_block': 9900000, 'end_block': 9909999}, 9570000: {'trx_total': 1812, 'ops_total': 1812, 'block_total': 10000, 'start_block': 9570000, 'end_block': 9579999}, 9390000: {'trx_total': 1171, 'ops_total': 1171, 'block_total': 10000, 'start_block': 9390000, 'end_block': 9399999}, 9600000: {'trx_total': 1432, 'ops_total': 1432, 'block_total': 10000, 'start_block': 9600000, 'end_block': 9609999}, 9810000: {'trx_total': 52524, 'ops_total': 52524, 'block_total': 10000, 'start_block': 9810000, 'end_block': 9819999}, 9480000: {'trx_total': 502, 'ops_total': 502, 'block_total': 10000, 'start_block': 9480000, 'end_block': 9489999}, 10020000: {'trx_total': 39859, 'ops_total': 39859, 'block_total': 10000, 'start_block': 10020000, 'end_block': 10029999}, 10230000: {'trx_total': 1502, 'ops_total': 1502, 'block_total': 10000, 'start_block': 10230000, 'end_block': 10239999}, 9290000: {'trx_total': 576, 'ops_total': 576, 'block_total': 10000, 'start_block': 9290000, 'end_block': 9299999}, 9270000: {'trx_total': 921, 'ops_total': 921, 'block_total': 10000, 'start_block': 9270000, 'end_block': 9279999}, 9500000: {'trx_total': 1558, 'ops_total': 1558, 'block_total': 10000, 'start_block': 9500000, 'end_block': 9509999}, 9710000: {'trx_total': 59803, 'ops_total': 68080, 'block_total': 10000, 'start_block': 9710000, 'end_block': 9719999}, 9920000: {'trx_total': 40857, 'ops_total': 40857, 'block_total': 10000, 'start_block': 9920000, 'end_block': 9929999}, 10130000: {'trx_total': 49244, 'ops_total': 49244, 'block_total': 10000, 'start_block': 10130000, 'end_block': 10139999}, 9190000: {'trx_total': 647, 'ops_total': 647, 'block_total': 10000, 'start_block': 9190000, 'end_block': 9199999}, 10120000: {'trx_total': 47505, 'ops_total': 47505, 'block_total': 10000, 'start_block': 10120000, 'end_block': 10129999}, 9400000: {'trx_total': 1438, 'ops_total': 1438, 'block_total': 10000, 'start_block': 9400000, 'end_block': 9409999}, 9610000: {'trx_total': 1423, 'ops_total': 1423, 'block_total': 10000, 'start_block': 9610000, 'end_block': 9619999}}

```  