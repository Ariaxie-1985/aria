# coding:utf-8
# @Time  : 2020/3/18 19:25
# @Author: Xiawang
# Description:
import time

import pytest

from api_script.jianzhao_web.resume_manage.candidate import can_new_list, can_new_additionalInfo, \
    can_new_get_resume_other_info, resume_preview_info, can_new_filter, can_batch_toStageLink, can_new_count, \
    interview_new_list
from api_script.jianzhao_web.resume_manage.resume import get_not_read_resume_count
from utils.util import assert_equal


def test_get_not_read_resume_count():
    r = get_not_read_resume_count()
    assert_equal(True, bool(r['content']['data']['resumeCount']), '统计未读简历数用例通过')


@pytest.mark.skip(reason="接口有拦截，暂跳过执行")
@pytest.mark.parametrize("stage", [('NEW')])
def test_can_new_list(stage):
    r = can_new_list(stage=stage)
    global resume_ids
    resume_ids = [resume['id'] for resume in r['content']['rows']]
    assert_equal(1, r.get('state'), '获取简历列表(新简历或初筛)用例通过')


@pytest.mark.skip(reason="接口有拦截，暂跳过执行")
@pytest.mark.parametrize("stage", [('NEW')])
def test_can_new_additionalInfo(stage):
    r = can_new_additionalInfo(resumeIds=','.join(resume_ids), stage=stage)
    assert_equal(1, r.get('state'), '获取简历的附加信息用例通过')


@pytest.mark.skip(reason="接口有拦截，暂跳过执行")
@pytest.mark.parametrize("stage", [('NEW')])
def test_can_new_get_resume_other_info(stage):
    r = can_new_get_resume_other_info(resumeIds=','.join(resume_ids), stage=stage)
    assert_equal(1, r.get('state'), '获取简历的其他信息用例通过')


@pytest.mark.skip(reason="接口有拦截，暂跳过执行")
@pytest.mark.parametrize("stage", [('NEW')])
def test_resume_preview_info(stage):
    r = resume_preview_info(resumeIds=resume_ids[0], stage=stage)
    assert_equal(1, r.get('state'), '查看简历的预览信息用例通过')


@pytest.mark.skip(reason="接口有拦截，暂跳过执行")
def test_can_batch_toStageLink():
    r = can_batch_toStageLink(resumeIds=resume_ids[0])
    assert_equal(1, r.get('state'), '初筛移至待沟通用例通过')


@pytest.mark.parametrize("stage", [('NEW')])
def test_can_new_filter(stage):
    r = can_new_filter(stage=stage)
    assert_equal(1, r.get('state'), '查看简历的筛选器用例通过')


@pytest.mark.parametrize("stage", [('NEW'), ('LINK'), ('INTERVIEW'), ('LUYONG')])
def test_can_new_count(stage):
    r = can_new_count(stage)
    assert_equal(1, r.get('state'), '统计简历阶段的简历数用例通过')


@pytest.mark.parametrize("range", [(0), (1), (2), (3)])
def test_interview_new_list(range):
    r = interview_new_list(range)
    assert_equal(1, r.get('state'), '统计面试日程通过')



