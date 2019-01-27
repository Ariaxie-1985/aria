# coding:utf-8
# @Time  : 2019-01-27 16:22
# @Author: cloudyyuan
from api_script.business.LagouPlus import lagouPlusqiu,lagouPlus
from util.util import login_home,get_code_token,form_post,get_header,get_requests,assert_equal
import json
login_home("anan@lagou.com","990eb670f81e82f546cfaaae1587279a")

def test_lagouPlus():
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
