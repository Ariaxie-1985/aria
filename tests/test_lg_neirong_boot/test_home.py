# coding:utf-8
# @Time  : 2020/2/14 12:16
# @Author: Xiawang
# Description:
from api_script.neirong_app.home import deliver_rec, fast_feedback, searchBySalary, home_headline, home_page
from utils.util import assert_equal


def test_deliver_rec(login_app, ip_port):
    r = deliver_rec(userToken=login_app, ip_port=ip_port)
    assert_equal(True, bool(r['content']), '大家都在投用例通过')


def test_fast_feedback(login_app, ip_port):
    r = fast_feedback(userToken=login_app, ip_port=ip_port)
    assert_equal(True, bool(r['content']), '极速反馈用例通过')


def test_home_headline(login_app, ip_port):
    r = home_headline(userToken=login_app, ip_port=ip_port)
    assert_equal(True, bool(r['content']), '获取拉勾头条用例通过')

def test_home_page(login_app, ip_port):
    r = home_page(userToken=login_app, ip_port=ip_port)
    assert_equal(True, bool(r['content']), '获取app首页用例通过')

def test_searchBySalary(login_app):
    r = searchBySalary(userToken=login_app)
    assert_equal(True, bool(r['content']), '薪资最高用例通过')
