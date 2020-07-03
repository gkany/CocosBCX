#!/bin/sh

bin="cli_wallet"
log=${bin}".log"

chain_id="c1ac4bb7bd7d94874a1cb98b39a8a582421d03d022dfa4be8c70567076e03ad0"

pkill ${bin}
sleep 1
nohup ./${bin} --chain-id ${chain_id}  -s ws://test.cocosbcx.net -r 0.0.0.0:8047 -d  >> ${log}  2>&1 &
sleep 1

if [ $# -gt 0 ]; then
    curl http://127.0.0.1:8047 -d '{"jsonrpc": "2.0", "method": "set_password", "params": ["123"], "id": 1}' >> ${log}
    curl http://127.0.0.1:8047 -d '{"jsonrpc": "2.0", "method": "unlock", "params": ["123"], "id": 1}' >> ${log}
    curl http://127.0.0.1:8047 -d '{"jsonrpc": "2.0", "method": "import_key", "params": ["nicotest", "5J2SChqa9QxrCkdMor9VC2k9NT4R4ctRrJA6odQCPkb3yL89vxo"], "id": 1}' >> ${log}
else
    curl http://127.0.0.1:8047 -d '{"jsonrpc": "2.0", "method": "unlock", "params": ["123"], "id": 1}' >> ${log}
fi

