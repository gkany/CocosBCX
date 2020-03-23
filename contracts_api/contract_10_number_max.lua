function test_number_max()
    max = chainhelper:number_max()
    chainhelper:log("test number_max, number_max: " .. tostring(max) .. ", type: " .. type(max))
end