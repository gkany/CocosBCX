
--[[
	void change_contract_authority(string authority);
]]
function test_change_contract_authority(public_key)
    chainhelper:log("public_key:" .. public_key)
    chainhelper:change_contract_authority(public_key)
end

