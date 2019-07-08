# coding:utf-8
# @Time  : 2019-07-08 10:34
# @Author: Xiawang
import random

from api_script.entry.deliver.deliver import deliver_check, deliver_create, deliver_get
from api_script.zhaopin_app.b_position import get_online_positions
from utils.util import assert_equal
import pytest
@pytest.importorskip('test_deliver.py', reason="等TCP转HTTP投递相关接口上线后再执行")

orderId = 0


def test_deliver_check():
    oneline_position = get_online_positions()
    positionId1 = oneline_position['content']['positions']['result'][0]['outerPositionId']
    positionId2 = oneline_position['content']['positions']['result'][30]['outerPositionId']
    positionIds = [positionId1, positionId2]

    for positionId in positionIds:
        res = deliver_check(positionId)
        if positionId == positionId2:
            assert_equal(209004, res['state'], '校验工作年限、学历与职位要求不符逻辑成功')
        elif positionId == positionId1:
            assert_equal(205009, res['state'], '校验职位已下线逻辑成功')


def test_deliver_create():
    oneline_position = get_online_positions()
    positionId1 = oneline_position['content']['positions']['result'][random.randint(0, 5)]['outerPositionId']
    positionId2 = oneline_position['content']['positions']['result'][random.randint(30, 50)]['outerPositionId']
    positionIds = [positionId1, positionId2]
    for positionId in positionIds:
        res = deliver_create(positionId, resumeId=536556, resumeType=1)
        global orderId
        orderId = res['content']['orderId']
        if positionId == positionId1:
            assert_equal(1, res['state'], '校验投递合格简历逻辑成功')
        elif positionId == positionId2:
            assert_equal(205009, res['state'], '校验职位已下线逻辑成功')


def test_deliver_get():
    res = deliver_get(orderId)
    assert_equal(orderId, res['content']['orderId'], '获取投递详情成功')
