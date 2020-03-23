function test_is_owner()
    if (chainhelper:is_owner())
    then
        chainhelper:log("contract.caller == contract.owner")
    else
        chainhelper:log("contract.caller != contract.owner")
    end
end