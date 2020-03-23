function init()
    read_list = {
        public_data = {
            msg = 'this is a init'
        }
    }
    chainhelper:read_chain();
    assert(public_data.is_init==nil,'contract has been initialized');
    public_data.userdata = {};
    public_data.is_init = 'this is a init';
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
    chainhelper:log('test setmsg')
    chainhelper:log(public_data.is_init)
    chainhelper:log(name)
    local userdata = public_data.userdata;
    userdata[id] = name
    public_data.savedata = userdata;
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
