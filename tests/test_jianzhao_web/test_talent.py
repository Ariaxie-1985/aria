# coding:utf-8
# @Author: Xiawang
from api_script.jianzhao_web.talent_communication.IM_update_resume_status import data_provider, chat_getMDSUserInfo, \
    position_selector, resume_interview, resume_lastInterview, resume_obsolete, can_searchCc, can_recentInterviewCc
from utils.util import assert_equal
import pytest

'''
人才沟通
'''

@pytest.importorskip('test_talent.py', reason="等IM变更简历状态（约面/淘汰）上线后再执行")
def setup_module(module):
    pass


def teardown_module(module):
    pass


sessionId, cUserId, outerPositionId, resumeId, positionId = 0, 0, 0, 0, 0


def test_data_provider(login_web_k8s_default):
    global sessionId, cUserId, outerPositionId, resumeId
    sessionId, cUserId, outerPositionId, resumeId = data_provider()


def test_chat_getMDSUserInfo():
    res = chat_getMDSUserInfo(cUserId, resumeId)
    assert_equal('NEW', res['content']['data']['resumeStage'], '校验获取的是否是新简历')


def test_position_selector():
    res = position_selector(resumeId, sessionId)
    for positions in res['content']['data']['positionSelectorVO']['typeList']:
        for position in positions['positionList']:
            if position['outerPositionId'] != outerPositionId:
                continue

            if position['outerPositionId'] == outerPositionId:
                global positionId
                positionId = position['id']

    assert_equal(1, res['state'], '获取所有的在线职位成功')


def test_resume_interview():
    res = resume_interview(resumeId, positionId)
    assert_equal(resumeId, res['content']['data']['resumeId'], '面试邀约成功')


def test_resume_lastInterview():
    res = resume_lastInterview(resumeId)
    assert_equal(resumeId, res['content']['data']['interview']['resumeId'], '获取最近一次面试邀约成功')


def test_resume_obsolete():
    res = resume_obsolete(resumeId)
    assert_equal(1, res['state'], '淘汰简历成功')


def test_can_searchCc():
    res = can_searchCc()



def test_can_recentInterviewCc():
    res = can_recentInterviewCc()