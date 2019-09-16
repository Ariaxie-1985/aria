# coding:utf-8
# @Time  : 2019-09-06 15:55
# @Author: Xiawang
# Description:
from flask import g
from flask_restful import Resource

from backend.common.authentication import auth


class Token(Resource):

    @auth.login_required
    def post(self):
        token = g.user.generate_auth_token(6000)
        return {'token': token.decode('ascii')}