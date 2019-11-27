from api_script.jianzhao_web.b_basic.admin_review import admin_review
from api_script.jianzhao_web.b_basic.b_upload import upload_permit
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import saveHR, add_saveCompany, submit_new
from api_script.jianzhao_web.company_new.users import user_register_lagou
from utils.util import assert_equal, pc_send_register_verifyCode, verify_code_message, login_verifyCode


def test_register_user(get_countryCode_phone_general_user):
    global countryCode, phone, user_name, verify_code
    countryCode, phone, user_name = get_countryCode_phone_general_user[0], get_countryCode_phone_general_user[1], \
                                    get_countryCode_phone_general_user[2]
    if pc_send_register_verifyCode(countryCode, phone) == 1:
        verify_code = verify_code_message(countryCode, phone)
        assert_equal(True, bool(verify_code), '获取验证码成功')

def test_join_company(get_company_name):
    register = user_register_lagou(countryCode, phone, verify_code)
    company_name = get_company_name[0]
    if register['state'] == 1:
        personal_msg_save = saveHR(company_name, user_name, 'ariaxie@lagou.com', '技术总监')
    else:
        assert_equal(1, register['state'], "校验B端用户注册是否成功")
    if personal_msg_save['state'] == 1:
        join_company = add_saveCompany()
        if join_company['state'] == 1:
            upload_p = upload_permit()
            if upload_p['state'] == 1:
                personal_certificate_submit = submit_new()
                assert_equal(1, personal_certificate_submit['state'], "校验提交招聘者身份审核是否成功")
            else:
                assert_equal(1, upload_p['state'], "校验提交身份信息是否成功")
        else:
            assert_equal(1, join_company['state'], "校验加入公司是否成功")
    else:
        assert_equal(1, personal_msg_save['state'], "校验保存用户信息是否成功")

def test_get_userid(get_user_info):
    global general_user_id
    general_user_id = get_user_info[0]
    assert_equal(True, bool(userid), '获取用户ID是否成功')

def test_login_user(get_countryCode_phone_admin_user):
    global countryCode, phone, user_name, verify_code
    countryCode, phone, user_name = get_countryCode_phone_admin_user[0], get_countryCode_phone_admin_user[1], \
                                    get_countryCode_phone_admin_user[2]
    if pc_send_register_verifyCode(countryCode, phone) == 1:
        verify_code = verify_code_message(countryCode, phone)
        assert_equal(True, bool(verify_code), '获取验证码成功')

def test_admin_review():
    login_verifyCode(countryCode, phone, verify_code)
    admin_review(userid=general_user_id)

