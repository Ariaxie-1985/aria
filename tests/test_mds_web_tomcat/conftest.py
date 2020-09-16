# coding:utf-8
# @Time  : 2019-11-07 11:46
# @Author: Xiawang
# Description:
import time
import pytest

from api_script.entry.account.passport import password_login
from backend.common.get_data import get_www_company_id
from utils.util import login, login_password
from faker import Faker
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import get_b_person_userId, get_b_index_Id

fake = Faker("zh_CN")


@pytest.fixture()
def get_user_info():
    userId, UserCompanyId, lg_CompanyId, name = get_b_index_Id()
    return userId, UserCompanyId, lg_CompanyId, name


@pytest.fixture(scope='session')
def get_password():
    return '990eb670f81e82f546cfaaae1587279a'


@pytest.fixture()
def get_positionType():
    firstType, positionType, positionThirdType, positionName = "开发|测试|运维类", "后端开发", "Java", "java工程师"
    return firstType, positionType, positionThirdType, positionName


@pytest.fixture(scope='session', params=[["19910626899", "9062e77da243687c68bf9665727b5c01"]])
def b_login_web(request):
    r = login_password(request.param[0], request.param[1])
    return r.get('state', 0)


def pytest_addoption(parser):
    parser.addoption(
        "--ip_port", action="store", default=None, help="ip:port"
    )


@pytest.fixture
def ip_port(request):
    return request.config.getoption("--ip_port")
