# coding:utf-8
# @Time  : 2020/6/2 10:31
# @Author: Xiawang
# Description:
import pytest

from api_script.entry.account.passport import password_login
from api_script.is_debug_login import debugSelfCheck
from api_script.open_lagou_com.account import openid_query
from api_script.open_lagou_com.authority import open_authority_token

access_token_list = []
collect_ignore = []
if debugSelfCheck().get('message', '失败') != '成功':
    collect_ignore.append("test_open_api_lagou_com/")

@pytest.fixture(scope='session')
def get_access_token():
    res = open_authority_token(appid='b1a5rsdsi7qukd3x', secret='2lvvus0lztf692u4vt9hqxare5qbm9ap',
                               grant_type='client_credential')
    access_token = res.get('access_token')
    access_token_list.append(access_token)
    return access_token


@pytest.fixture(scope='session')
def get_openid():
    res = openid_query(access_token=access_token_list[0], credential=13033647506)
    return res.get('openid')


@pytest.fixture(scope='session', params=[["0085220180917", "0085220180917"]])
def c_login_app(request):
    result = password_login(request.param[0], request.param[1])
    return result['content']['userToken'], result['content']['userInfo']['userId']

@pytest.fixture(scope='session', params=[["13033647506", "000000"]])
def b_login_app(request):
    result = password_login(request.param[0], request.param[1])
    return result['content']['userToken'], result['content']['userInfo']['userId']


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
