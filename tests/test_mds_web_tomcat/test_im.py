# coding:utf-8
# @Time  : 2020/3/20 17:58
# @Author: Xiawang
# Description:
import pytest

from api_script.jianzhao_web.im import settings_template, resume_report_reasons, im_session_list, im_session_get, \
    count_unRead_messages
from utils.util import assert_equal


def test_settings_template():
    r = settings_template()
    assert_equal(1, r.get('state'), '获取面试模板用例通过')


def test_resume_report_reasons():
    r = resume_report_reasons()
    assert_equal(True, r.get('success'), '获取简历举报原因用例通过')


@pytest.mark.parametrize("createBy", [(1), (2), (0)])
def test_im_session_list(createBy):
    r = im_session_list(createBy)
    for session in r['content']['rows']:
        if session.get('sessionType') == 0:
            global sessionId
            sessionId = session.get('sessionId')
            break
    assert_equal(1, r.get('state'), '获取im列表用例通过')


def test_im_session_get():
    r = im_session_get(session_id=sessionId)
    assert_equal(1, r.get('state'), '获取im某消息框用例通过')


def test_count_unRead_messages():
    r = count_unRead_messages()
    assert_equal(1, r.get('state'), '统计未读消息用例通过')
