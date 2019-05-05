# coding:utf-8
# @Time  : 2019-05-05 12:33
# @Author: Xiawang
from flask_restful import Resource, reqparse

from api_script.batch.C_registe_resume import c_register
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import b_register
from pathos.multiprocessing import ProcessingPool as newPool


class registe(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('countryCode', type=str, help="请输入注册用户手机号的归属区号", required=True)
        parser.add_argument('phone', type=str, help="请输入注册用户的手机号", required=True)
        parser.add_argument('type', type=str, help="用户类型，b表示B端、c表示C端", required=True)
        args = parser.parse_args()
        phone_list = args['phone'].split(',')
        countryCode_list = [args['countryCode'] for i in range(len(phone_list))]
        pool = newPool()
        if args['type'] == 'c':
            res_list = pool.map(c_register, phone_list, countryCode_list)
        elif args['type'] == 'b':
            res_list = pool.map(b_register, phone_list, countryCode_list)
        else:
            return {'state': 400, 'content': '类型错误无法执行注册流程，请输入"c"或"b"'}

        detail_info = {'操作成功': [], '该手机号已被注册': [], '请输入正确的手机号码': []}
        for i, r in enumerate(res_list):
            state = 1
            detail_info[r['message']].append(phone_list[i])

        if len(detail_info['操作成功']) and not (len(detail_info['该手机号已被注册']) or len(detail_info['请输入正确的手机号码'])):
            content = "创建用户成功{}个".format(len(detail_info['操作成功']))
        elif len(detail_info['操作成功']) and (len(detail_info['该手机号已被注册']) or len(detail_info['请输入正确的手机号码'])):
            content = "创建用户成功{}个, 创建用户失败{}个".format(len(detail_info['操作成功']),
                                                    (len(detail_info['该手机号已被注册']) + len(detail_info['请输入正确的手机号码'])))
        else:
            content = "创建用户失败{}个".format(len(detail_info['该手机号已被注册']) + len(detail_info['请输入正确的手机号码']))

        return {'state': state, "content": content, "detail": detail_info}
