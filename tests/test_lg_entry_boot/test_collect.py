# coding:utf-8
# @Time  : 2020/2/21 16:25
# @Author: Xiawang
# Description:
from api_script.entry.position.collect import collect_add, collect_list, collect_clear, collect_delete
from utils.util import assert_equal


def test_collect_add(login_app, query_position):
    r = collect_add(userToken=login_app, positionId=query_position)
    assert_equal(1, r['state'], '收藏职位用例通过')


def test_collect_list(login_app):
    r = collect_list(userToken=login_app)
    assert_equal(True, bool(r['content']['collectPositions']), '验证收藏职位用例通过')


def test_collect_clear(login_app):
    r = collect_clear(userToken=login_app)
    assert_equal(1, r['state'], '清除收藏职位的红点用例通过')


def test_collect_delete(login_app, query_position):
    r = collect_delete(userToken=login_app, positionId=query_position)
    assert_equal(1, r['state'], '取消已收藏职位用例通过')


def test_collect_list1(login_app):
    r = collect_list(userToken=login_app)
    assert_equal(False, bool(r['content']['collectPositions']), '验证取消已收藏职位用例通过')
