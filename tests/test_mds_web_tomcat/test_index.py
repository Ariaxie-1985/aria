# coding:utf-8
# @Time  : 2020/3/18 13:54
# @Author: Xiawang
# Description:
from api_script.business.userGoodsRecord import count_pending_apply_records
from api_script.jianzhao_web.index import search_plusSearchSelector, get_easy_plus_privilegeCount, \
    get_business_user_info, get_user_goods_info, get_yun_additional_info, is_hunting_gray, personal_assistant, \
    jump_easy_index_html, get_product_version, head_notifications, account_my_role, get_shield_expire, account_portrait, \
    notice_show, check_upgrade_to_share, get_my_member_info, search_colleague, sub_account_button, \
    is_show_position_notice
from api_script.jianzhao_web.open_channel.open_channel import settings_channel_support
from utils.util import assert_equal


def test_jump_easy_index_html():
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


def test_head_notifications():
    r = head_notifications()
    assert_equal(1, r.get('state', 0), "获取通知用例通过")


def test_account_my_role():
    r = account_my_role()
    assert_equal(1, r.get('state', 0), "获取当前用户的角色权限用例通过")


def test_get_shield_expire():
    r = get_shield_expire()
    assert_equal(1, r.get('state', 0), "获取当前消息是否过期用例通过")


def test_account_portrait():
    r = account_portrait()
    assert_equal(1, r.get('state', 0), "获取当前用户的头像用例通过")


def test_notice_show():
    r = notice_show()
    assert_equal(1, r.get('state', 0), "是否显示通知用例通过")


def test_count_pending_apply_records():
    r = count_pending_apply_records()
    assert_equal(1, r.get('state', 0), "管理员查询待处理权益申请数量用例通过")


def test_check_upgrade_to_share():
    r = check_upgrade_to_share()
    assert_equal(1, r.get('state', 0), "检查产品升级更新用例通过")


def test_get_my_member_info():
    r = get_my_member_info()
    assert_equal(1, r.get('state'), "获取当前用户信息用例通过")


def test_search_colleague():
    r = search_colleague()
    assert_equal(1, r.get('state'), "寻找同事用例通过")


def test_sub_account_button():
    r = sub_account_button()
    assert_equal(1, r.get('state'), "是否显示子账号按钮用例通过")


def test_is_show_position_notice():
    r = is_show_position_notice()
    assert_equal(1, r.get('state'), "是否显示职位通知用例通过")


def test_settings_channel_support():
    r = settings_channel_support()
    assert_equal(1, r.get('state'), "查询当前平台支持的渠道用例通过")
