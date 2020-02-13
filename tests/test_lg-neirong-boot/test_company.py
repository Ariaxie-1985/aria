# coding:utf-8
# @Time  : 2020-02-13 10:15
# @Author: Xiawang

from api_script.neirong_app.company import create_fuli, view_fuli
from utils.util import assert_equal


def setup_module():
    pass


def teardown_module():
    pass


def test_create_welfare():
    r = create_fuli()
    assert_equal(1, r['state'], "增加公司福利")


def test_view_welfare():
    r = view_fuli()
    assert_equal(1, r['state'], "获取公司福利")
