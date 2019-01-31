# coding:utf-8
# @Time  : 2018-12-26 15:37
# @Author: Xiawang
from api_script.business.SwitchingContract import lagouPlus
from api_script.business.sub_account import add_sub_account, remove_sub_account, get_userId, reAssignAllGoods, \
	get_user_goods_info, reAssign_subaccount_Goods, get_invalidUserId, get_subaccunt_goods, recover_sub_account
from api_script.business.Batch_Allocation import batchAllocate, batch_allocation
from utils.util import login
import logging

from utils.util import assert_equal

from utils.read_file import get_yaml_test_data

test_data = get_yaml_test_data("test_sub_account.yaml")

countrycode = test_data['countrycode']
username = test_data['username']
templateId = test_data['templateId']

'''
验证在不同套餐版本下子账号的添加, 权益调整, 移除, 无效后再恢复, 调整为分账号
'''

lagouPlus(templateId)

login(countrycode, username)

userId_list = get_userId()


def test_add_sub_account():
	'''
	测试验证添加子账号是否成功
	:return: Boolean, True表示测试通过, False表示测试失败
	'''
	log = logging.getLogger('test_add_sub_account')
	log.debug('验证添加子账号: ' + str(userId_list) + '是否成功')
	r = add_sub_account(userId_list)
	userId_r = r['content']['data']['data'][0]['userid']
	assert_equal(userId_list[1], userId_r, "添加子账号成功, 其userId: " + str(userId_r), "添加子账号失败, 其响应内容: " + str(r))


userinfolist = get_user_goods_info(userId_list)


def test_reAssignAllGoods():
	'''
	调整子账号的权益
	:return: 断言, Boolean, True表示测试通过, False表示测试失败
	'''
	log = logging.getLogger('test_reAssignAllGoods')
	log.debug('验证调整子账号的权益: ' + str(userId_list) + ' 是否成功')
	r = reAssignAllGoods(userinfolist)
	assert_equal("调整成功", r['message'], "调整子账号的权益成功, 其userId: " + str(userId_list), "调整子账号的权益失败, 其响应内容: " + str(r))


def test_reAssign_subaccount_Goods():
	'''
	调整子账号为分账号
	:return: 断言, Boolean, True表示测试通过, False表示测试失败
	'''
	subaccunt_goodslist = get_subaccunt_goods(userId_list)
	log = logging.getLogger('test_reAssign_subaccount_Goods')
	log.debug('验证调整子账号为分账号: ' + str(userId_list) + ' 是否成功')
	r = reAssign_subaccount_Goods(subaccunt_goodslist)
	assert_equal("调整成功", r['message'], "调整子账号为分账号成功, 其userId: " + str(userId_list), "调整子账号为分账号失败, 其响应内容: " + str(r))


def test_Batch_Allocation():
	'''
	批量分配
	:return:
	'''
	batchAllocate(userId_list, userinfolist)
	batch_allocation(userId_list)


def test_recover_sub_account():
	'''
	一键恢复无效子账号
	:return: Boolean, True表示测试通过, False表示测试失败
	'''
	# todo 待与杨振宇(Antonyyang)沟通
	lagouPlus(templateId)
	login(countrycode, username)
	invalidUserId = get_invalidUserId()
	r = recover_sub_account(invalidUserId)
	assert_equal(1, r['state'], "调整子账号为分账号成功, 其userId: " + str(invalidUserId), "调整子账号为分账号失败, 其响应内容: " + str(r))


def test_remove_sub_account():
	'''
	测试验证移除子账号是否成功
	:return: Boolean, True表示测试通过, False表示测试失败
	'''
	log = logging.getLogger('test_remove_sub_account')
	log.debug('验证移除子账号: ' + str(userId_list) + '是否成功')
	r = remove_sub_account(userId_list)
	assert_equal("删除成功", r['message'], "删除子账号成功, 其userId: " + str(userId_list), "删除子账号失败, 其响应内容: " + str(r))
