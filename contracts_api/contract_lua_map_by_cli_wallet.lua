function test_params_lua_map(key1, key2, argsluamap)
    chainhelper:log("[test lua_map] key1:"..key1..", key2:"..key2 .. ", argsluamap type: " .. type(argsluamap))
    argsJsonStr = cjson.encode(argsluamap)
    chainhelper:log("argsluamap json string: " .. argsJsonStr)

    chainhelper:log(argsluamap[key1])
    chainhelper:log(argsluamap[key2])
end