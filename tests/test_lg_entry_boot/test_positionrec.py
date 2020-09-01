# coding:utf-8
# @Time  : 2020/2/21 11:22
# @Author: Xiawang
# Description:
from api_script.entry.account.passport import password_login
from api_script.entry.positionindex import position_index_suggestion
from api_script.entry.positionrec.positionrec import get_position_delivered, get_position_rec, get_position_user_rec, \
    get_position_view
from api_script.entry.positionsearch.searchPosition import hotEmployee_activeHr, hotEmployee_nearby, \
    hotEmployee_selected, hotEmployee_topCompany, search_positions
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


def test_get_position_delivered(ip_port):
    r = get_position_delivered(userToken=userToken, userId=userId, ip_port=ip_port, positionId=query_position_id)
    assert_equal(1, r.get('state'), '投了又投用例通过')


def test_get_position_rec(ip_port):
    r = get_position_rec(userToken=userToken, userId=userId, ip_port=ip_port, positionId=query_position_id)
    assert_equal(1, r.get('state'), '相似职位用例通过')


def test_get_position_user_rec(ip_port):
    r = get_position_user_rec(userToken=userToken, userId=userId, ip_port=ip_port, positionId=query_position_id)
    assert_equal(1, r.get('state'), '猜你喜欢用例通过')


def test_get_position_view(ip_port):
    r = get_position_view(userToken=userToken, userId=userId, ip_port=ip_port, positionId=query_position_id)
    assert_equal(1, r.get('state'), '看了又看用例通过')


# def test_position_index_suggestion(ip_port):
#     r = position_index_suggestion(userToken=userToken, userId=userId, ip_port=ip_port)
#     assert_equal(True, bool(r['content']['suggestionList']), '个性化搜索用例通过')


def test_hotEmployee_activeHr(ip_port):
    r = hotEmployee_activeHr(userToken=userToken, userId=userId, ip_port=ip_port)
    assert_equal(True, bool(r['content']['positions']), '专属热招-聊出好机会用例通过')


def test_hotEmployee_nearby(ip_port):
    r = hotEmployee_nearby(userToken=userToken, userId=userId, ip_port=ip_port)
    assert_equal(True, bool(r['content']['positions']), '专属热招-附近热招用例通过')


def test_hotEmployee_selected(ip_port):
    r = hotEmployee_selected(userToken=userToken, userId=userId, ip_port=ip_port)
    assert_equal(True, bool(r['content']['positions']), '专属热招-小勾精选用例通过')


def test_hotEmployee_topCompany(ip_port):
    r = hotEmployee_topCompany(userToken=userToken, userId=userId, ip_port=ip_port)
    assert_equal(True, bool(r['content']['positions']), '专属热招-大厂专区用例通过')
