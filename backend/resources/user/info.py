# # coding:utf-8
# # @Time  : 2019-09-11 10:41
# # @Author: Xiawang
# # Description:
# from flask_restful import Resource, reqparse
#
# from backend.common.new_models import User
# from backend.common.state import ResponseCode, Results
#
#
# class Info(Resource):
#
#     def get(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('TOKEN', type=str, location='headers')
#         args = parser.parse_args()
#         user = User.verify_auth_token(args['TOKEN'])
#         if not user:
#             return Results().get(ResponseCode.FAIL_LOGIN_AUTH)
#         return Results().get(ResponseCode.SUCCESS, data={'id': user.id})
