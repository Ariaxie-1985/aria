# coding:utf-8
# @Time  : 2020/2/21 11:22
# @Author: Xiawang
# Description:
from api_script.entry.positionindex.suggestion import position_index_suggestion
from api_script.entry.positionrec.positionrec import get_position_delivered, get_position_rec, get_position_user_rec, \
    get_position_view
from api_script.entry.positionsearch.searchPosition import hotEmployee_activeHr, hotEmployee_nearby, \
    hotEmployee_selected, hotEmployee_topCompany
from utils.util import assert_equal


def test_get_position_delivered(login_app, query_position):
    r = get_position_delivered(userToken=login_app, positionId=query_position)
    assert_equal(True, bool(r['content']['positionList']), '投了又投用例通过')


def test_get_position_rec(login_app, query_position):
    r = get_position_rec(userToken=login_app, positionId=query_position)
    assert_equal(True, bool(r['content']['positionList']), '相似职位用例通过')


def test_get_position_user_rec(login_app, query_position):
    r = get_position_user_rec(userToken=login_app, positionId=query_position)
    assert_equal(True, bool(r['content']['positionList']), '猜你喜欢用例通过')


def test_get_position_view(login_app, query_position):
    r = get_position_view(userToken=login_app, positionId=query_position)
    assert_equal(True, bool(r['content']['positionList']), '看了又看用例通过')


def test_position_index_suggestion(login_app):
    r = position_index_suggestion(userToken=login_app)
    assert_equal(True, bool(r['content']['suggestionList']), '个性化搜索用例通过')


def test_hotEmployee_activeHr(login_app):
    r = hotEmployee_activeHr(userToken=login_app)
    assert_equal(True, bool(r['content']['positions']), '专属热招-聊出好机会用例通过')


def test_hotEmployee_nearby(login_app):
    r = hotEmployee_nearby(userToken=login_app)
    assert_equal(True, bool(r['content']['positions']), '专属热招-附近热招用例通过')


def test_hotEmployee_selected(login_app):
    r = hotEmployee_selected(userToken=login_app)
    assert_equal(True, bool(r['content']['positions']), '专属热招-小勾精选用例通过')


def test_hotEmployee_topCompany(login_app):
    r = hotEmployee_topCompany(userToken=login_app)
    assert_equal(True, bool(r['content']['positions']), '专属热招-大厂专区用例通过')
