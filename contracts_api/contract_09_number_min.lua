function test_number_min()
    min = chainhelper:number_min()
    chainhelper:log("test number_min, number_min: " .. tostring(min) .. ", type: " .. type(min))
end