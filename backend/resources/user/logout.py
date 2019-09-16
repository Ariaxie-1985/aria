# coding:utf-8
# @Time  : 2019-08-03 21:21
# @Author: Xiawang
from flask_login import login_required, logout_user
from flask_restful import Resource
from common.state import ResponseCode, Results


class Logout(Resource):

    @login_required
    def post(self):
        logout_user()
        return Results().get(ResponseCode.SUCCESS_LOGOUT)
