## 1. get_contract 接口

``` shell
dev@ubuntu:~$ curl https://test.cocosbcx.net -d '{"id":1, "method":"call", "params":[0,"get_contract",["1.16.1"]]}' && echo ""
```



## 2. get_contract_public_data 接口

### 2.1 获取完整数据

``` shell
dev@ubuntu:~$ curl https://test.cocosbcx.net -d '{"id":1, "method":"call", "params":[0,"get_contract_public_data",["1.16.1", []]]}' && echo ""

{"id":1,"jsonrpc":"2.0","result":[[{"key":[2,{"v":"account"}]},[4,{"v":[[{"key":[0,{"v":1}]},[2,{"v":"adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"}]],[{"key":[0,{"v":2}]},[2,{"v":"adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"}]],[{"key":[0,{"v":3}]},[2,{"v":"adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"}]],[{"key":[0,{"v":4}]},[2,{"v":"adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"}]],[{"key":[0,{"v":5}]},[2,{"v":"adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"}]],[{"key":[0,{"v":6}]},[2,{"v":"adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"}]],[{"key":[0,{"v":7}]},[2,{"v":"adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"}]],[{"key":[0,{"v":8}]},[2,{"v":"adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"}]],[{"key":[0,{"v":9}]},[2,{"v":"adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"}]],[{"key":[0,{"v":10}]},[2,{"v":"adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"}]]]}]],[{"key":[2,{"v":"sfdafdsa"}]},[0,{"v":666}]]]}
```



### 2.2 获取指定key的数据

#### 2.2.1 使用合约ID

``` shell
dev@ubuntu:~$ curl https://test.cocosbcx.net -d '{"id":1, "method":"call", "params":[0,"get_contract_public_data",["1.16.1", [[{"key":[2,{"v":"sfdafdsa"}]}]]]]}' && echo ""

{"id":1,"jsonrpc":"2.0","result":[[{"key":[2,{"v":"sfdafdsa"}]},[0,{"v":666}]]]}

```



#### 2.2.2 使用合约名

``` shell
dev@ubuntu:~$ curl https://test.cocosbcx.net -d '{"id":1, "method":"call", "params":[0,"get_contract_public_data",["contract.test1relevant2data", [[{"key":[2,{"v":"account"}]}]]]]}' && echo "" 
```



#### 2.2.3 多个key

``` shell
dev@ubuntu:~$ curl https://test.cocosbcx.net -d '{"id":1, "method":"call", "params":[0,"get_contract_public_data",["contract.test1relevant2data", [[{"key":[2,{"v":"account"}]}]]]]}' && echo "" 
{"id":1,"jsonrpc":"2.0","result":[[{"key":[2,{"v":"account"}]},[4,{"v":[[{"key":[0,{"v":1}]},[2,{"v":"adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"}]],[{"key":[0,{"v":2}]},[2,{"v":"adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"}]],[{"key":[0,{"v":3}]},[2,{"v":"adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"}]],[{"key":[0,{"v":4}]},[2,{"v":"adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"}]],[{"key":[0,{"v":5}]},[2,{"v":"adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"}]],[{"key":[0,{"v":6}]},[2,{"v":"adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"}]],[{"key":[0,{"v":7}]},[2,{"v":"adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"}]],[{"key":[0,{"v":8}]},[2,{"v":"adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"}]],[{"key":[0,{"v":9}]},[2,{"v":"adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"}]],[{"key":[0,{"v":10}]},[2,{"v":"adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"}]]]}]]]}

```

