import time
from api_script.jianzhao_web.b_basic.toB_comleteInfo_3 import company_auth, completeInfo
from utils.util import assert_equal, login_password
from .test_1_create_company import skip_
from .test_2_join_company import skip_1


@skip_1
@skip_
def test_login_admin_user(get_countryCode_phone_admin_user, get_password):
    global admin_countryCode, admin_phone, admin_user_name, verify_code
    admin_countryCode, admin_phone, admin_user_name = get_countryCode_phone_admin_user[0], \
                                                      get_countryCode_phone_admin_user[1], \
                                                      get_countryCode_phone_admin_user[2]
    login_result = login_password(admin_countryCode + admin_phone, get_password)
    assert_equal(1, login_result['state'], '校验管理员登录是否成功')


@skip_1
@skip_
def test_company_certification():
    company_auth_result = company_auth()
    if company_auth_result['state'] == 1:
        complete_info = completeInfo()
        assert_equal(1, complete_info['state'], "校验公司认证是否成功")
    else:
        assert_equal(1, company_auth_result['state'], "校验申请认证公司是否成功")


@skip_1
@skip_
def test_():
    time.sleep(3)
