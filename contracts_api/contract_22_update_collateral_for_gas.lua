function test_colllateral_gas(to, amount)
    chainhelper:log("[test_colllateral_gas] to: " .. to .. ", amount: " .. tostring(amount))
    chainhelper:update_collateral_for_gas(to, amount)
end