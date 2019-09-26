# coding:utf-8
# @Time  : 2019-09-23 14:52
# @Author: Xiawang
# Description:
import random
import pytest
from api_script.entry.account.passport import password_login
from api_script.entry.bigcompany.companybaseinfo import query_company_info
from api_script.entry.interview_experience.query import query_positionTypes, query_interview_experience
from api_script.entry.position.communicatePositions import query_positions, query_by_company
from api_script.entry.positionindex.hotCompany import switch_city
from api_script.entry.positionsearch.searchCompany import search_company
from api_script.entry.positionsearch.searchPosition import search_positions
from utils.util import assert_equal


@pytest.mark.parametrize("accountName,password", [("0085220180917", "0085220180917")])
def test_password_login(accountName, password):
    r = password_login(accountName, password)
    assert_equal(1, r['state'], '校验密码登录成功', '校验密码登录失败')
    global userToken
    userToken = r['content']['userToken']


@pytest.mark.parametrize("city", [("北京"), ("上海")])
def test_switch_city(city):
    r = switch_city(userToken, city=city)
    assert_equal(1, r['state'], '校验切换城市成功！')


@pytest.mark.parametrize("keyword,city,salaryLower,salaryUpper",
                         [("测试", "上海", 20000, 35000), ("Java", "北京", 15000, 25000)])
def test_search_positions(keyword, city, salaryLower, salaryUpper):
    r = search_positions(userToken, keyword=keyword, city=city, salaryLower=salaryLower, salaryUpper=salaryUpper)
    for position_info in r['content']['positionCardVos']:
        assert keyword in position_info['positionName']
        break


@pytest.mark.parametrize("city,keyword", [("北京", "百度")])
def test_search_company(city, keyword):
    r = search_company(userToken, city=city, keyword=keyword)
    result = r['content']['searchCompanys']
    global companyId, showId
    companyId = result[0]['companyId']
    showId = r['content']['showId']
    assert_equal(True, bool(result), "校验搜索公司{}成功！".format(keyword))


def test_query_company_info():
    r = query_company_info(userToken, companyId)
    assert_equal("百度", r['content']['companyShortName'], "校验获取百度公司信息成功")


def test_query_positions():
    r = query_positions(userToken, companyId)
    for positions in r['content']['positionVos']:
        assert_equal("百度", positions['companyShortName'], "校验获取公司的在招职位成功！")
        break


@pytest.mark.parametrize("positionType", [("全部"), ("技术")])
def test_query_by_company(positionType):
    r = query_by_company(userToken, companyId, positionType)
    positionVos = r['content']['positionVos']
    assert_equal(True, bool(positionVos), "校验根据筛选条件获取公司的在招职位成功")


def test_query_positionTypes():
    r = query_positionTypes(userToken, companyId)
    assert_equal(1, r['state'], "校验查询筛选成功！")
    global positionType
    position_info = r['content']['positionTypes']
    positionType = position_info[random.randint(0, 8)]['code']


def test_query_interview_experience():
    r = query_interview_experience(userToken, companyId, positionType)
    assert_equal(1, r['state'], "校验面试条件查询成功!")
