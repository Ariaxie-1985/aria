# coding:utf-8
# @Time  : 2019-03-07 17:27
# @Author: Xiawang

from api_script.neirong_app.AutoInviteSwitch import autoInviteSwitch_status
from utils.util import assert_equal


def setUp():
    pass


def tearDown():
    pass


def test_autoInviteSwitch_status(login_app, ip_port):
    r = autoInviteSwitch_status(userToken=login_app[0], userId=login_app[1], ip_port=ip_port)
    assert_equal(1, r['state'], "获取自动邀约的开关状态成功")
