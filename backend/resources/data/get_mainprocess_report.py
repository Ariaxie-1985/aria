# coding:utf-8
# @Time  : 2019-11-20 16:14
# @Author: Xiawang
# Description:
import os
from flask_restful import Resource, reqparse

from utils.analysis_html_report import analysis_html_report


class GetReport(Resource):
    """执行主流程测试"""


    def get(self):
        '''获取pytest测试报告
        ### 返回 json格式的主流程测试报告
        '''
        project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        os.chdir(project_path)
        result = analysis_html_report("{}/backend/templates/mainprocess_report.html".format(project_path), 3)
        result = {**{'state': 1}, **result}
        return result
