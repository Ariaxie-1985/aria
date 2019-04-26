# -*- coding:utf8 -*-
__author__ = 'arayang'

from utils.util import assert_equal
import pytest
from api_script.entry.bigcompany.onlineposition import *


def setup_module(module):
    pass


def teardown_module(module):
    pass


def test_onlineposition():
    onlineposition = onlinepositions().json()

    assert_equal(1,r['state'],'在招职位页')