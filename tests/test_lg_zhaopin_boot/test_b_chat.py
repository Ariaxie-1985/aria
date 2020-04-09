# coding:utf-8
# @Time  : 2020/2/26 16:28
# @Author: Xiawang
# Description:
from api_script.zhaopin_app.b_chat import chat_c_lastResume
from api_script.zhaopin_app.me import get_me_info
from utils.util import assert_equal


def test_get_me_info(b_login_app,ip_port):
    r = get_me_info(userToken=b_login_app[0], userId=b_login_app[1],ip_port=ip_port)
    assert_equal("拉勾测试-XM", r['content']['companyFullName'], "获取B端用户信息用例通过")


def test_chat_c_lastResume(b_login_app, c_login_app,ip_port):
    r = chat_c_lastResume(userToken=b_login_app[0], userId=b_login_app[1], cUserId=c_login_app[1],ip_port=ip_port)
    assert_equal(c_login_app[1], r['content']['userId'], "获取候选人最近一次投递状态用例通过")
