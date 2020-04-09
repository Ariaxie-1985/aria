# coding:utf-8
# @Time  : 2019-02-18 15:29
# @Author: Xiawang

import pytest

from api_script.entry.account.passport import password_login
from api_script.entry.positionsearch.searchPosition import search_positions


@pytest.fixture(scope='session', params=[["19910626899", "000000"]])
def login_app(request, ip_port):
    result = password_login(request.param[0], request.param[1], ip_port=ip_port)
    return result['content']['userToken'], result['content']['userInfo']['userId']


@pytest.fixture(scope='session')
def query_position(login_app, ip_port):
    r = search_positions(userToken=login_app[0], userId=login_app[1], ip_port=ip_port, keyword='JAVA')
    return r['content']['positionCardVos'][0]['positionId']


def pytest_addoption(parser):
    parser.addoption(
        "--ip_port", action="store", default=None, help="ip:port"
    )


@pytest.fixture
def ip_port(request):
    return request.config.getoption("--ip_port")
