
function test_invoke_contract_function(contract, func, args)
    local message = "contract:" .. contract .. ", func:" .. func
    message = message .. ", args type: " .. type(args) .. ", args: " .. args
    chainhelper:log(message)
    chainhelper:invoke_contract_function(contract, func, args);
end
