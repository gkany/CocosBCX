function test_adjust_lock_asset(symbol, amount)
    chainhelper:log("[test_adjust_lock_asset] symbol: " .. symbol .. ", amount: "..tostring(amount))
    chainhelper:adjust_lock_asset(symbol, amount)
end