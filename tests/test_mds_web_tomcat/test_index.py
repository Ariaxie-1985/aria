# coding:utf-8
# @Time  : 2020/3/18 13:54
# @Author: Xiawang
# Description:
from api_script.jianzhao_web.index import search_plusSearchSelector, get_easy_plus_privilegeCount, \
    get_business_user_info, get_user_goods_info, get_yun_additional_info, is_hunting_gray, personal_assistant, \
    jump_easy_index_html, get_product_version
from utils.util import assert_equal


def test_jump_easy_index_html(b_login_web):
    r = jump_easy_index_html()


def test_search_plusSearchSelector():
    r = search_plusSearchSelector()
    assert_equal(1, r.get('state', 0), "人才查找用例通过")


def test_get_easy_plus_privilegeCount():
    r = get_easy_plus_privilegeCount()
    assert_equal(1, r.get('state', 0), "获取当前用户的拉勾加权限信息用例通过")


def test_get_business_user_info():
    r = get_business_user_info()
    assert_equal(1, r.get('state', 0), "获取用户的商业信息用例通过")


def test_get_user_goods_info():
    r = get_user_goods_info()
    assert_equal(1, r.get('state', 0), "获取用户的权益信息用例通过")


def test_get_yun_additional_info():
    r = get_yun_additional_info()
    assert_equal(1, r.get('state', 0), "获取用户的简历的待办事项用例通过")


def test_is_hunting_gray():
    r = is_hunting_gray()
    assert_equal(1, r.get('state', 0), "获取用户的权益信息用例通过")


def test_personal_assistant():
    r = personal_assistant()
    assert_equal(1, r.get('state', 0), "获取当前公司的招聘顾问用例通过")


def test_get_product_version():
    r = get_product_version()
    assert_equal(True, bool(r['content']['data']['version']), "获取当前公司的拉勾加版本号用例通过")
