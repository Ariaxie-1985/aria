# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from api_script.jianzhao_web.gouinH5.list import list
from utils.util import login, assert_equal

def setup_module(module):
    pass


def teardown_module(module):
    pass

def test_list():
    r=list().json()
    assert_equal(1, r['state'], "查询商品列表成功")