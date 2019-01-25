# coding:utf-8
# @Time  : 2018-12-27 14:16
# @Author: Xiawang
import logging

from api_script.jianzhao_web.b_position.B_postposition import post_position
from api_script.jianzhao_web.resume_manage.candidate import multiChannel_myCompanyParentPositions, can_recommend, \
	can_batch_recommend, can_new_list
from util.util import login, assert_equal

username = 20181205
login("00852", username)


def test_post_position():
	r = post_position()
	positiId = r['content']['data']['parentPositionInfo']['parentPositionId']
	assert_equal(1, r['state'], "发布职位成功, , 该职位id是 " + str(positiId))
