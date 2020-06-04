# coding:utf-8
# @Time  : 2019-03-07 20:10
# @Author: Xiawang
import pytest

from api_script.luckyshare_app.luckyShare import activity_carp_entrance, activity_carp_summary, queryRedPointType, \
    activity_carp_removeRedDot, activity_carp_queryNotes, order_interview_queryList, positions_queryList, \
    buser_hr_getList, positionCategories_get, queryPositions, queryHistoryNotes, queryInterviews, \
    activity_carp_queryNotePreview, activity_carp_publicNote, cms_luckyShare_querylist, cms_luckyShare_audit
from utils.util import assert_equal


def setup_module(module):
    pass


def teardown_module(module):
    pass


@pytest.mark.parametrize('orderId', [(None), (0)])
def test_activity_carp_entrance(orderId):
    r = activity_carp_entrance(orderId)
    assert_equal(1, r['state'], "查询活动入口是否展示成功")


def test_activity_carp_summary():
    r = activity_carp_summary()
    assert_equal(1, r['state'], "查询活动入口是否展示成功")


@pytest.mark.parametrize('orderIds', [(1104578225485787136), (None)])
def test_queryRedPointType(orderIds):
    r = queryRedPointType(orderIds)
    if orderIds == None:
        assert_equal(1002, r['state'], "订单编号 orderIds 的判断是否为空 正确")
    else:
        assert_equal(1, r['state'], "查询红点成功")


@pytest.mark.parametrize('type', [(1), (2), (3)])
def test_activity_carp_removeRedDot(type):
    r = activity_carp_removeRedDot(type)
    if 1 <= type <= 3:
        assert_equal(1, r['state'], "消除红点成功")
    else:
        assert_equal(1002, r['state'], "对异常红点类型的处理正确")


@pytest.mark.parametrize('category1, category2, category3', [('开发|测试|运维类', '后端开发', 'Java')])
def test_activity_carp_queryNotes(category1, category2, category3):
    r = activity_carp_queryNotes(category1, category2, category3)
    assert_equal(1, r['state'], "查询帖子列表成功")


def test_queryInterviews():
    r = queryInterviews()
    assert_equal(1, r['state'], "查询历史晒贴")

@pytest.mark.skip(reason="接口文档没发现此接口")
@pytest.mark.parametrize('ids', [(None)])
def test_order_interview_queryList(ids):
    r = order_interview_queryList(ids)
    if ids == None:
        assert_equal(1002, r['state'], "对订单编号为空的处理正确")
    else:
        assert_equal(1, r['state'], "单独及批量查询面试订单成功")


def test_positions_queryList():
    r = positions_queryList()
    assert_equal(1002, r['state'], "对职位id为空的处理正确")


def test_queryPositions():
    r = queryPositions()
    assert_equal(1, r['state'], "对曝光职位为空判断成功")


def test_queryHistoryNotes():
    r = queryHistoryNotes()
    assert_equal(1, r['state'], "查询历史晒贴")

@pytest.mark.skip(reason="需要构造测试数据")
@pytest.mark.parametrize('orderId', [(1104578225485787136)])
def test_activity_carp_queryNotePreview(orderId):
    r = activity_carp_queryNotePreview(orderId)
    assert_equal(1, r['state'], "查询发帖前的预览信息")

@pytest.mark.skip(reason="暂无面试记录，数据需构造")
@pytest.mark.parametrize('content, userName', [('测试发帖了', '小宸')])
def test_activity_carp_publicNote(content, userName):
    r = activity_carp_publicNote(content, userName)
    assert_equal(1002, r['state'], "面试订单不存在")


@pytest.mark.skip(reason="暂时不执行")
def test_cms_luckyShare_querylist(login_home_k8s_default):
    r = cms_luckyShare_querylist()
    assert_equal(True, r['success'], "home后台锦鲤贴列表查询成功")


@pytest.mark.skip(reason="暂时不执行")
def test_cms_luckyShare_audit(login_home_k8s_default):
    r = cms_luckyShare_audit()
    assert_equal(True, r['success'], "home后台锦鲤贴列表查询成功")
