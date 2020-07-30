app=${1:-"continuity_monitor.py"}
cmd="python3 "${app}
echo ${cmd}
nohup  ${cmd}  >> ./console.log 2>&1 &

