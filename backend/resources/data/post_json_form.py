# coding:utf-8
# @Time  : 2020/12/28 16:38
# @Author: Xiawang
# Description:
import random

from flask_restful import Resource, reqparse


class post_Json(Resource):
    """发布职位"""

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('firstType', type=str, help="请输入职位的一级类别", default="市场|商务类")
        parser.add_argument('positionType', help="请输入职位的二级类别", default="市场|营销")
        parser.add_argument('positionThirdType', type=str, help="请输入职位的三级类别", default="市场营销")
        parser.add_argument('positionName', default="高级市场营销经理", type=str, help="职位名称")
        parser.add_argument('workAddress', type=str, help="工作地址", required=True)
        args = parser.parse_args()

        return {
            'state': 1,
            'content': '创建职位成功',
            'data': {
                'positionId': random.randint(1111, 9999),
                'positionName': args['positionName'],
                'firstType': args['firstType'],
                'positionType': args['positionType'],
                'positionThirdType': args['positionThirdType'],
                'workAddress': args['workAddress']
            }
        }
