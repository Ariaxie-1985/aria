# coding:utf-8
# @Time  : 2020/2/26 19:01
# @Author: Xiawang
# Description:
import pytest

from api_script.zhaopin_app.wechat import wechat_qr_code
from utils.util import assert_equal


@pytest.mark.parametrize("qrcodeType", [("TALENT_HUNTER"), ("FLOW_FROM_HOME_PAGE"), ("FLOW_FROM_RESUME_PAGE"),
                                        ("FLOW_FROM_RESUME_FIXED"), ("FLOW_FROM_IM_PAGE"), ("SMALL_CHANGE_AMOUNT_LG"),
                                        ("PAY_CONVERSION")])
def test_wechat_qr_code(b_login_app, qrcodeType,ip_port):
    r = wechat_qr_code(qrcodeType=qrcodeType, userToken=b_login_app[0], userId=b_login_app[1],ip_port=ip_port)
    assert_equal(True, bool(r['content']['url']), "获取拉勾公众号二维码用例通过")
