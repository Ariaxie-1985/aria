# coding:utf-8
# @Time  : 2019-03-20 18:53
# @Author: Xiawang
from flask_restful import Resource, reqparse

from api_script.home.data_import import import_linkManInfo, import_contacts
from utils.util import login_home_code


class Contract_Data_Import(Resource):

    def post(self):
        '''
                @@@
                ### home后台-拉勾加-合同导入

                ### Author = Xiawang

                ### Request Header
                | 字段 | 值 |
                | ---- | ---- |
                | method | POST |
                | content-type | application/json |


                ### 参数

                | 字段 | 必填 | 类型 | 描述|
                | ---- | ---- | ---- | ---- |
                | companyId | True | string | 公司id |
                | contractNo | True | string | 合同编号, 注意唯一性 |



                ### 请求示例
                ```json
                 {
                    "companyId":"1",
                    "contractNo":"fkdshjfd1"
                }
                ```


                ### 返回

                | 字段 | 类型 | 描述|
                | ---- | ---- | ---- | ---- |
                | state | int | 1表示成功, 400表示错误 |
                | content | string | 合同导入的结果 |



                ### 响应示例
                ```json
                {
                    "state": 1,
                    "content": "导入公司联系人信息 导入成功! 导入合同信息 导入成功! "
                }
                ```

                @@@
                '''
        parser = reqparse.RequestParser()
        parser.add_argument('companyId', type=str, help="请输入公司id", required=True)
        parser.add_argument('contractNo', type=str, help="请输入合同编号, 注意唯一性", required=True)
        args = parser.parse_args()
        state = 0
        info1 = ''
        info2 = ''
        login_res = login_home_code('00853', 22222222)
        if login_res['state'] == 1:
            import1_res = import_linkManInfo(args['companyId'], args['contractNo'])
            if import1_res['success'] == True:
                state = 1
                info1 = "导入公司联系人信息 导入成功! "
            else:
                state = 400
                info1 = "导入公司联系人信息 导入失败! "

            import2_res = import_contacts(args['companyId'], args['contractNo'])
            if import2_res['success'] == True:
                state = 1
                info2 = "导入合同信息 导入成功! "
            else:
                state = 400
                info2 = "导入合同信息 导入失败! "
        else:
            state = 400
            info1 = "登录home后台失败, 无法继续数据导入流程, 请重试！ "
        return {'state': state, 'content': info1 + info2}
