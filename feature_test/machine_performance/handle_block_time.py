# -*- coding: utf-8 -*- 

import time 
import xlwt 
import sys
import os

#生成当前时间的时间戳，只有一个参数即时间戳的位数，默认为10位，输入位数即生成相应位数的时间戳，比如可以生成常用的13位时间戳
def now_to_timestamp(digits = 10):
 time_stamp = time.time()
 digits = 10 ** (digits -10)
 time_stamp = int(round(time_stamp*digits))
 return time_stamp
 
#将时间戳规范为10位时间戳
def timestamp_to_timestamp10(time_stamp):
 time_stamp = int (time_stamp* (10 ** (10-len(str(time_stamp)))))
 return time_stamp
 
#将当前时间转换为时间字符串，默认为2020-07-20T07:47:36格式
def now_to_date(format_string="%Y-%m-%dT%H:%M:%S"):
 time_stamp = int(time.time())
 time_array = time.localtime(time_stamp)
 str_date = time.strftime(format_string, time_array)
 return str_date

#将10位时间戳转换为时间字符串，默认为2020-07-20T07:47:36格式
def timestamp_to_date(time_stamp, format_string="%Y-%m-%dT%H:%M:%S"):
 time_array = time.localtime(time_stamp)
 str_date = time.strftime(format_string, time_array)
 return str_date
 
#将时间字符串转换为10位时间戳，时间字符串默认为2020-07-20T07:47:36格式
def date_to_timestamp(date, format_string="%Y-%m-%dT%H:%M:%S"):
 time_array = time.strptime(date, format_string)
 time_stamp = int(time.mktime(time_array))
 return time_stamp

def calc_elapsed_time(d1, d2):
    t1 = date_to_timestamp(d1)
    t2 = date_to_timestamp(d2)
    return t2 - t1

def set_style(name='Times New Roman', height=220, bold=False):
    style = xlwt.XFStyle() # 初始化样式
 
    font = xlwt.Font() # 为样式创建字体
    font.name = name # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height
 
    # borders= xlwt.Borders()
    # borders.left= 6
    # borders.right= 6
    # borders.top= 6
    # borders.bottom= 6

    style.font = font
    # style.borders = borders

    al = xlwt.Alignment()
    al.horz = 0x02      # 设置水平居中
    al.vert = 0x01      # 设置垂直居中
    style.alignment = al
    return style

def cmd_exec(cmd, log=True):
    if log:
        print('>>> {}'.format(cmd))
    os.system(cmd)

def handle_log(input="witness_node.log", output="block_time.log"):
    excel_file = "{}.xlsx".format(output.split(".")[0])
    cmd = 'rm {} {}'.format(output, excel_file)
    cmd_exec(cmd)

    cmd = 'grep "test_handle_block" {} | cut -d "]" -f 3 | cut -d " " -f 4,7 >> {}'.format(input, output)
    cmd_exec(cmd)


'''
>>> cat got_block.log
2911292ms th_a       application.cpp:538           handle_block         ] Got block: #4960000 time: 2020-03-24T10:27:22 latency: 10945269292 ms from: hashquark  irreversible: 4959992 (-8), now: 2020-07-29T02:48:31
2920599ms th_a       application.cpp:538           handle_block         ] Got block: #4970000 time: 2020-03-24T16:00:42 latency: 10925278599 ms from: beijing-bp  irreversible: 4969991 (-9), now: 2020-07-29T02:48:40
2929625ms th_a       application.cpp:538           handle_block         ] Got block: #4980000 time: 2020-03-24T21:34:02 latency: 10905287625 ms from: blockchainkeys  irreversible: 4979992 (-8), now: 2020-07-29T02:48:49

>>> grep "handle_block" got_block.log | grep "Got block" | cut -d "]" -f 2 | cut -d " " -f 4,17
#4960000 2020-07-29T02:48:31
#4970000 2020-07-29T02:48:40
#4980000 2020-07-29T02:48:49
'''
def handle_get_block(filename="block_time.log", console=True):
    print("handle {}".format(filename))
    excel_file = xlwt.Workbook() #创建工作簿
    sheet1 = excel_file.add_sheet(u'获取和处理区块耗时统计', cell_overwrite_ok=True) #创建sheet
    row0 = [u'区块', u'区块范围', u'总耗时/单位秒']
    column_widths = [256*20, 256*20, 256*20]

    #生成第一行
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))
        width = column_widths[i]
        if width > 0:
            column = sheet1.col(i)
            column.width = width

    # read log data
    with open(filename, 'r') as f:
        last_block = -1
        last_time = 0
        column = 1
        max_elapsed_time = -1
        min_elapsed_time = sys.maxsize
        print("[elapsed_time] init, max: {}, min: {}".format(max_elapsed_time, min_elapsed_time))
        if console:
            print("-------- excel data --------")
            print("block, block range, total_time")
        for line in f:
            #print("line: {}".format(line))
            excel_row_data = []
            tokens = line.split(' ')
            block_num = int(tokens[0].strip()[1:-1])
            now_time = tokens[1].strip()
            if last_block == -1:
                last_block = block_num
                last_time = now_time
                continue

            #if int(block_num) - int(last_block) < 10000:
            if block_num - last_block < 2:
                print("last_block: {}, block_num: {}".format(last_block, block_num))
                break
            total_time = calc_elapsed_time(last_time, now_time)
            block_range = '{}~{}'.format(last_block, block_num)
            if console:
                print("{}, {}, {}".format(block_num, block_range, total_time))

            # calc max or min elapsed time
            if max_elapsed_time < total_time:
                max_elapsed_time = total_time
            if min_elapsed_time > total_time:
                min_elapsed_time = total_time

            # excel row data
            excel_row_data.append(block_num)
            excel_row_data.append(block_range)
            excel_row_data.append(total_time)

            # write data to excel 
            for i in range(0, len(excel_row_data)):
                sheet1.write(column, i, excel_row_data[i], set_style())
            column += 1
            last_block = block_num
            last_time = now_time
        f.close()
        if console:
            print("-------- excel data END --------")
        print("[elapsed_time] max: {}, min: {}".format(max_elapsed_time, min_elapsed_time))
    
    result_filename = "{}.xlsx".format(filename.split(".")[0])
    excel_file.save(result_filename) #保存文件

def pre_handle_get_block_log(input="got_block.log", output="block_time.log"):
    excel_file = "{}.xlsx".format(output.split(".")[0])
    cmd = 'rm {} {}'.format(output, excel_file)
    cmd_exec(cmd)

    cmd = 'grep "handle_block" {} | grep "Got block" | cut -d "]" -f 2 | cut -d " " -f 4,17 >> {}'.format(input, output)
    cmd_exec(cmd)


def handle_reIndex_block_log(input="witness_node.log", output="block_time.log"):
    excel_file = "{}.xlsx".format(output.split(".")[0])
    cmd = 'rm {} {}'.format(output, excel_file)
    cmd_exec(cmd)

    cmd = 'grep "test_reindex" {} | grep "handle block" | cut -d "]" -f 3 | cut -d " " -f 3,6 >> {}'.format(input, output)
    cmd_exec(cmd)

def write_sheet_title(sheet, rows, column_widths):
    #生成第一行
    for i in range(0, len(rows)):
        sheet.write(0, i, rows[i], set_style('Times New Roman', 220, True))
        width = column_widths[i]
        if width > 0:
            column = sheet.col(i)
            column.width = width

def handle_reIndex_block_time(filename="handle_block_time.log", console=True):
    print("handle {}".format(filename))
    excel_file = xlwt.Workbook() #创建工作簿

    row0 = [u'区块', u'处理总耗时/单位毫秒']
    column_widths = [256*25, 256*25]

    default = xlwt.easyxf('font: name Arial;') # define style out the loop will work

    # read log data
    with open(filename, 'r') as f:
        last_block = -1
        last_time = 0
        column = 1
        max_elapsed_time = -1
        min_elapsed_time = sys.maxsize
        print("[elapsed_time] init, max: {}, min: {}".format(max_elapsed_time, min_elapsed_time))
        if console:
            print("-------- excel data --------")
            print("block, block range, total_time")
        index = 0
        sheet_max_row_size = 65500
        sheet = None
        for line in f:
            if (index-1) % sheet_max_row_size == 0:
                title = u'获取区块耗时统计{}'.format(last_block+1)
                sheet = excel_file.add_sheet(title, cell_overwrite_ok=True) #创建sheet
                write_sheet_title(sheet, row0, column_widths)
                column = 1
            index += 1
            excel_row_data = []
            tokens = line.split(',')
            block_num = int(tokens[0].strip())
            total_time = float(tokens[1].strip()) * 1000
            total_time = round(total_time, 8)
            if last_block == -1:
                last_block = block_num
                last_time = total_time
                continue

            if console:
                print("{}, {}".format(block_num, total_time))

            # calc max or min elapsed time
            if max_elapsed_time < total_time:
                max_elapsed_time = total_time
            if min_elapsed_time > total_time:
                min_elapsed_time = total_time

            # excel row data
            excel_row_data.append(block_num)
            excel_row_data.append(total_time)

            # write data to excel 
            try:
                for i in range(0, len(excel_row_data)):
                    # sheet.write(column, i, excel_row_data[i], set_style())
                    sheet.write(column, i, excel_row_data[i], default)
            except Exception as e:
                print("excel_row_data: {}".format(excel_row_data))
                print("[ERROR] column: {}, error: {}".format(column, repr(e)))
                break
            column += 1
            last_block = block_num
            last_time = total_time
        f.close()
        if console:
            print("-------- excel data END --------")
        print("[elapsed_time] max: {}, min: {}".format(max_elapsed_time, min_elapsed_time))
    
    result_filename = "{}.xlsx".format(filename.split(".")[0])
    excel_file.save(result_filename) #保存文件

def main():
    input = "witness_node.log"
    output = "block_time.log"
    handle_log(input, output)
    handle(filename=output, console=False)

def test_reIndex():
    input = "witness_node.log"
    output = "reIndex_block_time.log"
    #handle_reIndex_block_log(input, output)
    handle_reIndex_block_time(filename=output, console=False)

def test_handle_get_block():
    #input = "/home/dev/CocosBCX/feature_test/bugfix_cpu/got_block.log"
    #input = "got_block.log"
    #input = "got_block_100_record.log"
    input = "witness_node.log"
    output = "witness_node_block_time_ck_chain_slave_prod_001.log"
    pre_handle_get_block_log(input, output)
    handle_get_block(output)

if __name__ == '__main__':
    # handle(filename="data.log")  
    # main()
    # handle_reindex_block_time()
    #test_reIndex()
    test_handle_get_block()

'''
localhost:reindex a123$ python3 handle_block_time.py 
handle reIndex_block_time.log
[elapsed_time] init, max: -1, min: 9223372036854775807

[elapsed_time] max: 294823.087, min: 0.051
'''
