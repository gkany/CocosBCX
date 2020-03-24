--[[
    void relate_nh_asset(string parent_token_hash_or_id,
        string child_token_hash_or_id, bool relate, bool enable_logger = false)
]]
function test_relate_nh_asset(parent, child, relate, enable_logger)
    chainhelper:log("parent: " .. parent .. ", child: " .. child .. ", is_relate: " .. tostring(relate))
    chainhelper:relate_nh_asset(parent, child, relate, enable_logger)
end

function test_create_nh_asset(owner, symbol, world_view, base_describe, enable_logger)
    chainhelper:log("[test_create_nh_asset]symbol: " .. symbol .. ", owner: "..owner)
    nh_asset_id = chainhelper:create_nh_asset(owner, symbol, world_view, base_describe, enable_logger)
    chainhelper:log("new nh_asset_id: " .. nh_asset_id)
end