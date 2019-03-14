# -*- coding: utf8 -*-
__author__ = 'yqzhang'

from flask_restful import Resource, reqparse
from utils.util import login
from api_script.jianzhao_web.b_position.B_move_to_communicated import move_to_communicated,getIds
from api_script.jianzhao_web.b_position.move_to_interview import move_to_interview
from api_script.jianzhao_web.b_position.B_move_to_eliminate import move_to_eliminate
from api_script.jianzhao_web.b_position.B_move_to_stageoffer import move_to_stageoffer
from  api_script.jianzhao_web.b_position.B_move_to_employ import move_to_employ

class b_process_resume(Resource):



    def post(self):

        '''
        web端简历处理接口，resumeId，positionId非必填，默认该账号第一条数据

        请求参数示例：
                 {
            "countrycode": "00852",
            "username": "20181205",
            "type": 3,
            "resumeId": 1081023879159488512,
			"positionId": 13844989
        }
        type:1    待沟通
        type:2    面试
        type:3    淘汰
        type:4    录用
        type:5    入职

        header:
        content-type:application/json
        '''


        parser = reqparse.RequestParser()

        parser.add_argument('countrycode', type=str, help="请输入用户手机号的归属区号", required=True)
        parser.add_argument('username', type=str, help="请输入用户的手机号", required=True)
        args1 = parser.parse_args()
        login(args1['countrycode'],args1['username'])

        try:
            pos,res=getIds()
        except Exception as IndexError:
            return {'state':1002,'message':'获取职位和简历id失败，该账号简历列表可能为空'}

        parser.add_argument('type', type=int, choices=(1, 2, 3,4,5), help="请选择简历处理方式", required=True)
        parser.add_argument('resumeId', type=int, help="请输入简历id", required=False, default=res)
        parser.add_argument('positionId', type=int, help="请输入应聘职位id", required=False, default=pos)
        args = parser.parse_args()

        if int(args['type']) == 1:
            r = move_to_communicated(args['positionId'], args['resumeId'])
            if r['state'] == 1:
                return {'state': 1, 'message': '移动到待沟通成功'}
            else:
                return {'state': r['state'], 'message': r['message']}
        if int(args['type']) == 2:
            # move_to_communicated(args['positionId'],args['resumeId'])
            r = move_to_interview(args['positionId'], args['resumeId'])
            if r['state'] == 1:
                return {'state': 1, 'message': '移动到面试成功'}
            else:
                return {'state': r['state'], 'message': r['message']}
        if int(args['type']) == 3:
            r = move_to_eliminate(args['positionId'], args['resumeId'])
            if r['state'] == 1:
                return {'state': 1, 'message': '淘汰成功'}
            else:
                return {'state': r['state'], 'message': r['message']}
        if int(args['type']) == 4:
            r = move_to_stageoffer(args['positionId'], args['resumeId'])
            if r['state'] == 1:
                return {'state': 1, 'message': '录用成功'}
            else:
                return {'state': r['state'], 'message': r['message']}
        if int(args['type']) == 5:
            r = move_to_employ(args['positionId'], args['resumeId'])
            if r['state'] == 1:
                return {'state': 1, 'message': '入职成功'}
            else:
                return {'state': r['state'], 'message': r['message']}