# coding:utf-8
# @Time  : 2020/2/26 17:22
# @Author: Xiawang
# Description:
from api_script.zhaopin_app.bUser import member_all, interviewTemplate_create_update, interviewTemplate_all, \
    interviewTemplate_del
from utils.util import assert_equal, assert_in, assert_not_in


def test_member_all(b_login_app, ip_port):
    r = member_all(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port)
    assert_equal(True, bool(r['content']['result']), "查看我公司下的成员用例通过")


def test_interviewTemplate_create_update(b_login_app, ip_port):
    r = interviewTemplate_create_update(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port)
    global templateId
    templateId = r.get('content', 0)
    assert_equal(1, r['state'], '创建面试信息用例通过')


def test_interviewTemplate_all(b_login_app, ip_port):
    r = interviewTemplate_all(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port)
    global template_list
    template_list = [t['id'] for t in r['content']]
    assert_in(templateId, template_list, "添加面试信息用例通过")


def test_interviewTemplate_del(b_login_app, ip_port):
    r = interviewTemplate_del(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port, templateId=templateId)
    assert_in(templateId, template_list, "删除面试信息用例通过")


def test_interviewTemplate_all1(b_login_app, ip_port):
    r = interviewTemplate_all(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port)
    template_list = [t['id'] for t in r['content']]
    assert_not_in(templateId, template_list, "删除面试信息用例通过")
