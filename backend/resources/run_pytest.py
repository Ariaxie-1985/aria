# coding:utf-8
# @Time  : 2019-02-15 15:57
# @Author: Xiawang

import os
import subprocess

from flask import render_template, make_response
from flask_restful import Resource, reqparse
from utils.analysis_html_report import analysis_html_report


class run_Pytest(Resource):

    def get(self):
        '''
        @@@
        ### 对外接口: 获取pytest测试报告


        ### Request Header
        | 字段 | 值 |
        | ---- | ---- |
        | method | GET |
        | Accept | text/html |


        直接在浏览器请求访问即可

        ### 返回
         report html

        '''
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('report.html'), 200, headers)

    def post(self):
        '''
        @@@
        ### 对外接口: 执行pytest


        ### Request Header
        | 字段 | 值 |
        | ---- | ---- |
        | method | POST |
        | content-type | application/json |


        ### 参数

        | 字段 | 必填 | 类型 | 描述|
        | ---- | ---- | ---- | ---- |
        | module | True | string | 选项值, business, jianzhao_web, zhaopin, all |
        |  |  | string | jianzhao_web，简招web |
        |  |  | string | zhaopin， 招聘业务 |
        |  |  | string | business, 商业 |
        |  |  | string | all, 商业 |


        ### 请求示例
        ```json
         {
            "module":"business"
         }
        ```


        ### 返回

        | 字段 | 类型 | 描述|
        | ---- | ---- | ---- | ---- |
        | state | int | 1表示成功, 400表示错误 |
        | data | dict | 构造数据的结果 |
        | result | dict | 测试报告信息 |
        | content | string | 报告生成结果 |
        | info | dict | 报告的具体信息 |
        | time | list | 报告的生成时间 |
        | result | list | 测试用例执行的汇总结果 |


        ### 响应示例
        ```json
        {
            "state": 1,
            "content": {
                "result": {
                    "content": "报告生成成功",
                    "info": {
                        "time": [
                            "Report generated on 03-Mar-2019 at 12:13:05 by pytest-html v1.20.0",
                            "13 tests ran in 87.12 seconds. "
                        ],
                        "result": [
                            [
                                "8 passed",
                                "0 skipped",
                                "5 failed",
                                "0 errors",
                                "0 expected failures",
                                "0 unexpected passes"
                            ],
                            null
                        ]
                    }
                }
            }
        }
        ```

        @@@
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('module', type=str, choices=('business', 'jianzhao_web', 'zhaopin', 'all'),
                            help="请输入正确模块值: 'business' or 'jianzhao_web' or 'zhaopin' or 'all'", required=True)
        args = parser.parse_args()
        project_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        os.chdir(project_path)
        state = 0
        info = None
        if args['module'] == "business":
            subprocess.call("sh {}/run_business.sh".format(project_path), shell=True)
            # subprocess.run("pytest {}/tests/test_business/".format(project_path), shell=True,
            #                stdout=subprocess.PIPE)
            result = analysis_html_report("{}/backend/templates/report.html".format(project_path), 1)
            state = 1
            info = {"result": result}
        elif args['module'] == 'jianzhao_web':
            subprocess.call("sh {}/run_jianzhao_web.sh".format(project_path), shell=True)
            result = analysis_html_report("{}/backend/templates/report.html".format(project_path), 1)
            state = 1
            info = {"result": result}
        elif args['module'] == 'zhaopin':
            subprocess.call("sh {}/run_zhaopin.sh".format(project_path), shell=True)
            result = analysis_html_report("{}/backend/templates/report.html".format(project_path), 1)
            state = 1
            info = {"result": result}
        elif args['module'] == "all":
            subprocess.call("sh {}/run.sh".format(project_path), shell=True)
            result = analysis_html_report("{}/backend/templates/report.html".format(project_path), 1)
            state = 1
            info = {"result": result}

        return {'state': state, "data": info}
