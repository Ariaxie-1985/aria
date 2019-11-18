# # coding:utf-8
# # @Time  : 2019-04-02 11:29
# # @Author: Xiawang
# from backend.OperationMysql import OperationMysql
#
# op_mysql = OperationMysql()
# from flask_restful import Resource, reqparse
#
#
# class getUserId(Resource):
#     """ 获取用户id """
#
#     def get(self):
#
#         parser = reqparse.RequestParser()
#         parser.add_argument('phone', type=str, help="请输入正确手机号", required=True)
#         args = parser.parse_args()
#         try:
#             userid = op_mysql.search_all("SELECT userId FROM r_resume where phone = %s" % args['phone'])
#             state = 1
#             info = userid[0]
#         except:
#             state = 400
#             info = "找不到userId, 请确认下手机号填写是否正确"
#         return {'state': state, 'content': info}
