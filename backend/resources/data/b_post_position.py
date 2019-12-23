# coding:utf-8
# @Time  : 2019-02-15 15:32
# @Author: Xiawang
from flask import request
from flask_restful import Resource, reqparse

from api_script.batch.B_postposition import post_position
from backend.common.address import junge_address
from backend.common.update_user_company_id import get_user_company_id, update_user_company_id
from utils.util import login


class B_Post_Position(Resource):
    """发布职位"""

    def post(self):
        """
        @@@
        ### Auther = Xiawang

        ### 发布职位


        ### Request Header
        | 字段 | 值 |
        | ---- | ---- |
        | method | POST |
        | content-type | application/json |


        ### 参数

        | 字段 | 必填 | 类型 | 描述|
        | ---- | ---- | ---- | ---- |
        | countrycode | True | string | B端用户手机号的归属区号 |
        | username | True | string | B端用户手机号 |
        | sum | True | int | 发布职位总数 |


        ### 请求示例
        ```json
         {
            "countrycode": "00852",
            "username": "20181205",
            "sum": 1
        }
        ```


        ### 返回

        | 字段 | 类型 | 描述|
        | ---- | ---- | ---- | ---- |
        | state | int | 1表示成功, 400表示错误 |
        | content | string | 构造数据的结果 |
        | data | list | 发布成功的职位信息 |
        | failinfo | list | 发布失败的职位信息 |


        ### 响应示例
        ```json
        {
            "state": 1,
            "message": "发布职位1个, 其中1个成功",
            "data": [{
                "position_name": "金融产品经理",
                "parentPositionId": 1788012,
                "positionId": 13846665
            }],
            "failinfo": [
                null
            ]
        }
        ```

        @@@
        """

        j = 0
        successlist = []
        faillist = [None]
        data = {}
        parser = reqparse.RequestParser()
        parser.add_argument('countrycode', type=str, help="请输入用户手机号的归属区号", required=True)
        parser.add_argument('username', type=str, help="请输入用户的手机号", required=True)
        parser.add_argument('firstType', type=str, help="请输入职位的一级类别", default="市场|商务类")
        parser.add_argument('positionType', help="请输入职位的二级类别", default="市场|营销")
        parser.add_argument('positionThirdType', type=str, help="请输入职位的三级类别", default="市场营销")
        parser.add_argument('positionName', default="高级市场营销经理", type=str, help="职位名称")
        parser.add_argument('workAddress', type=str, help="工作地址", required=True)
        parser.add_argument('sum', type=int, help="请输入发布职位的数量", required=True)
        args = parser.parse_args()

        address_id = junge_address(args['workAddress'])

        if args['workAddress'] == '' or (not bool(address_id)):
            return {'state': 400, 'message': '输入的工作地址没存在对应id,请重新输入'}

        login_res = login(args['countrycode'], args['username'])
        if login_res['state'] != 1:
            return {"message": login_res['message']}
        else:
            userId, companyId = get_user_company_id()
            flag = update_user_company_id(address_id, userId, companyId)
            if flag == False:
                return {'state': 400, 'message': '工作地址修改不成功,请重新输入'}

        result = post_position(sum=args['sum'], positionName=args['positionName'], firstType=args['firstType'],
                               positionType=args['positionType'],
                               positionThirdType=args['positionThirdType'],
                               workAddressId=address_id)

        state = 0
        for i in result:
            if i['state'] == 1:
                j += 1
                print(i)
                data["position_name"] = i['content']['data']['parentPositionInfo']['positionName']
                data["parentPositionId"] = i['content']['data']['parentPositionInfo']['parentPositionId']
                data["positionId"] = i['content']['data']['parentPositionInfo']['positionChannelInfoList'][0][
                    'positionId']
                successlist.append(data)
                data = {}
                state = 1
            else:
                data['state'] = i['state']
                data['message'] = i['message']
                faillist.append(data)
                data = {}
                state = 400

        return {"state": state, "content": "发布职位" + str(args['sum']) + "个, 其中" + str(j) + "个成功", "data": successlist,
                "errors": faillist}


if __name__ == '__main__':
    b = B_Post_Position()
    b.post()
