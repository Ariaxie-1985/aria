import time

import pytest

from api_script.jianzhao_web.b_basic.toB_comleteInfo_3 import company_auth, completeInfo
from utils.util import login, login_password, login_verifyCode, pc_send_register_verifyCode, verify_code_message, \
    assert_equal, pc_send_login_verifyCode


@pytest.mark.skip(reason='暂时不执行')
def test_login_admin_user(get_countryCode_phone_admin_user):
    global countryCode, phone, user_name, verify_code
    countryCode, phone, user_name = get_countryCode_phone_admin_user[0], get_countryCode_phone_admin_user[1], \
                                    get_countryCode_phone_admin_user[2]
    if pc_send_login_verifyCode(countryCode, phone) == 1:
        verify_code = verify_code_message(countryCode, phone)
        assert_equal(True, bool(verify_code), '获取验证码成功')
        login_result = login_verifyCode(countryCode, phone, verify_code)
        assert_equal(1, login_result['state'], '校验管理员登录是否成功')


def test_company_certification():
    company_auth_result = company_auth()
    if company_auth_result['state'] == 1:
        complete_info = completeInfo()
        assert_equal(1, complete_info['state'], "校验公司认证是否成功")
    else:
        assert_equal(1, company_auth_result['state'], "校验申请认证公司是否成功")


def test_():
    time.sleep(120)
