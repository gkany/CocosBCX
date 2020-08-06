# -*- coding: utf-8 -*- 

import time 
import xlwt 
import sys
import os
import subprocess

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
    return os.system(cmd)

def subprocess_cmd_exec(cmd, log=True):
    if log:
        print('>>> {}'.format(cmd))
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout
    return pipe.read()

def write_sheet_title(sheet, rows, column_widths=None):
    #生成第一行
    for i in range(0, len(rows)):
        sheet.write(0, i, rows[i], set_style('Times New Roman', 220, True))
        
        width = 256*25
        if column_widths:
            width = column_widths[i]
        if width > 0:
            column = sheet.col(i)
            column.width = width

def top_monitor(pid=None):
    if not pid:
        print("NO PID. EXIT")

    cmd = "top -pid {}".format(pid)
    cmd_result = str(subprocess_cmd_exec(cmd), encoding = "utf-8")
    print(cmd_result)


def test_node_run_mainjs():
    cmd = 'ps -ef  | grep "WeChat"  | grep -v "grep"'
    #cmd = "top -pid {}".format(pid)
    cmd_result = str(subprocess_cmd_exec(cmd), encoding = "utf-8")
    print(cmd_result)
    tokens = cmd_result.split()
    print("tokens: {}".format(tokens))
    pid = tokens[1]
    print("pid: {}".format(pid))
    result = top_monitor(pid)


def main():
    test_node_run_mainjs()
    pass


if __name__ == '__main__':
    main()

