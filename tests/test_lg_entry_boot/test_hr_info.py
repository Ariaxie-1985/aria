# coding:utf-8
# @Time  : 2020/2/17 16:38
# @Author: Xiawang
# Description:
from api_script.entry.account.passport import password_login
from api_script.entry.buser.hr_info import get_hr_info, get_hr_card, get_info, get_baseStatus
from utils.util import assert_equal

userToken, userId = '', ''


def test_login_app(ip_port):
    result = password_login("19910626899", "000000", ip_port=ip_port)
    global userToken, userId
    userToken, userId = result['content']['userToken'], result['content']['userInfo']['userId']
    assert_equal(1, result.get('state'), '登录用例通过')


def test_get_hr_info(ip_port):
    r = get_hr_info(userToken=userToken, ip_port=ip_port, publisherId=15130154)
    assert_equal(418937, r['content']['companyId'], '获取HR信息用例通过')


def test_get_hr_card(ip_port):
    r = get_hr_card(userToken=userToken, ip_port=ip_port, publisherId=15130154)
    assert_equal(15130154, r['content'][0]['hrId'], '获取HR卡片信息用例通过')


def test_get_info(ip_port):
    r = get_info(userToken=userToken, ip_port=ip_port, publisherId=15130154)
    assert_equal("拉勾测试简称XM", r['content']['company'], '获取HR信息用例通过')


def test_get_baseStatus(ip_port):
    r = get_baseStatus(userToken=userToken, ip_port=ip_port, publisherId=15130154)
    assert_equal(418937, r['content']['companyId'], '获取HR的基本状态用例通过')
