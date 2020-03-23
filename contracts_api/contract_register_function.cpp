


void lua_scheduler::chain_function_bind()
{
    registerMember("name", &contract_base_info::name);
    registerMember("id", &contract_base_info::id);
    registerMember("owner", &contract_base_info::owner);
    registerMember("caller", &contract_base_info::caller);
    registerMember("creation_date", &contract_base_info::creation_date);
    registerMember("contract_authority", &contract_base_info::contract_authority);
    registerMember("invoker_contract_id", &contract_base_info::invoker_contract_id);

    registerFunction("log", &register_scheduler::log);
    registerFunction("number_max", &register_scheduler::nummax);
    registerFunction("number_min", &register_scheduler::nummin);
    registerFunction("real_time", &register_scheduler::real_time);
    registerFunction("time", &register_scheduler::head_block_time);
    registerFunction("hash256", &register_scheduler::hash256);
    registerFunction("hash512", &register_scheduler::hash512);
    registerFunction("make_memo", &register_scheduler::make_memo);
    registerFunction("make_release", &register_scheduler::make_release);
    registerFunction("random", &register_scheduler::contract_random);
    registerFunction("is_owner", &register_scheduler::is_owner);
    registerFunction("read_chain", &register_scheduler::read_cache);
    registerFunction("write_chain", &register_scheduler::fllush_cache);
    registerFunction("create_nh_asset", &register_scheduler::create_nh_asset);
    registerFunction("adjust_lock_asset", &register_scheduler::adjust_lock_asset);
    registerFunction("nht_describe_change", &register_scheduler::nht_describe_change);
    registerFunction("set_permissions_flag", &register_scheduler::set_permissions_flag);
    registerFunction("set_invoke_percent", &register_scheduler::set_invoke_percent);
    registerFunction("set_invoke_share_percent", &register_scheduler::set_invoke_share_percent);
    registerFunction("invoke_contract_function", &register_scheduler::invoke_contract_function);
    registerFunction("change_contract_authority", &register_scheduler::change_contract_authority);
    registerFunction("update_collateral_for_gas", &register_scheduler::update_collateral_for_gas);
    lua_register(mState, "import_contract", &import_contract);
    lua_register(mState, "get_account_contract_data", &get_account_contract_data);
    lua_register(mState, "format_vector_with_table", &format_vector_with_table);
    registerFunction<register_scheduler, void(string, double, string, bool)>("transfer_from_owner",
                                                                             [](register_scheduler &fc_register, string to, double amount, string symbol, bool enable_logger = false) {
                                                                                 fc_register.transfer_from(fc_register.contract.owner, to, amount, symbol, enable_logger);
                                                                             });
    registerFunction<register_scheduler, void(string, double, string, bool)>("transfer_from_caller",
                                                                             [](register_scheduler &fc_register, string to, double amount, string symbol, bool enable_logger = false) {
                                                                                 fc_register.transfer_from(fc_register.caller, to, amount, symbol, enable_logger);
                                                                             });
    registerFunction<register_scheduler, void(string, string, bool)>("transfer_nht_from_owner",
                                                                     [](register_scheduler &fc_register, string to, string token_hash_or_id, bool enable_logger = false) {
                                                                         auto &token = fc_register.get_nh_asset(token_hash_or_id);
                                                                         auto &account_to = fc_register.get_account(to).id;
                                                                         fc_register.transfer_nht(fc_register.contract.owner, account_to, token, enable_logger);
                                                                     });
    registerFunction<register_scheduler, void(string, string, bool)>("transfer_nht_from_caller",
                                                                     [](register_scheduler &fc_register, string to, string token_hash_or_id, bool enable_logger = false) {
                                                                         auto &token = fc_register.get_nh_asset(token_hash_or_id);
                                                                         auto &account_to = fc_register.get_account(to).id;
                                                                         fc_register.transfer_nht(fc_register.caller, account_to, token, enable_logger);
                                                                     });
    registerFunction<register_scheduler, int64_t(string, string)>("get_account_balance",
                                                                  [](register_scheduler &fc_register, string account, string symbol) -> int64_t {
                                                                      auto &account_ob = fc_register.get_account(account);
                                                                      auto &asset = fc_register.get_asset(symbol);
                                                                      return fc_register.get_account_balance(account_ob.id, asset.id);
                                                                  });
    registerFunction<register_scheduler, void(string, string, bool)>("change_nht_active_by_owner",
                                                                     [](register_scheduler &fc_register, string beneficiary_account, string token_hash_or_id, bool enable_logger = false) {
                auto& token = fc_register.get_nh_asset(token_hash_or_id);
                auto& account_to = fc_register.get_account(beneficiary_account).id;
                fc_register.transfer_nht_active(fc_register.contract.owner, account_to, token,enable_logger); });
    registerFunction<register_scheduler, void(string, string, bool)>("transfer_nht_active_from_caller",
                                                                     [](register_scheduler &fc_register, string to, string token_hash_or_id, bool enable_logger = false) {
                auto& token = fc_register.get_nh_asset(token_hash_or_id);
                auto& account_to = fc_register.get_account(to).id;
                fc_register.transfer_nht_active(fc_register.caller, account_to, token,enable_logger); });
    /*            
    registerFunction<register_scheduler, void(string, string, bool)>("transfer_nht_ownership_from_owner",
                                                                     [](register_scheduler &fc_register, string to, string token_hash_or_id, bool enable_logger = false) {
                auto& token =fc_register.get_nh_asset(token_hash_or_id);
                auto& account_to = fc_register.get_account(to).id;
                fc_register.transfer_nht_ownership(fc_register.contract.owner, account_to, token,enable_logger); });
    registerFunction<register_scheduler, void(string, string, bool)>("transfer_nht_ownership_from_caller",
                                                                     [](register_scheduler &fc_register, string to, string token_hash_or_id, bool enable_logger = false) {
                auto& token =fc_register.get_nh_asset(token_hash_or_id);
                auto& account_to = fc_register.get_account(to).id;;
                fc_register.transfer_nht_ownership(fc_register.caller, account_to, token,enable_logger); });
    */
    registerFunction<register_scheduler, void(string, string, bool)>("transfer_nht_dealership_from_owner",
                                                                     [](register_scheduler &fc_register, string to, string token_hash_or_id, bool enable_logger = false) {
                auto& token =fc_register.get_nh_asset(token_hash_or_id);
                auto& account_to = fc_register.get_account(to).id;
                fc_register.transfer_nht_dealership(fc_register.contract.owner, account_to, token,enable_logger); });
    registerFunction<register_scheduler, void(string, string, bool)>("transfer_nht_dealership_from_caller",
                                                                     [](register_scheduler &fc_register, string to, string token_hash_or_id, bool enable_logger = false) {
                auto& token =fc_register.get_nh_asset(token_hash_or_id);
                auto& account_to = fc_register.get_account(to).id;
                fc_register.transfer_nht_dealership(fc_register.caller, account_to, token,enable_logger); });
    registerFunction<register_scheduler, void(string, string, bool, bool)>("set_nht_limit_list",
                                                                           [](register_scheduler &fc_register, string token_hash_or_id, string contract_name_or_ids, bool limit_type, bool enable_logger = false) {
                auto& token =fc_register.get_nh_asset(token_hash_or_id);
                fc_register.set_nht_limit_list(fc_register.caller, token, contract_name_or_ids, limit_type, enable_logger); });
    registerFunction<register_scheduler, void(string, string, bool, bool)>("relate_nh_asset",
                                                                           [](register_scheduler &fc_register, string parent_token_hash_or_id, string child_token_hash_or_id, bool relate, bool enable_logger = false) {
                auto& parent =fc_register.get_nh_asset(parent_token_hash_or_id);
                auto& child =fc_register.get_nh_asset(child_token_hash_or_id);
                fc_register.relate_nh_asset(fc_register.caller, parent, child, relate, enable_logger); });
}

#pragma once
#include <graphene/chain/contract_object.hpp>
#include <graphene/chain/nh_asset_object.hpp>
namespace graphene
{
namespace chain
{
#define LUA_C_ERR_THROW(L,eMsg) \
lua_scheduler::Pusher<string>::push(L, eMsg).release();\
lua_scheduler::luaError(L);

struct register_scheduler
{
    database &db;
    contract_object &contract;
    account_id_type caller;
    contract_result &result;
    struct process_variable& _process_value;
    const transaction_evaluation_state * trx_state;
    lua_scheduler &context;
    const flat_set<public_key_type>& sigkeys;
    contract_result& apply_result;
    map<lua_key,lua_types>& account_conntract_data;
    register_scheduler(database &db,account_id_type caller ,contract_object &contract,const transaction_evaluation_state * mode, 
        contract_result &result,lua_scheduler &context,const flat_set<public_key_type>& sigkeys, contract_result& apply_result,map<lua_key,lua_types>& account_data)
        : db(db),contract(contract),caller(caller), result(result),_process_value(contract.get_process_variable()),trx_state(mode),context(context),sigkeys(sigkeys),
        apply_result(apply_result),account_conntract_data(account_data){
          result.contract_id= contract.id;
        }
    bool is_owner();
    void log(string message);
    int contract_random();
    void set_permissions_flag(bool flag);
    void set_invoke_percent(double percent);
    void set_invoke_share_percent(double percent);
    void read_cache();
    void fllush_cache();
    lua_Number nummin();
    lua_Number nummax();
    const nh_asset_object& get_nh_asset(string hash_or_id);
    string hash256(string source);
    string hash512(string source);
    uint32_t head_block_time();
    uint64_t real_time();
    const account_object& get_account(string name_or_id);
    void adjust_lock_asset(string symbol_or_id,int64_t amount);
    static std::pair<bool, lua_types *>  find_luaContext( lua_map* context, vector<lua_types> keys,int start=0,bool is_clean=false);
    string create_nh_asset(string owner_id_or_name,string symbol,string world_view,string base_describe,bool enable_logger);
    void fllush_context(const lua_map& keys, lua_map &data_table,vector<lua_types>&stacks, string tablename);
    void read_context( lua_map& keys, lua_map &data_table,vector<lua_types>&stacks, string tablename);
    static void filter_context(const lua_map &data_table, lua_map keys,vector<lua_types>&stacks,lua_map *result_table);
    void transfer_by_contract(account_id_type from, account_id_type to, asset token, contract_result &result,bool enable_logger=false);
    const asset_object& get_asset(string symbol_or_id);
    int64_t get_account_balance(account_id_type account,asset_id_type asset_id);
    void transfer_from(account_id_type from, string to, double amount, string symbol_or_id,bool enable_logger=false);
    void transfer_nht(account_id_type from,account_id_type account_to,const nh_asset_object& token ,bool enable_logger=false);
    void nht_describe_change(string nht_hash_or_id,string key,string value,bool enable_logger=false);
    void change_contract_authority(string authority);
    memo_data make_memo(string receiver_id_or_name, string key, string value, uint64_t ss,bool enable_logger=false);
    void invoke_contract_function(string contract_id_or_name,string function_name,string value_list_json);
    const contract_object& get_contract(string name_or_id);
    void make_release();
	// transfer of non homogeneous asset's use rights
	void transfer_nht_active(account_id_type from,account_id_type account_to,const nh_asset_object& token ,bool enable_logger=false);
	// transfer of non homogeneous asset's ownership
    void transfer_nht_ownership(account_id_type from, account_id_type account_to,const nh_asset_object &token, bool enable_logger=false);
	// transfer of non homogeneous asset's authority
	void transfer_nht_dealership(account_id_type from, account_id_type account_to,const nh_asset_object &token, bool enable_logger=false);
	// set non homogeneous asset's limit list
	void set_nht_limit_list(account_id_type nht_owner,const nh_asset_object &token, const string& contract_name_or_ids, bool limit_type, bool enable_logger=false);
    // relate parent nh asset and child nh asset
    void relate_nh_asset(account_id_type nht_creator, const nh_asset_object &parent_nh_asset, const nh_asset_object &child_nh_asset, bool relate, bool enable_logger=false);

    void update_collateral_for_gas(string to, int64_t amount);

};
}}

