# coding:utf-8
# @Time  : 2019-01-27 16:22
# @Author: cloudyyuan
from api_script.business.Refreshed import Refreshed
from utils.util import login ,get_code_token,form_post,assert_equal
import time

def setup_module(module):
    pass


def teardown_module(module):
    pass

def test_Refreshed(login_web_k8s_env_b):
    '''
    18版合同“刷新职位”
    :return:
    '''
    Refreshed(30)


