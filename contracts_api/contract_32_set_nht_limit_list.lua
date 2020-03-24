--[[
    void set_nht_limit_list(string token_hash_or_id,
        string contract_name_or_ids, bool limit_type, bool enable_logger = false)
]]
function test_set_nht_limit_list(nh_asset, contract, limit_type, enable_logger)
    chainhelper:log("nh_asset: " .. nh_asset .. ", contract_name_or_ids: "..contract)
    chainhelper:set_nht_limit_list(nh_asset, contract, limit_type, enable_logger)
end

function test_create_nh_asset(owner, symbol, world_view, base_describe, enable_logger)
    chainhelper:log("[test_create_nh_asset]symbol: " .. symbol .. ", owner: "..owner)
    nh_asset_id = chainhelper:create_nh_asset(owner, symbol, world_view, base_describe, enable_logger)
    chainhelper:log("new nh_asset_id: " .. nh_asset_id)
end