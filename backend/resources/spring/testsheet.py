# coding:utf-8
# @Time  : 2019-08-03 23:50
# @Author: Xiawang
import time

from flask_restful import Resource, reqparse
from common.authentication import auth
from common.response_structure import ResponseStructure
from common.state import ResponseCode, Results
from common.verify_ import verify_user, verify_negative_number, verify_title
from common.new_models import TestSheet, User
from common.extensions import convert_json
from common.page import Page


class SprintTestSheet(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, default='')
        parser.add_argument('name', type=str, default='')
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=10)
        parser.add_argument('TOKEN', location='headers', type=str)
        args = parser.parse_args()
        user = User.verify_auth_token(args['TOKEN'])
        if not user:
            return Results().get(ResponseCode.FAIL_LOGIN_AUTH)

        pageNo = verify_negative_number(args['page'], 1)
        per_page = verify_negative_number(args['per_page'], 10)
        user_id = verify_user(args['name'])
        result_data = Results().set_data()
        total_count = 0
        if user_id is None and (args['title'] == '' or args['title'] is None):
            for t in TestSheet.select().order_by(TestSheet.create_time.desc()).paginate(pageNo, per_page):
                testsheet_data = convert_json(TestSheet, t.id)
                ResponseStructure().set_username(data=testsheet_data, id=testsheet_data['qa_id'],
                                                 user='qa_name')
                ResponseStructure().set_username(data=testsheet_data, id=testsheet_data['backend_id'],
                                                 user='backend_name')
                ResponseStructure().set_username(data=testsheet_data, id=testsheet_data['front_id'], user='front_name')
                result_data.append(testsheet_data)

            total_count = TestSheet.select().count()

        if user_id and args['title']:
            for t in TestSheet.select().join(User).where(TestSheet.title % '%{}%'.format(args['title']),
                                                         User.id == user_id).order_by(
                TestSheet.create_time.desc()).paginate(pageNo, per_page):
                testsheet_data = convert_json(TestSheet, t.id)
                ResponseStructure().set_username(data=testsheet_data, id=testsheet_data['qa_id'],
                                                 user='qa_name')
                ResponseStructure().set_username(data=testsheet_data, id=testsheet_data['backend_id'],
                                                 user='backend_name')
                ResponseStructure().set_username(data=testsheet_data, id=testsheet_data['front_id'], user='front_name')
                result_data.append(testsheet_data)
            total_count = TestSheet.select().join(User).where(TestSheet.title % '%{}%'.format(args['title']),
                                                              User.username == args['name']).count()

        if args['title'] and not args['name']:
            for t in TestSheet.select().where(TestSheet.title % '%{}%'.format(args['title'])).order_by(
                    TestSheet.create_time.desc()).paginate(pageNo, per_page):
                testsheet_data = convert_json(TestSheet, t.id)
                ResponseStructure().set_username(data=testsheet_data, id=testsheet_data['qa_id'],
                                                 user='qa_name')
                ResponseStructure().set_username(data=testsheet_data, id=testsheet_data['backend_id'],
                                                 user='backend_name')
                ResponseStructure().set_username(data=testsheet_data, id=testsheet_data['front_id'], user='front_name')
                result_data.append(testsheet_data)
            total_count = TestSheet.select().where(TestSheet.title % args['title']).count()

        if user_id and not args['title']:
            for t in TestSheet.select().where(
                    (TestSheet.qa_id == user_id) | (TestSheet.backend_id == user_id) | (
                            TestSheet.front_id == user_id)).order_by(
                TestSheet.create_time.desc()).paginate(pageNo, per_page):
                testsheet_data = convert_json(TestSheet, t.id)
                ResponseStructure().set_username(data=testsheet_data, id=testsheet_data['qa_id'],
                                                 user='qa_name')
                ResponseStructure().set_username(data=testsheet_data, id=testsheet_data['backend_id'],
                                                 user='backend_name')
                ResponseStructure().set_username(data=testsheet_data, id=testsheet_data['front_id'], user='front_name')
                result_data.append(testsheet_data)
            total_count = TestSheet.select().where((TestSheet.qa_id == user_id) | (TestSheet.backend_id == user_id) | (
                    TestSheet.front_id == user_id)).count()

        total_page_count = Page().get_total_page_count(total_count, per_page)
        is_has_next_page, is_has_previous_page = Page().verify_previous_page_and_next_page(pageNo, total_page_count)
        page_result = Page().pagination(currentPageNo=args['page'], hasNextPage=is_has_next_page,
                                        hasPreviousPage=is_has_previous_page,
                                        totalCount=total_count, totalPageCount=total_page_count)
        return Results().get(ResponseCode.SUCCESS_GET_TESTSHEET, data=result_data, page_result=page_result)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='请输入迭代名')
        parser.add_argument('be', type=str, default="", help='请输入后端开发负责人姓名')
        parser.add_argument('be_remark', type=str, default="")
        parser.add_argument('fe', type=str, default="", help='请输入前端开发负责人姓名')
        parser.add_argument('fe_remark', type=str, default="")
        parser.add_argument('qa', type=str, required=True, help='请输入测试负责人姓名')
        parser.add_argument('remark', type=str, default="")
        parser.add_argument('TOKEN', location='headers', type=str)
        args = parser.parse_args()
        user = User.verify_auth_token(args['TOKEN'])
        if not user:
            return Results().get(ResponseCode.FAIL_LOGIN_AUTH)
        if (verify_user(args['be']) or verify_user(args['fe'])) and verify_user(args['qa']):
            be_id, fe_id, qa_id = verify_user(args['be']), verify_user(args['fe']), verify_user(
                args['qa'])
        else:
            return Results().get(ResponseCode.FAIL_FIND_USER)

        testsheet_id = TestSheet.insert(title=args['name'], qa_id=qa_id, backend_id=be_id,
                                        backend_content=args['be_remark'],
                                        front_id=fe_id, front_content=args['fe_remark'],
                                        content=args['remark']).execute()
        testsheet_data = convert_json(TestSheet, testsheet_id)
        return Results().get(ResponseCode.SUCCESS_CREATE_TESTSHEET, testsheet_data)

    @auth.login_required
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='请输入迭代Id')
        parser.add_argument('name', type=str, required=True, help='请输入迭代名')
        parser.add_argument('be', type=str, default="", help='请输入后端开发负责人姓名')
        parser.add_argument('be_remark', type=str, default="")
        parser.add_argument('fe', type=str, default="", help='请输入前端开发负责人姓名')
        parser.add_argument('fe_remark', type=str, default="")
        parser.add_argument('qa', type=str, required=True, help='请输入测试负责人姓名')
        parser.add_argument('remark', type=str, default="")
        parser.add_argument('TOKEN', location='headers', type=str)
        args = parser.parse_args()
        user = User.verify_auth_token(args['TOKEN'])
        if not user:
            return Results().get(ResponseCode.FAIL_LOGIN_AUTH)
        if (verify_user(args['be']) or verify_user(args['fe'])) and verify_user(args['qa']):
            be_id, fe_id, qa_id = verify_user(args['be']), verify_user(args['fe']), verify_user(
                args['qa'])
        else:
            return Results().get(ResponseCode.FAIL_FIND_USER)

        testsheet = TestSheet.update({TestSheet.title: args['name'], TestSheet.backend_id: be_id,
                                      TestSheet.backend_content: args['be_remark'], TestSheet.front_id: fe_id,
                                      TestSheet.front_content: args['fe_remark'], TestSheet.qa_id: qa_id,
                                      TestSheet.content: args['remark'],
                                      TestSheet.update_time: time.strftime("%Y-%m-%d %H:%M:%S",
                                                                           time.localtime())}).where(
            TestSheet.id == args['id'])
        result = testsheet.execute()
        result = convert_json(TestSheet, args['id'])
        return Results().get(response_code=ResponseCode.SUCCESS_UPDATE_TESTSHEET, data=result)

    def patch(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='请输入迭代Id')
        parser.add_argument('TOKEN', location='headers', type=str)
        args = parser.parse_args()
        user = User.verify_auth_token(args['TOKEN'])
        if not user:
            return Results().get(ResponseCode.FAIL_LOGIN_AUTH)
        if TestSheet.get_or_none(TestSheet.id == args['id']) == None:
            return Results().get(response_code=ResponseCode.FAIL_FIND_TESTSHEET)
        testsheet = TestSheet.update(
            {TestSheet.status: '已部署', TestSheet.update_time: time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                    time.localtime())}).where(
            TestSheet.id == args['id'])
        result = testsheet.execute()
        result = convert_json(TestSheet, args['id'])
        return Results().get(response_code=ResponseCode.SUCCESS_UPDATE_TESTSHEET, data=result)
