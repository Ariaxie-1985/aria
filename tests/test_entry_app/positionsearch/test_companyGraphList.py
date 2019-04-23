# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from utils.util import assert_equal
import pytest
from api_script.entry.positionsearch.companyGraphList import *

def setup_module(module):
    pass


def teardown_module(module):
    pass


def test_hrinfo():
    r=companyGraphList()
    assert_equal(1, r['state'], "公司图谱成功")