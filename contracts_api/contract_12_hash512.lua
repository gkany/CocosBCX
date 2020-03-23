function test_hash512(str)
    result = chainhelper:hash512(str)
    chainhelper:log("[test hash512]" .. str .. "--- hash512 --->" .. result)
end