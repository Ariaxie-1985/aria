# coding:utf-8
# @Time  : 2020/3/9 17:15
# @Author: Xiawang
# Description:
import pytest

from api_script.zhaopin_app.orderResumes import orderResumes_query, orderResumes_filter, orderResumes_positions_pages, \
    orderResumes_sameResume_query, orderResumes_detail, orderResumes_read
from utils.util import assert_equal


def test_orderResumes_filter(b_login_app):
    r = orderResumes_filter(userToken=b_login_app[0])
    assert_equal(1, r['state'], "简历搜索筛选用例通过")


def test_orderResumes_positions_pages(b_login_app):
    r = orderResumes_positions_pages(userToken=b_login_app[0])
    assert_equal(True, bool(r['content']['totalCount']), "分页查询用于简历查询的职位用例通过")


@pytest.mark.parametrize("resumeStageCode", [(1), (2), (4), (24), (32), (64)])
def test_orderResumes_query(b_login_app, resumeStageCode):
    r = orderResumes_query(userToken=b_login_app[0], resumeStageCode=resumeStageCode)
    global orderResumeId
    orderResumeId = r['content']['result'][0].get('orderResumeId')
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
