# coding:utf-8
# @Time  : 2020/2/14 12:16
# @Author: Xiawang
# Description:
from api_script.neirong_app.home import deliver_rec, fast_feedback, headline
from utils.util import assert_equal


def test_deliver_rec(login_app):
    r = deliver_rec(userToken=login_app)
    assert_equal(True, bool(r['content']), '大家都在投用例通过')


def test_fast_feedback(login_app):
    r = fast_feedback(userToken=login_app)
    assert_equal(True, bool(r['content']), '极速反馈用例通过')


def test_headline(login_app):
    r = headline(userToken=login_app)
    assert_equal(True, bool(r['content']), '获取拉勾头条用例通过')


def test_searchBySalary(login_app):
    r = headline(userToken=login_app)
    assert_equal(True, bool(r['content']), '薪资最高用例通过')
