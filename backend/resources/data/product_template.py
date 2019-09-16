# coding:utf-8
# @Time  : 2019-07-24 16:59
# @Author: Xiawang
from flask_restful import Resource, reqparse

from backend.common.get_product_template import get_product_template


class productTemplate(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help="请输入正确模板名称", required=True)
        args = parser.parse_args()

        product_template_list = get_product_template(args['name'])
        return {'message': 'success', 'items': product_template_list}
