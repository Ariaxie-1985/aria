# coding:utf-8
# @Time  : 2019-07-09 17:37
# @Author: Xiawang
from flask_restful import Resource, reqparse

from utils.util import login_home_code
from api_script.business.new_lagouPlus import contractController_list, open_product, close_contract


class Open_Product(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('companyId', type=int, help="请输入正确公司id")
        parser.add_argument('userId', type=str, help="请输入正确userid")
        parser.add_argument('startTimeStr', type=str, help="请输入正确日期: yyyy-mm-dd")
        parser.add_argument('endTimeStr', type=str, help="请输入正确日期: yyyy-mm-dd")
        parser.add_argument('can', type=bool, help="请输入布尔值来决定是否终止已有的合同")
        parser.add_argument('templateId', type=int, help="请输入产品套餐id")
        args = parser.parse_args()
        login_r = login_home_code('00853', 22222222)
        state = 0
        try:
            if login_r['state'] == 1:
                contractNo = contractController_list(args['companyId'])
                if args['can'] == False:

                    res = open_product(templateId=args['templateId'], companyId=args['companyId'],
                                       contractNo=contractNo,
                                       userId=args['userId'], startTimeStr=args['startTimeStr'],
                                       endTimeStr=args['endTimeStr'])
                    if res['success'] == True:
                        state = 1
                        content = "开通产品成功！"

                else:
                    if close_contract(contractNo) == True:
                        res = open_product(templateId=args['templateId'], companyId=args['companyId'],
                                           contractNo=contractNo,
                                           userId=args['userId'], startTimeStr=args['startTimeStr'],
                                           endTimeStr=args['endTimeStr'])
                        if res['success'] == True:
                            state = 1
                            content = "开通产品成功！"
            else:
                return {'state': 400, 'content': "登录失败, 请重试！"}
        except:
            return {'state': 400, 'content': "开通产品失败, 请重试！"}

        return {'state': state, 'content': content}
