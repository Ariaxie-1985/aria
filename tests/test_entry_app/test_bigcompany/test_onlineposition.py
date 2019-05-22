# -*- coding:utf8 -*-
__author__ = 'arayang'

from utils.util import assert_equal
import pytest
from api_script.entry.bigcompany.onlineposition import *
@pytest.importorskip('test_onlineposition.py', reason="等上线后再执行")


def setup_module(module):
    pass


def teardown_module(module):
    pass


def test_onlineposition():
    onlineposition = onlinepositions().json()

    assert_equal(1,onlineposition['state'],'在招职位页')