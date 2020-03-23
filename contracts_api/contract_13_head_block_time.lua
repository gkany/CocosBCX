function test_head_block_time()
    head_block_time = date('%Y-%m-%dT%H:%M:%S', chainhelper:time())
    chainhelper:log('head_block_time is ' .. head_block_time)
end