# coding:utf-8
# @Time  : 2019-01-27 16:22
# @Author: cloudyyuan
import pytest

from api_script.business.Akeytorefresh import akeyRefresh, Refreshed

from utils.util import login


def setup_module(module):
    pass


def test_akeyRefresh(login_web_k8s_env_b):
    ''''
    获取第二个职位进行一键刷新
    '''

    akeyRefresh(30)


def test_Refreshed():
    '''
    18版合同“一键刷新”
    刷新所有职位，包括已经刷新过一次的
    :return:
    '''
    Refreshed(30)


def teardown_module(module):
    pass
