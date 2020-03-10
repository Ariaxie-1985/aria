# coding:utf-8
# @Time  : 2020-02-26 10:29
# @Author: Xiawang

import pytest

from api_script.entry.account.passport import password_login


@pytest.fixture(scope='session', params=[["19910626899", "000000"]])
# @pytest.fixture(scope='session', params=[["13033647506", "000000"]])
def b_login_app(request):
    result = password_login(request.param[0], request.param[1])
    return result['content']['userToken'], result['content']['userInfo']['userId']


@pytest.fixture(scope='session', params=[["0085220180917", "0085220180917"]])
def c_login_app(request):
    result = password_login(request.param[0], request.param[1])
    return result['content']['userToken'], result['content']['userInfo']['userId']
