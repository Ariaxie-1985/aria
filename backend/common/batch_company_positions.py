# coding:utf-8
# @Time  : 2019-06-25 12:01
# @Author: Xiawang

'''
根据每个商圈的所有工作地址发布职位
1.连接数据库，创建游标
2.获取数据并加工
3.执行请求、输出日志
'''
import json
import random

import pymysql
from pathos.multiprocessing import ProcessingPool as newPool
from utils.util import form_post, get_code_token, login, json_post


def get_data(city):
    def connect_db():  # 闭包, 保证数据库配置的安全性
        db = pymysql.connect(
            host='10.1.200.166',
            port=3306,
            user='lagouro',
            passwd='Q12_#*s#$opIx',
            db='testing_platform',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = db.cursor()
        return db, cursor

    db, cursor = connect_db()
    db.ping(reconnect=True)
    cursor.execute('select id,biz_area from t_work_address where city = "{}" limit 200'.format(city))
    return cursor.fetchall()


def process_data(db_data):
    '''
    将有商圈的 address_id 去重放入 list 中
    :param db_data: list
    '''
    id_area_data = []
    for biz_areas in db_data:
        try:
            biz_area = json.loads(biz_areas['biz_area'])
        except:
            continue
        if not bool(biz_area) == False or biz_area == '""':
            address_id = biz_areas['id']
            id_area_data.append(int(address_id))
    return list(set(id_area_data))


def run(phone_list, address_list):
    error = 0
    success = 0
    pool = newPool()
    res_list = pool.map(post_position, phone_list, address_list)
    for index, value in enumerate(res_list):
        if 'state' not in value[0] or value[0]['state'] != 1:
            error = error + 1
            continue

        if value[0]['state'] == 1:
            success = success + 1

        if len(address_list) % 1000 == 0:
            print('发布职位完成 {} 个'.format(index + 1))
    print('~~~~~~~~~~~~~~~~~~~~~~' * 8)
    print('成功发布职位 {} 个'.format(success))
    print('失败发布职位 {} 个'.format(error))


def post_position(phone, addressId):
    '''
    批量发布职位
    :param sum: 发布职位个数
    :return: 发布职位的请求

    '''
    login('00852', phone)
    reslist = []
    posit_list = [('开发|测试|运维类', '后端开发', 'Java', '高级Java'), ('开发|测试|运维类', '移动前端开发', 'IOS', '高级IOS'),
                  ('开发|测试|运维类', '移动前端开发', 'Android', '高级Android')]
    for i in range(3):
        refer_createPosition_url = "https://easy.lagou.com/position/multiChannel/createPosition.htm"
        Position_header = get_code_token(refer_createPosition_url)
        createPosition_url = "https://easy.lagou.com/parentPosition/multiChannel/create.json"
        createPosition_data = {**{'isSchoolJob': '0',
                                  'channelTypes': 'LAGOU',
                                  'department': '111',
                                  'jobNature': '全职',
                                  'salaryMin': '11',
                                  'salaryMax': '12',
                                  'education': '不限',
                                  'workAddressId': addressId,
                                  'positionBrightPoint': '11111',
                                  'workYear': '3-5年',
                                  'channels': '108',
                                  'recommend': True,
                                  'extraInfor': '[{"labels":[{"id":"1","name":"电商"}]}]',
                                  'positionDesc': '<p>111111111111111111111111111111111111111111111</p>',
                                  'labels': '[{"id":"1","name":"电商"}]',
                                  'parentExtraInfo': '{}',
                                  "useEnergyCard": False},
                               "firstType": posit_list[i][0],
                               "positionType": posit_list[i][1],
                               "positionThirdType": posit_list[i][2],
                               "positionName": posit_list[i][3]}

        remark = "批量发布职位" + str(sum) + "个成功"
        r = form_post(
            url=createPosition_url,
            data=createPosition_data,
            headers=Position_header,
            remark=remark)
        reslist.append(r)
    return reslist


def setup_data(phone):
    phone_list = []
    # url_b = 'http://10.1.200.141:9004/entry/registration'
    url_b = 'http://127.0.0.1:9004/entry/registration'
    data_b = {
        "countryCode": "00852",
        "phone": phone,
        "type": 'b'
    }
    r1 = json_post(url=url_b, headers={}, data=data_b, remark='注册B端')
    if r1['state'] == 1:
        url = 'http://127.0.0.1:9004/jianzhao/company/registration'
        data = {
            "countryCode": "00852",
            "phone": phone
        }
        r = json_post(url=url, headers={}, data=data, remark='创建公司')
        if r.get('state', 0) == 1:
            phone_list.append(phone)
    return phone_list


def run_setup():
    phone_list = [x + 1 for x in range(60000000, 90000000)]
    pool = newPool()
    res_list = pool.map(setup_data, phone_list)
    return res_list

postype = [{'firstType': '开发|测试|运维类', 'positionType': '人工智能', 'positionThirdType': '机器学习', 'positionName': '机器学习'},
           {'firstType': '产品|需求|项目类', 'positionType': '产品经理', 'positionThirdType': '产品经理', 'positionName': '产品经理'},
           {'firstType': '设计类', 'positionType': '交互', 'positionThirdType': '交互设计师', 'positionName': 'UI设计'},
           {'firstType': '运营|编辑|客服类', 'positionType': '运营', 'positionThirdType': '用户运营', 'positionName': '用户运营'},
           {'firstType': '市场|商务类', 'positionType': '市场|营销', 'positionThirdType': '市场营销', 'positionName': '市场营销'},
           {'firstType': '销售类', 'positionType': '销售', 'positionThirdType': '销售经理', 'positionName': '销售经理'},
           {'firstType': '综合职能|高级管理', 'positionType': '人力资源', 'positionThirdType': 'HRBP', 'positionName': 'HRBP'},
           {'firstType': '金融类', 'positionType': '互联网金融', 'positionThirdType': '金融产品经理', 'positionName': '金融产品经理'},
           {'firstType': '非互联网职位', 'positionType': '生产|加工|制造', 'positionThirdType': '技工', 'positionName': '模具工'}]


def post_position_city(sum, addressId):
    '''
    批量发布职位
    :param sum: 发布职位个数
    :return: 发布职位的请求

    '''
    reslist = []
    login('00852', 20181205)
    for i in range(sum):
        position_info = postype[random.randint(0,8)]
        firstType = position_info['firstType']
        positionType = position_info['positionType']
        positionThirdType = position_info['positionThirdType']
        positionName = position_info['positionName']
        refer_createPosition_url = "https://easy.lagou.com/position/multiChannel/createPosition.htm"
        Position_header = get_code_token(refer_createPosition_url)
        createPosition_url = "https://easy.lagou.com/parentPosition/multiChannel/create.json"
        createPosition_data = {**{'isSchoolJob': '1',
                                  'channelTypes': 'LAGOU',
                                  'department': '111',
                                  'jobNature': '全职',
                                  'salaryMin': '11',
                                  'salaryMax': '12',
                                  'education': '不限',
                                  'workAddressId': addressId,
                                  'positionBrightPoint': '11111',
                                  'workYear': '应届毕业生',
                                  'channels': '108',
                                  'recommend': True,
                                  'extraInfor': '[{"labels":[{"id":"1","name":"电商"}]}]',
                                  'positionDesc': '<p>111111111111111111111111111111111111111111111</p>',
                                  'labels': '[{"id":"1","name":"电商"}]',
                                  'parentExtraInfo': '{}',
                                  "useEnergyCard": False},
                               "firstType": firstType,
                               "positionType": positionType,
                               "positionThirdType": positionThirdType,
                               "positionName": positionName+str(random.randint(10,110))}

        remark = "批量发布职位" + str(sum) + "个成功"
        r = form_post(
            url=createPosition_url,
            data=createPosition_data,
            headers=Position_header,
            remark=remark)
        reslist.append(r)
    return reslist

if __name__ == '__main__':
    db_data = get_data('成都')
    # print(db_data)
    # phone_list = run_setup()
    sum_list = [i for i in range(100)]
    # print(sum_list)
    address_list = process_data(db_data)
    # print(len(address_list))
    pool = newPool()

    b_phone_list = pool.map(post_position_city, sum_list, address_list)

    # run(b_phone_list, address_list)
    # setup_data(18900208)
