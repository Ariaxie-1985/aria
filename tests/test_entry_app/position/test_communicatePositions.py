# -*- coding: utf8 -*-
__author__ = 'yqzhang'

from utils.util import assert_equal
import pytest
from api_script.entry.position.communicatePositions import *

def setup_module(module):
    pass


def teardown_module(module):
    pass


def test_hrinfo():
    r=communicatePositions()
    assert_equal(1, r['state'], "查询在招职位成功")