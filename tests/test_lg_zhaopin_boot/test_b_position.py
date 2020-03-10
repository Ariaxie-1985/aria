# coding:utf-8
# @Time  : 2020/3/3 16:02
# @Author: Xiawang
# Description:
import pytest

from api_script.zhaopin_app.b_position import positions_category, category_mapping, get_online_positions, \
    publish_position, positions_offline, positions_invite, positions_is_hot, get_other_positions, get_offline_positions, \
    positions_details, positions_red_point_hint
from utils.util import assert_equal


def test_positions_category(b_login_app):
    r = positions_category(userToken=b_login_app[0])
    try:
        actual_result = r['content']['positionTypeTreeVO']['itPositionFirstCategorys'][0]['name']
    except (IndexError, KeyError):
        actual_result = ""
    assert_equal('开发|测试|运维类', actual_result, '获取职业静态信息用例通过')


@pytest.mark.parametrize("positionName,expect", [("java", '后端开发'), ('测试', '测试')])
def test_category_mapping(b_login_app, positionName, expect):
    r = category_mapping(userToken=b_login_app[0], positionName=positionName)
    assert_equal(expect, r['content']['secCategory'], '职位名称映射职位分类用例通过')


def test_is_enough_positions(b_login_app):
    global flag, positions_result
    positions_result = get_online_positions(userToken=b_login_app[0], H9=True)
    flag = positions_result['content']['onlinePositionNum']
    assert_equal(1, positions_result['state'], '确认在线职位数是否足够发布职位用例通过')


@pytest.mark.skipif('flag <= 20', reason="发布职位权益足够，无需下线职位")
def test_offline_position(b_login_app):
    positionIds = []
    for position_info in positions_result['content']['positions']['result']:
        positionId = position_info['positionId']
        positionIds.append(positionId)
    for id in positionIds:
        positions_offline(id, userToken=b_login_app[0], H9=True)


def test_publish_position(b_login_app):
    r = publish_position(userToken=b_login_app[0])
    assert_equal(1, r['state'], "校验发布职位成功")
    global positionId, mdsPositionId
    try:
        positionId = r['content']['lagouPositionId']
        mdsPositionId = r['content']['mdsPositionId']
    except:
        positionId = 0


def test_positions_details(b_login_app):
    r = positions_details(userToken=b_login_app[0], positionId=mdsPositionId)
    assert_equal(1, r['state'], '查看职位详情用例通过')


def test_positions_invite(b_login_app):
    r = positions_invite(userToken=b_login_app[0], positionId=mdsPositionId, userId=15166231)
    assert_equal(1, r['state'], '批量邀约候选人用例通过')


@pytest.mark.parametrize("positionName", [("Python工程师"), ("测试工程师")])
def test_positions_is_hot(b_login_app, positionName):
    r = positions_is_hot(userToken=b_login_app[0], positionName=positionName)
    assert_equal(True, r['content']['isHot'], '是否热门职位用例通过')


def test_get_other_positions(b_login_app):
    r = get_other_positions(userToken=b_login_app[0])
    assert_equal(1, r['state'], '获取其他职位列表用例通过')


def test_get_offline_positions(b_login_app):
    r = get_offline_positions(userToken=b_login_app[0])
    assert_equal(1, r['state'], '获取已下线列表用例通过')


def test_positions_red_point_hint(b_login_app):
    r = positions_red_point_hint(userToken=b_login_app[0])
    assert_equal(1, r['state'], '首页导航职位红点用例通过')
