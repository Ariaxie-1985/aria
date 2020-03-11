# coding:utf-8
# @Time  : 2019-11-07 11:46
# @Author: Xiawang
# Description:
import pytest

from api_script.entry.account.passport import password_login


@pytest.fixture(scope='session', params=[["0085320200306", "qqqqqq"]])
def c_login_education(request):
    result = password_login(request.param[0], request.param[1])
    return result['content']['userToken'], result['content']['userInfo']['userId']
