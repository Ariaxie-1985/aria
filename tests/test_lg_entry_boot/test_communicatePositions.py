# coding:utf-8
# @Time  : 2020/2/20 18:52
# @Author: Xiawang
# Description:
import pytest

from api_script.entry.account.passport import password_login
from api_script.entry.position.communicatePositions import get_position_detail, get_position_publisher, \
    get_communicate_positions
from api_script.entry.positionsearch.searchPosition import search_positions
from utils.util import assert_equal

userToken, userId = '', ''

query_position_id = 0

def test_login_app(ip_port):
    result = password_login("19910626899", "000000", ip_port=ip_port)
    global userToken, userId
    userToken, userId = result['content']['userToken'], result['content']['userInfo']['userId']
    assert_equal(1, result.get('state'), '登录用例通过')


def test_query_position(ip_port):
    r = search_positions(userToken=userToken, userId=userId, ip_port=ip_port, keyword='JAVA')
    global query_position_id
    query_position_id = r['content']['positionCardVos'][0]['positionId']
    assert_equal(1, r.get('state'), '查询职位id用例通过')


def test_get_position_detail(ip_port):
    r = get_position_detail(userToken=userToken, userId=userId, ip_port=ip_port, positionId=query_position_id)
    assert_equal(query_position_id, r['content']['positionId'], '根据职位id查询职位详情用例通过')


@pytest.mark.parametrize("hr_Id", [(15130154)])
def test_get_position_publisher(hr_Id):
    r = get_position_publisher(userToken=userToken, userId=userId, hr_Id=hr_Id)
    assert_equal(True, bool(r['content']['positions']), 'HR发布职位列表用例通过')


@pytest.mark.parametrize("hr_Id", [(15130154)])
def test_get_communicate_positions(hr_Id):
    r = get_communicate_positions(userToken=userToken, userId=userId, hr_Id=hr_Id)
    assert_equal(True, bool(r['content']['positions']), '查询沟通职位列表用例通过')
