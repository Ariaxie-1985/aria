# coding:utf-8
# @Time  : 2019-02-18 15:29
# @Author: Xiawang

import pytest

from utils.util import login_home, login_home_code


@pytest.fixture()
def login_home_k8s_default():
    login_home_code('00853', 22222222)



