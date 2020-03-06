#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import socket
import datetime
import xlwt

log_path = "/mnt/witness/logs/witness_node.log"  # mainnet
#log_path = "/mnt/new_witness/logs/witness_node.log" # testnet

tag = "blocks"

titles = ["区块编号", "出块见证人", "不可逆区块", "同步延迟(ms)", "出块时间"]

def get_host_name():
    try:
        hostname = socket.getfqdn(socket.gethostname())
    except Exception as e:
        hostname = "localhost"
    if 'HOST_NAME' in os.environ:
        hostname = os.environ['HOST_NAME']  
    return hostname

def task(path):
    yes_time = datetime.datetime.now() + datetime.timedelta(days=-1)
    yes_date = yes_time.strftime('%Y-%m-%d')

    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = workbook.add_sheet(tag, cell_overwrite_ok=True)
    row = 0
    for index, title in enumerate(titles):
        sheet.write(row, index, title)
    row = row + 1

    with open(path, 'r') as f:
        for line in f:
            #if line.find("Got block") != -1 and line.find("handle_block") != -1:
            if line.find("Got block") != -1 and line.find("handle_block") != -1 and line.find(yes_date) != -1:
                tokens = line.split(':')
                block_num_temp = tokens[2].split()
                block_num = block_num_temp[0].split('#')[1]
                date_time_temp ='{}:{}:{}'.format(tokens[3], tokens[4], tokens[5]).split()
                date_time = date_time_temp[0]
                latency = tokens[6].split()[0]
                witness = tokens[-2].strip().split()[0]
                irreversible = tokens[-1].split()[0]
                # write
                sheet.write(row, 0, block_num)
                sheet.write(row, 1, witness)
                sheet.write(row, 2, irreversible)
                sheet.write(row, 3, latency)
                sheet.write(row, 4, date_time)
                row = row + 1
        f.close()
    hostname = get_host_name()
    file_name = "{}_{}_{}.xls".format(hostname, tag, yes_date)
    workbook.save(file_name)

def main():
    task(log_path)

if __name__ == '__main__':
    main()
