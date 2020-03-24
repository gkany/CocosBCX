--[[
    string create_nh_asset(string owner_id_or_name, string symbol,
        string world_view, string base_describe, bool enable_logger);
]]
function test_create_nh_asset(owner, symbol, world_view, base_describe, enable_logger)
    chainhelper:log("[test_create_nh_asset]symbol: " .. symbol .. ", owner: "..owner)
    nh_asset_id = chainhelper:create_nh_asset(owner, symbol, world_view, base_describe, enable_logger)
    chainhelper:log("new nh_asset_id: " .. nh_asset_id)
end

--[[
	void nht_describe_change(
        string nht_hash_or_id, string key, string value, bool enable_logger=false);
]]
function test_nht_describe_change(nh_asset_id, key, value, enable_logger)
    chainhelper:log("[test_nht_describe_change]nh id: " .. nh_asset_id .. ", "..key.. ":" ..value)
    chainhelper:nht_describe_change(nh_asset_id, key, value, enable_logger)
end
