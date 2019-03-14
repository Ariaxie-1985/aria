# coding:utf-8
# @Time  : 2019-03-13 15:23
# @Author: Xiawang
from flask_restful import Resource, reqparse

from api_script.c_web.c_position.C_sendResume import sendResume
from api_script.jianzhao_web.b_position.B_offlineposition import online_positionId_outerPositionId, offlinePosition
from utils.util import login


class submit_Resume_To_Position(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        if parser.parse_args() == {} or not (parser.parse_args()):
            parser.add_argument('c_countrycode', type=str, default='00852', help="请输入C端用户手机号的归属区号")
            parser.add_argument('c_username', type=str, default='20181208', help="请输入C端用户的手机号")
            parser.add_argument('b_countrycode', type=str, default='00852', help="请输入B端用户手机号的归属区号")
            parser.add_argument('b_username', type=str, default='20181205', help="请输入B端用户的手机号")
            parser.add_argument('positionId', type=int, help="请输入需投递的职位id")
            args = parser.parse_args()
        state = 0
        info = None
        b_login_r = login(args['b_countrycode'], args['b_username'])
        if b_login_r['state'] == 1:
            if args['positionId']:
                login(args['c_countrycode'], args['c_username'])
                sendResume(args['positionId'])
                state = 1
            else:
                positionId, outerPositionId = online_positionId_outerPositionId()
                c_login_r = login(args['c_countrycode'], args['c_username'])
                if c_login_r['state'] == 1:
                    sendResume_r = sendResume(outerPositionId)
                    if sendResume_r['success'] == True:
                        state = 1
                        info = "C端用户 {} 简历投递成功了，投递职位id: {}".format(args['c_username'], positionId)
                        b_login_r = login(args['b_countrycode'], args['b_username'])
                        if b_login_r['state'] == 1:
                            offline_res = offlinePosition(positionId)
                            if offline_res['state'] == 1:
                                info = "恭喜C端用户 {} 简历投递成功了，投递职位id: {}".format(args['c_username'], positionId)
                            else:
                                info = "恭喜C端用户 {} 简历投递成功了，投递职位id: {}, 但该职位没下线成功，再次投递此职位会报错哦".format(args['c_username'],
                                                                                                    positionId)
                    else:
                        info = "C端用户 {} 已经投递过该职位, 请更改职位id".format(positionId)
                else:
                    info = 'C端用户没登录成功，投递简历流程无法继续'

        else:
            info = {'content': 'B端登录失败，投递简历流程无法继续'}

        return {'state': state, 'content': info}
