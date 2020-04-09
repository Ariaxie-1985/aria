# coding:utf-8
# @Time  : 2020/2/21 16:25
# @Author: Xiawang
# Description:
from api_script.entry.account.passport import password_login
from api_script.entry.position.collect import collect_add, collect_list, collect_clear, collect_delete
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


def test_collect_add(ip_port):
    r = collect_add(userToken=userToken, userId=userId, ip_port=ip_port, positionId=query_position_id)
    assert_equal(1, r['state'], '收藏职位用例通过')


def test_collect_list(ip_port):
    r = collect_list(userToken=userToken, userId=userId, ip_port=ip_port)
    assert_equal(True, bool(r['content']['collectPositions']), '验证收藏职位用例通过')


def test_collect_clear(ip_port):
    r = collect_clear(userToken=userToken, userId=userId, ip_port=ip_port)
    assert_equal(1, r['state'], '清除收藏职位的红点用例通过')


def test_collect_delete(ip_port):
    r = collect_delete(userToken=userToken, userId=userId, ip_port=ip_port, positionId=query_position_id)
    assert_equal(1, r['state'], '取消已收藏职位用例通过')


def test_collect_list1(ip_port):
    r = collect_list(userToken=userToken, userId=userId, ip_port=ip_port)
    assert_equal(False, bool(r['content']['collectPositions']), '验证取消已收藏职位用例通过')
