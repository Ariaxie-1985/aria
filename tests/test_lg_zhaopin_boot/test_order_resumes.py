# coding:utf-8
# @Time  : 2020/3/9 17:15
# @Author: Xiawang
# Description:
import pytest

from api_script.zhaopin_app.orderResumes import orderResumes_query, orderResumes_filter, orderResumes_positions_pages, \
    orderResumes_sameResume_query, orderResumes_detail, orderResumes_read, orderResumes_resume_link, \
    orderResumes_resume_interview, orderResumes_process_query, orderResumes_resume_obsolete, orderResumes_resume_luyong, \
    orderResumes_resume_employed, orderResumes_resume_new, orderResumes_stage, orderResumes_interview_datetime
from utils.util import assert_equal


def test_orderResumes_filter(b_login_app):
    r = orderResumes_filter(userToken=b_login_app[0])
    assert_equal(1, r['state'], "简历搜索筛选用例通过")


def test_orderResumes_positions_pages(b_login_app):
    r = orderResumes_positions_pages(userToken=b_login_app[0])
    assert_equal(True, bool(r['content']['totalCount']), "分页查询用于简历查询的职位用例通过")


@pytest.mark.parametrize("resumeStageCode", [(64), (2), (4), (24), (32), (1)])
def test_orderResumes_query(b_login_app, resumeStageCode):
    r = orderResumes_query(userToken=b_login_app[0], resumeStageCode=resumeStageCode)
    global orderResumeId
    # 获取的是新简历第一个简历的订单简历id
    orderResumeId = r['content']['result'][0]['orderResumeId']
    assert_equal(True, bool(r['content']['result'][0]), "根据简历状态筛选获取简历列表用例通过")


def test_orderResumes_sameResume_query(b_login_app):
    r = orderResumes_sameResume_query(userToken=b_login_app[0], resumeId=orderResumeId)
    assert_equal(True, bool(r['content']['totalCount']), "多次投递记录用例通过")


def test_orderResumes_detail(b_login_app):
    r = orderResumes_detail(userToken=b_login_app[0], resumeId=orderResumeId)
    assert_equal(str(orderResumeId), r['content']['orderResumeId'], "查询简历详情用例通过")


def test_orderResumes_read(b_login_app):
    r = orderResumes_read(userToken=b_login_app[0], resumeId=orderResumeId)
    assert_equal(1, r['state'], '设置简历已读用例通过')


def test_orderResumes_resume_link(b_login_app):
    r = orderResumes_resume_link(userToken=b_login_app[0], resumeId=orderResumeId)
    assert_equal(1, r['state'], '标记初筛用例通过')


def test_orderResumes_process_query(b_login_app):
    r = orderResumes_process_query(userToken=b_login_app[0], resumeId=orderResumeId)
    for comment in r['content']['comments']:
        if comment['operate'].get('operateType') == 'DELIVER_RESUME':
            global positionId
            positionId = comment['operate']['parameters']['positionId']
    assert_equal(1, r.get('state', 0), "查询简历参与者的评价记录")


def test_orderResumes_resume_interview(b_login_app):
    r = orderResumes_resume_interview(userToken=b_login_app[0], resumeId=orderResumeId, positionId=positionId)
    global resume_state
    resume_state = r['state']
    if resume_state == 2002016:
        pytest.skip("这个时间候选人已经有面试了,无需面试")
    assert_equal(1, r['state'], '邀约面试用例通过')


def test_orderResumes_resume_luyong(b_login_app):
    r = orderResumes_resume_luyong(userToken=b_login_app[0], resumeId=orderResumeId)
    assert_equal(1, r['state'], '录用候选人用例通过')


def test_orderResumes_resume_employed(b_login_app):
    r = orderResumes_resume_employed(userToken=b_login_app[0], resumeId=orderResumeId)
    assert_equal(1, r['state'], '候选人已入职用例通过')


def test_orderResumes_resume_obsolete(b_login_app):
    r = orderResumes_resume_obsolete(userToken=b_login_app[0], resumeId=orderResumeId)
    assert_equal(1, r['state'], '候选人状态调整为不合适用例通过')


def test_orderResumes_resume_new(b_login_app):
    r = orderResumes_resume_new(userToken=b_login_app[0], resumeId=orderResumeId)
    assert_equal(1, r['state'], '将淘汰简历重新恢复为候选人用例通过')


# todo 需要抓包看看，明天到公司
def test_orderResumes_stage(b_login_app):
    r = orderResumes_stage(userToken=b_login_app[0], resumeId=orderResumeId)
    assert_equal(1, r['state'], '查询简历阶段用例通过')


def test_orderResumes_interview_datetime(b_login_app):
    r = orderResumes_interview_datetime(userToken=b_login_app[0], resumeId=orderResumeId)
    if r.get('state', 1) == 2002010:
        pytest.skip("简历处于不能修改面试时间的阶段, 跳过")
    assert_equal(1, r['state'], '修改面试时间用例通过')
