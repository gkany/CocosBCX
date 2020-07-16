#########################################################################
# File Name: start.sh
# Author: xxx
# mail: xxx
# Created Time: Wed 18 Mar 2020 07:22:08 AM EDT
#########################################################################
#!/bin/bash

dir="witness_node_data_dir"
rm -rf $dir
mkdir $dir
cp config.ini ${dir}/config.ini 

#node="witness_node"
node=${1:-"witness_node"}
nohup ./${node} --genesis-json genesis.json -d witness_node_data_dir >> witness_node.log 2>&1 &


