# coding:utf-8
# @Time  : 2019-03-07 17:27
# @Author: Xiawang
import pytest

from api_script.neirong_app.AutoInviteSwitch import autoInviteSwitch_status, autoInviteSwitch_open
from utils.util import assert_equal, assert_not_equal

display = 2
noExposureSwitchDisplay = 2
noExposureSwitchStatus = 1
status = 1


def test_autoInviteSwitch_status():
    r = autoInviteSwitch_status().json()
    global display, noExposureSwitchDisplay, noExposureSwitchStatus, status
    try:
        display = r['content']['display']
        noExposureSwitchDisplay = r['content']['noExposureSwitchDisplay']
        noExposureSwitchStatus = r['content']['noExposureSwitchStatus']
        status = r['content']['status']
    finally:
        assert_equal(1, r['state'], "获取自动邀约(特权职位/普通职位&无曝光职位)的开关状态成功", "获取自动邀约(特权职位/普通职位&无曝光职位)的开关状态失败")


@pytest.mark.skipif(display == 2, reason="普通/特权邀约功能按钮不显示，跳过此用例")
def test_autoInviteSwitch_open_1():
    if status == 1:
        r = autoInviteSwitch_open(1, 2)
        assert_equal(1, r['state'], "普通/特权邀约功能的自动邀约开启成功")
    elif status == 2:
        r = autoInviteSwitch_open(1, 1)
        assert_equal(1, r['state'], "普通/特权邀约功能的自动邀约关闭成功")


@pytest.mark.skipif(noExposureSwitchDisplay == 2, reason="无曝光邀约功能按钮不显示，跳过此用例")
def test_autoInviteSwitch_open_2():
    if noExposureSwitchStatus == 1:
        r = autoInviteSwitch_open(2, 2)
        assert_equal(1, r['state'], "无曝光邀约功能的自动邀约开启成功")
    elif status == 2:
        r = autoInviteSwitch_open(2, 1)
        assert_equal(1, r['state'], "无曝光邀约功能的自动邀约关闭成功")


@pytest.mark.skipif(display == 1, reason="普通/特权邀约功能按钮不显示，跳过此用例")
def test_autoInviteSwitch_open_3():
    if status == 1:
        r = autoInviteSwitch_open(1, 2)
        assert_not_equal(1, r['state'], "普通/特权邀约功能的自动邀约无法开启, 因为不显示该按钮")
    elif status == 2:
        r = autoInviteSwitch_open(1, 1)
        assert_not_equal(1, r['state'], "普通/特权邀约功能的自动邀约无法关闭, 因为不显示该按钮")


@pytest.mark.skipif(noExposureSwitchDisplay == 1, reason="无曝光邀约功能按钮不显示，跳过此用例")
def test_autoInviteSwitch_open_4():
    if noExposureSwitchStatus == 1:
        r = autoInviteSwitch_open(2, 2)
        assert_not_equal(1, r['state'], "无曝光邀约功能的自动邀约无法开启, 因为不显示该按钮")
    elif status == 2:
        r = autoInviteSwitch_open(2, 1)
        assert_not_equal(1, r['state'], "无曝光邀约功能的自动邀约无法关闭, 因为不显示该按钮")
