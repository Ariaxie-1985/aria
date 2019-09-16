# coding:utf-8
# @Time  : 2019-03-14 15:43
# @Author: Xiawang
import re

from flask_restful import Resource, reqparse

from api_script.c_web.c_position.C_sendResume import sendResume
from api_script.jianzhao_web.b_position.B_offlineposition import online_positionId_outerPositionId, offlinePosition
from utils.util import login


class submit_Resume_To_Position(Resource):
    """C端用户投递给B端公司在线的某职位"""

    def post(self):
        '''
                @@@
                ### Auther = Xiawang

                ### C端用户投递给B端公司在线的某职位


                ### Request Header
                | 字段 | 值 |
                | ---- | ---- |
                | method | POST |
                | content-type | application/json |


                ### 参数

                | 字段 | 必填 | 类型 | 描述|
                | ---- | ---- | ---- | ---- |
                | c_countrycode | True | string | C端用户手机号的归属区号 |
                | c_username |  True | string | C端用户的手机号 |
                | outerPositionId | True | string | 职位页面的职位id----页面必填,接口非必填 |


                ### 请求示例
                ```json
                 {
                    "c_countrycode": "00852",
                    "c_username": "20181208",
                    "outerPositionId": "574444"
                }
                ```


                ### 返回

                | 字段 | 类型 | 描述|
                | ---- | ---- | ---- | ---- |
                | state | int | 1表示成功, 400表示错误 |
                | content | string | 投递简历的结果 |



                ### 响应示例
                ```json
                {
                    "state": 400,
                    "content": "默认B端用户登录失败，无法继续投递简历流程"
                }

                ```

                @@@
                '''
        parser = reqparse.RequestParser()
        parser.add_argument('c_countrycode', type=str, help="请输入C端用户手机号的归属区号", required=True)
        parser.add_argument('c_username', type=str, help="请输入C端用户的手机号", required=True)
        parser.add_argument('outerPositionId', type=int, help="请填写投递的职位id, 在职位页url中去找")
        args = parser.parse_args()

        state = 0
        info = None
        if args['outerPositionId']:
            login_c = login(args['c_countrycode'], args['c_username'])
            if login_c['state'] == 1:
                send_r = sendResume(args['outerPositionId'])
                if '<i>' in send_r['msg']:
                    new_msg = ''.join(re.split('[<i></i> ]', send_r['msg']))
                else:
                    new_msg = send_r['msg']

                if send_r['success'] == True:
                    state = 1
                    info = "C端用户 {} {}，投递职位id: {}".format(args['c_username'], new_msg, args['outerPositionId'])
                else:
                    stat = 400
                    info = "C端用户 {} {}，投递职位id: {}".format(args['c_username'], new_msg, args['outerPositionId'])
            else:
                stat = 400
                info = "C端用户登录失败，无法继续投递简历流程"
        else:
            b_login_r = login('00852', '20181205')
            if b_login_r['state'] == 1:
                try:
                    positionId, outerPositionId = online_positionId_outerPositionId()
                except KeyError:
                    state = 400
                    info = "没有获取到职位id，无法投递"
                c_login_r = login(args['c_countrycode'], args['c_username'])
                if c_login_r['state'] == 1:
                    sendResume_r = sendResume(outerPositionId)
                    if '<i>' in sendResume_r['msg']:
                        new_msg = ''.join(re.split('[<i></i> ]', sendResume_r['msg']))
                    else:
                        new_msg = sendResume_r['msg']
                    if sendResume_r['success'] == True:
                        state = 1
                        info = "C端用户{} {} 投递职位id: {}".format(args['c_username'], new_msg, positionId)
                        # b_login_r = login('00852', '20181205')
                        # if b_login_r['state'] == 1:
                        #     offline_res = offlinePosition(positionId)
                        #     if offline_res['state'] == 1:
                        #         state = 1
                        #         info = "恭喜C端用户 {} {}，投递职位id: {}".format(args['c_username'], new_msg,
                        #                                                 positionId)
                        #     else:
                        #         state = 1
                        #         info = "恭喜C端用户 {} {}，投递职位id: {}, 但该职位没下线成功，再次投递此职位会报错哦".format(args['c_username'],
                        #                                                                        new_msg,
                        #                                                                        positionId)
                    else:
                        state = 400
                        info = "C端用户 {} {}，投递职位id: {}".format(args['c_username'], new_msg, positionId)
                else:
                    state = 400
                    info = "C端用户登录失败，无法继续投递简历流程"
            else:
                state = 400
                info = '默认B端用户登录失败，无法继续投递简历流程'

        return {'state': state, 'content': info}
