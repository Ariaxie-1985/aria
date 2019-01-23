# coding:utf-8
# @Time  : 2019-01-09 16:35
# @Author: Xiawang

from flask import request
from flask_restful import Resource

from api_script.jianzhao_web.b_basic.home_review_company_4 import passCompanyApprove
from api_script.jianzhao_web.b_basic.home_review_person_2 import passPersonApprove
from api_script.jianzhao_web.b_basic.toB_comleteInfo_3 import completeInfo_process
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import saveHR_process
from api_script.batch.B_postposition import post_position
from api_script.batch.C_registe_resume import registe_c
from util.util import login, login_home


class HelloWorld(Resource):
	def get(self):
		return {'hello': 'world'}


class B_Post_Position(Resource):

	def post(self):
		j = 0
		successlist = []
		failinfo = [None]
		data = {}
		request_data = request.get_json()
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


class B_Basic_Process(Resource):

	def post(self):
		'''
		B端注册-公司成立-招聘者认证提交及审核-公司认证及审核流程

		:return:
		'''
		HRInfo = {}
		CompanyInfo = {}
		ApproveInfo = {}
		Application = {}
		request_data = request.get_json()
		try:
			[r1, r2, r3, r4] = saveHR_process(request_data['phone'],
			                                  request_data['countryCode'],
			                                  request_data['companyShortName'],
			                                  request_data['companyFullName'],
			                                  request_data['userName'],
			                                  request_data['resumeReceiveEmail'],
			                                  request_data['updateCompanyShortName'])
			if r1['state'] == r2['state'] == r3['state'] == r4['state'] == 1:
				HRInfo['phone'] = request_data['phone']
				HRInfo['countryCode'] = request_data['countryCode']
				CompanyInfo['companyShortName'] = request_data['companyShortName']
				CompanyInfo['companyFullName'] = request_data['companyFullName']
			login_home("anan@lagou.com", "990eb670f81e82f546cfaaae1587279a")
			r5 = passPersonApprove()
			login(request_data['countryCode'], request_data['phone'])
			[r6, r7] = completeInfo_process()
			if r4['state'] == r7['state'] == 1:
				Application['person'] = "招聘者申请认证成功"
				Application['company'] = "公司申请认证成功"
			login_home("anan@lagou.com", "990eb670f81e82f546cfaaae1587279a")
			r8 = passCompanyApprove()
			if r5['success'] == True and r6['state'] == 1 and r8['success'] == True:
				ApproveInfo['passPersonApprove'] = "招聘者认证提交及审核通过"
				ApproveInfo['passCompanyApprove'] = "公司认证提交及审核通过"
			return {
				"content": "B端注册-公司成立-招聘者认证提交及审核-公司认证及审核流程通过！",
				"data": {"HRInfo": HRInfo, "CompanyInfo": CompanyInfo, "Application": Application,
				         "ApproveInfo": ApproveInfo}
			}
		except Exception as e:
			if r1['state'] != 1:
				info = "该手机号已被注册, 该用户的手机号: " + str(request_data['phone'])
			elif r2['state'] != 1:
				info = "上传B端用户信息失败，该用户的手机号: " + request_data['userName']
			elif r3['state'] != 1:
				info = "B端成立公司失败，该公司简称:" + request_data['companyShortName']
			elif r4['state'] != 1:
				info = "B端提交招聘者审核失败，该公司简称: " + request_data['companyShortName']
			elif r5['success'] != True:
				info = "home后台-审核中心-个人认证-审核招聘者失败, 该公司的简称: " + request_data['companyShortName']
			elif r6['state'] != 1:
				info = "上传营业执照失败, 该公司的简称: " + request_data['companyShortName']
			elif r7['state'] != 1:
				info = "简称为 " + request_data['companyShortName'] + " 申请认证公司失败"
			elif r8['success'] != True:
				info = "home后台-公司认证-审核公司成功！该公司的简称: " + request_data['companyShortName']
			return {"content": "执行失败", "data": str(e), "faiinfo": info}


'''
3.发简历
4.C端注册并生成简历
'''


class C_Basic_Process(Resource):

	def post(self):
		'''
		Args:
		phone: str, 手机号
		countryCode: str, 地区编号
		userIdentity: int, 1学生, 2非学生
		sum: int, 构造C端账号的数量
		:return:
		'''
		request_data = request.get_json()
		phone = int(request_data['phone'])
		a = 0
		for i in range(request_data['sum']):
			a += 1
			phone += a
			r = registe_c(phone, request_data['countryCode'], request_data['userIdentity'])
			print(r)
			if len(r) == 8:
				return {"content": "8组数据"}
			elif len(r) == 7:
				return {"content": "7组数据"}
