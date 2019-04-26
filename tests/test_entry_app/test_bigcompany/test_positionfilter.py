# -*- coding: utf8 -*-
__author__ = 'arayang'

from utils.util import assert_equal
import pytest
from api_script.entry.bigcompany.positionfilter import *


def setup_module(module):
    pass


def teardown_module(module):
    pass


# @pytest.mark.parametrize("companyid",[()])
def test_positionfilter():
    companyscore = positionfilter().json()

    assert_equal(1, companyscore['state'], "公司主页职位筛选结果")