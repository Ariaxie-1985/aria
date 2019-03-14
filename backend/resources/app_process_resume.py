# -*- coding: utf8 -*-
__author__ = 'yqzhang'

from flask_restful import Resource, reqparse
from api_script.zhaopin_app.OrderResume_app.ResumeState import *

class app_process_resume(Resource):

    '''
    app简历处理接口，resumeId非必填，默认该账号第一条数据

    请求参数示例：
             {
        "userid": 100013384,
        "type": 3,
        "resumeId": 1081023879159488512,

    }
    type:1    待沟通
    type:2    面试
    type:3    淘汰
    type:4    录用
    type:5    入职

    header:
    content-type:application/json
    '''

    def post(self):
        parser = reqparse.RequestParser()


        parser.add_argument('userid', type=int, help="请输入B端用户id", required=True)
        parser.add_argument('type', type=int,choices=(1, 2, 3,4,5), help="请选择简历处理方式", required=True)
        args = parser.parse_args()
        try:
            OrderResumeId = ResumeID(args['userid'])
        except Exception as IndexError:
            return {'state':1002,'message':'获取职位和简历id失败，该账号简历列表可能为空'}

        parser.add_argument('resumeid', type=int, help="请输入简历id", required=False,default=OrderResumeId)
        args2=parser.parse_args()

        if int(args['type'])==1:
            r=OrderResumeState(args['userid'],args2['resumeid'])
            if r['state']==1:
                return {'state':1,'message':'移动到待沟通成功'}
            else:
                return {'state':r['state'],'message':r['message']}
        if int(args['type'])==2:
            # OrderResumeState(args['userid'],args2['resumeid'])
            r=Interview(args['userid'],args2['resumeid'])
            if r['state']==1:
                return {'state':1,'message':'安排面试成功'}
            else:
                return {'state':r['state'],'message':r['message']}
        if int(args['type'])==3:
            r=taotai(args['userid'],args2['resumeid'])
            if r['state']==1:
                return {'state':1,'message':'淘汰成功'}
            else:
                return {'state':r['state'],'message':r['message']}
        if int(args['type'])==4:
            # OrderResumeState(args['userid'],args2['resumeid'])
            # Interview(args['userid'],args2['resumeid'])
            r=luyong(args['userid'],args2['resumeid'])
            if r['state']==1:
                return {'state':1,'message':'录用成功'}
            else:
                return {'state':r['state'],'message':r['message']}
        if int(args['type'])==5:
            # OrderResumeState(args['userid'],args2['resumeid'])
            # Interview(args['userid'],args2['resumeid'])
            r=ruzhi(args['userid'],args2['resumeid'])
            if r['state']==1:
                return {'state':1,'message':'入职成功'}
            else:
                return {'state':r['state'],'message':r['message']}


