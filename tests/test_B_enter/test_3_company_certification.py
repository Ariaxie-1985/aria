from api_script.jianzhao_web.b_basic.toB_comleteInfo_3 import company_auth, completeInfo
from utils.util import login, login_password, login_verifyCode, pc_send_register_verifyCode, verify_code_message, \
    assert_equal


def test_login_user(get_countryCode_phone_admin_user):
    global countryCode, phone, user_name, verify_code
    countryCode, phone, user_name = get_countryCode_phone_admin_user[0], get_countryCode_phone_admin_user[1], \
                                    get_countryCode_phone_admin_user[2]
    if pc_send_register_verifyCode(countryCode, phone) == 1:
        verify_code = verify_code_message(countryCode, phone)
        assert_equal(True, bool(verify_code), '获取验证码成功')


def test_company_certification():
    login_verifyCode(countryCode, phone, verify_code)
    company_auth()
    completeInfo()


if __name__ == '__main__':
    login('00852', '24482062')
    test_company_certification()
