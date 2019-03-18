# coding:utf-8
# @Time  : 2019-02-26 14:31
# @Author: Xiawang
from flask_restful import Resource, reqparse

from api_script.jianzhao_web.b_basic.home_review_person_2 import passPersonApprove
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import add_people_into_company
from utils.util import login_home


class B_Add_People_Into_Company(Resource):

    def post(self):
        """
        @@@
        ### Auther = Xiawang

        ### B端注册加入公司-招聘者认证提交及审核流程


        ### Request Header
        | 字段 | 值 |
        | ---- | ---- |
        | method | POST |
        | content-type | application/json |


        ### 参数

        | 字段 | 必填 | 类型 | 描述|
        | ---- | ---- | ---- | ---- |
        | countryCode | True | string | B端注册用户手机号的地区编号 |
        | phone | True | string | B端注册用户的手机号 |
        | userName | True | string | B端注册用户的姓名 |
        | companyFullName | True | string | B端注册公司的全称 |
        | resumeReceiveEmail | True | string | B端注册用户接收简历的邮箱 |

        ### 请求示例
        ```json
        {
            "countryCode": "00852",
            "phone": "20030902",
            "userName": "小菜",
            "companyFullName": "烽火啊啊啊",
            "resumeReceiveEmail": "tester2018@sina.com"
        }
        ```


        ### 返回

        | 字段 | 类型 | 描述|
        | ---- | ---- | ---- | ---- |
        | state | int | 1表示成功, 400表示错误 |
        | content | string | 构造数据的结果 |
        | data | dict | 构造成功数据的具体信息 |
        | HRInfo | dict | 招聘者信息 |
        | CompanyInfo | dict | 公司信息 |
        | Application | dict | 招聘者和公司的认证的申请结果 |
        | ApproveInfo | string | 招聘者和公司的认证的审核结果 |

        ### 响应示例
        ```json
        {
            "state": 1,
            "content": "B端注册加入公司-招聘者认证提交及审核流程通过！",
            "data": {
                "HRInfo": {
                    "phone": "20021215",
                    "countryCode": "00852",
                    "userId": 100016374
                },
                "CompanyInfo": {
                    "companyFullName": "拉勾测试自动化default公司",
                    "companyId": 142136
                },
                "ApproveInfo": {
                    "passPersonApprove": "招聘者认证提交及审核通过"
                }
            }
        }
        ```

        @@@
        """
        parser = reqparse.RequestParser()
        parser.add_argument('countryCode', type=str, help="请输入B端注册用户手机号的归属区号", required=True)
        parser.add_argument('phone', type=str, help="请输入B端注册用户的手机号", required=True)
        parser.add_argument('userName', type=str, help="请输入B端注册用户的姓名", required=True)
        parser.add_argument('resumeReceiveEmail', type=str, help="请输入接收简历的邮箱地址", required=True)
        parser.add_argument('companyFullName', type=str, help="请输入注册公司的全称", required=True)
        args = parser.parse_args()
        HRInfo = {}
        CompanyInfo = {}
        ApproveInfo = {}
        r1, r2, r3, r4 = add_people_into_company(args['phone'],
                                                 args['countryCode'],
                                                 args['companyFullName'],
                                                 args['userName'],
                                                 args['resumeReceiveEmail']
                                                 )
        state = 0
        try:
            if r1['state'] != 1:
                state = 400
                info = "该手机号已被注册, 该用户的手机号: " + args['phone']

            if r2['state'] != 1:
                state = 400
                info = "上传B端用户信息失败，该用户的手机号: " + args['userName']

            if r3['state'] != 1:
                state = 400
                info = "B端加入公司失败，该公司全称:" + args['companyFullName']

            if r4['state'] != 1:
                state = 400
                info = "B端提交招聘者审核失败，该公司简称: " + args['companyShortName']
        except TypeError:
            info = info

        if not (state == 400):
            if r1['state'] == r2['state'] == r3['state'] == r4['state'] == 1:
                state = 3
                HRInfo['phone'] = args['phone']
                HRInfo['countryCode'] = args['countryCode']
                CompanyInfo['companyFullName'] = args['companyFullName']

            login_home("anan@lagou.com", "990eb670f81e82f546cfaaae1587279a")

            r51, r52, r53 = passPersonApprove()
            try:
                if r51['success'] != True:
                    state = 400
                    info = "home后台-审核中心-个人认证-审核招聘者失败, 该公司的简称: " + args['companyShortName']
                else:
                    CompanyInfo['companyId'] = r52
                    HRInfo['userId'] = r53
                    ApproveInfo['passPersonApprove'] = "招聘者认证提交及审核通过"
                    state = 1
            except TypeError:
                info = info

        if state == 1:
            return {
                "state": 1,
                "content": "B端注册加入公司-招聘者认证提交及审核流程通过！",
                "data": {"HRInfo": HRInfo, "CompanyInfo": CompanyInfo, "ApproveInfo": ApproveInfo}
            }
        return {"state": 400, "content": "执行失败", "faiinfo": info}
