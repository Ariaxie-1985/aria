# coding:utf-8
# @Time  : 2019-11-07 11:46
# @Author: Xiawang
# Description:
import time
import pytest

from api_script.education.account import getToken
from api_script.entry.account.passport import password_login
from api_script.jianzhao_web.index import dashboard_index_get_user_id
from backend.common.get_data import get_www_company_id
from faker import Faker
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import get_b_person_userId, get_b_index_Id
from utils.util import login_password


fake = Faker("zh_CN")

'''
1.数据共享

@pytest.fixture()
使用场景:
1.1.为测试用例传参, 起到数据共享作用
1.2.可以做测试用例的初始化操作

作用域
1.1.默认function: 一个函数内部共享一个fixture
1.2.class: 一个class内共享同一个fixture
1.3.module: 一个.py文件内共享同一个fixture
1.4.session:当前目录下多个.py文件共享同一个fixture
    
'''

# 主流程测试产生的测试账号
test_telephone = []
test_company_name = []
test_usertoken = []


@pytest.fixture(scope='session')
def get_company_name():
    company_name = '拉勾测试自动化' + fake.company() + str(time.time()).split('.')[0]
    test_company_name.append(company_name)
    return company_name


@pytest.fixture()
def get_country_code_phone_user():
    countryCode, phone = "00852", str(30000000 + int(str(time.time()).split('.')[1]))
    test_telephone.append(countryCode + phone)
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


@pytest.fixture()
def www_get_userId():
    userId = dashboard_index_get_user_id()
    return userId


@pytest.fixture(scope='session')
def get_password():
    '''
    :return: 123456的固定加密值
    '''
    return '990eb670f81e82f546cfaaae1587279a'


@pytest.fixture()
def get_positionType():
    firstType, positionType, positionThirdType, positionName = "开发|测试|运维类", "后端开发", "Java", "java工程师"
    return firstType, positionType, positionThirdType, positionName


@pytest.fixture()
def get_company_id():
    return get_www_company_id()


@pytest.fixture(scope="module")
def telephone():
    return test_telephone


# @pytest.fixture(scope='session', params=[["13033647506", "000000"]])
@pytest.fixture(scope='session', params=[["19910626899", "000000"]])
def b_login_app(request):
    result = password_login(request.param[0], request.param[1])
    return result['content']['userToken'], result['content']['userInfo']['userId']

@pytest.fixture(scope='session', params=[["0085220180917", "0085220180917"]])
def c_login_app(request):
    result = password_login(request.param[0], request.param[1])
    return result['content']['userToken'], result['content']['userInfo']['userId']


@pytest.fixture(scope='session')
def c_userId_0085220180917():
    # 用户账号: 0085220180917 的 userId
    userId = 15166231
    return userId


@pytest.fixture()
def get_add_colleague_user():
    phone = 13683326352
    '''phone = '17620060403'''
    return phone


@pytest.fixture(scope='session', params=[["18810769854", "aaaaaa"]])
def c_login_education(request):
    result = password_login(request.param[0], request.param[1], app_type='LGEdu')
    test_usertoken.append(result['content']['userToken'])
    return result['content']['userToken'], result['content']['userInfo']['userId']



@pytest.fixture(scope='function', params=[["0085219820080", "qqqqqq"]])
def ice_breaking_edu(request):
    result = password_login(request.param[0], request.param[1], app_type='LGEdu')
    return result['content']['userToken'], result['content']['userInfo']['userId']

@pytest.fixture(scope='session')
def get_h5_token():
    result = getToken(userToken=test_usertoken[0])
    return result['content']['gateLoginToken']



# 2.当某用例失败后,接下来的依赖用例直接标记失败,不执行
# 用 pytest_configure(), pytest_runtest_setup(), pytest_runtest_makereport()三个函数共同合作的
def pytest_runtest_makereport(item, call):
    '''
    在第一个没有报失败的用例停止执行
    :param item: 测试用例
    :param call:调用步骤,pytest_runtest_setup(item), pytest_runtest_call(item), pytest_runtest_teardown(item)
    :return:一个测试报告对象
    '''
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item


def pytest_runtest_setup(item):
    '''
    called before ``pytest_runtest_call(item)
    每个测试用例的初始化,如果上一个用例是failed,接下来的用例有失败的, 就标记 xfail
    :param item: 测试用例
    :return:
    '''
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("previous test failed (%s)" % previousfailed.name)


def pytest_configure(config):
    '''
    编写新的hook函数
    :param config: pytest命令配置
    :return: 增加name:markers, 命令:incremental，备注:mark test to run only on named main_process的配置
    '''
    config.addinivalue_line(
        "markers", "incremental: mark test to run only on named main_process"
    )
