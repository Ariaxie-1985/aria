# coding:utf-8
# @Time  : 2019-01-27 16:22
# @Author: cloudyyuan
import json

from api_script.business.Batch_Allocation import batch_allocation, batchAllocate
from api_script.business.sub_account import get_user_goods_info, get_userId
from utils.BeautifulSoup import exist_class_name
from utils.util import login,get_requests,form_post,get_code_token,gethtml,assert_equal
import logging
logging.getLogger().setLevel(logging.INFO)

def setup_module(module):
    login('00852', '20181205')


def teardown_module(module):
    pass

def test_batch_allocation():
    '''
    #查看是否出现可以批量分配
    :return:
    '''
    userinfo = get_userId()
    print(userinfo)

    user_goods_info = get_user_goods_info(userinfo)
    goods_list = user_goods_info[userinfo[0]][2]
    print(goods_list)
    # print(r)

    userId_list = [100014642, 100014643]
    batch_allocation(userId_list)

def test_batchAllocate():
    '''
    1、批量分配
    2、验证是否分配成功
    :return:
    '''
    userinfo = get_userId()
    print(userinfo)

    user_goods_info = get_user_goods_info(userinfo)
    goods_list = user_goods_info[userinfo[0]][2]
    print(goods_list)
    # print(r)

    userId_list = [100014642, 100014643]
    batchAllocate(userId_list, user_goods_info)

