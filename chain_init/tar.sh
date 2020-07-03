#########################################################################
# File Name: tar.sh
# Author: xxx
# mail: xxx
# Created Time: Wed 27 May 2020 02:41:42 AM UTC
#########################################################################
#!/bin/bash

file=$1
tar -zcvf  ${file}.tar.gz  $file

