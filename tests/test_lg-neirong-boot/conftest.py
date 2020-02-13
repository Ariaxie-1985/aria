# coding:utf-8
# @Time  : 2019-02-18 15:29
# @Author: Xiawang

import pytest

from api_script.entry.account.passport import password_login


@pytest.fixture(params=[["19910626899", "000000"]])
def login_app(request):
    result = password_login(request.param[0], request.param[1])
    return result['content']['userToken']
