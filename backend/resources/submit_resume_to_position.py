# coding:utf-8
# @Time  : 2019-03-13 15:23
# @Author: Xiawang
from flask_restful import Resource, reqparse

from api_script.business.B_energycard import getpositionId
from api_script.c_web.c_position.C_sendResume import sendResume
from utils.util import login


class submit_Resume_To_Position(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('c_countrycode', type=str, default='00852', help="请输入C端用户手机号的归属区号")
        parser.add_argument('c_username', type=str, default='20181208', help="请输入C端用户的手机号")
        parser.add_argument('b_countrycode', type=str, default='00852', help="请输入B端用户手机号的归属区号")
        parser.add_argument('b_username', type=str, default='20181205', help="请输入B端用户的手机号")
        parser.add_argument('positionId', type=int, help="请输入需投递的职位id")
        args = parser.parse_args()
        state = 0
        login(args['b_countrycode'], args['b_username'])
        if args['positionId']:
            login(args['c_countrycode'], args['c_username'])
            sendResume(args['positionId'])
            state = 1
        else:
            positionId = getpositionId()
            print('--------------------')
            print(positionId)
            login(args['c_countrycode'], args['c_username'])
            sendResume(positionId)

        return {'state':state, 'content':'投递简历成功'}