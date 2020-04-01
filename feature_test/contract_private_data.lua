function init()
    read_list = {
        public_data = {
            count = 0
        },
        private_data = {
            count = 0
        }
    }
    chainhelper:read_chain();
    --[[assert(public_data.count == nil and private_data.count == nil,'contract has been initialized');]]
    public_data.userdata = {};
    public_data.count = 0;
    private_data.userdata = {}
    private_data.count = 0
    write_list = {
        public_data = {},
        private_data = {}
    }
    chainhelper:write_chain();
end

function insert_public(id, name)
    read_list = {
        public_data = {}
    }
    chainhelper:read_chain()
    str = cjson.encode(public_data)
    chainhelper:log("public data: " .. str)

    chainhelper:log('insert public user: ' .. name .. ", count: " .. public_data.count)
    local person = {}
    person["id"] = id
    person["name"] = name

    public_data.count = public_data.count + 1
    local userdata = public_data.userdata;
    --[[local key = "key_" .. tostring(public_data.count)]]
    local key = tostring(public_data.count)
    userdata[key] = person
    public_data.userdata = userdata;
    write_list = {
        public_data = {}
    }
    chainhelper:write_chain();
end

function insert_private(id, name)
    read_list = {
        private_data = {}
    }
    chainhelper:read_chain()
    str = cjson.encode(private_data)
    chainhelper:log("private data: " .. str)

    private_data.count = private_data.count + 1
    chainhelper:log('insert private user: ' .. name .. ", count: " .. tostring(private_data.count))
    local person = {}
    person["id"] = id
    person["name"] = name
    local userdata = private_data.userdata;
    local key = "key_" .. tostring(private_data.count)
    userdata[key] = person
    private_data.userdata = userdata;
    write_list = {
        private_data = {}
    }
    chainhelper:write_chain();
end

function get_contract_public_data(name_or_id)
    data = chainhelper:get_contract_public_data(name_or_id)
    jsonStr = cjson.encode(data)
    chainhelper:log(jsonStr)
end

function get_public_data1(key)
    read_list = {
        public_data = {
            userdata = {
                key_6 = {}
            }
        }
    }
    chainhelper:read_chain()
    str = cjson.encode(public_data.userdata)
    chainhelper:log("public data1111: " .. str)

    --[[
    read_list = {
        public_data = {
            userdata = {
            }
        }
    }
    chainhelper:read_chain()
    str = cjson.encode(public_data.userdata)
    chainhelper:log("public data: " .. str)
]]
end

function get_public_data2(key)
    read_list = {
        public_data = {
            userdata = {
                key = {}
            }
        }
    }
    chainhelper:read_chain()
    str = cjson.encode(public_data.userdata)
    chainhelper:log("public data2222: " .. str)
end
