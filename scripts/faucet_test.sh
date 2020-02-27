## testnet
base_url="test-faucet.cocosbcx.net"
echo $base_url
curl https://${base_url}/api/v1/accounts -H "Content-Type:application/json" -H "authorization:YnVmZW5nQDIwMThidWZlbmc="  -X POST --data '{"account":{"name":"test300","owner_key":"COCOS8J2bZ2r96WKJcePL22975Qh94qrfZ8LsK7mkc44nsoJrDQmCao","referror":"","memo_key":"COCOS51EP3KzxW42gzsmmwMEqvejkHRohKkgZEfpktbWkN4uFDXMs2B","active_key":"COCOS51EP3KzxW42gzsmmwMEqvejkHRohKkgZEfpktbWkN4uFDXMs2B"}}'

echo " "


## mainnet
#base_url="faucet.cocosbcx.net"

#base_url="http://test-faucet.cocosbcx.net"
#echo $base_url
#curl https://${base_url}/api/v1/accounts -H "Content-Type:application/json" -H "authorization:YnVmZW5nQDIwMThidWZlbmc="  -X POST --data '{"account":{"name":"tess11","owner_key":"COCOS8J2bZ2r96WKJcePL22975Qh94qrfZ8LsK7mkc44nsoJrDQmCao","referror":"","memo_key":"COCOS51EP3KzxW42gzsmmwMEqvejkHRohKkgZEfpktbWkN4uFDXMs2B","active_key":"COCOS51EP3KzxW42gzsmmwMEqvejkHRohKkgZEfpktbWkN4uFDXMs2B"}}'

#echo " "

