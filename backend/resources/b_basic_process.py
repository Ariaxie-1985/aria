# coding:utf-8
# @Time  : 2019-02-15 15:44
# @Author: Xiawang
from flask import request
from flask_restful import Resource, reqparse

from api_script.jianzhao_web.b_basic.home_review_company_4 import passCompanyApprove
from api_script.jianzhao_web.b_basic.home_review_person_2 import passPersonApprove
from api_script.jianzhao_web.b_basic.toB_comleteInfo_3 import completeInfo_process
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import saveHR_process
from utils.util import login_home, login


class B_Basic_Process(Resource):

	def post(self):
		""" B端注册-公司成立-招聘者认证提交及审核-公司认证及审核流程

		:arg:
		{
			"countryCode": "00852",             // string, B端注册用户手机号的地区编号
			"phone": "20030902",                // string, B端注册用户的手机号
			"userName": "小菜",                  // string, B端注册用户的姓名
			"companyShortName": "烽火啊啊啊",     // string, B端注册公司的简称
			"companyFullName": "烽火啊啊啊",      // string, B端注册公司的全称
			"updateCompanyShortName": "烽火啊啊啊",  // string, B端注册公司的别称
			"resumeReceiveEmail": "tester2018@sina.com"  // string, B端注册用户接收简历的邮箱
		}


		:return:
		{
			"state": 1,     // int, 1表示成功, 400表示错误
			"content": "B端注册-公司成立-招聘者认证提交及审核-公司认证及审核流程通过！",
			"data": {
				"HRInfo": {                 // 招聘者信息
					"phone": "20030902",
					"countryCode": "00852"
				},
				"CompanyInfo": {            // 公司信息
					"companyShortName": "公司简称",
					"companyFullName": "公司全称"
				},
				"Application": {            // 招聘者和公司的认证的申请结果
					"person": "招聘者申请认证成功",
					"company": "公司申请认证成功"
				},
				"ApproveInfo": {            // 招聘者和公司的认证的审核结果
					"passPersonApprove": "公司认证提交及审核通",
					"passCompanyApprove": "招聘者认证提交及审核通过"
				}
			}
		}
		"""

		parser = reqparse.RequestParser()
		parser.add_argument('countryCode', type=str, help="请输入B端注册用户手机号的归属区号", required=True)
		parser.add_argument('phone', type=str, help="请输入B端注册用户的手机号", required=True)
		parser.add_argument('userName', type=str, help="请输入B端注册用户的姓名", required=True)
		parser.add_argument('resumeReceiveEmail', type=str, help="请输入接收简历的邮箱地址", required=True)
		parser.add_argument('companyShortName', type=str, help="请输入注册公司的简称", required=True)
		parser.add_argument('companyFullName', type=str, help="请输入注册公司的全称", required=True)
		parser.add_argument('updateCompanyShortName', type=str, help="请输入注册公司的别称", required=True)
		args = parser.parse_args()
		HRInfo = {}
		CompanyInfo = {}
		ApproveInfo = {}
		Application = {}
		info = None
		r1, r2, r3, r4 = saveHR_process(args['phone'],
		                                args['countryCode'],
		                                args['companyShortName'],
		                                args['companyFullName'],
		                                args['userName'],
		                                args['resumeReceiveEmail'],
		                                args['updateCompanyShortName'])
		state = 0
		if r1['state'] != 1:
			state = 400
			info = "该手机号已被注册, 该用户的手机号: " + args['phone']
		elif r2['state'] != 1:
			state = 400
			info = "上传B端用户信息失败，该用户的手机号: " + args['userName']
		elif r3['state'] != 1:
			state = 400
			info = "B端成立公司失败，该公司简称:" + args['companyShortName']
		elif r4['state'] != 1:
			state = 400
			info = "B端提交招聘者审核失败，该公司简称: " + args['companyShortName']

		if not (state == 400):
			if r1['state'] == r2['state'] == r3['state'] == r4['state'] == 1:
				state = 3
				HRInfo['phone'] = args['phone']
				HRInfo['countryCode'] = args['countryCode']
				CompanyInfo['companyShortName'] = args['companyShortName']
				CompanyInfo['companyFullName'] = args['companyFullName']

			login_home("anan@lagou.com", "990eb670f81e82f546cfaaae1587279a")
			r5 = passPersonApprove()
			if r5['success'] != True:
				state = 400
				info = "home后台-审核中心-个人认证-审核招聘者失败, 该公司的简称: " + args['companyShortName']

			login(args['countryCode'], args['phone'])
			[r6, r7] = completeInfo_process()
			if r6['state'] != 1:
				state = 400
				info = "上传营业执照失败, 该公司的简称: " + args['companyShortName'] + "，"
			elif r7['state'] != 1:
				state = 400
				info = "简称为 " + args['companyShortName'] + " 申请认证公司失败"
			if not (state == 400):
				if r4['state'] == r7['state'] == 1:
					Application['person'] = "招聘者申请认证成功"
					Application['company'] = "公司申请认证成功"
					state = 2

				login_home("anan@lagou.com", "990eb670f81e82f546cfaaae1587279a")
				r8 = passCompanyApprove()
				if r8['success'] != True:
					state = 400
					info = "home后台-公司认证-审核公司成功！该公司的简称: " + args['companyShortName']

				if r5['success'] == True and r6['state'] == 1 and r8['success'] == True:
					ApproveInfo['passPersonApprove'] = "招聘者认证提交及审核通过"
					ApproveInfo['passCompanyApprove'] = "公司认证提交及审核通过"
					state = 1

		if state == 1:
			return {
				"state": 1,
				"content": "B端注册-公司成立-招聘者认证提交及审核-公司认证及审核流程通过！",
				"data": {"HRInfo": HRInfo, "CompanyInfo": CompanyInfo, "Application": Application,
				         "ApproveInfo": ApproveInfo}
			}
		return {"state": 400, "content": "执行失败", "faiinfo": info}


