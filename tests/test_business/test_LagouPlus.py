# coding:utf-8
# @Time  : 2019-01-27 16:22
# @Author: cloudyyuan
from api_script.business.LagouPlus import lagouPlusqiu,lagouPlus
from utils.util import login_home,get_code_token,form_post,get_header,get_requests,assert_equal
import json
def setup_module(module):
    pass


def teardown_module(module):
    pass


def test_lagouPlus(login_home_k8s_env_b):
    '''
    终止当前套餐
    新增17套餐
    查看套餐是否正常
    :return:
    '''
    lagouPlus()

def test_lagouPlusqiu():
    '''
    终止当前套餐
    新增18套餐
    查看套餐是否正常
    :return:
    '''
    lagouPlusqiu()
