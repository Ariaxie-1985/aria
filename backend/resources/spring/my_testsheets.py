# # coding:utf-8
# # @Time  : 2019-09-11 11:02
# # @Author: Xiawang
# # Description:
# from flask_restful import Resource, reqparse
#
# from backend.common.extensions import convert_json
# from backend.common.new_models import User, TestSheet
# from backend.common.response_structure import ResponseStructure
# from backend.common.state import Results, ResponseCode
#
#
# class MyTestSheets(Resource):
#
#     def get(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('TOKEN', type=str, location='headers')
#         args = parser.parse_args()
#         user = User.verify_auth_token(args['TOKEN'])
#         if not user:
#             return Results().get(ResponseCode.FAIL_LOGIN_AUTH)
#         results = TestSheet.get_or_none(TestSheet.qa_id == user.id, TestSheet.status=='待部署')
#         if results is None:
#             return Results().get(ResponseCode.SUCCESS)
#         result_data = Results().set_data()
#         results = TestSheet.select().where(TestSheet.qa_id == user.id, TestSheet.status == '待部署').order_by(
#             TestSheet.create_time.desc())
#
#         for result in results:
#             testsheet_data = convert_json(TestSheet, result.id)
#             ResponseStructure().set_username(data=testsheet_data, id=testsheet_data['qa_id'],
#                                              user='qa_name')
#             ResponseStructure().set_username(data=testsheet_data, id=testsheet_data['backend_id'],
#                                              user='backend_name')
#             ResponseStructure().set_username(data=testsheet_data, id=testsheet_data['front_id'], user='front_name')
#             result_data.append(testsheet_data)
#
#         return Results().get(ResponseCode.SUCCESS, data=result_data)
