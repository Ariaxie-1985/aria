# coding:utf-8
# @Time  : 2020/2/17 16:39
# @Author: Xiawang
# Description:
from api_script.entry.config.appSetting import get_info, get_app_theme, get_im_entrance
from utils.util import assert_equal


def test_get_info(login_app):
    r = get_info(userToken=login_app)
    assert_equal(True, bool(r['content']), '查询app端配置用例成功')


def test_get_app_theme(login_app):
    r = get_app_theme(userToken=login_app)
    assert_equal(1, r['state'], '查询app端主题用例成功')


def test_get_im_entrance(login_app):
    r = get_im_entrance(userToken=login_app)
    assert_equal(1, r['state'], '查询APP消息页活动入口用例成功')
