# -*- coding: utf8 -*-
__author__ = 'arayang'

from utils.util import assert_equal
import pytest
from api_script.entry.buser.hr_info import *
from api_script.entry.bigcompany.big_company import *
@pytest.importorskip('test_companybaseinfo.py', reason="等上线后再执行")

def setup_module(module):
    pass


def teardown_module(module):
    pass


# @pytest.mark.parametrize("companyid",[()])
def test_companybaseinfo():
    company = companyinfos()
    assert_equal(1, company['state'], "公司基本信息查询成功")
