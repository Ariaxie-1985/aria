# coding:utf-8

from flask_restful import Api

from backend.resources.user import user
from backend.resources.user.hello import helloWorld
from backend.resources.user.info import Info
from backend.resources.user.login import Login
from backend.resources.user.logout import Logout
from backend.resources.user.register import Register
from backend.resources.user.token import Token

api = Api(user)

api.add_resource(helloWorld, '/hello')
api.add_resource(Login, '/login')
api.add_resource(Register, '/register')
api.add_resource(Logout, '/logout')
api.add_resource(Token, '/token')
api.add_resource(Info, '/info')

import backend.resources.user.urls
