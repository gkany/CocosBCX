--[[
        void transfer_from_caller(string, double, string, bool)
    [](register_scheduler &fc_register, string to, double amount, string symbol, bool enable_logger = false) {
]]
function test_transfer_from_caller(to, amount, symbol, enable_logger)
    chainhelper:log("to: " .. to .. ", amount: " .. tostring(amount) .. ", symbol: " .. symbol)
    chainhelper:transfer_from_caller(to, amount, symbol, enable_logger)
end