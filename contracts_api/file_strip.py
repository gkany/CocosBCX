#-*- coding: utf-8  -*-

import sys

def new_file_name(old_file_name, token):
    if old_file_name.find(".") != -1:
        tokens = old_file_name.split(".")
        # print(tokens)
        tokens2 = tokens[:-1]
        # print(tokens2)
        file_name = "{}_{}.{}".format(''.join(tokens2), token, tokens[-1])
        print(file_name)
        return file_name
    else
        return old_file_name + "_" + token

def line_strip(src_file_name, dst_file_name):
    src_file = open(src_file_name, 'r')
    dst_file = open(dst_file_name, "w+")
    for line in src_file.readlines():
        dst_file.write(line.strip()+"\n")
    src_file.close()
    dst_file.close()

def line_lstrip(src_file_name, dst_file_name):
    src_file = open(src_file_name, 'r')
    dst_file = open(dst_file_name, "w+")
    for line in src_file.readlines():
        dst_file.write(line.lstrip()+"\n")
    src_file.close()
    dst_file.close()

def line_rstrip(src_file_name, dst_file_name):
    src_file = open(src_file_name, 'r')
    dst_file = open(dst_file_name, "w+")
    for line in src_file.readlines():
        dst_file.write(line.rstrip()+"\n")
    src_file.close()
    dst_file.close()

def main(file_name, strip_type):
    dst_file_name = new_file_name(file_name, strip_type)
    if strip_type == "lstrip":
        line_lstrip(file_name, dst_file_name)
    elif strip_type == "rstrip":
        line_rstrip(file_name, dst_file_name)
    else:
        line_strip(file_name, dst_file_name)

if __name__ == '__main__':
    print('>> {}\n'.format(sys.argv))
    if len(sys.argv) >= 2:
        file_name = sys.argv[1]
        if len(sys.argv) >= 3:
            strip_type = sys.argv[2]
        else:
            strip_type = "strip"
        main(file_name, strip_type)
    else:
        print("Usage:\n./{} file_name strip_type \n".format(sys.argv[0]))
