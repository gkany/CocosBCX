#########################################################################
# File Name: start.sh
# Author: xxx
# mail: xxx
# Created Time: Wed 18 Mar 2020 07:22:08 AM EDT
#########################################################################
#!/bin/bash

#node=$1
node=${1:-"witness_node"}
nohup ./${node} --genesis-json genesis.json -d witness_node_data_dir >> witness_node.log 2>&1 &

