# coding:utf-8
# @Time  : 2019-02-15 15:32
# @Author: Xiawang
from flask import request
from flask_restful import Resource, reqparse

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
			state : 1成功、 400失败
			{"state":1,"message": "发布职位" + str(j) + "个成功", "content": successlist, "failinfo": failinfo}
		"""
		j = 0
		successlist = []
		failinfo = [None]
		data = {}
		parser = reqparse.RequestParser()
		parser.add_argument('countrycode',type=str,help="请输入用户手机号的归属区号",required=True)
		parser.add_argument('username', type=str, help="请输入用户的手机号",required=True)
		parser.add_argument('sum', type=int, help="请输入发布职位的数量",required=True)
		args = parser.parse_args()
		login_res = login(args['countrycode'], args['username'])
		if login_res['state'] != 1:
			return {"message": login_res['message']}
		result = post_position(args['sum'])

		state = 0
		for i in result:
			if i['state'] == 1:
				j += 1
				data["position_name"] = i['content']['data']['onlinehunting_position_name']
				data["parentPositionId"] = i['content']['data']['parentPositionInfo']['parentPositionId']
				data["positionId"] = i['content']['data']['parentPositionInfo']['positionChannelInfoList'][0][
					'positionId']
				successlist.append(data)
				data = {}
				state =1
			else:
				data['state'] = i['state']
				data['message'] = i['message']
				failinfo.append(data)
				data = {}
				state = 400

		return {"state":state, "message": "发布职位"+str(args['sum'])+"个, 其中" + str(j) + "个成功", "content": successlist, "failinfo": failinfo}

