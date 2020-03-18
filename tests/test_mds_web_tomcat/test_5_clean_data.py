# coding:utf-8
# @Time  : 2019-11-26 18:34
# @Author: Xiawang
# Description:
from api_script.entry.cuser.baseStatus import batchCancel
from api_script.home import forbid
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import remove_member, close_trial_package
from utils.read_file import record_test_data
from utils.util import assert_equal, login_password
from .test_1_create_company import skip_
from .test_2_join_company import skip__


@skip__
@skip_
def test_login_general_user(get_countryCode_phone_general_user, get_password):
    global general_countryCode, general_phone, user_name, verify_code
    general_countryCode, general_phone, user_name = get_countryCode_phone_general_user[0], \
                                                    get_countryCode_phone_general_user[1], \
                                                    get_countryCode_phone_general_user[2]
    login_result = login_password(general_countryCode + general_phone, get_password)
    assert_equal(1, login_result['state'], '校验普通用户登录是否成功')


@skip__
@skip_
def test_remove_general_user(get_user_info, get_password):
    global general_userId, UserCompanyId, lg_CompanyId
    general_userId, UserCompanyId, lg_CompanyId = get_user_info[0], get_user_info[1], get_user_info[2]
    remove_result = remove_member(general_userId)
    if not remove_result:
        close_trial_package(lg_CompanyId)
        login_password(general_countryCode + general_phone, get_password)
        remove_result = remove_member(general_userId)
    assert_equal(True, remove_result, '校验移除普通用户成功！')


@skip__
@skip_
def test_record_general_user():
    record_test_data(2, userId=general_userId, UserCompanyId=UserCompanyId, lg_CompanyId=lg_CompanyId)


@skip__
@skip_
def test_batchCancel():
    r = batchCancel(userIds=general_userId)
    assert_equal(1, r['state'], "普通用户注销账号成功")


@skip__
@skip_
def test_login_admin_user(get_countryCode_phone_admin_user, get_password):
    global admin_countryCode, admin_phone, user_name, verify_code
    admin_countryCode, admin_phone, user_name = get_countryCode_phone_admin_user[0], get_countryCode_phone_admin_user[
        1], \
                                                get_countryCode_phone_admin_user[2]
    login_result = login_password(admin_countryCode + admin_phone, get_password)
    assert_equal(1, login_result['state'], '校验管理员登录是否成功')


@skip__
@skip_
def test_remove_admin_user(get_user_info, get_password):
    global admin_userId
    admin_userId, UserCompanyId, lg_CompanyId = get_user_info[0], get_user_info[1], get_user_info[2]
    remove_result = remove_member(admin_userId)
    if not remove_result:
        close_trial_package(lg_CompanyId)
        login_password(admin_countryCode + admin_phone, get_password)
        remove_result = remove_member(admin_userId)
    assert_equal(True, remove_result, '校验移除管理员用户成功！')


@skip__
@skip_
def test_record_admin_user():
    record_test_data(2, userId=admin_userId, UserCompanyId=UserCompanyId, lg_CompanyId=lg_CompanyId)


@skip__
@skip_
def test_batchCancel():
    r = batchCancel(userIds=admin_userId)
    assert_equal(1, r['state'], "普通用户注销账号成功")


@skip__
@skip_
def test_login_home():
    # 线上home后台的用户账号和密码, 勿动
    r = login_password('betty@lagou.com', '00f453dfec0f2806db5cfabe3ea94a35')
    assert_equal(1, r['state'], '校验登录home成功！')


@skip__
@skip_
def test_forbid_general_user():
    forbid_result = forbid.forbid_user(general_userId)
    assert_equal(True, forbid_result, '校验普通用户是否封禁成功1')


@skip__
@skip_
def test_forbid_admin_user():
    forbid_result = forbid.forbid_user(admin_userId)
    assert_equal(True, forbid_result, '校验管理员用户是否封禁成功1')


@skip__
@skip_
def test_forbid_company():
    forbid_result = forbid.forbid_company(lg_CompanyId)
    assert_equal(True, forbid_result, '校验公司是否封禁成功')
