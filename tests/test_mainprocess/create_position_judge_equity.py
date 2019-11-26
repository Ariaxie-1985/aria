# coding:utf-8
# @Time  : 2019-11-07 14:44
# @Author: Xiawang
# Description:
import datetime

import pytest
import random

from api_script.business.new_lagouPlus import open_product
from api_script.home.data_import import import_linkManInfo, import_contacts
from api_script.jianzhao_web.b_position.B_postposition import createPosition_999
from utils.util import assert_equal, login


# @pytest.mark.parametrize("firstType,positionType,positionThirdType,positionName",
#                          [("开发|测试|运维类", "后端开发", "Java", "java工程师")])
def setup_module():
    login("00852", "20181205")


def teardown_module():
    pass


def test_free_company_create_position_person_and_company_enough_equity(get_positionType):
    r = createPosition_999(firstType=get_positionType[0], positionType=get_positionType[1],
                           positionThirdType=get_positionType[2],
                           positionName=get_positionType[3])
    assert_equal(1, r['state'], '免费公司发布一个职位成功')


def test_buy_paid_package(get_company_id):
    contractNo = 'lagou-autotest-{}-{}'.format(str(datetime.date.today()), str(random.randint(1, 99)))
    r1 = import_linkManInfo(get_company_id[0], contractNo)
    r2 = import_contacts(get_company_id[0], contractNo)
    open_product(templateId=79, companyId=get_company_id, contractNo=contractNo, userId=234234,
                 startTimeStr=str(datetime.date.today()),
                 endTimeStr="2021-01-08")
    assert_equal(2, r1['state'] + r2['state'], "导入合同成功！")


def test_paid_company_create_position_person_and_company_enough_equity(get_positionType):
    r = createPosition_999(firstType=get_positionType[0], positionType=get_positionType[1],
                           positionThirdType=get_positionType[2],
                           positionName=get_positionType[3])
    assert_equal(1, r['state'], '付费公司发布职位成功')
