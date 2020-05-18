# coding:utf-8
# @Time  : 2020/2/17 16:39
# @Author: Xiawang
# Description:
from api_script.entry.account.passport import password_login
from api_script.entry.config.appSetting import get_info, get_app_theme, get_im_entrance
from utils.util import assert_equal

userToken, userId = '', ''


def test_login_app(ip_port):
    result = password_login("19910626899", "000000", ip_port=ip_port)
    global userToken, userId
    userToken, userId = result['content']['userToken'], result['content']['userInfo']['userId']
    assert_equal(1, result.get('state'), '登录用例通过')


def test_get_info(ip_port):
    r = get_info(userToken=userToken, userId=userId, ip_port=ip_port)
    assert_equal(True, bool(r['content']), '查询app端配置用例成功')


def test_get_app_theme(ip_port):
    r = get_app_theme(userToken=userToken, userId=userId, ip_port=ip_port)
    assert_equal(1, r['state'], '查询app端主题用例成功')


def test_get_im_entrance(ip_port):
    r = get_im_entrance(userToken=userToken, userId=userId, ip_port=ip_port)
    assert_equal(1, r['state'], '查询APP消息页活动入口用例成功')
