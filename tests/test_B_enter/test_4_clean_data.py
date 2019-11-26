# coding:utf-8
# @Time  : 2019-11-26 18:34
# @Author: Xiawang
# Description:
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import remove_member, close_trial_package
from utils.read_file import record_test_data
from utils.util import pc_send_register_verifyCode, verify_code_message, assert_equal, login_verifyCode


def test_login_general_user(get_countryCode_phone_general_user):
    global countryCode, phone, user_name, verify_code
    countryCode, phone, user_name = get_countryCode_phone_general_user[0], get_countryCode_phone_general_user[1], \
                                    get_countryCode_phone_general_user[2]
    if pc_send_register_verifyCode(countryCode, phone) == 1:
        verify_code = verify_code_message(countryCode, phone)
        assert_equal(True, bool(verify_code), '获取验证码成功')


def test_remove_general_user(get_user_info):
    global userId, UserCompanyId, lg_CompanyId
    userId, UserCompanyId, lg_CompanyId = get_user_info[0], get_user_info[1], get_user_info[2]
    login_verifyCode(countryCode, phone, verify_code)
    if not remove_member(userId):
        close_trial_package(lg_CompanyId)
        login_verifyCode(countryCode, phone, verify_code)
        result = remove_member(userId)
        assert_equal(True, result, '移除普通用户')


def test_record_general_user():
    record_test_data(2, userId=userId, UserCompanyId=UserCompanyId, lg_CompanyId=lg_CompanyId)


def test_login_admin_user(get_countryCode_phone_admin_user):
    global countryCode, phone, user_name, verify_code
    countryCode, phone, user_name = get_countryCode_phone_admin_user[0], get_countryCode_phone_admin_user[1], \
                                    get_countryCode_phone_admin_user[2]
    if pc_send_register_verifyCode(countryCode, phone) == 1:
        verify_code = verify_code_message(countryCode, phone)
        assert_equal(True, bool(verify_code), '获取验证码成功')


def test_remove_admin_user(get_user_info):
    userId, UserCompanyId, lg_CompanyId = get_user_info[0], get_user_info[1], get_user_info[2]
    login_verifyCode(countryCode, phone, verify_code)
    if not remove_member(userId):
        close_trial_package(lg_CompanyId)
        login_verifyCode(countryCode, phone, verify_code)
        result = remove_member(userId)
        assert_equal(True, result, '移除管理员用户')


def test_record_admin_user():
    record_test_data(2, userId=userId, UserCompanyId=UserCompanyId, lg_CompanyId=lg_CompanyId)
