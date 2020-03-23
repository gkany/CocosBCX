function init()
    read_list = {
        public_data = {
            msg = false
        }
    }
    chainhelper:read_chain();
    assert(public_data.is_init == nil,'contract has been initialized');
    public_data.userdata = {};
    public_data.is_init = true;
    write_list = {
        public_data = {}
    }
    chainhelper:write_chain();
end

function insert(id, name)
    read_list = {
        public_data = {}
    }
    chainhelper:read_chain()
    chainhelper:log('insert user: ' .. name .. ', init status: ' .. tostring(public_data.is_init))
    local userdata = public_data.userdata;
    userdata[id] = name
    public_data.userdata = userdata;
    write_list = {
        public_data = {}
    }
    chainhelper:write_chain();
end

function get_contract_public_data(name_or_id)
    data = chainhelper:get_contract_public_data(name_or_id)
    jsonStr = cjson.encode(data)
    chainhelper:log(jsonStr)
end
