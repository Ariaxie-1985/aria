# -*- coding: utf8 -*-
__author__ = 'yqzhang'

from utils.util import assert_equal
import pytest
from api_script.entry.buser.hrinfo import *

def setup_module(module):
    pass


def teardown_module(module):
    pass

@pytest.mark.skip(reason="有问题, 暂不执行")
def test_hrinfo():
    r=hrinfo()
    assert_equal(1, r['state'], "查询hr信息成功")
# test_hrinfo()