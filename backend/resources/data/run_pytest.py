# coding:utf-8
# @Time  : 2019-02-15 15:57
# @Author: Xiawang

import os
import subprocess

from flask import render_template, make_response
from flask_restful import Resource, reqparse
from utils.analysis_html_report import analysis_html_report


class run_Pytest(Resource):
    """执行pytest"""
    Business_module = {
        'business': "/root/.local/bin/pipenv run pytest {}/tests/test_business/ --html=backend/templates/{}_report.html --self-contained-html",
        'jianzhao_web': '/root/.local/bin/pipenv run pytest {}/tests/test_jianzhao_web/ --html=backend/templates/{}_report.html --self-contained-html',
        'zhaopin': '/root/.local/bin/pipenv run pytest {}/tests/test_zhaopin_app/ --html=backend/templates/{}_report.html --self-contained-html',
        'entry_app': '/root/.local/bin/pipenv run pytest {}/tests/test_entry_app/ --html=backend/templates/{}_report.html --self-contained-html',
        'all': '/root/.local/bin/pipenv run pytest {}/ --html=backend/templates/{}_report.html --self-contained-html',
        'neirong_app': '/root/.local/bin/pipenv run pytest {}/tests/test_neirong_app/ --html=backend/templates/{}_report.html --self-contained-html',
        'mainprocess': 'pytest {}/tests/test_mainprocess/ --html=backend/templates/{}_report.html --self-contained-html',

    }

    def get(self):
        '''获取pytest测试报告
        @@@
        ### 对外接口: 获取pytest测试报告

        ### Author = Xiawang

        ### Request Header
        | 字段 | 值 |
        | ---- | ---- |
        | method | GET |
        | Accept | text/html |


        ### 参数

        | 字段 | 必填 | 类型 | 描述|
        | ---- | ---- | ---- | ---- |
        | module | True | string | 选项值, business, jianzhao_web, zhaopin, all |
        |  |  | string | jianzhao_web，简招web |
        |  |  | string | zhaopin， 招聘业务 |
        |  |  | string | business, 商业业务 |
        |  |  | string | entry_app, app端的入口业务 |
        |  |  | string | neirong_app, app端的内容业务 |
        |  |  | string | all, 全部业务 |


        ### 请求示例--直接在浏览器请求访问
        ```json
        http://127.0.0.1:9004/pytest?module=business

        http://127.0.0.1:9004/pytest?module=jianzhao_web

        http://127.0.0.1:9004/pytest?module=zhaopin
        ```

        ### 返回
         report html

        '''
        parser = reqparse.RequestParser()
        parser.add_argument('module', type=str,
                            choices=('business', 'jianzhao_web', 'zhaopin', 'all', 'entry_app', 'mainprocess'),
                            help="请输入正确模块值: 'business' or 'jianzhao_web' or 'zhaopin' or 'all'", required=True)
        args = parser.parse_args()
        headers = {'Content-Type': 'text/html'}
        html = '{}_report.html'.format(args['module'])
        return make_response(render_template(html), 200, headers)

    def post(self):
        '''执行pytest
        @@@
        ### 对外接口: 执行pytest

        ### Author = Xiawang

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
        |  |  | string | business, 商业业务 |
        |  |  | string | entry_app, app端的入口业务 |
        |  |  | string | neirong_app, app端的内容业务 |
        |  |  | string | all, 全部业务 |


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
        parser.add_argument('module', type=str,
                            choices=('business', 'jianzhao_web', 'zhaopin', 'all', 'entry_app', 'mainprocess'),
                            help="请输入正确模块值: 'business' or 'jianzhao_web' or 'zhaopin' or 'all'", required=True)
        args = parser.parse_args()
        project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        os.chdir(project_path)
        state = 1
        info = None
        subprocess.call(self.Business_module[args['module']].format(project_path, args['module']), shell=True)
        result = analysis_html_report("{}/backend/templates/{}_report.html".format(project_path, args['module']), 3)
        if bool(result['info']['result']['fail_result']):
            state = 0
        info = {"result": result}
        return {'state': state, "data": info}
