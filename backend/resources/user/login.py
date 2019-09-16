# coding:utf-8
from flask import g, current_app, make_response
from flask_restful import Resource, reqparse

from common.authentication import load_user
from common.new_models import User
from common.state import Results, ResponseCode


class Login(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help='请输入您的英文名', required=True)
        parser.add_argument('password', type=str, help='请输入您的密码', required=True)
        args = parser.parse_args()

        user_info = User.get_or_none(User.username == args['username'])
        if user_info is None:
            return Results().get(ResponseCode.FAIL_LOGIN_USERNAME)

        check_result = user_info.verify_password(args['password'])
        if not check_result:
            return Results().get(ResponseCode.FAIL_LOGIN_PASSWORD)

        if load_user(user_info.id):
            token = g.user.generate_auth_token()
            return Results().set_response(data=Results().get(ResponseCode.SUCCESS_LOGIN), token=token)
        else:
            Results().get(ResponseCode.FAIL_LOGIN)
        # if load_user(user_info.id):
        #     return Results().get(ResponseCode.SUCCESS_LOGIN)
        # else:
        #     return Results().get(ResponseCode.FAIL_LOGIN)
