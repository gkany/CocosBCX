function test_get_account_balance(account, symbol)
    balance = chainhelper:get_account_balance(account, symbol)
    chainhelper:log("account: " ..account .. ", balance: " .. tostring(balance) .. " " .. symbol)
end