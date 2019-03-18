# -*- coding: utf8 -*-
__author__ = 'yqzhang'

from flask_restful import Resource, reqparse
from api_script.zhaopin_app.b_position import post_positions


class app_post_position(Resource):

    def post(self):

        """
                   @@@
                   ### Auther = yqzhang

                   ### app发布职位


                   ### Request Header
                   | 字段 | 值 |
                   | ---- | ---- |
                   | method | POST |
                   | content-type | application/json |


                   ### 参数

                   | 字段 | 必填 | 类型 | 描述|
                   | ---- | ---- | ---- | ---- |
                   | userid | True | int | B端用户id |
                   | positionname | False | string | 职位名 |
                   | sum | True | int | 发布职位总数 |
                   | workyear | False | str | 经验 |
                   | typeid | False | int |职位类型: typeid字段:  1：普通职位，2：特权，3：无曝光，默认不填为校招职位，如果填写此字段需同时填写workyear字段，如："1-3年"
                    workyear字段默认为应届毕业生 |




                   ### 请求示例
                   ```json
                    {

                       "userid": 100013384,
                       "sum": 1
                   }
                   ```


                   ### 返回

                   | 字段 | 类型 | 描述|
                   | ---- | ---- | ---- | ---- |
                   | state | int | 1表示成功, 400表示错误 |
                   | content | string | 构造数据的结果 |
                   | positionid | list | 发布成功的职位信息 |
                   | fail num | int | 发布失败数 |
                   | success num | int | 发布成功数 |

                   ### 响应示例
                   ```json
                   {
                        "state": 1,
                        "message": "成功",
                        "content": {
                            "positionid": [
                                13846665
                            ],
                            "succees num": 1,
                            "fail num": 0
                        }
                    }
                   ```

                   @@@
                   """

        parser = reqparse.RequestParser()
        parser.add_argument('userid', type=int, help="B端用户id", required=True)
        parser.add_argument('positionname', type=str, help="请输入职位名", required=False, default='Java开发工程师')
        parser.add_argument('sum', type=int, help="请输入发布职位的数量", required=False, default=1)
        parser.add_argument('workyear', type=str, help="请输入经验", required=False, default='应届毕业生')
        parser.add_argument('typeid', type=int, help="请输入职位类型", choices=(1, 2, 3), required=False, default=None)
        args1 = parser.parse_args()

        result = []
        # fail=[]
        s = 0
        f = 0
        for i in range(args1['sum']):

            r = post_positions('开发|测试|运维类', args1['workyear'], '后端开发', 'Java', args1['positionname'], args1['typeid'])
            if r['state'] == 1:
                if r['content']['status'] == 1:

                    result.append(r['content']['mdsPositionId'])
                    s = s + 1
                else:
                    # fail.append()
                    f = f + 1
            else:
                return {'state': 401, 'message': '职位创建失败'}
        if s == 0:
            return {'state': 400, 'message': '所有职位均创建失败'}
        else:
            return {'state': 1, 'message': '成功', 'content': {'positionid': result, 'success num': s, 'fail num': f}}
