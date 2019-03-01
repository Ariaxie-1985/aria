# coding:utf-8
# @Time  : 2019-02-15 15:57
# @Author: Xiawang

import os
import subprocess

from flask import request
from flask_restful import Resource, reqparse

from utils.analysis_html_report import analysis_html_report


class run_Pytest(Resource):
    def post(self):
        '''对外接口: 执行pytest
        :arg
            module: str, 固定值: business, jianzhao_web, zhaopin, ALL

        :return: {'state':state,"content":info}
        '''

        parser = reqparse.RequestParser()
        parser.add_argument('module', type=str, choices=('business', 'jianzhao_web', 'zhaopin', 'ALL'),
                            help="请输入正确模块值: 'business' or 'jianzhao_web' or 'zhaopin' or 'ALL'", required=True)
        args = parser.parse_args()
        project_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        os.chdir(project_path)
        if args['module'] == "business":
            subprocess.call("sh {}/run_business.sh".format(project_path), shell=True)
            result = analysis_html_report("{}/htmlreport/report.html".format(project_path), 1)
            state = 1
            info = {"result": result}
        elif args['module'] == 'jianzhao_web':
            subprocess.call("sh {}/run_jianzhao_web.sh".format(project_path), shell=True)
            result = analysis_html_report("htmlreport/report.html", 1)
            state = 1
            info = {"result": result}
        elif args['module'] == 'zhaopin':
            subprocess.call("sh {}/run_zhaopin.sh".format(project_path), shell=True)
            result = analysis_html_report("htmlreport/report.html", 1)
            state = 1
            info = {"result": result}
        elif args['module'] == "ALL":
            subprocess.call("sh {}/run.sh".format(project_path), shell=True)
            result = analysis_html_report("htmlreport/report.html", 1)
            state = 1
            info = {"result": result}
        else:
            state = 404
            info = {"error": "字段 module 的值传参错误, 请在此列表选择['business', 'jianzhao_web', 'zhaopin', 'ALL']"}

        return {'state': state, "content": info}
