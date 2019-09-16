# coding:utf-8
# @Time  : 2019-05-05 12:33
# @Author: Xiawang
from flask_restful import Resource, reqparse

from api_script.batch.C_registe_resume import c_register
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import b_register
from pathos.multiprocessing import ProcessingPool as newPool


class registe(Resource):
    """注册账号(B端&C端，可批量)"""

    def post(self):
        '''
        @@@
        ### Author = Xiawang

        ### Request Header
        | 字段 | 值 |
        | ---- | ---- |
        | method | POST |
        | Accept | application/json |


        ### 参数

        | 字段 | 必填 | 类型 | 描述|
        | ---- | ---- | ---- | ---- |
        | countryCode | True | string | 用户地区编号 |
        | phone | True | string | 用户手机号,支持用多个英文逗号分隔多个手机号 |
        | type | True | string | 用户注册类型 b表示b端，c表示c端 |



        ### 请求示例
        ```json
            {
                "countryCode": "00852",
                "phone": "19900223",
                "type": "c"
            }

        ```

        ### 返回
         ```json
         {
            state: 1,
            content: "创建用户成功1个",
            detail: {
                操作成功: ["19900223"],
                该手机号已被注册: [],
                请输入正确的手机号码: []
            }
        }
        ```
        '''
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
        print(res_list)
        detail_info = {'操作成功': [], '该手机号已被注册': [], '请输入正确的手机号码': [], '请勿重复提交,刷新页面后重试': []}
        for i, r in enumerate(res_list):
            state = 1
            detail_info[r['message']].append(phone_list[i])

        if len(detail_info['操作成功']) and not (len(detail_info['该手机号已被注册']) or len(detail_info['请输入正确的手机号码'])):
            content = "创建用户成功{}个".format(len(detail_info['操作成功']))
        elif len(detail_info['操作成功']) and (len(detail_info['该手机号已被注册']) or len(detail_info['请输入正确的手机号码'])):
            content = "创建用户成功{}个, 创建用户失败{}个".format(len(detail_info['操作成功']),
                                                    (len(detail_info['该手机号已被注册']) + len(
                                                        detail_info['请输入正确的手机号码']) + len(
                                                        detail_info['请勿重复提交,刷新页面后重试'])))
        else:
            content = "创建用户失败{}个".format(
                len(detail_info['该手机号已被注册']) + len(detail_info['请输入正确的手机号码']) + len(detail_info['请勿重复提交,刷新页面后重试']))

        return {'state': state, "content": content, "detail": detail_info}
