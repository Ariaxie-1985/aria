# coding:utf-8
# @Time  : 2020/2/25 15:15
# @Author: Xiawang
# Description:
import pytest

from api_script.entry.account.passport import password_login
from api_script.entry.campus import get_hot_company, get_user_info, get_campus_count
from utils.util import assert_equal

userToken, userId = '', ''


def test_login_app(ip_port):
    result = password_login("19910626899", "000000", ip_port=ip_port)
    global userToken, userId
    userToken, userId = result['content']['userToken'], result['content']['userInfo']['userId']
    assert_equal(1, result.get('state'), '登录用例通过')


@pytest.mark.parametrize("city", [("北京")])
def test_get_hot_company(city, ip_port):
    r = get_hot_company(userToken=userToken, userId=userId, ip_port=ip_port, city=city)
    global companyId
    companyId = r['content'][0]['id']
    assert_equal(True, bool(r['content']), "获取校招的热门公司用例通过")


def test_get_user_info(ip_port):
    r = get_user_info(userToken=userToken, userId=userId, ip_port=ip_port)
    assert_equal(1, r['state'], "校招--获取用户信息用例通过")


def test_get_campus_count(ip_port):
    r = get_campus_count(userToken=userToken, userId=userId, ip_port=ip_port, companyId=companyId)
    assert_equal(1, r['state'], "获取校友数量用例通过")
