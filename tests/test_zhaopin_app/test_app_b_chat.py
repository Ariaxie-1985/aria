# coding:utf-8
# @Time  : 2019-01-17 16:22
# @Author: Xiawang
import pytest
from api_script.zhaopin_app.b_chat import chat_invite_msg, chat_inspect_reports_all, chat_inspect_list, \
    chat_inspect_reports
from api_script.zhaopin_app.b_crm import crm_positions_tag_report
from api_script.zhaopin_app.b_goods import goods_product_version, getPopUpData, getRightsList, getUserInfo
from api_script.zhaopin_app.b_searchResumePosition import get_strict_pages_positions, get_strict_pages_orderResumes
from utils.util import assert_equal


def setup_module(module):
    pass


def teardown_module(module):
    pass


@pytest.mark.parametrize("type", [('POSITION_ENERGY_CARD_MESSAGE')])
def test_positions_tag_report(type):
    res = crm_positions_tag_report(type)
    assert_equal(1, res['state'], "CRM上报销售线索成功", "CRM上报销售线索失败, 失败信息: " + res['message'])


def test_goods_product_version():
    res = goods_product_version()
    assert_equal(1, res['state'], "获取当前用户商业产品版本号成功", "获取当前用户商业产品版本号失败, 失败信息: " + res['message'])


def test_get_strict_pages_positions():
    res = get_strict_pages_positions()
    assert_equal(1, res['state'], "分页查询用于简历查询的职位（排除没有拉勾职位id的职位）成功",
                 "分页查询用于简历查询的职位（排除没有拉勾职位id的职位）失败, 失败信息: " + res['message'])


def test_get_strict_pages_orderResumes():
    res = get_strict_pages_orderResumes()
    global ids
    ids = []
    if len(res['content']['result']):
        for id in res['content']['result']:
            ids.append(id['outerPositionId'])
    assert_equal(1, res['state'], "分页查询用于简历查询的职位成功", "分页查询用于简历查询的职位失败, 失败信息: " + res['message'])


def test_chat_inspect_list():
    res = chat_inspect_list()
    global c_userId
    if len(res['content']):
        c_userId = res['content'][0]['userId']
    assert_equal(1, res['state'], "谁看过我列表获取成功", "谁看过我列表获取失败, 失败信息: " + res['message'])


def test_chat_invite_msg():
    res = chat_invite_msg(ids[0], c_userId)
    assert_equal(1, res['state'], "邀请投递成功", "邀请投递失败, 失败信息: " + res['message'])


def test_chat_inspect_reports():
    res = chat_inspect_reports(ids)
    assert_equal(1, res['state'], "谁看过我,标记已读成功", "谁看过我,标记已读失败, 失败信息: " + res['message'])


@pytest.mark.parametrize("createBy", [0, 1, 2])
def test_chat_inspect_reports_all(createBy):
    res = chat_inspect_reports_all(createBy)
    assert_equal(1, res['state'], "谁看过我,标记已读成功", "谁看过我,标记已读失败, 失败信息: " + res['message'])


# yq新增:2019.2.26
def test_getPopUpData():
    res = getPopUpData()
    assert_equal(1, res['state'], "操作成功", "操作失败, 失败信息: " + res['message'])


def test_getRightsList():
    res = getRightsList()
    assert_equal(1, res['state'], "操作成功", "操作失败, 失败信息: " + res['message'])


def test_getUserInfo():
    res = getUserInfo()
    assert_equal(1, res['state'], "操作成功", "操作失败, 失败信息: " + res['message'])
