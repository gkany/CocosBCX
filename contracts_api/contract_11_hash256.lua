function test_hash256(str)
    result = chainhelper:hash256(str)
    chainhelper:log("[test hash256]" .. str .. "--- hash256 --->" .. result)
end