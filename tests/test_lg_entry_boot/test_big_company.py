# coding:utf-8
# @Time  : 2020/2/17 16:36
# @Author: Xiawang
# Description:
import pytest

from api_script.entry.account.passport import password_login
from api_script.entry.bigcompany.big_company import query_company_index, query_all_company, query_urgent_positions, \
    is_big_company
from api_script.entry.company import get_hot_company, get_company_questions, company_attention_add, \
    company_attention_list, company_attention_delete
from api_script.entry.interview_experience.query import query_interview_experience, query_company_score
from utils.util import assert_equal, assert_in
import random

userToken, userId = '', ''


def test_login_app(ip_port):
    result = password_login("19910626899", "000000", ip_port=ip_port)
    global userToken, userId
    userToken, userId = result['content']['userToken'], result['content']['userInfo']['userId']
    assert_equal(1, result.get('state'), '登录用例通过')


@pytest.mark.parametrize("city", [('北京')])
def test_get_hot_company(ip_port, city):
    r = get_hot_company(userToken=userToken, userId=userId, ip_port=ip_port, city=city)
    global hot_companyId
    hot_companyId = r['content'][random.randint(0, 5)]['companyId']
    assert_equal(True, bool(hot_companyId), '查询热门公司的主页用例通过')


def test_query_company_index(ip_port):
    r = query_company_index(userToken=userToken, userId=userId, ip_port=ip_port, companyId=hot_companyId)
    assert_equal(1, r.get('state'), '查询公司用例成功')
    if r['content']['companyId']:
        actual_companyId = r['content']['companyId']
    elif r['content']['companyProductVos']:
        actual_companyId = r['content']['companyProductVos'][0]['companyId']
    elif r['content']['companyLeaderVos']:
        actual_companyId = r['content']['companyLeaderVos'][0]['companyId']
    elif r['content']['companyHistoryVos']:
        actual_companyId = r['content']['companyHistoryVos'][0]['companyId']
    assert_equal(hot_companyId, actual_companyId, '查询公司id:{}的主页用例通过'.format(hot_companyId))


def test_query_all_company(ip_port):
    r = query_all_company(userToken=userToken, userId=userId, ip_port=ip_port)
    assert_in(423911, r['content'], '查询所有大公司ID列表用例通过')


def test_query_urgent_positions(ip_port):
    r = query_urgent_positions(userToken=userToken, userId=userId, ip_port=ip_port, companyId=hot_companyId)
    assert_equal(1, r['state'], '查询所有大公司ID列表用例通过')


def test_is_big_company(ip_port):
    r = is_big_company(userToken=userToken, userId=userId, ip_port=ip_port, companyId=423911)
    assert_equal(True, r['content'], '是否大公司用例通过')


def test_get_company_questions(ip_port):
    r = get_company_questions(userToken=userToken, userId=userId, ip_port=ip_port, companyId=hot_companyId)
    assert_equal(True, bool(r['content']['questionV2s']), '公司问答列表查询用例通过')


def test_company_attention_add(ip_port):
    r = company_attention_add(userToken=userToken, userId=userId, ip_port=ip_port, companyId=hot_companyId)
    assert_equal(1, r['state'], '关注公司用例通过')


def test_company_attention_list(ip_port):
    r = company_attention_list(userToken=userToken, userId=userId, ip_port=ip_port)
    assert_equal(hot_companyId, r['content']['attentionCompanies'][0]['companyId'], '验证关注公司是否成功用例通过')


def test_company_attention_delete(ip_port):
    r = company_attention_delete(userToken=userToken, userId=userId, ip_port=ip_port, companyId=hot_companyId)
    assert_equal(1, r['state'], '查询关注的公司列表用例通过')


def test_company_attention_list1(ip_port):
    r = company_attention_list(userToken=userToken, userId=userId, ip_port=ip_port)
    assert_equal(False, bool(r['content']['attentionCompanies']), '验证取消关注公司是否成功用例通过')


@pytest.mark.parametrize('positionType', [(0), (1), (2)])
def test_query_interview_experience(positionType, ip_port):
    r = query_interview_experience(userToken=userToken, userId=userId, ip_port=ip_port,
                                   companyId=hot_companyId, positionType=positionType)
    assert_equal(True, bool(r['content']['interviewScore']), '查询面试评价用例通过')


def test_query_company_score(ip_port):
    r = query_company_score(userToken=userToken, userId=userId, ip_port=ip_port, companyId=hot_companyId)
    assert_equal(True, bool(r['content']['comprehensiveScore']), '查询公司面试评价分数用例通过')
