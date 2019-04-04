# coding:utf-8
# @Time  : 2019-04-02 11:29
# @Author: Xiawang
from backend.OperationMysql import OperationMysql

op_mysql = OperationMysql()
from flask_restful import Resource, reqparse


class getUserId(Resource):
    """ 获取用户id """

    def get(self):
        '''获取用户id
        @@@
        ### Author = Xiawang

        ### Request Header
        | 字段 | 值 |
        | ---- | ---- |
        | method | GET |
        | Accept | application/json |


        ### 参数

        | 字段 | 必填 | 类型 | 描述|
        | ---- | ---- | ---- | ---- |
        | phone | True | string | 用户手机号，非0086地区编号的手机号填写格式：地区编号+手机号 |



        ### 请求示例--直接在浏览器请求访问
        ```json
        http://127.0.0.1:9004/customer?phone=0085220181208

        ```

        ### 返回
         ```json
         {
            "state": 1,
            "content": {
                "userId": 537
            }
        }
        ```

        '''
        parser = reqparse.RequestParser()
        parser.add_argument('phone', type=str, help="请输入正确手机号", required=True)
        args = parser.parse_args()
        try:
            userid = op_mysql.search_all("SELECT userId FROM r_resume where phone = %s" % args['phone'])
            state = 1
            info = userid[0]
        except:
            state = 400
            info = "找不到userId, 请确认下手机号填写是否正确"
        return {'state': state, 'content': info}
