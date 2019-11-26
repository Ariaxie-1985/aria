# coding:utf-8
# @Time  : 2019-11-26 14:58
# @Author: Xiawang
# Description:
import time

import pytest
from faker import Faker

from api_script.jianzhao_web.b_basic.toB_saveHR_1 import get_b_userId

fake = Faker("zh_CN")


@pytest.fixture(scope='session')
def get_company_name():
    company_name = '拉勾测试自动化' + fake.company() + str(20000000 + int(str(time.time()).split('.')[1]))
    return company_name


@pytest.fixture(scope='session')
def get_countryCode_phone_admin_user():
    countryCode, phone = "00852", str(20000000 + int(str(time.time()).split('.')[1]))
    user_name = '拉勾测试自动化' + fake.name()
    return countryCode, phone, user_name


@pytest.fixture(scope='session')
def get_countryCode_phone_general_user():
    countryCode, phone = "00852", str(20000000 + int(str(time.time()).split('.')[1]))
    user_name = '拉勾测试自动化' + fake.name()
    return countryCode, phone, user_name


@pytest.fixture(scope='session')
def get_user_info():
    userId, UserCompanyId, lg_CompanyId = get_b_userId()
    return userId, UserCompanyId, lg_CompanyId
