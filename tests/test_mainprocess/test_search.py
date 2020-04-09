# coding:utf-8
# @Time  : 2019-09-23 14:52
# @Author: Xiawang
# Description:
import logging
import random
import pytest
from api_script.entry.bigcompany.big_company import query_company_index
from api_script.entry.interview_experience.query import query_positionTypes, query_interview_experience
from api_script.entry.position.communicatePositions import query_positions, query_by_company
from api_script.entry.positionindex.hotCompany import switch_city
from api_script.entry.positionsearch.searchCompany import search_company
from api_script.entry.positionsearch.searchPosition import search_positions
from utils.util import assert_equal


@pytest.mark.parametrize("city", [("北京"), ("上海")])
def test_switch_city(c_login_app, city):
    r = switch_city(userToken=c_login_app[0], city=city)
    assert_equal(1, r['state'], '校验切换城市成功！')


@pytest.mark.parametrize("keyword,city,salaryLower,salaryUpper",
                         [("测试", "上海", 20000, 35000), ("JAVA", "北京", 15000, 25000)])
def test_search_positions(c_login_app, keyword, city, salaryLower, salaryUpper):
    r = search_positions(userToken=c_login_app[0], keyword=keyword, city=city, salaryLower=salaryLower,
                         salaryUpper=salaryUpper)
    positionName_list = [position_info['positionName'] for position_info in r['content']['positionCardVos']]
    for positionName in positionName_list:
        if keyword == "测试":
            check_result = "测试" in positionName.upper() or "QA" in positionName.upper()
            assert_equal(True, check_result, "校验搜索职位{}成功！".format(keyword))
        else:
            check_result = bool(keyword or 'ｊａｖａ' in positionName.upper())
            assert_equal(True, check_result,
                         "校验搜索职位{}成功！".format(keyword))
        break


@pytest.mark.parametrize("city,keyword", [("北京", "百度")])
def test_search_company(c_login_app, city, keyword):
    r = search_company(userToken=c_login_app[0], city=city, keyword=keyword)
    result = r['content']['searchCompanys']
    global companyId, showId
    companyId = result[0]['companyId']
    showId = r['content']['showId']
    assert_equal(True, bool(result), "校验搜索公司{}成功！".format(keyword))


def test_query_company_info(c_login_app):
    r = query_company_index(userToken=c_login_app[0], companyId=companyId)
    assert_equal("百度", r['content']['companyShortName'], "校验获取百度公司信息成功")


def test_query_positions(c_login_app):
    r = query_positions(userToken=c_login_app[0], companyId=companyId)
    for positions in r['content']['positionVos']:
        assert_equal("百度", positions['companyShortName'], "校验获取公司的在招职位成功！")
        break


@pytest.mark.parametrize("positionType", [("全部"), ("技术")])
def test_query_by_company(c_login_app, positionType):
    r = query_by_company(userToken=c_login_app[0], companyId=companyId, positionType=positionType)
    positionVos = r['content']['positionVos']
    assert_equal(True, bool(positionVos), "校验根据筛选条件获取公司的在招职位成功")


def test_query_positionTypes(c_login_app):
    r = query_positionTypes(userToken=c_login_app[0], companyId=companyId)
    assert_equal(1, r['state'], "校验查询筛选成功！")
    global positionType
    position_info = r['content']['positionTypes']
    positionType = position_info[random.randint(0, 8)]['code']


def test_query_interview_experience(c_login_app):
    r = query_interview_experience(userToken=c_login_app[0], companyId=companyId, positionType=positionType)
    assert_equal(1, r['state'], "校验面试条件查询成功!")
