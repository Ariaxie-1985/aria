# coding:utf-8
# @Time  : 2019-05-31 11:42
# @Author: betty

from api_script.neirong.company.create_fuli import create_fuli
from api_script.neirong.company.view_fuli import view_fuli
from utils.util import assert_equal


def setup_module():
    pass


def teardown_module():
    pass


def test_create_fuli():
    r = create_fuli()
    assert_equal(1, r['state'], "增加公司福利")


def test_view_fuli():
    r = view_fuli()
    assert_equal(1, r['state'], "获取公司福利")
