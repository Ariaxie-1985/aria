# coding:utf-8
# @Time  : 2018-12-27 14:16
# @Author: Xiawang
import logging
import time
import pytest
from api_script.business.SwitchingContract import lagouPlus
from api_script.jianzhao_web.b_position.B_postposition import post_position, myOnlinePositions
from utils.util import login, assert_equal


def setup_module(module):
	pass


def teardown_module(module):
	pass


def test_post_position(login_web_k8s_default):
	r = post_position()
	positiId = r['content']['data']['parentPositionInfo']['parentPositionId']
	assert_equal(1, r['state'], "发布职位成功, , 该职位id是 " + str(positiId))


@pytest.mark.skip(reason="没写完，先跳过")
def test_myOnlinePositions(pageNo):
	res = myOnlinePositions(pageNo)


