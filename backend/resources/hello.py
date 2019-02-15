# coding:utf-8
# @Time  : 2019-02-15 15:42
# @Author: Xiawang
from flask_restful import Resource


class HelloWorld(Resource):
	def get(self):
		'''首页

		:return: {'hello': 'world'}
		'''
		return {'hello': 'world'}