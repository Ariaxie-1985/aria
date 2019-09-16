# coding:utf-8
# @Time  : 2019-07-25 21:37
# @Author: Xiawang

from flask_restful import Resource


class helloWorld(Resource):

    def get(self):
        return {'Say': "Hello, World"}




