function test_set_invoke_share_percent(percent)
    chainhelper:log("test set_invoke_share_percent, percent: " .. tostring(percent) .. ", type: " .. type(percent))
    chainhelper:set_invoke_share_percent(percent)
end