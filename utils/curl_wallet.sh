#!/bin/sh

password="123456"
cli_wallet_url="http://127.0.0.1:8048"

#curl $cli_wallet_url d '{"jsonrpc": "2.0", "method": "set_password", "params": ["123"], "id": 1}' && echo " "
curl $cli_wallet_url -d '{"jsonrpc": "2.0", "method": "info", "params": [], "id": 1}' && echo " "

curl $cli_wallet_url -d '{"jsonrpc": "2.0", "method": "unlock", "params": ['${password}'], "id": 1}' && echo " "


curl $cli_wallet_url -d '{"jsonrpc": "2.0", "method": "suggest_brain_key", "params": [], "id": 1}' && echo " "
