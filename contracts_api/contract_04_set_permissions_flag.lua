function test_set_permissions_flag(flag)
    chainhelper:log("test set_permissions_flag, flag: " .. tostring(flag))
    chainhelper:set_permissions_flag(flag)
end