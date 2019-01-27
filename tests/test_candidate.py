# coding:utf-8
# @Time  : 2019-01-25 15:56
# @Author: Xiawang
import os

import pytest

from api_script.jianzhao_web.resume_manage.candidate import can_new_list, can_new_createFilter, can_new_myfilters, \
	resume_deleteResumeFilter, can_recommend, can_batch_recommend, resume_uploadLocalResume, resume_uploadCandidateson, \
	multiChannel_myCompanyParentPositions
from util.read_file import get_file_path
from util.util import assert_equal, login


file_path = get_file_path("简历模板.pdf")

login("00852", "20181205")


def test_can_new_list():
	r = can_new_list()
	global resumeId, positionId, resumeIds
	resumeId = r['content']['rows'][-1]['id']
	resumeId1 = r['content']['rows'][1]['id']
	resumeId2 = r['content']['rows'][2]['id']
	positionId = r['content']['rows'][0]['positionId']
	resumeIds = resumeId1 + "," + resumeId2
	assert_equal(1, r['state'], "获取简历列表成功")


def test_can_new_createFilter():
	r = can_new_createFilter()
	assert_equal(1, r['state'], "创建候选人筛选器成功")


def test_can_new_myfilters():
	r = can_new_myfilters()
	global resumeFilterId
	resumeFilterId = r['content']['rows'][0]['id']
	assert_equal(1, r['state'], "获取候选人筛选器成功")


def test_resume_deleteResumeFilter():
	r = resume_deleteResumeFilter(resumeFilterId)
	assert_equal(1, r['state'], "删除候选人筛选器成功")


def test_can_new_list():
	r = can_new_list()
	global resumeId, positionId, resumeIds
	resumeId = r['content']['rows'][-1]['id']
	resumeId1 = r['content']['rows'][1]['id']
	resumeId2 = r['content']['rows'][2]['id']
	positionId = r['content']['rows'][0]['positionId']
	resumeIds = resumeId1 + "," + resumeId2
	assert_equal(1, r['state'], "获取简历列表成功")


def test_multiChannel_myCompanyParentPositions():
	r = multiChannel_myCompanyParentPositions()
	global parentPositionId
	parentPositionId = r['content']['data']['parentPositionCategory']['开发|测试|运维类'][0]['positionId']
	assert_equal(1, r['state'], "获取所在公司的父职位-parentPositionId成功")


@pytest.mark.xfail(reason="该职位下简历已经存在")
def test_can_recommend():
	r = can_recommend(resumeId, parentPositionId)
	assert_equal(1, r['state'], "推荐候选人到职位成功")


def test_can_batch_recommend():
	r = can_batch_recommend(resumeIds, parentPositionId)
	assert_equal(1, r['state'], "批量推荐候选人到职位成功")


def test_resume_uploadLocalResume():
	r = resume_uploadLocalResume(positionId, file_path)
	assert_equal(1, r['state'], "上传简历成功")


def test_resume_uploadCandidateson():
	r = resume_uploadCandidateson(parentPositionId, file_path)
	assert_equal(1, r['state'], "上传候选人成功")


