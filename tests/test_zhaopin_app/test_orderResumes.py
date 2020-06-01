# coding:utf-8
# @Time  : 2019-04-28 15:28
# @Author: Xiawang
import json

import pytest

from api_script.zhaopin_app.bUser import member_all
from api_script.zhaopin_app.orderResumes import orderResumes_query, orderResumes_filter, orderResumes_positions_pages, \
    orderResumes_sameResume_query, orderResumes_process_save, orderResumes_process_query, orderResumes_process_forward
from utils.util import assert_equal


@pytest.importorskip('test_orderResumes.py', reason="需要等上线后才可在default环境用, 预计15号上线")
@pytest.mark.parametrize('resumeStageCode', [(1), (2), (4), (24), (32), (64)])
def test_orderResumes_query(resumeStageCode):
    resumeStageCode_list = {1: '新简历', 2: '待沟通', 4: '面试', 24: '录用', 32: '已入职', 64: '已淘汰'}
    res = orderResumes_query(resumeStageCode)
    global resumeId
    try:
        resumeId = res.get(res['content']['result'][0]['orderResumeId'], 1120927027160162304)
    except IndexError:
        pass
    assert_equal(1, res['state'], '根据{}条件筛选获取简历列表成功'.format(resumeStageCode_list[resumeStageCode]))


def test_orderResumes_filter():
    res = orderResumes_filter()
    assert_equal(1, res['state'], '简历搜索筛选条目查询成功')


def test_orderResumes_positions_pages():
    res = orderResumes_positions_pages()
    assert_equal(1, res['state'], '分页查询用于简历查询的职位查询成功')


def test_orderResumes_sameResume_query():
    res = orderResumes_sameResume_query(resumeId)
    assert_equal(True, len(res['content']['result']), '多次投递记录查询成功')


def test_orderResumes_process_save():
    global contents
    contents = '为{}写简历评价'.format(resumeId)
    res = orderResumes_process_save(contents, resumeId)
    assert_equal(1, res['state'], '提交简历评价成功')


def test_orderResumes_process_query():
    res = orderResumes_process_query(resumeId)
    assert_equal(contents, res['content']['comments'][0]['comment']['content'], '查询简历参与者的评价记录成功')


def test_member_all():
    res = member_all()
    global atIds
    atIds = res['content']['result'][0]['userId']
    assert_equal(1, res['state'], '查询公司成员成功')


def test_orderResumes_process_forward():
    res = orderResumes_process_forward(atIds, resumeId)
    res_1 = orderResumes_process_query(resumeId)
    assert_equal(1, res['state'], "在简历评价里@同事成功！")
    ids = [cooperators['id'] for cooperators in res_1['content']['cooperators']]
    assert_equal(True, atIds in ids, "在简历评价里@同事成功！")
