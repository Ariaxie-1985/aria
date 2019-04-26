# -*- coding: utf8 -*-
__author__ = 'arayang'

from utils.util import assert_equal
import pytest
from api_script.entry.bigcompany.companyscore import *
def setup_module(module):
    pass


def teardown_module(module):
    pass

#@pytest.mark.parametrize("companyid",[()])
def test_companyscore():
    companyscore=companyscores().json()


    assert_equal(1,r['state'],"公司面试评分查询成功")