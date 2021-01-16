# coding:utf-8
# @Time  : 2020/12/28 16:24
# @Author: Xiawang
# Description:
from flask import render_template, make_response
from flask_restful import Resource, reqparse



class get_Index(Resource):
    """获取HTM"""
    def get(self):
        # parser = reqparse.RequestParser()
        # parser.add_argument('module', type=str,
        #                     required=True)
        # args = parser.parse_args()
        headers = {'Content-Type': 'text/html'}
        html = 'report0807.html'
        return make_response(render_template(html), 200, headers)