
--[[
    memo_data make_memo(string receiver_id_or_name,
        string key, string value, uint64_t ss, bool enable_logger=false);
]]
function test_make_memo(name, key, value, ss, enable_logger)
    local message = "name:" .. name .. ", key:" .. key .. ", ss:"..tostring(ss) .. ", enable_logger: "..tostring(enable_logger)
    chainhelper:log(message)

    local memo = chainhelper:make_memo(name, key, value, ss, enable_logger);
    chainhelper:log(type(memo))
end

