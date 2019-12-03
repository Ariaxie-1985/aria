# coding:utf-8
# @Time  : 2019-11-07 11:46
# @Author: Xiawang
# Description:
import time

import pytest

from backend.common.get_data import get_www_company_id
from utils.util import login


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
