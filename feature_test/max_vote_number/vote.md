
## 启动节点  
参考README.md

## 测试

### 接口测试
#### cli_wallet api
``` shell
curl http://127.0.0.1:8048 -d '{"id":1, "method":"get_global_extensions_properties", "params":[]}' && echo ""
```

#### chain api
``` shell
curl http://127.0.0.1:8059 -d '{"id":1, "method":"call", "params":[0, "get_global_property_extensions", []]}' && echo ""
```

### 发起修改参数提案, 批准  
``` shell
python3 vote.py

```

**注意** : 提案review时间应该大于当前时间到链维护的间隔，否则提案失败，这种情况执行会有提示，`Please wait for the next maintenance`, 可以根据需要修改vote.py逻辑，`sleep(delta_time)`

