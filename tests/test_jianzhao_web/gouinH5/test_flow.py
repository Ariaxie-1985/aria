# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from api_script.jianzhao_web.gouinH5.flow import flow
from utils.util import login, assert_equal

def setup_module(module):
    pass


def teardown_module(module):
    pass

def test_fiow():
    r=flow().json()
    assert_equal(1, r['state'], "查询勾印流水成功")
