# -*- coding: utf8 -*-
__author__ = 'arayang'

from utils.util import assert_equal
import pytest
from api_script.entry.buser.hrinfo import *
from api_script.entry.bigcompany.urgentpositions import *
def setup_module(module):
    pass


def teardown_module(module):
    pass

#@pytest.mark.parametrize("companyid",[()])
def test_urgentposition():
    urgentposition=urgentpositions().json()

    assert_equal(1,r['state'],"急招职位查询成功")