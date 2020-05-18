# coding:utf-8
# @Time  : 2019-06-12 12:37
# @Author: Xiawang

from flask_restful import Resource, reqparse
import pymysql

# db = pymysql.connect(
#     host='10.1.200.166',
#     port=3306,
#     user='lagouro',
#     passwd='Q12_#*s#$opIx',
#     db='testing_platform',
#     charset='utf8',
#     cursorclass=pymysql.cursors.DictCursor
# )
# cursor = db.cursor()


# class work_address(Resource):
#     def get(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('address', type=str, help="请输入正确地址", required=True)
#         args = parser.parse_args()
#         db.ping(reconnect=True)
#         cursor.execute(
#             "SELECT id, CONCAT(city,district,detail_address) FROM t_work_address WHERE CONCAT(city,district,detail_address) like '{}%' LIMIT 50".format(
#                 args['address']))
#         results = cursor.fetchall()
#         db.close()
#
#         data = []
#         for address in results:
#             items = {}
#             items['id'] = address['id']
#             items['address'] = address['CONCAT(city,district,detail_address)']
#             data.append(items)
#
#         return {'message': 'success', 'items': data}
