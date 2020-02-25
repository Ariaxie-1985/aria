# coding:utf-8
# @Time  : 2019-02-18 15:29
# @Author: Xiawang

import pytest

from api_script.entry.account.passport import password_login
from api_script.entry.positionsearch.searchPosition import search_positions


@pytest.fixture(scope='session', params=[["19910626899", "000000"]])
def login_app(request):
    result = password_login(request.param[0], request.param[1])
    return result['content']['userToken']


@pytest.fixture(scope='session')
def query_position(login_app):
    r = search_positions(userToken=login_app,keyword='JAVA')
    return r['content']['positionCardVos'][0]['positionId']
