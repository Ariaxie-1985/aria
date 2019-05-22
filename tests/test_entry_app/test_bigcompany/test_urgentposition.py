# -*- coding: utf8 -*-
__author__ = 'arayang'

from utils.util import assert_equal
import pytest
from api_script.entry.buser.hrinfo import *
from api_script.entry.bigcompany.urgentpositions import *
@pytest.importorskip('test_urgentposition.py', reason="等上线后再执行")


def setup_module(module):
    pass


def teardown_module(module):
    pass


# @pytest.mark.parametrize("companyid",[()])
def test_urgentposition():
    urgentposition = urgentpositions().json()

    assert_equal(1, urgentposition['state'], "急招职位查询成功")
