import time
from api_script.jianzhao_web.b_basic.toB_comleteInfo_3 import company_auth, completeInfo
from utils.util import assert_equal


def test_company_certification():
    company_auth_result = company_auth()
    if company_auth_result['state'] == 1:
        complete_info = completeInfo()
        assert_equal(1, complete_info['state'], "校验公司认证是否成功")
    else:
        assert_equal(1, company_auth_result['state'], "校验申请认证公司是否成功")


def test_():
    time.sleep(3)
