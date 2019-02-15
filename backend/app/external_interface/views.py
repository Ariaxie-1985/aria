# coding:utf-8
# @Time  : 2019-02-15 10:30
# @Author: Xiawang
import os
import subprocess

from flask import request
from flask_restful import Resource

from utils.analysis_html_report import analysis_html_report


class run_Pytest(Resource):
	def post(self):
		'''对外接口: 执行pytest
		:arg
			module: str, 固定值: business, jianzhao_web, zhaopin, ALL

		:return: {'state':state,"content":info}
		'''
		request_data = request.get_json()
		retval = os.getcwd()
		index_num = retval.find('lg_api_script')
		retval = retval[:index_num + 13]
		os.chdir(retval)
		if request_data.has_key('module'):
			module = request_data['module']
		else:
			state = 404
			info = {"error": "字段 module 的值传参错误, 请在此列表选择['business', 'jianzhao_web', 'zhaopin', 'ALL']"}

		if module == "business":
			subprocess.call("sh run_business.sh", shell=True)
			result = analysis_html_report("htmlreport/report.html", 1)
			state = 1
			info = {"result": result}
		elif module == 'jianzhao_web':
			subprocess.call("sh run_jianzhao_web.sh", shell=True)
			result = analysis_html_report("htmlreport/report.html", 1)
			state = 1
			info = {"result": result}
		elif module == 'zhaopin':
			subprocess.call("sh run_zhaopin.sh", shell=True)
			result = analysis_html_report("htmlreport/report.html", 1)
			state = 1
			info = {"result": result}
		elif module == "ALL":
			subprocess.call("sh run.sh", shell=True)
			result = analysis_html_report("htmlreport/report.html", 1)
			state = 1
			info = {"result": result}
		else:
			state = 404
			info = {"error": "字段 module 的值传参错误, 请在此列表选择['business', 'jianzhao_web', 'zhaopin', 'ALL']"}
		return {'state': state, "content": info}
