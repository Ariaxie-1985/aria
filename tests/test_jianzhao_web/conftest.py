# coding:utf-8
# @Time  : 2019-02-18 15:29
# @Author: Xiawang

import pytest

from utils.util import login, login_home, login_home_code


@pytest.fixture(params=[["00852", "20181205"]])
def login_web_k8s_env_b(request):
	login(request.param[0],request.param[1])


@pytest.fixture()
def login_home_k8s_env_b():
	login_home("18810896987","c47eeb69fa4e64971fb29cb1e9163a19")

