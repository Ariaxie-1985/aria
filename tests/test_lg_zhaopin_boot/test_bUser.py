# coding:utf-8
# @Time  : 2020/2/26 17:22
# @Author: Xiawang
# Description:
from api_script.zhaopin_app.bUser import member_all
from utils.util import assert_equal


def test_member_all(b_login_app):
    r = member_all(userToken=b_login_app[0])
    assert_equal(True, bool(r['content']['result']), "查看我公司下的成员用例通过")
