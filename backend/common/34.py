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
import pymysql
from pathos.multiprocessing import ProcessingPool as newPool
from utils.util import form_post, get_code_token, login


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
    cursor.execute('select id,biz_area from t_work_address where city = "{}"'.format(city))
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


def run(address_list):
    error = 0
    success = 0
    pool = newPool()
    sum_list = [1 for x in range(len(address_list))]
    res_list = pool.map(post_position, sum_list, address_list)
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


def post_position(sum, addressId):
    '''
    批量发布职位
    :param sum: 发布职位个数
    :return: 发布职位的请求

    '''
    login('00852', 20021215)
    reslist = []
    for i in range(sum):
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
                               "firstType": "开发|测试|运维类",
                               "positionType": "后端开发",
                               "positionThirdType": "Java",
                               "positionName": "高级Java"}

        remark = "批量发布职位" + str(sum) + "个成功"
        r = form_post(
            url=createPosition_url,
            data=createPosition_data,
            headers=Position_header,
            remark=remark)
        reslist.append(r)
    return reslist


if __name__ == '__main__':
    db_data = get_data('北京')
    address_list = process_data(db_data)
    run(address_list)
