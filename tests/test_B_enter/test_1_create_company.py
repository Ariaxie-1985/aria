from api_script.jianzhao_web.b_basic.toB_saveHR_1 import b_register, saveHR, saveCompany, submit, add_saveCompany, \
    submit_new, get_b_userId
from api_script.jianzhao_web.b_basic.b_upload import upload_permit
from api_script.jianzhao_web.company_new.users import user_register_lagou
from utils.util import assert_equal, pc_send_register_verifyCode, verify_code_message


def test_register_user(get_countryCode_phone_admin_user):
    global countryCode, phone, user_name, verify_code
    countryCode, phone, user_name = get_countryCode_phone_admin_user[0], get_countryCode_phone_admin_user[1], \
                                    get_countryCode_phone_admin_user[2]
    if pc_send_register_verifyCode(countryCode, phone) == 1:
        verify_code = verify_code_message(countryCode, phone)
        assert_equal(True, bool(verify_code), '获取验证码成功')


def test_create_company_info(get_company_name):
    register = user_register_lagou(countryCode, phone, verify_code)
    company_name = get_company_name[0]
    if register['state'] == 1:
        personal_msg_save_and_creat_company = saveHR(company_name, user_name,
                                                     'ariaxie@lagou.com')
        if personal_msg_save_and_creat_company['state'] == 1:
            company_msg_save = saveCompany(company_name)
            assert_equal(1, company_msg_save['state'], "校验公司是否新建成功")
        else:
            assert_equal(1, personal_msg_save_and_creat_company['state'], "校验HR信息是否保存成功")
    else:
        assert_equal(1, register['state'], "校验B端用户注册是否成功")


def test_personal_certificate():
    upload_p = upload_permit()
    if upload_p['state'] == 1:
        personal_certificate_submit = submit_new()
        assert_equal(1, personal_certificate_submit['state'], "校验提交招聘者身份审核是否成功")
    else:
        assert_equal(1, upload_p['state'], "校验提交身份信息是否成功")


def test_record_data():
    userId, UserCompanyId, lg_CompanyId = get_b_userId()
    assert_equal(True, bool(userId), '校验获取用户id是否成功')
    assert_equal(True, bool(UserCompanyId), '校验获取简招公司id是否成功')
    assert_equal(True, bool(lg_CompanyId), '校验获取拉勾公司id是否成功')


if __name__ == '__main__':
    test_create_company_info(user_name)
    test_personal_certificate()
