# coding:utf-8
# @Time  : 2019-03-28 11:24
# @Author: Xiawang
from flask_restful import Resource, reqparse

from api_script.batch.C_registe_resume import registe_c, create_resume
from pathos.multiprocessing import ProcessingPool as newPool
from faker import Faker

fake = Faker("zh_CN")


class C_Basic_Process(Resource):
    """C端注册并生成简历"""

    def post(self):
        '''
        @@@
        ### Auther = Xiawang


        ### C端注册并生成简历


        ### Request Header
        | 字段 | 值 |
        | ---- | ---- |
        | method | POST |
        | content-type | application/json |


        ### 参数

        | 字段 | 必填 | 类型 | 描述|
        | ---- | ---- | ---- | ---- |
        | phone | True | string | C端注册用户的手机号 |
        | countryCode | True | string | C端注册用户的手机号的地区编号 |
        | userIdentity | True | int | 1学生, 2非学生 |
        | sum | False | int | 构造C端账号的数量 |
        | name | False | string | C端注册用户的简历姓名 |
        | birthday | False | string | C端注册用户的简历姓名 |
        | liveCity | False | string | C端注册用户的现居住地, 例如 北京 |
        | joinWorkTime | False | string | C端注册用户的参加工作时间, 例如 2018.07 |
        | education | False | string | C端注册用户的学历, 例如 本科 |
        | startDate | False | string | C端注册用户的在校时间的开始时间 |
        | endDate | False | string | C端注册用户的在校时间的结束时间 |
        | city | False | string | C端注册用户的求职意向的期望城市 |
        | positionType | False | string | C端注册用户的 职位类型, 例如 全职|
        | positionName | False | list | C端注册用户的求职意向的期望职位 |
        | salarys | False | string | C端注册用户的求职意向的期望薪资, 例如 10k-20k |




        ### 请求示例
        ```json
         {
            "phone": "19000971,19000972",
            "countryCode": "00852",
            "userIdentity": 1,
            "name": "airpods2",
            "birthday": "1998.03",
            "liveCity": "北京",
            "joinWorkTime": "2018.07",
            "education": "本科",
            "startDate": "2014",
            "endDate": "2018",
            "city": "青岛",
            "positionType": "全职",
            "positionName": ["开发|测试|运维类", "后端开发", "PHP"],
            "salarys": "8k-15k"
        }
        ```


        ### 返回

        | 字段 | 类型 | 描述|
        | ---- | ---- | ---- | ---- |
        | state | int | 1表示成功, 400表示错误 |
        | content | string | 构造数据的结果 |
        | data | list | 注册成功的手机号 |
        | errors | list | 注册失败的手机号 |
        | detail | list | 注册失败的详细信息 |


        ### 响应示例
        ```json
        {
            "state": 1,
            "message": "注册用户2个, 其中注册成功2个, 注册失败0个",
            "data": [
                20080520,
                20080521
            ],
            "errors": [],
            "detail": []
        }
        ```

        @@@
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('countryCode', type=str, help="请输入注册用户手机号的归属区号", required=True)
        parser.add_argument('phone', type=str, help="请输入注册用户的手机号", required=True)
        # parser.add_argument('sum', type=int, help="请输入注册C端用户的数量")
        parser.add_argument('userIdentity', type=int, help="请输入注册C端用户的类型, 1学生、2非学生", required=True)
        parser.add_argument('isUnifiedEntrance', type=int, default=1, help="请输入注册C端用户的第一学历是否统招，1统招、0非统招")
        parser.add_argument('name', type=str, default=fake.name(), help="请输入注册C端用户的姓名")
        parser.add_argument('birthday', type=str, default='1995.10', help="请输入注册C端用户的生日")
        parser.add_argument('liveCity', type=str, default='北京', help="请输入注册C端用户的基本信息的生活所在地")
        parser.add_argument('joinWorkTime', type=str, default='2018.07', help="请输入注册C端用户参加工作的时间")
        parser.add_argument('education', type=str, default='本科', choices=('大专', '本科', '硕士', '博士', '其他'),
                            help="请输入注册C端用户的学历层次, 例如 大专, 本科, 硕士, 博士, 其他")
<<<<<<< HEAD
        parser.add_argument('startDate', type=str, default='2009', help="请输入注册C端用户的在校时间的开始时间")
        parser.add_argument('endDate', type=str, default='2013', help="请输入注册C端用户的在校时间的结束时间")
        parser.add_argument('isUnifiedEntrance', type=int, default=1, help="教育经历是否统招")
||||||| merged common ancestors
        parser.add_argument('startDate', type=str, default='2009', help="请输入注册C端用户的在校时间的开始时间")
        parser.add_argument('endDate', type=str, default='2013', help="请输入注册C端用户的在校时间的结束时间")
=======
        parser.add_argument('startDate', type=str, default='2009.09', help="请输入注册C端用户的在校时间的开始时间")
        parser.add_argument('endDate', type=str, default='2013.07', help="请输入注册C端用户的在校时间的结束时间")
>>>>>>> test_mainprocess
        parser.add_argument('city', type=str, default='北京', help="请输入注册C端用户的求职意向的期望城市")
        parser.add_argument('positionType', type=str, default='全职', choices=('全职', '兼职', '实习'),
                            help="请输入注册C端用户的求职意向的职位类型， 例如 全职, 兼职, 实习")
        parser.add_argument('positionNameType1', help="请输入注册C端用户的求职意向的职位名称", default="开发|测试|运维类")
        parser.add_argument('positionNameType2', help="请输入注册C端用户的求职意向的职位名称", default="人工智能")
        parser.add_argument('positionName', help="请输入注册C端用户的求职意向的职位名称", default="机器学习")
        parser.add_argument('salarys', type=str, default='10k-20k', help="请输入注册C端用户的求职意向的期望薪资")
        args = parser.parse_args()

        phone_list = args['phone'].split(',')
        '''弃用sum字段, 无需作此判断
        if (len(phone_list) > 1) and args['sum']:
            return {'state': 400, 'content': "多个手机号和多个账号数量互斥, 请二选一"}
        elif len(phone_list) >= 1:
            phone_list = phone_list
        elif args['sum'] >= 1:
            phone_list = [phone_list[0] + i for i in range(args['sum'])]
        '''
        phone_sum = len(phone_list)
        countryCode_list = [args['countryCode'] for i in range(phone_sum)]
        userIdentity_list = [args['userIdentity'] for i in range(phone_sum)]

        kw = {'name': args['name'], 'birthday': args['birthday'], 'liveCity': args['liveCity'],
              'joinWorkTime': args['joinWorkTime'], 'education': args['education'], 'startDate': args['startDate'],
              'endDate': args['endDate'], 'city': args['city'], 'positionType': args['positionType'],
              'positionName': args['positionName'], 'positionNameType1': args['positionNameType1'],
              'positionNameType2': args['positionNameType2'],
<<<<<<< HEAD
              'salarys': args['salarys'],'isUnifiedEntrance': args['isUnifiedEntrance']}
||||||| merged common ancestors
              'salarys': args['salarys']}
=======
              'salarys': args['salarys'], 'isUnifiedEntrance': args['isUnifiedEntrance']}
>>>>>>> test_mainprocess
        kw_list = [kw for i in range(phone_sum)]
        c_set = set()
        e_list = []
        result_list = []
        state = 0
        pool = newPool()
        res_list = pool.map(create_resume, phone_list, countryCode_list, userIdentity_list, kw_list)
        for i, r in enumerate(res_list):
            if r[0]['state'] == 1:
                if len(r) == 8:
                    [r1, r2, r3, r4, r5, r6, r7, r8] = r
                    try:
                        for j in [r2, r3, r4, r5, r6, r7, r8]:
                            if not (j['success'] == True):
                                state = 400
                                e_list.append(phone_list[i])
                                result_list.append(j['msg'])
                            else:
                                state = 1
                                c_set.add(phone_list[i])
                    except KeyError:
                        state = 400
                        e_list.append(phone_list[i])
                        result_list.append(j['msg'])


                elif len(r) == 7:
                    [r1, r2, r4, r5, r6, r7, r8] = r
                    try:
                        for j in [r2, r4, r5, r6, r7, r8]:
                            if not (j['success'] == True):
                                state = 400
                                e_list.append(phone_list[i])
                                result_list.append(j['msg'])
                            else:
                                state = 1
                                c_set.add(phone_list[i])
                    except KeyError:
                        state = 400
                        e_list.append(phone_list[i])
                        result_list.append(j['msg'])

            else:
                state = 400
                e_list.append(phone_list[i])
                result_list.append(r[0]['message'])

        return {'state': state,
                "content": "创建简历共" + str(phone_sum) + "个, 其中创建成功" + str(len(c_set)) + "个, 创建简历失败" + str(
                    len(e_list)) + "个",
                "data": list(c_set), "errors": e_list, "detail": result_list}
