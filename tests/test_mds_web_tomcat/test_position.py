# coding:utf-8
# @Time  : 2020/3/18 15:16
# @Author: Xiawang
# Description:
import time

import pytest

from api_script.jianzhao_web.b_position.B_postposition import get_all_position_category, multiChannel_filter, \
    count_by_status, myOnlinePositions, my_offline_positions, redirect_original_page, batch_refresh_info
from api_script.jianzhao_web.index import get_all_members
from api_script.jianzhao_web.talent.B_looking_for_talent import rec_talent, new_talent, talent_get_experiences, \
    talent_get_action_labels, talent_hunting, talent_inspect
from utils.util import assert_equal, assert_in


def test_get_all_position_category(b_login_web):
    r = get_all_position_category()
    assert_in('开发|测试|运维类', [category['firstType'] for category in r['content']['rows']], "获取职位的全部分类用例通过")


def test_multiChannel_filter():
    r = multiChannel_filter()
    assert_in('特权职位', [position_type['name'] for position_type in r['content']['data']['positionTypes']],
              "职位类型(特权职位)用例通过")


def test_count_by_status():
    r = count_by_status()
    assert_equal(True, bool(r['content']['data']['myOfflinePositionsCount']), "统计当前自己和公司的职位数量用例通过")


@pytest.mark.parametrize("pageNo", [(1)])
def test_myOnlinePositions(pageNo):
    r = myOnlinePositions(pageNo=pageNo)
    global positionId, outerPositionId
    positionId = r['content']['data']['parentPositionVOs'][0]['positions'][0]['positionId']
    outerPositionId = r['content']['data']['parentPositionVOs'][0]['positions'][0]['outerPositionId']
    assert_equal(1, r['state'], "获取在线职位用例通过")


def test_batch_refresh_info():
    r = batch_refresh_info()
    assert_equal(1, r['state'], "批量刷新职位用例通过")


def test_redirect_original_page():
    r = redirect_original_page(positionId=positionId)
    assert_equal(200, r.status_code, '获取职位详情用例通过')


@pytest.mark.parametrize('pageNo', [(1), (2)])
def test_my_offline_positions(pageNo):
    r = my_offline_positions(pageNo=pageNo)
    assert_equal(1, r['state'], '获取已下线的职位用例通过')


def test_get_all_members():
    r = get_all_members()
    assert_equal(True, bool(r['content']['data']['members']['result']), '获取公司内的所有成员用例通过')

second = 5
time.sleep(second)
def test_rec_talent():
    r = rec_talent(positionId=outerPositionId)
    assert_equal(True, bool(r['content']['data']['page']['result']), "推荐人才用例通过")

time.sleep(second)
def test_new_talent():
    r = new_talent(positionId=outerPositionId)
    global encryptUserId_list, show_id
    show_id = r['content']['data']['show_id']
    encryptUserId_list = []
    for result in r['content']['data']['page']['result']:
        encryptUserId_list.append(result['encryptUserId'])
    assert_equal(True, bool(r['content']['data']['page']['result']), "最新人才用例通过")

time.sleep(second)
def test_talent_get_experiences():
    r = talent_get_experiences(positionId=outerPositionId, show_id=show_id, cUserIds=','.join(encryptUserId_list))
    assert_equal(True, bool(r['content']['rows']), "获取推荐人才的教育经历用例通过")

time.sleep(second)
def test_talent_get_action_labels():
    r = talent_get_action_labels(positionId=outerPositionId, show_id=show_id, cUserIds=','.join(encryptUserId_list))
    assert_equal(True, bool(r['content']['rows']), "获取推荐人才的简历动态用例通过")

time.sleep(second)
def test_talent_hunting():
    r = talent_hunting(positionId=outerPositionId)
    assert_equal(1, r['state'], '猎头人才用例通过')

time.sleep(second)
def test_talent_inspect():
    r = talent_inspect(positionId=outerPositionId)
    assert_equal(1, r['state'], '谁看过我用例通过')
