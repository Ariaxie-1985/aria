# coding:utf-8
# @Time  : 2019-02-15 15:52
# @Author: Xiawang
from flask import request
from flask_restful import Resource

from api_script.batch.C_registe_resume import registe_c


class C_Basic_Process(Resource):

	def post(self):
		'''C端注册并生成简历
		Args:
		phone: str, 手机号
		countryCode: str, 地区编号
		userIdentity: int, 1学生, 2非学生
		sum: int, 构造C端账号的数量
		:return: {"content": "成功", "info": "用户手机号为" + str(phone) + "注册成功"+", 且个人基本信息更新成功"}
		'''
		request_data = request.get_json()
		phone = int(request_data['phone'])
		a = 0
		for i in range(request_data['sum']):
			a += 1
			phone += a
			r = registe_c(phone, request_data['countryCode'], request_data['userIdentity'])
			if len(r) == 8:
				[r1, r2, r3, r4, r5, r6, r7, r8] = r
				if r1['state'] == 1 and r2['success'] == r3['success'] == r4['success'] == r5['success'] == r6[
					'success'] == r7[
					'success'] == r8['success']:
					return {"state": 1, "content": "执行成功", "info": "用户手机号为" + str(phone) + "注册成功" + ", 且个人基本信息更新成功"}
			elif len(r) == 7:
				[r1, r2, r4, r5, r6, r7, r8] = r
				if r1['state'] == 1 and r2['success'] == r4['success'] == r5['success'] == r6['success'] == r7[
					'success'] == r8['success']:
					return {"state": 1, "content": "执行成功", "info": "用户手机号为" + str(phone) + "注册成功" + ", 且个人基本信息更新成功"}
			else:
				return {"state": 400, "content": "执行失败",
				        "info": {"注册用户": r1['message'], "基本信息": r2['msg'], "工作经历": r3['msg'], "教育经历": r4['msg'],
				                 "个人名片": r5['msg'], "求职意向": r6['msg'], "完善信息": r8['msg']}}
