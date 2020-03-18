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


@pytest.fixture(scope='session')
def get_company_name():
    company_name = '拉勾测试自动化' + fake.company() + str(time.time()).split('.')[0]
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


@pytest.fixture()
def get_user_id():
    userId = get_b_person_userId()
    return userId


@pytest.fixture()
def get_user_info():
    userId, UserCompanyId, lg_CompanyId = get_b_index_Id()
    return userId, UserCompanyId, lg_CompanyId


@pytest.fixture(scope='session')
def get_password():
    return '990eb670f81e82f546cfaaae1587279a'


@pytest.fixture()
def get_positionType():
    firstType, positionType, positionThirdType, positionName = "开发|测试|运维类", "后端开发", "Java", "java工程师"
    return firstType, positionType, positionThirdType, positionName



@pytest.fixture(params=[["00852", "20181205"]])
def login_web_k8s_default(request):
    login(request.param[0], request.param[1])


@pytest.fixture()
def get_company_id():
    return get_www_company_id()


@pytest.fixture()
def get_countryCode_phone():
    countryCode, phone = "00852", str(20000000 + int(str(time.time()).split('.')[1]))
    return countryCode, phone


# @pytest.fixture(scope='session', params=[["13033647506", "000000"]])
@pytest.fixture(scope='session', params=[["19910626899", "000000"]])
def b_login_app(request):
    result = password_login(request.param[0], request.param[1])
    return result['content']['userToken'], result['content']['userInfo']['userId']


@pytest.fixture(scope='session', params=[["0085220180917", "0085220180917"]])
def c_login_app(request):
    result = password_login(request.param[0], request.param[1])
    return result['content']['userToken'], result['content']['userInfo']['userId']


@pytest.fixture(scope='session', params=[["0085320200306", "qqqqqq"]])
def c_login_education(request):
    result = password_login(request.param[0], request.param[1])
    return result['content']['userToken'], result['content']['userInfo']['userId']

@pytest.fixture(scope='session', params=[["19910626899", "9062e77da243687c68bf9665727b5c01"]])
def b_login_web(request):
    r = login_password(request.param[0], request.param[1])
    return r.get('state',0)