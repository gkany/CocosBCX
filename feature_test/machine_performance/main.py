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

def machine_cpu_cores():
    cmd_cpu_core = 'cat /proc/cpuinfo| grep "cpu cores"| uniq'
    cpu_core_result = str(subprocess_cmd_exec(cmd_cpu_core), encoding = "utf-8")
    cpu_core_result = cpu_core_result.replace("\n", "")
    cpu_core_result = cpu_core_result.replace("\t", "")
    # print("cpu_core_result: {}".format(cpu_core_result))
    cpu_cores = cpu_core_result.split(":")[1]
    cpu_cores = int(cpu_cores.strip())
    # print("cpu cores: {}".format(cpu_cores))
    return cpu_cores

def exec_sysbench_cpu(output="sysbench_test"):
    max_requests = 20000  # 2w
    cpu_max_prime = 50000 # 5w

    # #for test 
    # max_requests = 200  # 200
    # cpu_max_prime = 500 # 500

    # 1. get cpu cores and sysbench cpu 
    cpu_cores = machine_cpu_cores()
    cpu_results = []
    i = 1
    while i <= cpu_cores: 
        cmd = "sysbench --num-threads={} --max-requests={} --test=cpu --cpu-max-prime={} run".format(
            i, max_requests, cpu_max_prime)
        cmd_result = str(subprocess_cmd_exec(cmd), encoding = "utf-8")
        cpu_result = {}
        results = cmd_result.split("\n")
        for line in results:
            line = line.strip()
            if line.find("Number of threads") != -1:
                threads = line.split(":")[1].strip()
                cpu_result["threads"] = threads
            elif line.find("total time:") != -1:
                total_time = line.split(":")[1].strip()
                cpu_result["total_time"] = total_time
            elif line.find("total number of events:") != -1:
                total_events = line.split(":")[1].strip()
                cpu_result["total_events"] = total_events
            elif line.find("total time taken by event execution:") != -1:
                total_event_time = line.split(":")[1].strip()
                cpu_result["total_event_time"] = total_event_time
            elif line.find("min:") != -1:
                per_req_min_time = line.split(":")[1].strip()
                cpu_result["min"] = per_req_min_time
            elif line.find("avg:") != -1:
                per_req_avg_time = line.split(":")[1].strip()
                cpu_result["avg"] = per_req_avg_time
            elif line.find("max:") != -1:
                per_req_max_time = line.split(":")[1].strip()
                cpu_result["max"] = per_req_max_time
        cpu_result["max_requests"] = max_requests
        cpu_result["max_prime"] = cpu_max_prime
        cpu_results.append(cpu_result)
        i = 2*i
    # print(cpu_results)

    # 2. write file 
    excel_file = xlwt.Workbook() #创建工作簿

    row0 = ['线程数', '最大请求数', '计算最大素数', '时间', '最小', '最大', '平均']
    print(row0)

    default = xlwt.easyxf('font: name Arial;') # define style out the loop will work
    title = u'sysbench cpu'
    sheet = excel_file.add_sheet(title, cell_overwrite_ok=True) #创建sheet
    write_sheet_title(sheet, row0)

    # write data to excel 
    column = 1
    for cpu_result in cpu_results:
        # print(">>> {}".format(cpu_result))
        excel_row_data = []
        excel_row_data.append(cpu_result["threads"])
        excel_row_data.append(cpu_result["max_requests"])
        excel_row_data.append(cpu_result["max_prime"])
        excel_row_data.append(cpu_result["total_time"])
        excel_row_data.append(cpu_result["min"])
        excel_row_data.append(cpu_result["max"])
        excel_row_data.append(cpu_result["avg"])
        print(excel_row_data)

        try:
            for i in range(0, len(excel_row_data)):
                # sheet.write(column, i, excel_row_data[i], set_style())
                sheet.write(column, i, excel_row_data[i], default)
        except Exception as e:
            print("excel_row_data: {}".format(excel_row_data))
            print("[ERROR] column: {}, error: {}".format(column, repr(e)))
            break
        column += 1
    result_filename = "{}.xlsx".format(output)
    excel_file.save(result_filename) #保存文件

def cpu_performance_test(output="cpu_performance", console=True):
    print("handle {}".format(filename))
    pass

def main():
    exec_sysbench_cpu()
    pass

if __name__ == '__main__':
    main()

'''
dev@ubuntu:~/data/mrepo/CocosBCX/feature_test/machine_performance$ python3 main.py 
>>> cat /proc/cpuinfo| grep "cpu cores"| uniq
>>> sysbench --num-threads=1 --max-requests=20000 --test=cpu --cpu-max-prime=50000 run
>>> sysbench --num-threads=2 --max-requests=20000 --test=cpu --cpu-max-prime=50000 run
>>> sysbench --num-threads=4 --max-requests=20000 --test=cpu --cpu-max-prime=50000 run
['线程数', '最大请求数', '计算最大素数', '时间', '最小', '最大', '平均']
['1', 20000, 50000, '182.2933s', '8.61ms', '13.43ms', '9.11ms']
['2', 20000, 50000, '113.5063s', '7.37ms', '73.35ms', '11.35ms']
['4', 20000, 50000, '53.7401s', '8.80ms', '24.73ms', '10.75ms']
'''
