# coding:utf-8
# @Time  : 2020/6/4 14:10
# @Author: Xiawang
# Description:
import time

import pytest

from api_script.open_lagou_com.resume import get_resume_list, get_online_resume, get_attachment_resume, get_contact, \
    get_interview, get_obsolete
from utils.util import assert_equal


@pytest.mark.incremental
class TestResume:

    @pytest.mark.parametrize("stage", [('OBSOLETE'), ('LINK'), ('INTERVIEW'), ('NEW')])
    def test_get_resume_list(self, get_access_token, stage):
        time.sleep(1.5)
        res = get_resume_list(access_token=get_access_token, stage=stage)
        assert_equal(0, res.get('code', 1), f'获取{stage}阶段请求成功', te='王霞')
        if len(res.get('data', [])) > 0:
            assert_equal(stage, res['data'][0]['stage'], f'获取{stage}的简历用例通过', f'获取{stage}的简历用例失败', '王霞')
            global resume_id
            resume_id = res['data'][0]['resume_id']

    def test_get_online_resume(self, get_access_token):
        res = get_online_resume(access_token=get_access_token, resume_id=resume_id)
        assert_equal(0, res.get('code', 1), f'获取在线简历信息请求成功', te='王霞')
        assert_equal(resume_id, res['data']['resumes']['resume_id'], '获取在线简历用例通过', f'获取在线简历{resume_id}用例失败', '王霞')

    def test_get_attachment_resume(self, get_access_token):
        res = get_attachment_resume(access_token=get_access_token, resume_id=resume_id)
        assert_equal(200, res.status_code, f'获取附件简历信息请求成功', te='王霞')
        assert_equal('pdf', res.headers.get('Attachment-Suffix'), '获取附件简历用例通过', f'获取附件简历{resume_id}用例失败', '王霞')

    def test_get_contact(self, get_access_token):
        res = get_contact(access_token=get_access_token, resume_id=resume_id)
        assert_equal(0, res.get('code', 1), f'标记初筛请求成功', te='王霞')
        assert_equal(resume_id, int(res['data']['resumeVo']['id']), '标记初筛用例通过', f'标记初筛{resume_id}用例失败', '王霞')

    def test_get_interview(self, get_access_token):
        res = get_interview(access_token=get_access_token, resume_id=resume_id)
        assert_equal(0, res.get('code', 1), f'邀约面试请求成功', te='王霞')
        assert_equal(resume_id, int(res['data']['resumeVo']['id']), '邀约面试用例通过', f'邀约面试{resume_id}用例失败', '王霞')

    def test_get_obsolete(self, get_access_token):
        res = get_obsolete(access_token=get_access_token, resume_id=resume_id)
        assert_equal(0, res.get('code', 1), f'淘汰候选人请求成功', te='王霞')
        assert_equal(resume_id, int(res['data']['resumeVo']['id']), '淘汰候选人用例通过', f'淘汰候选人{resume_id}用例失败', '王霞')
