function test_make_release()
    if (chainhelper:is_owner())
    then
        chainhelper:make_release()
        chainhelper:log("test_make_release")
    end
end