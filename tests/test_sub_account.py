# coding:utf-8
# @Time  : 2018-12-26 15:37
# @Author: Xiawang

from api_script.business.sub_account import add_sub_account, remove_sub_account, get_userId
from util.util import login, assert_equal
import logging

'''
验证子账号的添加, 权益调整, 移除, 无效后再恢复, 调整为分账号
'''
username = 20181205
login("00852", username)

userId = get_userId()


def test_add_sub_account():
	'''
	测试验证添加子账号是否成功
	:return: Boolean, True表示测试通过, False表示测试失败
	'''
	log = logging.getLogger('test_add_sub_account')
	log.debug('验证添加子账号: '+str(userId)+'是否成功')
	r = add_sub_account(userId)
	userId_r = r['content']['data']['data'][0]['userid']
	assert_equal(userId,userId_r,"添加子账号成功, 其userId: "+ str(userId_r),"添加子账号失败, 其响应内容: " + str(r))



def test_remove_sub_account():
	'''
	测试验证移除子账号是否成功
	:return: Boolean, True表示测试通过, False表示测试失败
	'''
	log = logging.getLogger('test_add_sub_account')
	log.debug('验证移除子账号: ' + str(userId) + '是否成功')
	r = remove_sub_account(userId)
	assert_equal(r['message'],"删除成功","删除子账号成功, 其userId: "+ str(userId),"删除子账号失败, 其响应内容: " + str(r))


