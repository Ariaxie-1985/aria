# coding:utf-8
# @Time  : 2020-02-13 10:15
# @Author: Xiawang
from random import randint

import pytest

from api_script.neirong_app.company import benefit_category_left, create_benefit, get_benefit_baseInfo, delete_benefit, \
    company_baseInfo, company_culture, company_detail, company_hasBenefit, company_question
from api_script.neirong_app.company_tab import queryCompanyList
from utils.util import assert_equal


def setup_module():
    pass


def teardown_module():
    pass


def test_benefit_category_left(login_app):
    r = benefit_category_left(userToken=login_app)
    global id
    id = r['content'][0]['labels'][0]['id']
    assert_equal(1, r['state'], "查询公司该城市下未添加的的福利标签数据用例成功")


def test_create_benefit(login_app):
    r = create_benefit(userToken=login_app, id=id)
    assert_equal(1, r['state'], "创建福利用例成功")


def test_get_benefit_baseInfo(login_app):
    r = get_benefit_baseInfo(userToken=login_app, companyId=418937)
    global labelIds, benefit_id
    labelIds = []
    for label in r['content'][0]['benefits']:
        if id == label['labelId']:
            benefit_id = label['id']
            labelIds.append(label['labelId'])
            break
    assert_equal(True, id in labelIds, "验证创建福利用例成功")


def test_delete_benefit(login_app):
    r = delete_benefit(userToken=login_app, id=benefit_id)
    assert_equal(1, r['state'], "删除福利用例成功")


def test_get_benefit_baseInfo1(login_app):
    r = get_benefit_baseInfo(userToken=login_app, companyId=418937)
    global labelIds
    labelIds = []
    for label in r['content'][0]['benefits']:
        labelIds.append(label['labelId'])
    assert_equal(True, id not in labelIds, "验证删除福利用例成功")


@pytest.mark.parametrize('city', [('深圳'), ('上海'), ('广州'), ('北京')])
def test_company_tab(city, login_app):
    r = queryCompanyList(city=city, userToken=login_app)
    global sz_companyId
    sz_companyId = r['content']['companyMsgVos'][randint(0, 5)]['companyId']
    assert_equal(True, len(r['content']['companyMsgVos']) > 6, '查询公司TAB页用例成功')


def test_company_baseInfo(login_app):
    r = company_baseInfo(userToken=login_app, companyId=sz_companyId)
    assert_equal(sz_companyId, r['content']['companyId'], '查询公司基本信息用例成功')


def test_company_culture(login_app):
    r = company_culture(userToken=login_app, companyId=sz_companyId)
    assert_equal(sz_companyId, r['content']['companyId'], '查询公司文化用例成功')


def test_company_detail(login_app):
    r = company_detail(userToken=login_app, companyId=sz_companyId)
    assert_equal(sz_companyId, r['content']['companyId'], '查询公司详情用例成功')


def test_company_hasBenefit(login_app):
    r = company_hasBenefit(userToken=login_app, companyId=sz_companyId)
    assert_equal(r['content'], r['content'], '查询公司是否有福利用例成功')


def test_company_question(login_app):
    r = company_question(userToken=login_app, companyId=sz_companyId)
    assert_equal(True, bool(r['content']), '查询公司是否有福利用例成功')
