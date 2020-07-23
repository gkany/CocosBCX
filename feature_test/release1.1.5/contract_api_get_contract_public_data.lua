function init()
    read_list = {
        public_data = {
            is_init = true
        }
    }
    chainhelper:read_chain();

    public_data.userdata = {};
    public_data.is_init = true;

    write_list = {
        public_data = {}
    }
    chainhelper:write_chain();
end

function insert(id, name)
    read_list = {
        public_data = {userdata=true}
    }
    chainhelper:read_chain()

    local userdata = public_data.userdata;
    userdata[id] = name
    public_data.userdata = userdata

    write_list = {
        public_data = {userdata=true}
    }
    chainhelper:write_chain();
end

function test(name_or_id) 
    data = chainhelper:get_contract_public_data(name_or_id) 
    jsonStr = cjson.encode(data)
    chainhelper:log("contract: " .. name_or_id .. ", public_data: " .. jsonStr)
end