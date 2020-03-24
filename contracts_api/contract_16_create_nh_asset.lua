--[[
    string create_nh_asset(string owner_id_or_name, string symbol,
        string world_view, string base_describe, bool enable_logger);
]]
function test_create_nh_asset(owner, symbol, world_view, base_describe, enable_logger)
    chainhelper:log("[test_create_nh_asset]symbol: " .. symbol .. ", owner: "..owner)
    nh_asset_id = chainhelper:create_nh_asset(owner, symbol, world_view, base_describe, enable_logger)
    chainhelper:log("new nh_asset_id: " .. nh_asset_id)
end
