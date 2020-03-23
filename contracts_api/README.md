## contract api
### 1. is_owner
* 函数名:
``` text
	[lua] is_owner  -->  [cpp] is_owner
```
* cpp函数原型：
``` c++
	bool is_owner();
```

### 2. log
* 函数名:
``` text
	[lua] log  -->  [cpp] log
```
* cpp函数原型：
``` c++
	void log(string message);
```

### 3. random
* 函数名:
``` text
	[lua] random  -->  [cpp] contract_random
```
* cpp函数原型：
``` c++
	int contract_random();
```

### 4. set_permissions_flag
* 函数名:
``` text
	[lua] set_permissions_flag  -->  [cpp] set_permissions_flag
```
* cpp函数原型：
``` c++
	void set_permissions_flag(bool flag);
```

### 5. set_invoke_percent
* 函数名:
``` text
	[lua] set_invoke_percent  -->  [cpp] set_invoke_percent
```
* cpp函数原型：
``` c++
	void set_invoke_percent(double percent);
```

### 6. set_invoke_share_percent
* 函数名:
``` text
	[lua] set_invoke_share_percent  -->  [cpp] set_invoke_share_percent
```
* cpp函数原型：
``` c++
	void set_invoke_share_percent(double percent);
```

### 7. read_chain
* 函数名:
``` text
	[lua] read_chain  -->  [cpp] read_cache
```
* cpp函数原型：
``` c++
	void read_cache();
```

### 8. write_chain
* 函数名:
``` text
	[lua] write_chain  -->  [cpp] fllush_cache
```
* cpp函数原型：
``` c++
	void fllush_cache();
```

### 9. number_min
* 函数名:
``` text
	[lua] number_min  -->  [cpp] nummin
```
* cpp函数原型：
``` c++
	lua_Number nummin();
```

### 10. number_max
* 函数名:
``` text
	[lua] number_max  -->  [cpp] nummax
```
* cpp函数原型：
``` c++
	lua_Number nummax();
```

### 11. hash256
* 函数名:
``` text
	[lua] hash256  -->  [cpp] hash256
```
* cpp函数原型：
``` c++
	string hash256(string source);
```

### 12. hash512
* 函数名:
``` text
	[lua] hash512  -->  [cpp] hash512
```
* cpp函数原型：
``` c++
	string hash512(string source);
```

### 13. time
* 函数名:
``` text
	[lua] time  -->  [cpp] head_block_time
```
* cpp函数原型：
``` c++
	uint32_t head_block_time();
```

### 14. real_time
* 函数名:
``` text
	[lua] real_time  -->  [cpp] real_time
```
* cpp函数原型：
``` c++
	uint64_t real_time();
```

### 15. adjust_lock_asset
* 函数名:
``` text
	[lua] adjust_lock_asset  -->  [cpp] adjust_lock_asset
```
* cpp函数原型：
``` c++
	void adjust_lock_asset(string symbol_or_id,int64_t amount);
```

### 16. create_nh_asset
* 函数名:
``` text
	[lua] create_nh_asset  -->  [cpp] create_nh_asset
```
* cpp函数原型：
``` c++
	string create_nh_asset(string owner_id_or_name,string symbol,string world_view,string base_describe,bool enable_logger);
```

### 17. nht_describe_change
* 函数名:
``` text
	[lua] nht_describe_change  -->  [cpp] nht_describe_change
```
* cpp函数原型：
``` c++
	void nht_describe_change(string nht_hash_or_id,string key,string value,bool enable_logger=false);
```

### 18. change_contract_authority
* 函数名:
``` text
	[lua] change_contract_authority  -->  [cpp] change_contract_authority
```
* cpp函数原型：
``` c++
	void change_contract_authority(string authority);
```

### 19. make_memo
* 函数名:
``` text
	[lua] make_memo  -->  [cpp] make_memo
```
* cpp函数原型：
``` c++
	memo_data make_memo(string receiver_id_or_name, string key, string value, uint64_t ss,bool enable_logger=false);
```

### 20. invoke_contract_function
* 函数名:
``` text
	[lua] invoke_contract_function  -->  [cpp] invoke_contract_function
```
* cpp函数原型：
``` c++
	void invoke_contract_function(string contract_id_or_name,string function_name,string value_list_json);
```

### 21. make_release
* 函数名:
``` text
	[lua] make_release  -->  [cpp] make_release
```
* cpp函数原型：
``` c++
	void make_release();
```

### 22. update_collateral_for_gas
* 函数名:
``` text
	[lua] update_collateral_for_gas  -->  [cpp] update_collateral_for_gas
```
* cpp函数原型：
``` c++
	void update_collateral_for_gas(string to, int64_t amount);
```

### 23. transfer_from_owner
* 函数名:
``` text
	[lua] transfer_from_owner  -->  [cpp] transfer_from_owner
```
* cpp函数原型：
``` c++
	void transfer_from_owner(string, double, string, bool)
```

### 24. transfer_from_caller
* 函数名:
``` text
	[lua] transfer_from_caller  -->  [cpp] transfer_from_caller
```
* cpp函数原型：
``` c++
	void transfer_from_caller(string, double, string, bool)
```

### 25. transfer_nht_from_owner
* 函数名:
``` text
	[lua] transfer_nht_from_owner  -->  [cpp] transfer_nht_from_owner
```
* cpp函数原型：
``` c++
	void transfer_nht_from_owner(string, string, bool)
```

### 26. transfer_nht_from_caller
* 函数名:
``` text
	[lua] transfer_nht_from_caller  -->  [cpp] transfer_nht_from_caller
```
* cpp函数原型：
``` c++
	void transfer_nht_from_caller(string, string, bool)
```

### 27. get_account_balance
* 函数名:
``` text
	[lua] get_account_balance  -->  [cpp] get_account_balance
```
* cpp函数原型：
``` c++
	int64_t get_account_balance(string, string)
```

### 28. change_nht_active_by_owner
* 函数名:
``` text
	[lua] change_nht_active_by_owner  -->  [cpp] change_nht_active_by_owner
```
* cpp函数原型：
``` c++
	void change_nht_active_by_owner(string, string, bool)
```

### 29. transfer_nht_active_from_caller
* 函数名:
``` text
	[lua] transfer_nht_active_from_caller  -->  [cpp] transfer_nht_active_from_caller
```
* cpp函数原型：
``` c++
	void transfer_nht_active_from_caller(string, string, bool)
```

### 30. transfer_nht_ownership_from_owner
* 函数名:
``` text
	[lua] transfer_nht_ownership_from_owner  -->  [cpp] transfer_nht_ownership_from_owner
```
* cpp函数原型：
``` c++
	void transfer_nht_ownership_from_owner(string, string, bool)
```

### 31. transfer_nht_ownership_from_caller
* 函数名:
``` text
	[lua] transfer_nht_ownership_from_caller  -->  [cpp] transfer_nht_ownership_from_caller
```
* cpp函数原型：
``` c++
	void transfer_nht_ownership_from_caller(string, string, bool)
```

### 32. transfer_nht_dealership_from_owner
* 函数名:
``` text
	[lua] transfer_nht_dealership_from_owner  -->  [cpp] transfer_nht_dealership_from_owner
```
* cpp函数原型：
``` c++
	void transfer_nht_dealership_from_owner(string, string, bool)
```

### 33. transfer_nht_dealership_from_caller
* 函数名:
``` text
	[lua] transfer_nht_dealership_from_caller  -->  [cpp] transfer_nht_dealership_from_caller
```
* cpp函数原型：
``` c++
	void transfer_nht_dealership_from_caller(string, string, bool)
```

### 34. set_nht_limit_list
* 函数名:
``` text
	[lua] set_nht_limit_list  -->  [cpp] set_nht_limit_list
```
* cpp函数原型：
``` c++
	void set_nht_limit_list(string, string, bool, bool)
```

### 35. relate_nh_asset
* 函数名:
``` text
	[lua] relate_nh_asset  -->  [cpp] relate_nh_asset
```
* cpp函数原型：
``` c++
	void relate_nh_asset(string, string, bool, bool)
```

