# coding:utf-8
# @Time  : 2019-01-25 15:56
# @Author: betty

import pytest

from api_script.neirong.company.view_fuli import view_fuli
from utils.util import assert_equal


def setup_module():
    pass

def teardown_module():
    pass

def test_view_fuli():
    r = view_fuli()
    print(r)
    assert_equal(1,r['state'],"获取公司福利")
