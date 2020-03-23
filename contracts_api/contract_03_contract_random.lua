function test_contract_random()
    num = chainhelper:random()
    chainhelper:log("random num: " .. tostring(num) .. ", type: " .. type(num))
end
