# coding:utf-8
# @Time  : 2020/3/9 17:15
# @Author: Xiawang
# Description:
import random

import pytest

from api_script.zhaopin_app.orderResumes import orderResumes_query, orderResumes_filter, orderResumes_positions_pages, \
    orderResumes_sameResume_query, orderResumes_detail, orderResumes_read, orderResumes_resume_link, \
    orderResumes_resume_interview, orderResumes_process_query, orderResumes_resume_obsolete, orderResumes_resume_luyong, \
    orderResumes_resume_employed, orderResumes_resume_new, orderResumes_stage, orderResumes_interview_datetime
from utils.util import assert_equal

order_resumeId = 0


def test_orderResumes_filter(b_login_app, ip_port):
    r = orderResumes_filter(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port)
    assert_equal(1, r['state'], "简历搜索筛选用例通过")


def test_orderResumes_positions_pages(b_login_app, ip_port):
    r = orderResumes_positions_pages(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port)
    assert_equal(True, bool(r['content']['totalCount']), "分页查询用于简历查询的职位用例通过")


@pytest.mark.parametrize("resumeStageCode", [(64), (2), (4), (24), (32), (1)])
def test_orderResumes_query(b_login_app, resumeStageCode, ip_port):
    r = orderResumes_query(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port,
                           resumeStageCode=resumeStageCode)
    global orderResumeId
    # 获取的是新简历第一个简历的订单简历id
    if resumeStageCode == 1:
        orderResumeId = r['content']['result'][random.randint(0, 19)]['orderResumeId']
    assert_equal(1, r.get('state'), "根据简历状态筛选获取简历列表用例通过")


@pytest.mark.parametrize('pageNo', [(1), (2), (3), (4)])
def test_orderResumes_sameResume_query(b_login_app, pageNo, ip_port):
    r = orderResumes_sameResume_query(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port,
                                      resumeId=orderResumeId, pageNo=pageNo)
    global order_resumeId, positionId
    for result in r['content']['result']:
        if result['resumeStage'] == "NEW":
            order_resumeId = result['id']
            positionId = result['positionId']
            break
    assert_equal(1, r.get('state'), "多次投递记录用例通过")


@pytest.mark.skipif('order_resumeId == 0', reason="未获取到订单简历id, 暂时跳过")
def test_orderResumes_stage_NEW(b_login_app, ip_port):
    r = orderResumes_stage(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port, resumeId=order_resumeId)
    assert_equal("NEW", r['content']['stage'], '新简历阶段用例通过')


@pytest.mark.skipif('order_resumeId == 0', reason="未获取到订单简历id, 暂时跳过")
def test_orderResumes_detail(b_login_app, ip_port):
    r = orderResumes_detail(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port, resumeId=order_resumeId)
    assert_equal(str(order_resumeId), r['content']['orderResumeId'], "查询简历详情用例通过")


@pytest.mark.skipif('order_resumeId == 0', reason="未获取到订单简历id, 暂时跳过")
def test_orderResumes_read(b_login_app, ip_port):
    r = orderResumes_read(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port, resumeId=order_resumeId)
    assert_equal(1, r['state'], '设置简历已读用例通过')


@pytest.mark.skipif('order_resumeId == 0', reason="未获取到订单简历id, 暂时跳过")
def test_orderResumes_resume_link(b_login_app, ip_port):
    r = orderResumes_resume_link(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port,
                                 resumeId=order_resumeId)
    assert_equal(1, r['state'], '标记初筛用例通过')


@pytest.mark.skipif('order_resumeId == 0', reason="未获取到订单简历id, 暂时跳过")
def test_orderResumes_stage_LINK(b_login_app, ip_port):
    r = orderResumes_stage(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port, resumeId=order_resumeId)
    assert_equal("LINK", r['content']['stage'], '标记初筛阶段用例通过')


@pytest.mark.skipif('order_resumeId == 0', reason="未获取到订单简历id, 暂时跳过")
def test_orderResumes_process_query(b_login_app, ip_port):
    r = orderResumes_process_query(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port,
                                   resumeId=order_resumeId)
    assert_equal(1, r.get('state', 0), "查询简历参与者的评价记录")


@pytest.mark.skipif('order_resumeId == 0', reason="未获取到订单简历id, 暂时跳过")
def test_orderResumes_resume_interview(b_login_app, ip_port):
    r = orderResumes_resume_interview(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port,
                                      resumeId=order_resumeId, positionId=positionId)
    global resume_state
    resume_state = r['state']
    if resume_state == 2002016:
        pytest.skip("这个时间候选人已经有面试了,无需面试")
    assert_equal(1, r['state'], '邀约面试用例通过')


@pytest.mark.skipif('order_resumeId == 0', reason="未获取到订单简历id, 暂时跳过")
@pytest.mark.skipif("resume_state == 2002016", reason="候选人已经有面试, 无需邀约面试, 跳过")
def test_orderResumes_stage_INTERVIEW(b_login_app, ip_port):
    r = orderResumes_stage(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port, resumeId=order_resumeId)
    assert_equal("INTERVIEW", r['content']['stage'], '面试阶段用例通过')


@pytest.mark.skipif('order_resumeId == 0', reason="未获取到订单简历id, 暂时跳过")
def test_orderResumes_interview_datetime(b_login_app, ip_port):
    r = orderResumes_interview_datetime(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port,
                                        resumeId=order_resumeId)
    if r.get('state', 1) == 2002010:
        pytest.skip("简历处于不能修改面试时间的阶段, 跳过")
    assert_equal(1, r['state'], '修改面试时间用例通过')


@pytest.mark.skipif('order_resumeId == 0', reason="未获取到订单简历id, 暂时跳过")
def test_orderResumes_resume_luyong(b_login_app, ip_port):
    r = orderResumes_resume_luyong(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port,
                                   resumeId=order_resumeId)
    assert_equal(1, r['state'], '录用候选人用例通过')


@pytest.mark.skipif('order_resumeId == 0', reason="未获取到订单简历id, 暂时跳过")
def test_orderResumes_stage_OFFER(b_login_app, ip_port):
    r = orderResumes_stage(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port, resumeId=order_resumeId)
    assert_equal("OFFER", r['content']['stage'], '录用阶段用例通过')


@pytest.mark.skipif('order_resumeId == 0', reason="未获取到订单简历id, 暂时跳过")
def test_orderResumes_resume_employed(b_login_app, ip_port):
    r = orderResumes_resume_employed(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port,
                                     resumeId=order_resumeId)
    assert_equal(1, r['state'], '候选人已入职用例通过')


@pytest.mark.skipif('order_resumeId == 0', reason="未获取到订单简历id, 暂时跳过")
def test_orderResumes_stage_EMPLOYED(b_login_app, ip_port):
    r = orderResumes_stage(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port, resumeId=order_resumeId)
    assert_equal("EMPLOYED", r['content']['stage'], '已入职阶段用例通过')


@pytest.mark.skipif('order_resumeId == 0', reason="未获取到订单简历id, 暂时跳过")
def test_orderResumes_resume_obsolete(b_login_app, ip_port):
    r = orderResumes_resume_obsolete(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port,
                                     resumeId=order_resumeId)
    assert_equal(1, r['state'], '候选人状态调整为不合适用例通过')


@pytest.mark.skipif('order_resumeId == 0', reason="未获取到订单简历id, 暂时跳过")
def test_orderResumes_stage_obsolete(b_login_app, ip_port):
    r = orderResumes_stage(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port, resumeId=order_resumeId)
    assert_equal("OBSOLETE", r['content']['stage'], '淘汰阶段用例通过')


@pytest.mark.skipif('order_resumeId == 0', reason="未获取到订单简历id, 暂时跳过")
def test_orderResumes_resume_new(b_login_app, ip_port):
    r = orderResumes_resume_new(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port,
                                resumeId=order_resumeId)
    assert_equal(1, r['state'], '将淘汰简历重新恢复为候选人用例通过')


@pytest.mark.skipif('order_resumeId == 0', reason="未获取到订单简历id, 暂时跳过")
def test_orderResumes_stage(b_login_app, ip_port):
    r = orderResumes_stage(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port, resumeId=order_resumeId)
    assert_equal("NEW", r['content']['stage'], '查询简历阶段用例通过')
