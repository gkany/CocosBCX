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

def exec_sysbench_cpu(output="dev_sysbench_cpu_test"):
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

'''
    sysbench --num-threads=2 --test=fileio --file-total-size=1G --file-test-mode=rndrw prepare
    sysbench --num-threads=2 --test=fileio --file-total-size=2G --file-test-mode=rndrw run
    sysbench --num-threads=2 --test=fileio --file-total-size=2G --file-test-mode=rndrw cleanup
    连续/顺序写(seqwr)、连续改写(seqrewr)、连续读(seqrd)、随机读(rndrd)、随机写(rndwr)、随机读写(rndrw)
'''
def exec_sysbench_io(output="dev_sysbench_io_test"):
    # 1. get cpu cores and sysbench fileio 
    total_size = '3G'
    test_modes = ["seqwr", "seqrewr", "seqrd", "rndrd", "rndwr", "rndrw"]
    io_cores = machine_cpu_cores()
    io_results = []
    for test_mode in test_modes:
        i = 1
        while i <= io_cores: 
            # 1. prepare
            cmd_prepare = 'sysbench --num-threads={} --test=fileio --file-total-size={} --file-test-mode={} prepare'.format(
                i, total_size, test_mode)
            cmd_result = str(subprocess_cmd_exec(cmd_prepare), encoding = "utf-8")

            # 2. run and result handle
            cmd_prepare = 'sysbench --num-threads={} --test=fileio --file-total-size={} --file-test-mode={} run'.format(
                i, total_size, test_mode)
            cmd_run_result = str(subprocess_cmd_exec(cmd_prepare), encoding = "utf-8")

            # 3. cleanup
            cmd_prepare = 'sysbench --num-threads={} --test=fileio --file-total-size={} --file-test-mode={} cleanup'.format(
                i, total_size, test_mode)
            cmd_result = str(subprocess_cmd_exec(cmd_prepare), encoding = "utf-8")

            io_result = {}
            results = cmd_run_result.split("\n")
            for line in results:
                line = line.strip()
                if line.find("Number of threads") != -1:
                    threads = line.split(":")[1].strip()
                    io_result["threads"] = threads
                elif line.find("total time:") != -1:
                    total_time = line.split(":")[1].strip()
                    io_result["total_time"] = total_time
                elif line.find("total number of events:") != -1:
                    total_events = line.split(":")[1].strip()
                    io_result["total_events"] = total_events
                elif line.find("total time taken by event execution:") != -1:
                    total_event_time = line.split(":")[1].strip()
                    io_result["total_event_time"] = total_event_time
                elif line.find("min:") != -1:
                    per_req_min_time = line.split(":")[1].strip()
                    io_result["min"] = per_req_min_time
                elif line.find("avg:") != -1:
                    per_req_avg_time = line.split(":")[1].strip()
                    io_result["avg"] = per_req_avg_time
                elif line.find("max:") != -1:
                    per_req_max_time = line.split(":")[1].strip()
                    io_result["max"] = per_req_max_time
                elif line.find("Read") != -1 and line.find("Written") != -1 and line.find("Total") != -1:
                    # Read 93.766Mb  Written 62.516Mb  Total transferred 156.28Mb  (105.73Mb/sec)
                    speed = line.split("(")[1][0:-1]
                    io_result["speed"] = speed
            io_result["mode"] = test_mode
            io_result["total_size"] = total_size
            io_results.append(io_result)
            i = 2*i
    # print(io_results)

    # 2. write file 
    excel_file = xlwt.Workbook() #创建工作簿

    row0 = ["线程数", "测试模式", "文件大小", "传输速度", "总执行时间", "最小", "最大", "平均"]
    print(row0)

    default = xlwt.easyxf('font: name Arial;') # define style out the loop will work
    title = u'sysbench io'
    sheet = excel_file.add_sheet(title, cell_overwrite_ok=True) #创建sheet
    write_sheet_title(sheet, row0)

    # write data to excel 
    column = 1
    for io_result in io_results:
        # print(">>> {}".format(io_result))
        excel_row_data = []
        excel_row_data.append(io_result["threads"])
        excel_row_data.append(io_result["mode"])
        excel_row_data.append(io_result["total_size"])
        excel_row_data.append(io_result["speed"])
        excel_row_data.append(io_result["total_time"])
        excel_row_data.append(io_result["min"])
        excel_row_data.append(io_result["max"])
        excel_row_data.append(io_result["avg"])
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


# sysbench --test=memory --memory-total-size=200G --memory-oper=read run
def exec_sysbench_memory(output="dev_sysbench_memory_test"):
    total_size = '200G'
    memory_opers = ['read', 'write']

    # 1. get memory cores and sysbench memory 
    memory_results = []
    for oper in memory_opers:
        cmd = "sysbench --test=memory --memory-total-size={} --memory-oper={} run".format(
            total_size, oper)
        cmd_result = str(subprocess_cmd_exec(cmd), encoding = "utf-8")
        memory_result = {}
        results = cmd_result.split("\n")
        for line in results:
            line = line.strip()
            if line.find("Number of threads") != -1:
                threads = line.split(":")[1].strip()
                memory_result["threads"] = threads
            elif line.find("total time:") != -1:
                total_time = line.split(":")[1].strip()
                memory_result["total_time"] = total_time
            elif line.find("total number of events:") != -1:
                total_events = line.split(":")[1].strip()
                memory_result["total_events"] = total_events
            elif line.find("total time taken by event execution:") != -1:
                total_event_time = line.split(":")[1].strip()
                memory_result["total_event_time"] = total_event_time
            elif line.find("min:") != -1:
                per_req_min_time = line.split(":")[1].strip()
                memory_result["min"] = per_req_min_time
            elif line.find("avg:") != -1:
                per_req_avg_time = line.split(":")[1].strip()
                memory_result["avg"] = per_req_avg_time
            elif line.find("max:") != -1:
                per_req_max_time = line.split(":")[1].strip()
                memory_result["max"] = per_req_max_time
            elif line.find("Operations performed:") != -1:
                op_speed = line.split("(")[1][0:-1]
                memory_result["op_speed"] = op_speed
            elif line.find("transferred") != -1:
                speed = line.split("(")[1][0:-1]
                memory_result["speed"] = speed
        memory_result["mode"] = oper
        memory_result["total_size"] = total_size
        memory_results.append(memory_result)
    # print(memory_results)

    # 2. write file 
    excel_file = xlwt.Workbook() #创建工作簿

    row0 = ["线程数", "测试模式", "总测试数据", "传输性能", "传输速度", "总执行时间", "最小", "最大", "平均"]
    print(row0)

    default = xlwt.easyxf('font: name Arial;') # define style out the loop will work
    title = u'sysbench memory'
    sheet = excel_file.add_sheet(title, cell_overwrite_ok=True) #创建sheet
    write_sheet_title(sheet, row0)

    # write data to excel 
    column = 1
    for memory_result in memory_results:
        # print(">>> {}".format(memory_result))
        excel_row_data = []
        excel_row_data.append(memory_result["threads"])
        excel_row_data.append(memory_result["mode"])
        excel_row_data.append(memory_result["total_size"])
        excel_row_data.append(memory_result["op_speed"])
        excel_row_data.append(memory_result["speed"])
        excel_row_data.append(memory_result["total_time"])
        excel_row_data.append(memory_result["min"])
        excel_row_data.append(memory_result["max"])
        excel_row_data.append(memory_result["avg"])
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

#################################  rebuild  ###################################
def sysbench_cpu():
    max_requests = 20000  # 2w
    cpu_max_prime = 50000 # 5w

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
    return cpu_results

def sysbench_io():
    # 1. get cpu cores and sysbench fileio 
    total_size = '3G'
    test_modes = ["seqwr", "seqrewr", "seqrd", "rndrd", "rndwr", "rndrw"]
    io_cores = machine_cpu_cores()
    io_results = []
    for test_mode in test_modes:
        i = 1
        while i <= io_cores: 
            # 1. prepare
            cmd_prepare = 'sysbench --num-threads={} --test=fileio --file-total-size={} --file-test-mode={} prepare'.format(
                i, total_size, test_mode)
            cmd_result = str(subprocess_cmd_exec(cmd_prepare), encoding = "utf-8")

            # 2. run and result handle
            cmd_prepare = 'sysbench --num-threads={} --test=fileio --file-total-size={} --file-test-mode={} run'.format(
                i, total_size, test_mode)
            cmd_run_result = str(subprocess_cmd_exec(cmd_prepare), encoding = "utf-8")

            # 3. cleanup
            cmd_prepare = 'sysbench --num-threads={} --test=fileio --file-total-size={} --file-test-mode={} cleanup'.format(
                i, total_size, test_mode)
            cmd_result = str(subprocess_cmd_exec(cmd_prepare), encoding = "utf-8")

            io_result = {}
            results = cmd_run_result.split("\n")
            for line in results:
                line = line.strip()
                if line.find("Number of threads") != -1:
                    threads = line.split(":")[1].strip()
                    io_result["threads"] = threads
                elif line.find("total time:") != -1:
                    total_time = line.split(":")[1].strip()
                    io_result["total_time"] = total_time
                elif line.find("total number of events:") != -1:
                    total_events = line.split(":")[1].strip()
                    io_result["total_events"] = total_events
                elif line.find("total time taken by event execution:") != -1:
                    total_event_time = line.split(":")[1].strip()
                    io_result["total_event_time"] = total_event_time
                elif line.find("min:") != -1:
                    per_req_min_time = line.split(":")[1].strip()
                    io_result["min"] = per_req_min_time
                elif line.find("avg:") != -1:
                    per_req_avg_time = line.split(":")[1].strip()
                    io_result["avg"] = per_req_avg_time
                elif line.find("max:") != -1:
                    per_req_max_time = line.split(":")[1].strip()
                    io_result["max"] = per_req_max_time
                elif line.find("Read") != -1 and line.find("Written") != -1 and line.find("Total") != -1:
                    # Read 93.766Mb  Written 62.516Mb  Total transferred 156.28Mb  (105.73Mb/sec)
                    speed = line.split("(")[1][0:-1]
                    io_result["speed"] = speed
            io_result["mode"] = test_mode
            io_result["total_size"] = total_size
            io_results.append(io_result)
            i = 2*i
    # print(io_results)
    return io_results

def sysbench_memory():
    total_size = '200G'
    memory_opers = ['read', 'write']

    # 1. get memory cores and sysbench memory 
    memory_results = []
    for oper in memory_opers:
        cmd = "sysbench --test=memory --memory-total-size={} --memory-oper={} run".format(
            total_size, oper)
        cmd_result = str(subprocess_cmd_exec(cmd), encoding = "utf-8")
        memory_result = {}
        results = cmd_result.split("\n")
        for line in results:
            line = line.strip()
            if line.find("Number of threads") != -1:
                threads = line.split(":")[1].strip()
                memory_result["threads"] = threads
            elif line.find("total time:") != -1:
                total_time = line.split(":")[1].strip()
                memory_result["total_time"] = total_time
            elif line.find("total number of events:") != -1:
                total_events = line.split(":")[1].strip()
                memory_result["total_events"] = total_events
            elif line.find("total time taken by event execution:") != -1:
                total_event_time = line.split(":")[1].strip()
                memory_result["total_event_time"] = total_event_time
            elif line.find("min:") != -1:
                per_req_min_time = line.split(":")[1].strip()
                memory_result["min"] = per_req_min_time
            elif line.find("avg:") != -1:
                per_req_avg_time = line.split(":")[1].strip()
                memory_result["avg"] = per_req_avg_time
            elif line.find("max:") != -1:
                per_req_max_time = line.split(":")[1].strip()
                memory_result["max"] = per_req_max_time
            elif line.find("Operations performed:") != -1:
                op_speed = line.split("(")[1][0:-1]
                memory_result["op_speed"] = op_speed
            elif line.find("transferred") != -1:
                speed = line.split("(")[1][0:-1]
                memory_result["speed"] = speed
        memory_result["mode"] = oper
        memory_result["total_size"] = total_size
        memory_results.append(memory_result)
    # print(memory_results)
    return memory_results

def exec_sysbench(output="dev_sysbench_test"):
    excel_file = xlwt.Workbook() #创建工作簿

    # 1. write sysbench cpu result
    print("----------------------------------------------------------------")
    print("------------------- sysbench cpu ------------------------")
    cpu_results = sysbench_cpu()
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

    # 2. write sysbench io result 
    print("------------------- sysbench io -------------------------")
    io_results = sysbench_io()
    row0 = ["线程数", "测试模式", "文件大小", "传输速度", "总执行时间", "最小", "最大", "平均"]
    print(row0)

    default = xlwt.easyxf('font: name Arial;') # define style out the loop will work
    title = u'sysbench io'
    sheet = excel_file.add_sheet(title, cell_overwrite_ok=True) #创建sheet
    write_sheet_title(sheet, row0)

    # write data to excel 
    column = 1
    for io_result in io_results:
        # print(">>> {}".format(io_result))
        excel_row_data = []
        excel_row_data.append(io_result["threads"])
        excel_row_data.append(io_result["mode"])
        excel_row_data.append(io_result["total_size"])
        excel_row_data.append(io_result["speed"])
        excel_row_data.append(io_result["total_time"])
        excel_row_data.append(io_result["min"])
        excel_row_data.append(io_result["max"])
        excel_row_data.append(io_result["avg"])
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

    # 3. write sysbench memory
    print("------------------- sysbench memory -------------------------")
    memory_results = sysbench_memory()
    row0 = ["线程数", "测试模式", "总测试数据", "传输性能", "传输速度", "总执行时间", "最小", "最大", "平均"]
    print(row0)

    default = xlwt.easyxf('font: name Arial;') # define style out the loop will work
    title = u'sysbench memory'
    sheet = excel_file.add_sheet(title, cell_overwrite_ok=True) #创建sheet
    write_sheet_title(sheet, row0)

    # write data to excel 
    column = 1
    for memory_result in memory_results:
        # print(">>> {}".format(memory_result))
        excel_row_data = []
        excel_row_data.append(memory_result["threads"])
        excel_row_data.append(memory_result["mode"])
        excel_row_data.append(memory_result["total_size"])
        excel_row_data.append(memory_result["op_speed"])
        excel_row_data.append(memory_result["speed"])
        excel_row_data.append(memory_result["total_time"])
        excel_row_data.append(memory_result["min"])
        excel_row_data.append(memory_result["max"])
        excel_row_data.append(memory_result["avg"])
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

def main():
    # exec_sysbench_cpu()
    # exec_sysbench_io()
    # exec_sysbench_memory()
    output = "ck_chain_slave_prod001_sysbench_test"
    output = "ck_ubuntu_dev_sysbench_test"
    exec_sysbench(output)
    pass

if __name__ == '__main__':
    main()

