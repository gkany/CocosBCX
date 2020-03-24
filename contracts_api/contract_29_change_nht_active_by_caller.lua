function test_change_nht_active_by_caller(to, token_hash_or_id, enable_logger)
    chainhelper:log("to: " .. to .. ", token_hash_or_id: " .. token_hash_or_id)
    chainhelper:change_nht_active_by_caller(to, token_hash_or_id, enable_logger)
end

function test_create_nh_asset(owner, symbol, world_view, base_describe, enable_logger)
    chainhelper:log("[test_create_nh_asset]symbol: " .. symbol .. ", owner: "..owner)
    nh_asset_id = chainhelper:create_nh_asset(owner, symbol, world_view, base_describe, enable_logger)
    chainhelper:log("new nh_asset_id: " .. nh_asset_id)
end