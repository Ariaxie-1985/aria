# coding:utf-8
# @Time  : 2019-11-26 18:34
# @Author: Xiawang
# Description:
import pytest

from api_script.jianzhao_web.b_basic.toB_saveHR_1 import remove_member, close_trial_package
from utils.read_file import record_test_data
from utils.util import pc_send_register_verifyCode, verify_code_message, assert_equal, login_verifyCode, \
    pc_send_login_verifyCode, login_password


def test_login_general_user(get_countryCode_phone_general_user):
    global countryCode, phone, user_name, verify_code
    countryCode, phone, user_name = get_countryCode_phone_general_user[0], get_countryCode_phone_general_user[1], \
                                    get_countryCode_phone_general_user[2]
    if pc_send_login_verifyCode(countryCode, phone) == 1:
        verify_code = verify_code_message(countryCode, phone, flag_num=1)
        assert_equal(True, bool(verify_code), '获取验证码成功')
        login_result = login_verifyCode(countryCode, phone, verify_code)
        assert_equal(1, login_result['state'], '校验普通用户登录是否成功')


def test_remove_general_user(get_user_info):
    global userId, UserCompanyId, lg_CompanyId
    userId, UserCompanyId, lg_CompanyId = get_user_info[0], get_user_info[1], get_user_info[2]
    remove_result = remove_member(userId)
    if not remove_result:
        close_trial_package(lg_CompanyId)
        login_verifyCode(countryCode, phone, verify_code)
        remove_result = remove_member(userId)
        assert_equal(True, remove_result, '校验移除普通用户成功')
    else:
        assert_equal(True, remove_result, '校验移除普通用户成功！')


@pytest.mark.skip(reason="暂时不记录")
def test_record_general_user():
    record_test_data(2, userId=userId, UserCompanyId=UserCompanyId, lg_CompanyId=lg_CompanyId)


def test_login_admin_user(get_countryCode_phone_admin_user):
    global countryCode, phone, user_name, verify_code
    countryCode, phone, user_name = get_countryCode_phone_admin_user[0], get_countryCode_phone_admin_user[1], \
                                    get_countryCode_phone_admin_user[2]
    if pc_send_login_verifyCode(countryCode, phone) == 1:
        verify_code = verify_code_message(countryCode, phone, flag_num=2)
        assert_equal(True, bool(verify_code), '获取验证码成功')
        login_result = login_verifyCode(countryCode, phone, verify_code)
        assert_equal(1, login_result['state'], '校验管理员登录是否成功')


def test_remove_admin_user(get_user_info):
    userId, UserCompanyId, lg_CompanyId = get_user_info[0], get_user_info[1], get_user_info[2]

    if not remove_member(userId):
        close_trial_package(lg_CompanyId)
        login_password('betty@lagou.com', '00f453dfec0f2806db5cfabe3ea94a35')
        result = remove_member(userId)
        assert_equal(True, result, '移除管理员用户')


@pytest.mark.skip(reason="暂时不记录")
def test_record_admin_user():
    record_test_data(2, userId=userId, UserCompanyId=UserCompanyId, lg_CompanyId=lg_CompanyId)
