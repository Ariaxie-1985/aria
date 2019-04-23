#@author:betty
#@time:2019-4-23

import pytest
from api_script.neirong.company.create_fuli import create_fuli
from api_script.neirong.company.view_fuli import view_fuli
from utils.util import assert_equal
from tests.test_neirong_app.test_view_fuli import test_view_fuli


def setup_module():
    pass

def teardown_module():
    pass

def test_create_fuli():
    r = create_fuli()
    print(r)
    assert_equal(1, r['state'], "增加公司福利")


def test_view_fuli():
    r = view_fuli()
    print(r)
    assert_equal(1, r['state'], "获取公司福利")
