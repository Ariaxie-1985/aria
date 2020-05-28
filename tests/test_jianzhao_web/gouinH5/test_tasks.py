# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from api_script.jianzhao_web.gouinH5.tasks import tasks

from utils.util import login, assert_equal
import pytest
def setup_module(module):
    pass


def teardown_module(module):
    pass
@pytest.mark.skip(reason="有问题, 暂不执行")
def test_tasks():
    r=tasks()

    assert_equal(1, r['state'], "任务中心首页请求成功")

