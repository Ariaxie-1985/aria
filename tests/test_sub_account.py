# coding:utf-8
# @Time  : 2018-12-26 15:37
# @Author: Xiawang

from api_script.business.sub_account import add_sub_account, remove_sub_account, get_userId, reAssignAllGoods, \
	get_user_goods_info, reAssign_subaccount_Goods, get_invalidUserId
from api_script.business.Batch_Allocation import batchAllocate,batch_allocation
from util.util import login, assert_equal
import logging

'''
验证子账号的添加, 权益调整, 移除, 无效后再恢复, 调整为分账号
'''


username = 20181205
login("00852", username)
userlist = get_userId()
invalidUserId = get_invalidUserId()
userinfolist = get_user_goods_info(userlist)


def test_add_sub_account():
	'''
	测试验证添加子账号是否成功
	:return: Boolean, True表示测试通过, False表示测试失败
	'''
	log = logging.getLogger('test_add_sub_account')
	log.debug('验证添加子账号: '+str(userlist)+'是否成功')
	r = add_sub_account(userlist)
	userId_r = r['content']['data']['data'][0]['userid']
	assert_equal(userlist[0],userId_r,"添加子账号成功, 其userId: "+ str(userId_r),"添加子账号失败, 其响应内容: " + str(r))

def test_Batch_Allocation():
	'''
	批量分配
	:return:
	'''
	batchAllocate()
	batch_allocation()

def test_reAssignAllGoods():
	'''
	调整子账号的权益
	:return: 断言, Boolean, True表示测试通过, False表示测试失败
	'''
	log = logging.getLogger('test_reAssignAllGoods')
	log.debug('验证调整子账号的权益: ' + str(userlist) + ' 是否成功')
	r = reAssignAllGoods(userinfolist)
	assert_equal(1,r['state'],"调整子账号的权益成功, 其userId: "+ str(userlist),"调整子账号的权益失败, 其响应内容: " + str(r))


def test_reAssign_subaccount_Goods():
	'''
	调整子账号为分账号
	:return: 断言, Boolean, True表示测试通过, False表示测试失败
	'''
	log = logging.getLogger('test_reAssign_subaccount_Goods')
	log.debug('验证调整子账号为分账号: ' + str(userlist) + ' 是否成功')
	r = reAssign_subaccount_Goods(userinfolist)
	assert_equal(1,r['state'],"调整子账号为分账号成功, 其userId: "+ str(userlist),"调整子账号为分账号失败, 其响应内容: " + str(r))


def test_recover_sub_account():
	'''
	一键恢复无效子账号
	:return: Boolean, True表示测试通过, False表示测试失败
	'''
	log = logging.getLogger('test_recover_sub_account')
	log.debug('验证一键恢复无效子账号: ' + str(userlist) + ' 是否成功')
	r = reAssign_subaccount_Goods(invalidUserId)
	assert_equal(1, r['state'], "调整子账号为分账号成功, 其userId: " + str(invalidUserId), "调整子账号为分账号失败, 其响应内容: " + str(r))


def test_remove_sub_account():
	'''
	测试验证移除子账号是否成功
	:return: Boolean, True表示测试通过, False表示测试失败
	'''
	log = logging.getLogger('test_remove_sub_account')
	log.debug('验证移除子账号: ' + str(userlist) + '是否成功')
	r = remove_sub_account(userlist)
	assert_equal("删除成功",r['message'],"删除子账号成功, 其userId: "+ str(userlist),"删除子账号失败, 其响应内容: " + str(r))


