# coding:utf-8
# @Time  : 2020/2/25 15:15
# @Author: Xiawang
# Description:
import pytest

from api_script.entry.campus import get_hot_company, get_user_info, get_campus_count
from utils.util import assert_equal


@pytest.mark.parametrize("city", [("北京")])
def test_get_hot_company(login_app, city, ip_port):
    r = get_hot_company(userToken=login_app[0], userId=login_app[1], ip_port=ip_port, city=city)
    global companyId
    companyId = r['content'][0]['id']
    assert_equal(True, bool(r['content']), "获取校招的热门公司用例通过")


def test_get_user_info(login_app, ip_port):
    r = get_user_info(userToken=login_app[0], userId=login_app[1], ip_port=ip_port)
    assert_equal(1, r['state'], "校招--获取用户信息用例通过")


def test_get_campus_count(login_app, ip_port):
    r = get_campus_count(userToken=login_app[0], userId=login_app[1], ip_port=ip_port, companyId=companyId)
    assert_equal(1, r['state'], "获取校友数量用例通过")
