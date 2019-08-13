# coding:utf-8
# @Time  : 2019-08-08 14:38
# @Author: Xiawang

# coding:utf-8
import random
import time

import pymysql
import requests
from faker import Faker

from api_script.jianzhao_web.b_basic.company import saveCompanyProfile
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import b_register
from backend.common.batch_company_positions import post_position
from utils.util import get_code_token, login, get_requests

fake = Faker("zh_CN")


def phone_prodiver():
    '''生成B端注册手机号'''
    success_list = []
    for phone in range(20030528, 20030828):
        res = b_register(phone=phone, countryCode='00853')
        if res['state'] == 1:
            success_list.append(phone)

        if len(success_list) == 210:
            break
    print(len(success_list), )
    return success_list


def address_id(code):
    '''code: 市的code, 获取市的区域的code, 返回lbsList'''
    login('00852', 20181205)
    url = 'https://easy.lagou.com/lbs/getChildLbsInfoByCode.json?code={}'.format(code)
    header = get_code_token(url='https://easy.lagou.com/position/multiChannel/createPosition.htm')
    remark = '获取地址id'
    content = get_requests(url=url, headers=header, remark=remark).json()
    return content['content']['data']['lbsList']


def parse_address(data):
    '''将lbsList处理成直辖市及省及其区域的id'''
    ids = {}
    for address in data:
        ids[address['name']] = address['id']
    print(ids)
    return ids


def connect_lagou():
    db = pymysql.connect(
        host='10.1.200.166',
        port=3306,
        user='lagouro',
        passwd='Q12_#*s#$opIx',
        db='lagou',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = db.cursor()
    return db, cursor


def province_company_address(cursor, province):
    '''查出省及直辖市的前200个地址数据, 清洗为需要的数据'''
    address_list = []
    sql = 'SELECT detailAddress,province,city,district,businessArea,lat,lng,companyId,userId FROM company_address WHERE province = "{}" and businessArea != "" and lat != "" and lng != "" LIMIT 200'.format(
        province)
    cursor.execute(sql)
    results = cursor.fetchall()
    for result in results:
        address_dict = {}
        address_dict['detailAddress'] = result['detailAddress']
        address_dict['provinceId'] = result['province']
        address_dict['cityId'] = result['city']
        address_dict['districtId'] = result['district']
        address_dict['businessArea'] = result['businessArea']
        address_dict['companyLng'] = result['lng']
        address_dict['companyLat'] = result['lat']
        address_dict['companyId'] = result['companyId']
        address_dict['userId'] = result['userId']
        address_list.append(address_dict)
    print(address_list)
    return address_list


def format_address(address_list, ids):
    '''把地址数据的str换成int, 其中'''
    for address_info in address_list:
        if address_info['provinceId'] == '上海':
            address_info['provinceId'] = 2

        if address_info['cityId'] == '上海':
            address_info['cityId'] = 5

        address_info['districtId'] = ids[address_info['districtId']]
    print(address_list)
    return address_list


def create_company(company_info):
    success_company_list = []
    fail_company_list = []
    checkedindustryField_list = ['电商', '金融', '企业服务', '教育', '文娱丨内容', "游戏", "消费生活", "硬件", "社交", "旅游",
                                 "体育", "工具", "汽车丨出行", "物流丨运输", "医疗丨健康", "广告营销", "数据服务"]
    financeStage_list = ['C轮', 'D轮及以上', '上市公司']

    url = 'http://127.0.0.1:18980/jianzhao/company/registration'
    for index, phone in enumerate(new_phone_list):
        try:
            company_info_dict = {}
            company_name = fake.company()
            data = {
                'companyFullName': company_name,
                'companyShortName': company_name,
                'countryCode': '00853',
                'phone': phone,
                'resumeReceiveEmail': fake.company_email(),
                'updateCompanyShortName': company_name,
                'userName': fake.name(),
                'userPosition': fake.job(),
                'detailAddress': company_info[index]['detailAddress'],
                'provinceId': company_info[index]['provinceId'],
                'cityId': company_info[index]['cityId'],
                'districtId': company_info[index]['districtId'],
                'businessArea': company_info[index]['businessArea'],
                'companyLng': company_info[index]['companyLng'],
                'companyLat': company_info[index]['companyLat'],
                'checkedindustryField': checkedindustryField_list[random.randint(0, 16)],
                'financeStage': financeStage_list[random.randint(0, 2)]
            }
        except:
            continue
        try:
            res = requests.post(url=url, data=data).json()
        except:
            continue
        if res['state'] == 1:
            company_info_dict['phone'] = res['data']['HRInfo']['phone']
            company_info_dict['companyId'] = res['data']['CompanyInfo']['companyId']
            success_company_list.append(company_info_dict)
            print('第{}个公司创建成功'.format(len(success_company_list)))
        else:
            company_info_dict['phone'] = res['data']['HRInfo']['phone']
            company_info_dict['companyId'] = res['data']['CompanyInfo']['companyId']
            fail_company_list.append(company_info_dict)
        if len(success_company_list) == 150:
            break
        time.sleep(1)
    print(success_company_list)
    return success_company_list


def update_address_list():
    ''''''
    # company_list = phone_company()
    db, cursor = connect_lagou()
    for com in company_list:
        companyId = com['companyId']
        cursor.execute("SELECT id,userId FROM company_address WHERE companyId = {}".format(companyId))
        address_id = cursor.fetchall()[0]
        com.update(address_id)
    print(company_list)
    return company_list


def create_company_picture(company_info):
    '''创建公司图集'''
    for da in company_info:
        login('00853', da['phone'])
        r = saveCompanyProfile(da['companyId'])
        if r['state'] == 1:
            da['pic'] = 1
            print(str(da['companyId']) + '公司图片添加成功')
        else:
            continue
        return company_info


def post_xiaozhao_position(data):
    # data = provider_data()
    for da in data:
        r = post_position(da['phone'], da['id'])
        da.update(r)
    print(data)
    return data


if __name__ == '__main__':
    # phone_list = phone_prodiver()
    # lbsList = address_id(code=)
    # address_ids = parse_address(data=lbsList)
    # db, cursor = connect_lagou()
    # address_list = province_company_address(cursor, province='')
    # parse_address_list = format_address(address_list=address_list, ids=address_ids)

    # company_info = provider_sh_data()
    # company_list = create_company(company_info)

    create_company_picture()
