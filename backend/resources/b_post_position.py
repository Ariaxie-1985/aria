# coding:utf-8
# @Time  : 2019-02-15 15:32
# @Author: Xiawang
from flask import request
from flask_restful import Resource

from api_script.batch.B_postposition import post_position
from utils.util import login


class B_Post_Position(Resource):

	# @cross_origin()
	def post(self):
		"""发布职位
		Args:
			countrycode: str, 用户手机号的归属区号
			username: str, 用户手机号
			sum: int, 发布职位总数

		:return:
			{"message": "发布职位" + str(j) + "个成功", "content": successlist, "failinfo": failinfo}
		"""
		j = 0
		successlist = []
		failinfo = [None]
		data = {}
		request_data = request.get_json()
		print(request_data)
		print(type(request_data))
		# if request_data.has_key('countrycode') and request_data.has_key('username') and request_data['sum']:
		login_res = login(request_data['countrycode'], request_data['username'])
		if login_res['state'] != 1:
			return {"message": login_res['message']}
		result = post_position(int(request_data['sum']))

		for i in result:
			if i['state'] == 1:
				j += 1
				data["position_name"] = i['content']['data']['onlinehunting_position_name']
				data["parentPositionId"] = i['content']['data']['parentPositionInfo']['parentPositionId']
				data["positionId"] = i['content']['data']['parentPositionInfo']['positionChannelInfoList'][0][
					'positionId']
				successlist.append(data)
				data = {}
			else:
				data['state'] = i['state']
				data['message'] = i['message']
				failinfo.append(data)
				data = {}

		return {"message": "发布职位" + str(j) + "个成功", "content": successlist, "failinfo": failinfo}
