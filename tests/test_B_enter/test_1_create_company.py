import time
import pytest

from api_script.jianzhao_web.b_basic.company import jump_html
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import saveHR, saveCompany, \
    submit_new
from api_script.jianzhao_web.b_basic.b_upload import upload_permit
from api_script.jianzhao_web.company_new.users import user_register_lagou
from api_script.neirong_app.account import upate_user_password
from utils.util import assert_equal, pc_send_register_verifyCode, verify_code_message


def test_register_admin_user(get_countryCode_phone_admin_user):
    global countryCode, phone, user_name, verify_code
    countryCode, phone, user_name = get_countryCode_phone_admin_user[0], get_countryCode_phone_admin_user[1], \
                                    get_countryCode_phone_admin_user[2]
    if pc_send_register_verifyCode(countryCode, phone) == 1:
        verify_code = verify_code_message(countryCode, phone)
        assert_equal(True, bool(verify_code), '获取验证码成功')
        register = user_register_lagou(countryCode, phone, verify_code)
        assert_equal(1, register['state'], '校验管理员注册是否成功！')
    else:
        assert_equal(1, 2, '校验发送验证码是否成功')


def test_create_company_info(get_company_name):
    company_name = get_company_name
    personal_msg_save_and_creat_company = saveHR(company_name, user_name,
                                                 'ariaxie@lagou.com')
    if personal_msg_save_and_creat_company['state'] == 1:
        company_msg_save = saveCompany(company_name)
        assert_equal(1, company_msg_save['state'], "校验公司是否新建成功")
    else:
        assert_equal(1, personal_msg_save_and_creat_company['state'], "校验HR信息是否保存成功")


def test_jump_html():
    save_result = jump_html()
    assert_equal(1, save_result['state'], '校验是否跳过选择优质简历')


def test_admin_personal_certificate():
    upload_p = upload_permit()
    if upload_p['state'] == 1:
        personal_certificate_submit = submit_new()
        assert_equal(1, personal_certificate_submit['state'], "校验提交招聘者身份审核是否成功")
    else:
        assert_equal(1, upload_p['state'], "校验提交身份信息是否成功")


def test_():
    time.sleep(120)


@pytest.mark.parametrize('newPassword', [('990eb670f81e82f546cfaaae1587279a')])
def test_update_admin_user(newPassword):
    r = upate_user_password(newPassword)
    assert_equal(1, r['state'], '管理员修改密码成功')
