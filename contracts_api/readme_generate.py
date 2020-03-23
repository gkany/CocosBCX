print("### 1. read register_scheduler::function registerFunction")
func_names = {}  # lua_func:cpp_func
src_file_name = "contract_register_function.cpp"
src_file = open(src_file_name, 'r')
for line in src_file.readlines():
    if line.find("registerFunction(") != -1:
        tokens = line.split("&")
        lua_func_name = tokens[0].split('"')[1]
        print("   " + lua_func_name)
        func_name = tokens[1]
        func_name = func_name[:-3]
        # print("   " + func_name)
        func_name = func_name.split("::")[1]
        func_names[lua_func_name] = func_name
    elif line.find("registerFunction<") != -1:
        pass
    else:
        continue
src_file.close()

print("\n### 2. write register_scheduler::register-function to README.md")
readme_file = open("README.md", "w+")
readme_file.write("## contract api\n")
api_count = 1

flag = False
src_file = open(src_file_name, 'r')
for line in src_file.readlines():
    if flag or line.find("struct register_scheduler") != -1:
        flag = True
    else:
        continue
    for lua_func_name in func_names:
        cpp_func_name = func_names[lua_func_name]
        if line.find(cpp_func_name+"(") != -1 and line.find("registerFunction(") == -1:
            api_desc = "### {}. {}\n* 函数名:\n``` text\n\t[lua] {}  -->  [cpp] {}\n```\n* cpp函数原型：\n``` c++\n\t{}\n```\n\n".format(
                api_count, lua_func_name, lua_func_name, cpp_func_name, line.strip())
            # print(api_desc)
            readme_file.write(api_desc)
            api_count += 1
print("total api function: {}".format(api_count))
src_file.close()

print("\n### 3. write register-lambda-function to README.md")
startWith = "registerFunction<register_scheduler, "
src_file = open(src_file_name, 'r')
for line in src_file.readlines():
    if line.find("registerFunction<") != -1:
        line = line.strip()
        tokens = line.split(">")
        func_name = tokens[1][2:-2]
        print("   " + func_name)
        params = tokens[0][len(startWith):]
        params_tokens = params.split("(")
        full_func_name = "{} {}({}".format(params_tokens[0], func_name, params_tokens[1])
        # print(full_func_name)
        # api_desc = "### {}. {}\n> 函数原型：\n``` c++\n{}\n```\n\n".format(api_count, func_name, full_func_name)
        api_desc = "### {}. {}\n* 函数名:\n``` text\n\t[lua] {}  -->  [cpp] {}\n```\n* cpp函数原型：\n``` c++\n\t{}\n```\n\n".format(
            api_count, func_name, func_name, func_name, full_func_name)
        # print(api_desc)
        readme_file.write(api_desc)
        api_count += 1
src_file.close()
readme_file.close()

