## testnet
base_url="faucet.cocosbcx.net"
echo $base_url
curl https://${base_url}/api/v1/accounts -H "Content-Type:application/json" -H "authorization:YnVmZW5nQDIwMThidWZlbmc="  -X POST --data '{"account":{"name":"test302","owner_key":"COCOS6PYytLNg45crj81jqVXFrZTExMDmNTctX3jDWhzWT9ikJzmEuw","referror":"","memo_key":"COCOS6PYytLNg45crj81jqVXFrZTExMDmNTctX3jDWhzWT9ikJzmEuw","active_key":"COCOS6PYytLNg45crj81jqVXFrZTExMDmNTctX3jDWhzWT9ikJzmEuw"}}'

echo " "


