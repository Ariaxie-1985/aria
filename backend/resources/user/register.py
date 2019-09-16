# coding:utf-8
import datetime
import time

from flask import g
from flask_restful import fields, Resource, reqparse

from backend.common.new_models import User
from backend.common.state import Results, ResponseCode


def email(email_str):
    if email_str[-10:] == '@lagou.com':
        return email_str
    else:
        return False


post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'position', dest='position',
    type=str, location='json',
    required=True, choices=('测试', '开发', '其他'), help='请输入合理职位',
)
post_parser.add_argument(
    'email', dest='email',
    type=email, location='json',
    required=True, help='请输入合法邮箱',
)
post_parser.add_argument(
    'password', dest='password',
    type=str, location='json',
    help='请输入密码',
)
post_parser.add_argument(
    'repassword', dest='repassword',
    type=str, location='json',
    help='请输入确认密码',
)


class Register(Resource):
    '''json
    {
        "state": 1,
        'message':'成功',
        'data': null
        }
    '''

    def post(self):
        args = post_parser.parse_args()
        if args.email == False:
            return Results().get(ResponseCode.FAIL_STANDARD_EMAIL)

        if not args.password == args.repassword:
            return Results().get(ResponseCode.FAIL_RE_PASSWORD)

        username = args.email.split('@')[0]
        password_hash = User().hash_password(password=args['password'])
        user, created = User.get_or_create(email=args['email'],
                                           defaults={'username': username, 'position': args['position'],
                                                     'password_hash': password_hash,
                                                     'create_time': time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                  time.localtime()),
                                                     'update_time': time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                  time.localtime())
                                                     })
        if created == False:
            return Results().get(ResponseCode.FAIL_REGISTER_EMAIL)
        return Results().get(ResponseCode.SUCCESS)
