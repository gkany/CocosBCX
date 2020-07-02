cli_wallet test log
--------------------

## 1. contract api test contract share fee result  
``` json  
unlocked >>> get_object 1.16.2
get_object 1.16.2
[{
    "id": "1.16.2",
    "creation_date": "2020-06-29T05:38:46",
    "owner": "1.2.16",
    "name": "contract.testapi.helloworld",
    "user_invoke_share_percent": 100,
    "current_version": "4cc7d3bc7d7c153af6d273cd707d9de96538bee582ab8f6abeddc51ccd46e52c",
    "contract_authority": "COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx",
    "is_release": false,
    "check_contract_authority": false,
    "contract_data": [],
    "contract_ABI": [[{
          "key": [
            2,{
              "v": "test_helloworld"
            }
          ]
        },[
          5,{
            "is_var_arg": false,
            "arglist": []
          }
        ]
      ]
    ],
    "lua_code_b_id": "2.2.2"
  }
]
unlocked >>> call_contract_function nicotest contract.testapi.helloworld test_helloworld [] true
call_contract_function nicotest contract.testapi.helloworld test_helloworld [] true
[
  "32dbbcdcf938e32487ea3b3c89cafee1813f5da0b337358dcfd52e3385205f53",{
    "ref_block_num": 490,
    "ref_block_prefix": 1823332787,
    "expiration": "2020-06-29T06:00:30",
    "operations": [[
        35,{
          "caller": "1.2.16",
          "contract_id": "1.16.2",
          "function_name": "test_helloworld",
          "value_list": [],
          "extensions": []
        }
      ]
    ],
    "extensions": [],
    "signatures": [
      "206dcf11dad70485892e6fe1606265da5ff3d56aad43b2383179787d13622508fa10431ba747f7d4418c3ac7432e536e1c45db647e08dfc67b290d215e096346f6"
    ]
  }
]
unlocked >>> get_transaction_in_block_info 32dbbcdcf938e32487ea3b3c89cafee1813f5da0b337358dcfd52e3385205f53 
get_transaction_in_block_info 32dbbcdcf938e32487ea3b3c89cafee1813f5da0b337358dcfd52e3385205f53 
{
  "id": "3.1.5",
  "block_num": 501,
  "trx_in_block": 0,
  "trx_hash": "32dbbcdcf938e32487ea3b3c89cafee1813f5da0b337358dcfd52e3385205f53"
}
unlocked >>> get_block 501
get_block 501
{
  "previous": "000001f41d1bcc34044bc06f42e8a45d2de7b3aa",
  "timestamp": "2020-06-29T05:40:08",
  "witness": "1.6.1",
  "transaction_merkle_root": "86b8e35995a1817bff3afbb979249c4a0c3ba37a",
  "witness_signature": "2011729a4ca57f7f23bca877e44a696d2b1833b5e7a5225c7a933826b72940a4726b5dd2fe66e4605132deb383af9ed861c91d952365e9169fc407a3330c65269c",
  "block_id": "000001f522d05f47887a3049d700041e9409b8d3",
  "transactions": [[
      "32dbbcdcf938e32487ea3b3c89cafee1813f5da0b337358dcfd52e3385205f53",{
        "ref_block_num": 490,
        "ref_block_prefix": 1823332787,
        "expiration": "2020-06-29T06:00:30",
        "operations": [[
            35,{
              "caller": "1.2.16",
              "contract_id": "1.16.2",
              "function_name": "test_helloworld",
              "value_list": [],
              "extensions": []
            }
          ]
        ],
        "extensions": [],
        "signatures": [
          "206dcf11dad70485892e6fe1606265da5ff3d56aad43b2383179787d13622508fa10431ba747f7d4418c3ac7432e536e1c45db647e08dfc67b290d215e096346f6"
        ],
        "operation_results": [[
            4,{
              "fees": [{
                  "amount": 2369757,
                  "asset_id": "1.3.0"
                }
              ],
              "contract_id": "1.16.2",
              "contract_affecteds": [[
                  3,{
                    "affected_account": "1.2.16",
                    "message": "Hi, Cocos-BCX contract"
                  }
                ]
              ],
              "real_running_time": 318,
              "existed_pv": false,
              "process_value": "",
              "relevant_datasize": 35
            }
          ]
        ]
      }
    ]
  ]
}
unlocked >>> 

unlocked >>> get_contract contract.testapi.contractfeeshare
get_contract contract.testapi.contractfeeshare
{
  "id": "1.16.3",
  "creation_date": "2020-06-29T06:04:08",
  "owner": "1.2.16",
  "name": "contract.testapi.contractfeeshare",
  "user_invoke_share_percent": 100,
  "current_version": "9ec301b628cb6bab0572e37bf736c982d7e928f88ca1bde62c26b11d319ea924",
  "contract_authority": "COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx",
  "is_release": false,
  "check_contract_authority": false,
  "contract_data": [],
  "contract_ABI": [[{
        "key": [
          2,{
            "v": "test_contract_fee_share"
          }
        ]
      },[
        5,{
          "is_var_arg": false,
          "arglist": []
        }
      ]
    ],[{
        "key": [
          2,{
            "v": "test_helloworld"
          }
        ]
      },[
        5,{
          "is_var_arg": false,
          "arglist": []
        }
      ]
    ],[{
        "key": [
          2,{
            "v": "test_set_percent"
          }
        ]
      },[
        5,{
          "is_var_arg": false,
          "arglist": [
            "percent"
          ]
        }
      ]
    ]
  ],
  "lua_code_b_id": "2.2.3"
}
unlocked >>> call_contract_function nicotest contract.testapi.contractfeeshare test_helloworld [] true
call_contract_function nicotest contract.testapi.contractfeeshare test_helloworld [] true
[
  "92ae6e9deb1d8bafe56eb9698cc74c1dcfcf7ef6adfdd261a2377120c6b85b66",{
    "ref_block_num": 1160,
    "ref_block_prefix": 1351888536,
    "expiration": "2020-06-29T06:25:18",
    "operations": [[
        35,{
          "caller": "1.2.16",
          "contract_id": "1.16.3",
          "function_name": "test_helloworld",
          "value_list": [],
          "extensions": []
        }
      ]
    ],
    "extensions": [],
    "signatures": [
      "20138281d85790e35e93dbdb6600795263580fca68ca24e1ee147b64606e1e0e2f330fb2f96dcc27aca765d9d70feba911d7629c4664080d33086f03e01d098127"
    ]
  }
]
unlocked >>> call_contract_function nicotest contract.testapi.contractfeeshare test_contract_fee_share [] true
call_contract_function nicotest contract.testapi.contractfeeshare test_contract_fee_share [] true
[
  "772901845baf84e57141583c7a0f8af0662a5fa9766f841b90024420c53a680a",{
    "ref_block_num": 1169,
    "ref_block_prefix": 2333482435,
    "expiration": "2020-06-29T06:25:36",
    "operations": [[
        35,{
          "caller": "1.2.16",
          "contract_id": "1.16.3",
          "function_name": "test_contract_fee_share",
          "value_list": [],
          "extensions": []
        }
      ]
    ],
    "extensions": [],
    "signatures": [
      "2014e9fb2d0b1c0f47e3e7c0ddfc2bbb53d078d06253f1bc65b4fc31f89139b4b54dd4799c160db5c93630dd6c6852c6805fa4d5f1765df4dea17934fed2ac12d0"
    ]
  }
]
unlocked >>> get_transaction_in_block_info 772901845baf84e57141583c7a0f8af0662a5fa9766f841b90024420c53a680a
get_transaction_in_block_info 772901845baf84e57141583c7a0f8af0662a5fa9766f841b90024420c53a680a
{
  "id": "3.1.8",
  "block_num": 1178,
  "trx_in_block": 0,
  "trx_hash": "772901845baf84e57141583c7a0f8af0662a5fa9766f841b90024420c53a680a"
}
unlocked >>> get_block 1178
get_block 1178
{
  "previous": "000004996f94f3f830c45e05e39fb262687e9d0b",
  "timestamp": "2020-06-29T06:05:08",
  "witness": "1.6.7",
  "transaction_merkle_root": "d85c95e5c037313c9f0ed1b1234cd1da8998a9ec",
  "witness_signature": "20773b0e1075a7b603fe30a3ce67de4928f97b98fb6160e952acd733f7403189683e62629b05c3b631e19ad60b3a6ed8cf96ad290fa03863c0fcbfb33177a54778",
  "block_id": "0000049a49f4cfc464cc035cb01ea20eb1791d8b",
  "transactions": [[
      "772901845baf84e57141583c7a0f8af0662a5fa9766f841b90024420c53a680a",{
        "ref_block_num": 1169,
        "ref_block_prefix": 2333482435,
        "expiration": "2020-06-29T06:25:36",
        "operations": [[
            35,{
              "caller": "1.2.16",
              "contract_id": "1.16.3",
              "function_name": "test_contract_fee_share",
              "value_list": [],
              "extensions": []
            }
          ]
        ],
        "extensions": [],
        "signatures": [
          "2014e9fb2d0b1c0f47e3e7c0ddfc2bbb53d078d06253f1bc65b4fc31f89139b4b54dd4799c160db5c93630dd6c6852c6805fa4d5f1765df4dea17934fed2ac12d0"
        ],
        "operation_results": [[
            4,{
              "fees": [{
                  "amount": 2506218,
                  "asset_id": "1.3.0"
                }
              ],
              "contract_id": "1.16.3",
              "contract_affecteds": [[
                  3,{
                    "affected_account": "1.2.16",
                    "message": "contract_fee_share_test"
                  }
                ],[
                  5,{
                    "affected_account": "1.2.16",
                    "message": "100"
                  }
                ]
              ],
              "real_running_time": 432,
              "existed_pv": false,
              "process_value": "",
              "relevant_datasize": 50
            }
          ]
        ]
      }
    ]
  ]
}
unlocked >>> call_contract_function nicotest contract.testapi.contractfeeshare test_set_percent [[3, {"v":20}]] true
call_contract_function nicotest contract.testapi.contractfeeshare test_set_percent [[3, {"v":20}]] true
448804ms th_a       wallet.cpp:1784               sign_transaction     ] Caught exception while broadcasting tx 83a37d562b2b817eabcf9c6ba9e8d37cf9e3360e:  0 exception: unspecified
unspecified: Try the contract resolution execution failure,[3,{"v":true}]
    {"error":"unspecified: Try the contract resolution execution failure,[3,{\"v\":true}]","data":{"id":47,"jsonrpc":"2.0","error":{"code":47,"message":"unspecified: Try the contract resolution execution failure,[3,{\"v\":true}]"}}}
    th_a  state.cpp:38 handle_reply
0 exception: unspecified
unspecified: Try the contract resolution execution failure,[3,{"v":true}]
    {"error":"unspecified: Try the contract resolution execution failure,[3,{\"v\":true}]","data":{"id":47,"jsonrpc":"2.0","error":{"code":47,"message":"unspecified: Try the contract resolution execution failure,[3,{\"v\":true}]"}}}
    th_a  state.cpp:38 handle_reply

    {"account_id_or_name":"nicotest","contract_id_or_name":"contract.testapi.contractfeeshare","function_name":"test_set_percent","value_list":[[3,{"v":true}]],"broadcast":true}
    th_a  wallet.cpp:2086 call_contract_function
unlocked >>> 

unlocked >>> call_contract_function nicotest contract.testapi.contractfeeshare test_set_percent [[1, {"v":20}]] true
call_contract_function nicotest contract.testapi.contractfeeshare test_set_percent [[1, {"v":20}]] true
[
  "2e074c56450cb874bc91a973b8c1153fec03ab0887e007fa448f7dcb4af404c5",{
    "ref_block_num": 1245,
    "ref_block_prefix": 1927034532,
    "expiration": "2020-06-29T06:28:24",
    "operations": [[
        35,{
          "caller": "1.2.16",
          "contract_id": "1.16.3",
          "function_name": "test_set_percent",
          "value_list": [[
              1,{
                "v": "20.00000000000000000"
              }
            ]
          ],
          "extensions": []
        }
      ]
    ],
    "extensions": [],
    "signatures": [
      "20300680b5207846289f1744660e6142f5ee1a0c9bfa8906dd704c82083f58ffac57c3f1b297228caee224e895706817182800f45b2355636ec30832fd8ae8f882"
    ]
  }
]
unlocked >>> get_contract contract.testapi.contractfeeshare
get_contract contract.testapi.contractfeeshare
{
  "id": "1.16.3",
  "creation_date": "2020-06-29T06:04:08",
  "owner": "1.2.16",
  "name": "contract.testapi.contractfeeshare",
  "user_invoke_share_percent": 20,
  "current_version": "9ec301b628cb6bab0572e37bf736c982d7e928f88ca1bde62c26b11d319ea924",
  "contract_authority": "COCOS56a5dTnfGpuPoWACnYj65dahcXMpTrNQkV3hHWCFkLxMF5mXpx",
  "is_release": false,
  "check_contract_authority": false,
  "contract_data": [],
  "contract_ABI": [[{
        "key": [
          2,{
            "v": "test_contract_fee_share"
          }
        ]
      },[
        5,{
          "is_var_arg": false,
          "arglist": []
        }
      ]
    ],[{
        "key": [
          2,{
            "v": "test_helloworld"
          }
        ]
      },[
        5,{
          "is_var_arg": false,
          "arglist": []
        }
      ]
    ],[{
        "key": [
          2,{
            "v": "test_set_percent"
          }
        ]
      },[
        5,{
          "is_var_arg": false,
          "arglist": [
            "percent"
          ]
        }
      ]
    ]
  ],
  "lua_code_b_id": "2.2.3"
}
unlocked >>> call_contract_function nicotest contract.testapi.contractfeeshare test_contract_fee_share [] true
call_contract_function nicotest contract.testapi.contractfeeshare test_contract_fee_share [] true
[
  "5916e225aa52524e6ca52b6da2a3fe78fa4ce02583089454360865c89040c828",{
    "ref_block_num": 1262,
    "ref_block_prefix": 3170299570,
    "expiration": "2020-06-29T06:29:02",
    "operations": [[
        35,{
          "caller": "1.2.16",
          "contract_id": "1.16.3",
          "function_name": "test_contract_fee_share",
          "value_list": [],
          "extensions": []
        }
      ]
    ],
    "extensions": [],
    "signatures": [
      "2076d3f2ab7c7ede9e31b8bf1324d3ce87e8af83d4a4fe120c7df51807e1f6bc063dbb459878606d811babda9fec9f79259d8722d92ca4f0420c45b4a5edc54560"
    ]
  }
]
unlocked >>> 

unlocked >>> get_transaction_in_block_info 5916e225aa52524e6ca52b6da2a3fe78fa4ce02583089454360865c89040c828
get_transaction_in_block_info 5916e225aa52524e6ca52b6da2a3fe78fa4ce02583089454360865c89040c828
{
  "id": "3.1.10",
  "block_num": 1271,
  "trx_in_block": 0,
  "trx_hash": "5916e225aa52524e6ca52b6da2a3fe78fa4ce02583089454360865c89040c828"
}
unlocked >>> get_block 1271
get_block 1271
{
  "previous": "000004f62d9ef6c4485d76a21a46c0ee51f591a0",
  "timestamp": "2020-06-29T06:08:34",
  "witness": "1.6.2",
  "transaction_merkle_root": "cde41a4476b1327056d0539e7810dd64679eec15",
  "witness_signature": "2035c68028db4497b807c97fec3768465c93764c08d7037f048fcc5d45cc452626444ec396d0211dddba3722944813a81b7a0e2bfd69fcef09e425dd133af0b28d",
  "block_id": "000004f723197aa1da088a894939d3d2b26f0552",
  "transactions": [[
      "5916e225aa52524e6ca52b6da2a3fe78fa4ce02583089454360865c89040c828",{
        "ref_block_num": 1262,
        "ref_block_prefix": 3170299570,
        "expiration": "2020-06-29T06:29:02",
        "operations": [[
            35,{
              "caller": "1.2.16",
              "contract_id": "1.16.3",
              "function_name": "test_contract_fee_share",
              "value_list": [],
              "extensions": []
            }
          ]
        ],
        "extensions": [],
        "signatures": [
          "2076d3f2ab7c7ede9e31b8bf1324d3ce87e8af83d4a4fe120c7df51807e1f6bc063dbb459878606d811babda9fec9f79259d8722d92ca4f0420c45b4a5edc54560"
        ],
        "operation_results": [[
            4,{
              "fees": [{
                  "amount": 488187,
                  "asset_id": "1.3.0"
                }
              ],
              "contract_id": "1.16.3",
              "contract_affecteds": [[
                  3,{
                    "affected_account": "1.2.16",
                    "message": "contract_fee_share_test"
                  }
                ],[
                  5,{
                    "affected_account": "1.2.16",
                    "message": "20"
                  }
                ],[
                  5,{
                    "affected_account": "1.2.16",
                    "message": "80"
                  }
                ]
              ],
              "real_running_time": 355,
              "existed_pv": false,
              "process_value": "",
              "relevant_datasize": 62
            }
          ]
        ]
      }
    ]
  ]
}
unlocked >>> call_contract_function init0 contract.testapi.contractfeeshare test_contract_fee_share [] true
call_contract_function init0 contract.testapi.contractfeeshare test_contract_fee_share [] true
[
  "83dce51fcd80570f02a521bd016f00e97f51fa2e91455aebe77a63a6473689ce",{
    "ref_block_num": 1488,
    "ref_block_prefix": 851812315,
    "expiration": "2020-06-29T06:37:26",
    "operations": [[
        35,{
          "caller": "1.2.5",
          "contract_id": "1.16.3",
          "function_name": "test_contract_fee_share",
          "value_list": [],
          "extensions": []
        }
      ]
    ],
    "extensions": [],
    "signatures": [
      "1f19ed88eb9596773fb17321eb74edd743dfcea3a485d7102dbadbbe4233625dbe0f06f1967ffb21ec7c42ccc86884bf1700e77b1f7600f0b3ed1f0cf46801cf91"
    ]
  }
]
unlocked >>> get_transaction_in_block_info 83dce51fcd80570f02a521bd016f00e97f51fa2e91455aebe77a63a6473689ce 
get_transaction_in_block_info 83dce51fcd80570f02a521bd016f00e97f51fa2e91455aebe77a63a6473689ce 
{
  "id": "3.1.11",
  "block_num": 1498,
  "trx_in_block": 0,
  "trx_hash": "83dce51fcd80570f02a521bd016f00e97f51fa2e91455aebe77a63a6473689ce"
}
unlocked >>> get_block 1498
get_block 1498
{
  "previous": "000005d90a92ae17e180783bea285c481396edc0",
  "timestamp": "2020-06-29T06:16:58",
  "witness": "1.6.9",
  "transaction_merkle_root": "82ac4ac7ddad1d2ce0ddc8774f208fc595dd5642",
  "witness_signature": "1f2884e550c271b1a9706c60e1e1ca50e91b772c12e07876daa92a48d299f0c9cc3d92c00ad0eb11885c1e718b8f20152ff6b0f37e28f2998a9bd23a6a8f310e24",
  "block_id": "000005da03b14bc8ba4b5f924b9b188340f749a3",
  "transactions": [[
      "83dce51fcd80570f02a521bd016f00e97f51fa2e91455aebe77a63a6473689ce",{
        "ref_block_num": 1488,
        "ref_block_prefix": 851812315,
        "expiration": "2020-06-29T06:37:26",
        "operations": [[
            35,{
              "caller": "1.2.5",
              "contract_id": "1.16.3",
              "function_name": "test_contract_fee_share",
              "value_list": [],
              "extensions": []
            }
          ]
        ],
        "extensions": [],
        "signatures": [
          "1f19ed88eb9596773fb17321eb74edd743dfcea3a485d7102dbadbbe4233625dbe0f06f1967ffb21ec7c42ccc86884bf1700e77b1f7600f0b3ed1f0cf46801cf91"
        ],
        "operation_results": [[
            4,{
              "fees": [{
                  "amount": 484387,
                  "asset_id": "1.3.0"
                }
              ],
              "contract_id": "1.16.3",
              "contract_affecteds": [[
                  3,{
                    "affected_account": "1.2.5",
                    "message": "contract_fee_share_test"
                  }
                ],[
                  5,{
                    "affected_account": "1.2.16",
                    "message": "20"
                  }
                ],[
                  5,{
                    "affected_account": "1.2.5",
                    "message": "80"
                  }
                ]
              ],
              "real_running_time": 336,
              "existed_pv": false,
              "process_value": "",
              "relevant_datasize": 62
            }
          ]
        ]
      }
    ]
  ]
}
unlocked >>> 
```  


## 2. contract result record test  
``` text  
unlocked >>> call_contract_function nicotest contract.testapi.contractfeeshare test_helloworld [] true
call_contract_function nicotest contract.testapi.contractfeeshare test_helloworld [] true
[
  "2e5242bc98b6c2fbbe6b39ef54e94b1362a6ba4df45a03b5b7a71a61cd12664d",{
    "ref_block_num": 5909,
    "ref_block_prefix": 2107846706,
    "expiration": "2020-06-29T10:05:38",
    "operations": [[
        35,{
          "caller": "1.2.16",
          "contract_id": "1.16.3",
          "function_name": "test_helloworld",
          "value_list": [],
          "extensions": []
        }
      ]
    ],
    "extensions": [],
    "signatures": [
      "2025d5c5e66870f890228c27bb485d6fb31726e7285ad9c2aeb8141075b9ee06da31c20708b52dffd238838ea39f2d37543695cc05fdb102c3e484cdfb20118621"
    ]
  }
]
unlocked >>> get_transaction_in_block_info 2e5242bc98b6c2fbbe6b39ef54e94b1362a6ba4df45a03b5b7a71a61cd12664d
get_transaction_in_block_info 2e5242bc98b6c2fbbe6b39ef54e94b1362a6ba4df45a03b5b7a71a61cd12664d
{
  "id": "3.1.16",
  "block_num": 5918,
  "trx_in_block": 0,
  "trx_hash": "2e5242bc98b6c2fbbe6b39ef54e94b1362a6ba4df45a03b5b7a71a61cd12664d"
}
unlocked >>> get_block 5918
get_block 5918
{
  "previous": "0000171dd1b142e1947a8e797938bd50ef93c594",
  "timestamp": "2020-06-29T09:45:10",
  "witness": "1.6.8",
  "transaction_merkle_root": "c0969795b72897d98bb60aad5c9fae62e8534126",
  "witness_signature": "1f6f681ae16f4f37a0e30271f52cc35825c7926383dbbda8561e44321e439ba3991990c2fa89f21a006763d22faf18b9ac2ff43c1a1f758e8b5f38e218f7f27fff",
  "block_id": "0000171e5fd134d10c9e030066ed855026892847",
  "transactions": [[
      "2e5242bc98b6c2fbbe6b39ef54e94b1362a6ba4df45a03b5b7a71a61cd12664d",{
        "ref_block_num": 5909,
        "ref_block_prefix": 2107846706,
        "expiration": "2020-06-29T10:05:38",
        "operations": [[
            35,{
              "caller": "1.2.16",
              "contract_id": "1.16.3",
              "function_name": "test_helloworld",
              "value_list": [],
              "extensions": []
            }
          ]
        ],
        "extensions": [],
        "signatures": [
          "2025d5c5e66870f890228c27bb485d6fb31726e7285ad9c2aeb8141075b9ee06da31c20708b52dffd238838ea39f2d37543695cc05fdb102c3e484cdfb20118621"
        ],
        "operation_results": [[
            4,{
              "fees": [{
                  "amount": 2437757,
                  "asset_id": "1.3.0"
                }
              ],
              "contract_id": "1.16.3",
              "contract_affecteds": [[
                  3,{
                    "affected_account": "1.2.16",
                    "message": "Hi, Cocos-BCX contract"
                  }
                ],[
                  5,{
                    "affected_account": "1.2.16",
                    "message": "100%"
                  }
                ]
              ],
              "real_running_time": 386,
              "existed_pv": false,
              "process_value": "",
              "relevant_datasize": 35
            }
          ]
        ]
      }
    ]
  ]
}
unlocked >>> call_contract_function init0 contract.testapi.contractfeeshare test_helloworld [] true
call_contract_function init0 contract.testapi.contractfeeshare test_helloworld [] true
[
  "f08084e47e30ca0b8a0af285e7323763be62906cd6b6c97280f0f3d8706c35e4",{
    "ref_block_num": 5922,
    "ref_block_prefix": 882391783,
    "expiration": "2020-06-29T10:06:16",
    "operations": [[
        35,{
          "caller": "1.2.5",
          "contract_id": "1.16.3",
          "function_name": "test_helloworld",
          "value_list": [],
          "extensions": []
        }
      ]
    ],
    "extensions": [],
    "signatures": [
      "2008d9188cd8fb97c3dc3dc3b81e43457ed7d1d8d50259e7e1d1d0c1de3c195de92091e7982cd831be18fc9e398b220f763f13f15ad1d89db85c9e049f0c155c2b"
    ]
  }
]
unlocked >>> get_transaction_in_block_info f08084e47e30ca0b8a0af285e7323763be62906cd6b6c97280f0f3d8706c35e4 
get_transaction_in_block_info f08084e47e30ca0b8a0af285e7323763be62906cd6b6c97280f0f3d8706c35e4 
{
  "id": "3.1.17",
  "block_num": 5935,
  "trx_in_block": 0,
  "trx_hash": "f08084e47e30ca0b8a0af285e7323763be62906cd6b6c97280f0f3d8706c35e4"
}
unlocked >>> get_block 5935,
get_block 5935,
{
  "previous": "0000172e4c4f081fcdc1c02e082e9fe98f783281",
  "timestamp": "2020-06-29T09:45:48",
  "witness": "1.6.7",
  "transaction_merkle_root": "77a25cdeac9b3f139a2bcf213fa96420bf78f099",
  "witness_signature": "1f21be29ac99f1baa3d263941626f0c43ae6836b658b38e79d4318ef6a948c9b712e81a81c2043865459735e4718021df7cf4435b1356633644530f5c96c6b03a0",
  "block_id": "0000172f6933c695e1f84f9f2ac91d33ce1cf1b3",
  "transactions": [[
      "f08084e47e30ca0b8a0af285e7323763be62906cd6b6c97280f0f3d8706c35e4",{
        "ref_block_num": 5922,
        "ref_block_prefix": 882391783,
        "expiration": "2020-06-29T10:06:16",
        "operations": [[
            35,{
              "caller": "1.2.5",
              "contract_id": "1.16.3",
              "function_name": "test_helloworld",
              "value_list": [],
              "extensions": []
            }
          ]
        ],
        "extensions": [],
        "signatures": [
          "2008d9188cd8fb97c3dc3dc3b81e43457ed7d1d8d50259e7e1d1d0c1de3c195de92091e7982cd831be18fc9e398b220f763f13f15ad1d89db85c9e049f0c155c2b"
        ],
        "operation_results": [[
            4,{
              "fees": [{
                  "amount": 2446757,
                  "asset_id": "1.3.0"
                }
              ],
              "contract_id": "1.16.3",
              "contract_affecteds": [[
                  3,{
                    "affected_account": "1.2.5",
                    "message": "Hi, Cocos-BCX contract"
                  }
                ],[
                  5,{
                    "affected_account": "1.2.16",
                    "message": "20%"
                  }
                ],[
                  5,{
                    "affected_account": "1.2.5",
                    "message": "80%"
                  }
                ]
              ],
              "real_running_time": 395,
              "existed_pv": false,
              "process_value": "",
              "relevant_datasize": 35
            }
          ]
        ]
      }
    ]
  ]
}
unlocked >>> 
``` 

## 4. 合约费用  
``` text  
unlocked >>> list_account_balances nicotest
list_account_balances nicotest
97799999788.17858 COCOS

unlocked >>> list_account_balances init1
list_account_balances init1
200164211.08998 COCOS

unlocked >>> call_contract_function init1 contract.testapi.contractfeeshare test_helloworld [] true
call_contract_function init1 contract.testapi.contractfeeshare test_helloworld [] true
[
  "e8c507eb4d1af6b70b96a554b69a83580c690ad92afa27e3ce76ec1326aa830b",{
    "ref_block_num": 5753,
    "ref_block_prefix": 3499263594,
    "expiration": "2020-06-30T09:19:34",
    "operations": [[
        35,{
          "caller": "1.2.6",
          "contract_id": "1.16.1",
          "function_name": "test_helloworld",
          "value_list": [],
          "extensions": []
        }
      ]
    ],
    "extensions": [],
    "signatures": [
      "201b6449436831b94de62c5f9d8e1e153f91d7afb19b477ae6cca36e9c489fdbbb3b2e037a93514c09001c22347058a6673a91c59ba05d192ff8adf1b4b60dcce7"
    ]
  }
]
unlocked >>> list_account_balances init1
list_account_balances init1
200164202.55446 COCOS

unlocked >>> list_account_balances nicotest
list_account_balances nicotest
97799999754.03653 COCOS

unlocked >>> get_transaction_in_block_info e8c507eb4d1af6b70b96a554b69a83580c690ad92afa27e3ce76ec1326aa830b 
get_transaction_in_block_info e8c507eb4d1af6b70b96a554b69a83580c690ad92afa27e3ce76ec1326aa830b 
{
  "id": "3.1.10",
  "block_num": 5762,
  "trx_in_block": 0,
  "trx_hash": "e8c507eb4d1af6b70b96a554b69a83580c690ad92afa27e3ce76ec1326aa830b"
}
unlocked >>> get_block 5762
get_block 5762
{
  "previous": "0000168129121bbafb744d3a847eea631473b8b3",
  "timestamp": "2020-06-30T08:59:06",
  "witness": "1.6.5",
  "transaction_merkle_root": "79baa8d17180cbae032643f24d62fc37d97915cf",
  "witness_signature": "1f77592c9ccfe6ba4700b8eea025ff8264b0bb06c9bb345efb514e0fbaa62671a64ffbc33f1feca942f0820851057c2771533bca3c61f1848fc1733fb063f54b29",
  "block_id": "00001682c7bc10cbba294b104c52fab789a8b97c",
  "transactions": [[
      "e8c507eb4d1af6b70b96a554b69a83580c690ad92afa27e3ce76ec1326aa830b",{
        "ref_block_num": 5753,
        "ref_block_prefix": 3499263594,
        "expiration": "2020-06-30T09:19:34",
        "operations": [[
            35,{
              "caller": "1.2.6",
              "contract_id": "1.16.1",
              "function_name": "test_helloworld",
              "value_list": [],
              "extensions": []
            }
          ]
        ],
        "extensions": [],
        "signatures": [
          "201b6449436831b94de62c5f9d8e1e153f91d7afb19b477ae6cca36e9c489fdbbb3b2e037a93514c09001c22347058a6673a91c59ba05d192ff8adf1b4b60dcce7"
        ],
        "operation_results": [[
            4,{
              "fees": [{
                  "amount": 4267757,
                  "asset_id": "1.3.0"
                }
              ],
              "contract_id": "1.16.1",
              "contract_affecteds": [[
                  3,{
                    "affected_account": "1.2.6",
                    "message": "Hi, Cocos-BCX contract"
                  }
                ],[
                  5,{
                    "fees": [{
                        "amount": 853552,
                        "asset_id": "1.3.0"
                      }
                    ],
                    "affected_account": "1.2.6",
                    "message": "20%"
                  }
                ],[
                  5,{
                    "fees": [{
                        "amount": 3414205,
                        "asset_id": "1.3.0"
                      }
                    ],
                    "affected_account": "1.2.16",
                    "message": "80%"
                  }
                ]
              ],
              "real_running_time": 2216,
              "existed_pv": false,
              "process_value": "",
              "relevant_datasize": 35
            }
          ]
        ]
      }
    ]
  ]
}
unlocked >>> 
```

### 手续费计算  
``` 
>>> cfee = 853552
>>> ofee = 3414205
>>> 
>>> total_fee = 4267757
>>> 
>>> cfee + ofee
4267757
>>> cdelta = 200164211.08998 - 200164202.55446
>>> cdelta
8.535520017147064
>>> 
>>> odelta = 97799999788.17858 - 97799999754.03653 
>>> odelta
34.14204406738281
>>> 
```  
