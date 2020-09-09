function test_create_nh_asset(owner, symbol, world_view, base_describe, enable_logger)
	chainhelper:log("[test_create_nh_asset]symbol: " .. symbol .. ", owner: "..owner)
	nh_asset_id = chainhelper:create_nh_asset(owner, symbol, world_view, base_describe, enable_logger)
	chainhelper:log("new nh_asset_id: " .. nh_asset_id)
end 

function test_get_nft_asset(hash_or_id)
	chainhelper:log('input params: ' .. tostring(hash_or_id))
	local asset = chainhelper:get_nft_asset(hash_or_id);
	chainhelper:log('result type: ' .. type(asset))
	chainhelper:log('get_nft_asset result: ' .. tostring(asset))
end
