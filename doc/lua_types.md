# Cocos-BCX lua types 类型说明

-----------

## 1. lua types类型

lua_types类型是Cocos-BCX链上对类型进行的封装，在c++和lua合约中通用。

``` c++
typedef static_variant<
    LUATYPE_NAME(int),    //0
    LUATYPE_NAME(number), //1
    LUATYPE_NAME(string), //2
    LUATYPE_NAME(bool),   //3
    LUATYPE_NAME(table),  //4
    LUATYPE_NAME(function), //5
    lua_userdata>         //6
    lua_types;
```



## 2. 合约调用

> 说明：这里以cli_wallet 合约调用为例来说明lua_types的使用格式

### 2.1 cli_wallet合约调用接口

``` c++
    pair<tx_hash_type, signed_transaction> call_contract_function(
        string account_id_or_name, 
        string contract_id_or_name, 
        string function_name, 
        vector<lua_types> value_list, 
        bool broadcast = false
    );
```

#### 2.1.2 lua_types格式

``` json
[lua_type_index, {"v":lua_type_data}]
```

对象类型是二元数组，包含值类型和值数据，二元数组说明如下：([0] 数组第0个元素，[1]数组第一个元素)

``` text
[0] -- lua_type_index
对应lua语言数据类型，类型索引编号如下：
> int 			-- 0 
> number		-- 1
> string 		-- 2
> bool 			-- 3
> table			-- 4
> function		-- 5
> userdata 		-- 6

[1] -- data_object
数据对象

```



#### 2.1.3 value_list 格式

  ``` json
  [
  	[ lua_type_index1, {"v": lua_type_data1} ], 
      [ lua_type_index2, {"v": lua_type_data2} ], 
      ... 
  ]
  ```

#### 2.1.4 lua_type对象示例 -- 基础类型

> 基础类型 : int bool string number

* 单个参数

  ``` python
  [0, {"v": 1}]
  
  [1, {"v": 3.14}]
  
  [2, {"v": "lua type test string"}]
  
  [3, {"v": True}]
  
  [3, {"v": False}]
  
  [4, {"v": [
               [ {"key":[2,{"v":"name"}]},
                	[2, {"v":"zhang3"}]
               ],
               [ {"key":[2,{"v":"age"}]},
                	[0, {"v":22}]
               ],
               [ {"key":[2,{"v":"sex"}]},
                	[2, {"v":"man"}]
               ],
               [ {"key":[2,{"v":"height"}]},
                	[0, {"v":170}]
               ],
               [ {"key":[2,{"v":"weight"}]},
                	[1, {"v":65.3}]
               ],
               [ {"key":[2,{"v":"address"}]},
                	[2,{"v":"beijing chaoyang wangjing"}]
               ],
               [ {"key":[2,{"v":"is_student"}]},
                	[3, {"v":False}]
               ]
       	 ]
        }
    ]
  ```

  

#### 2.1.5 lua_type对象示例 -- 复杂类型 lua_function

  lua_function数据结构：

``` c++
struct FunctionSummary
{    //处理lua函数信息
     //short arg_num;  //入参个数
     //short ret_num;  //返回值个数
    bool is_var_arg;                  //是否为可变参数
    std::vector<std::string> arglist; //入参参数名，按序push
};

typedef struct FunctionSummary lua_function;
```

示例：

a. 无参

``` json
[
    5,
    {
        "is_var_arg": false,
        "arglist": []
    }
]
```



b. 有参

``` json
[
    5,
    {
        "is_var_arg": false,
        "arglist": [
            "num",
            "amount"
        ]
    }
]
```



#### 2.1.6 lua_type对象示例 -- 复杂类型 lua_userdata

数据结构：

``` c++
#define lua_userdata memo_data, asset /*6*/

struct asset
{
    share_type    amount; 
    asset_id_type asset_id;  // class asset_object对象id，asset_object可参考链上COCOS、GAS结构

};

struct memo_data
{
    public_key_type from;
    public_key_type to;
    uint64_t nonce = 0;
    vector<char> message;
};

```

说明：

* memo_data 示例：

  ``` json
  {
      "from": "COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx",
      "to": "COCOS5TrJztVAY5F9aWDw5KtDHfdrffQn7F3sjgbL8YyssiKhVCLNf7",
      "nonce": "8144095480802660175",
      "message": "4246403acf98b22f78f13a5dd76f2977"
  }
  ```

  



## 3. 合约数据

合约数据是lua_map结构：

lua_map本质是一个map，key 类型：lua_key，value 类型：lua_types

``` c++
typedef std::map<lua_key, lua_types> lua_map;
```

lua_key是lua_types的子集，有如下四种类型：

``` TEXT
int 			-- 0 
number			-- 1
string 			-- 2
bool 			-- 3
```

数据格式示例如下：

``` json
[
    [ {"key":[2,{"v":"height"}]}, [0, {"v":170}] ],
    [ {"key":[2,{"v":"weight"}]}, [1, {"v":65.3}] ],
    [ {"key":[2,{"v":"address"}]}, [2,{"v":"beijing chaoyang wangjing"}] ],
    [ {"key":[2,{"v":"is_student"}]}, [3, {"v":False}] ]
]
```



实际合约数据格式：

``` json
{
    "id": "1.16.1",
    "creation_date": "2019-12-02T10:15:40",
    "owner": "1.2.22",
    "name": "contract.test1relevant2data",
    "user_invoke_share_percent": 100,
    "current_version": "a60ca8366b607830697081a4ee53e86b6b76ad5b52aa18102c046b7d27b011b4",
    "contract_authority": "COCOS7RccjsewZQrLVEq7qKkmB5w1CxxocD9NFD2mdKUJAN7rudvcir",
    "is_release": false,
    "check_contract_authority": false,
    "contract_data": [
        [
            {
                "key": [
                    2,
                    {
                        "v": "account"
                    }
                ]
            },
            [
                4,
                {
                    "v": [
                        [
                            {
                                "key": [
                                    0,
                                    {
                                        "v": 1
                                    }
                                ]
                            },
                            [
                                2,
                                {
                                    "v": "adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"
                                }
                            ]
                        ],
                        [
                            {
                                "key": [
                                    0,
                                    {
                                        "v": 2
                                    }
                                ]
                            },
                            [
                                2,
                                {
                                    "v": "adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"
                                }
                            ]
                        ],
                        [
                            {
                                "key": [
                                    0,
                                    {
                                        "v": 3
                                    }
                                ]
                            },
                            [
                                2,
                                {
                                    "v": "adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"
                                }
                            ]
                        ],
                        [
                            {
                                "key": [
                                    0,
                                    {
                                        "v": 4
                                    }
                                ]
                            },
                            [
                                2,
                                {
                                    "v": "adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"
                                }
                            ]
                        ],
                        [
                            {
                                "key": [
                                    0,
                                    {
                                        "v": 5
                                    }
                                ]
                            },
                            [
                                2,
                                {
                                    "v": "adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"
                                }
                            ]
                        ],
                        [
                            {
                                "key": [
                                    0,
                                    {
                                        "v": 6
                                    }
                                ]
                            },
                            [
                                2,
                                {
                                    "v": "adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"
                                }
                            ]
                        ],
                        [
                            {
                                "key": [
                                    0,
                                    {
                                        "v": 7
                                    }
                                ]
                            },
                            [
                                2,
                                {
                                    "v": "adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"
                                }
                            ]
                        ],
                        [
                            {
                                "key": [
                                    0,
                                    {
                                        "v": 8
                                    }
                                ]
                            },
                            [
                                2,
                                {
                                    "v": "adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"
                                }
                            ]
                        ],
                        [
                            {
                                "key": [
                                    0,
                                    {
                                        "v": 9
                                    }
                                ]
                            },
                            [
                                2,
                                {
                                    "v": "adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"
                                }
                            ]
                        ],
                        [
                            {
                                "key": [
                                    0,
                                    {
                                        "v": 10
                                    }
                                ]
                            },
                            [
                                2,
                                {
                                    "v": "adsssssssssssssssssssssoooooooooooooooooooooooooooooooooooo"
                                }
                            ]
                        ]
                    ]
                }
            ]
        ],
        [
            {
                "key": [
                    2,
                    {
                        "v": "sfdafdsa"
                    }
                ]
            },
            [
                0,
                {
                    "v": 666
                }
            ]
        ]
    ],
    "contract_ABI": [
        [
            {
                "key": [
                    2,
                    {
                        "v": "contract_data"
                    }
                ]
            },
            [
                5,
                {
                    "is_var_arg": false,
                    "arglist": []
                }
            ]
        ]
    ],
    "lua_code_b_id": "2.2.1"
}

```





