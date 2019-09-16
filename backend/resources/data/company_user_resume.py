# coding:utf-8
# @Time  : 2019-07-25 16:10
# @Author: Xiawang


from flask_restful import Resource, reqparse
from backend.common.get_data import get_compangy, get_userId_resumeId
from utils.util import login


class getInfo(Resource):
    """ 获取用户id """

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('countryCode', type=str, help="请输入正确地区编号", required=True)
        parser.add_argument('phone', type=str, help="请输入正确手机号", required=True)
        args = parser.parse_args()

        login(args['countryCode'], args['phone'])
        cuserId, resumeId = get_userId_resumeId()
        company_id, compant_mds_Id, buserId = get_compangy()

        return {'state': 1, 'content': {'cuserId': cuserId, 'resumeId': resumeId, 'company_id': company_id,
                                        'compant_mds_Id': compant_mds_Id, 'buserId': buserId}}
