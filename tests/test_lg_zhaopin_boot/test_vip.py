# coding:utf-8
# @Time  : 2020/2/26 18:44
# @Author: Xiawang
# Description:
from api_script.zhaopin_app.vip import get_vip_detail, post_vip_detail
from utils.util import assert_equal


def test_get_vip_detail(b_login_app):
    r = get_vip_detail(userToken=b_login_app[0])
    assert_equal(True, bool(r['content']['vipLevelList']), "获取拉勾VIP模板详情用例通过")


def test_post_vip_detail(b_login_app):
    r = post_vip_detail(userToken=b_login_app[0])
    assert_equal(True, bool(r['content']['vipLevelList']), "获取拉勾VIP模板详情用例通过")
