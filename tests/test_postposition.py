# coding:utf-8
# @Time  : 2018-12-27 14:16
# @Author: Xiawang
import logging

from api_script.jianzhao_web.b_position.B_postposition import post_position
from util.util import login

username = 20181205
login("00852", username)

def test_post_position():
	log = logging.getLogger('test_post_position')
	log.info('验证批量发布职位是否成功')
	r = post_position()
	positiId = r['content']['data']['parentPositionInfo']['parentPositionId']
	assert r['state'] == 1
	if positiId:
		log.info("发布职位成功, 该职位id是 "+str(positiId))
