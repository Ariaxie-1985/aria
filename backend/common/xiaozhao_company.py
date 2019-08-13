# coding:utf-8
# @Time  : 2019-07-31 17:31
# @Author: Xiawang
import random
import time

import requests
from faker import Faker

# 注册账号
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import b_register
from backend.common.data import provider_data, provider_sh_data

success_list = []

# for phone in range(20033290, 20033500):
#     res = b_register(phone=phone, countryCode='00853')
#     if res['state'] == 1:
#         success_list.append(phone)
#
#     if len(success_list) == 120:
#         break
# print(len(success_list),)
# print(success_list)




new_phone_list = [20033290, 20033291, 20033292, 20033293, 20033294, 20033295, 20033296, 20033297, 20033298, 20033299, 20033300, 20033301, 20033302, 20033303, 20033304, 20033305, 20033306, 20033307, 20033308, 20033309, 20033310, 20033311, 20033312, 20033313, 20033314, 20033315, 20033316, 20033317, 20033318, 20033319, 20033320, 20033321, 20033322, 20033323, 20033324, 20033325, 20033326, 20033327, 20033328, 20033329, 20033330, 20033331, 20033332, 20033333, 20033334, 20033335, 20033336, 20033337, 20033338, 20033339, 20033340, 20033341, 20033342, 20033343, 20033344, 20033345, 20033346, 20033347, 20033348, 20033349, 20033350, 20033351, 20033352, 20033353, 20033354, 20033355, 20033356, 20033357, 20033358, 20033359, 20033360, 20033361, 20033362, 20033363, 20033364, 20033365, 20033366, 20033367, 20033368, 20033369, 20033370, 20033371, 20033372, 20033373, 20033374, 20033375, 20033376, 20033377, 20033378, 20033379, 20033380, 20033381, 20033382, 20033383, 20033384, 20033385, 20033386, 20033387, 20033388, 20033389, 20033390, 20033391, 20033392, 20033393, 20033394, 20033395, 20033396, 20033397, 20033398, 20033399, 20033400, 20033401, 20033402, 20033403, 20033404, 20033405, 20033406, 20033407, 20033408, 20033409]

# 创建公司
fake = Faker("zh_CN")
success_company_list = []
fail_company_list = []
checkedindustryField_list = ['电商', '金融', '企业服务', '教育', '文娱丨内容', "游戏", "消费生活", "硬件", "社交", "旅游",
                             "体育", "工具", "汽车丨出行", "物流丨运输", "医疗丨健康", "广告营销", "数据服务"]
financeStage_list = ['C轮', 'D轮及以上', '上市公司']
company_info = {'detailAddress': '明发商业广场5栋', 'provinceId': 539, 'cityId': 635, 'districtId': 2093, 'businessArea': '岔路口,宁南', 'companyLng': '118.80421655', 'companyLat': '31.97069981', 'companyId': 430, 'userId': 1419}


url = 'http://127.0.0.1:18980/jianzhao/company/registration'
for index, phone in enumerate(new_phone_list):
    company_info_dict = {}
    company_name = fake.company() + str(random.randint(100000, 999999))
    try:
        data = {
            'companyFullName': company_name,
            'companyShortName': company_name,
            'countryCode': '00853',
            'phone': phone,
            'resumeReceiveEmail': fake.company_email(),
            'updateCompanyShortName': company_name,
            'userName': fake.name(),
            'userPosition': fake.job(),
            'detailAddress': company_info['detailAddress'],
            'provinceId': company_info['provinceId'],
            'cityId': company_info['cityId'],
            'districtId': company_info['districtId'],
            'businessArea': company_info['businessArea'],
            'companyLng': company_info['companyLng'],
            'companyLat': company_info['companyLat'],
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
        print('第{}个公司创建成功,公司id: {}'.format(len(success_company_list), res['data']['CompanyInfo']['companyId']))

    if len(success_company_list) == 120:
        break
    time.sleep(1)

print(len(success_company_list))
print(success_company_list)


def post_hetong_chanping(companyId, contractNo, userId):
    url = 'http://10.1.200.141:18980/home/import'
    data = {'companyId': companyId, 'contractNo': contractNo}
    r = requests.post(url=url, json=data).json()
    if r['state'] == 1:
        return 0
    url = 'http://10.1.200.141:18980/home/product'
    data = {'companyId': companyId, 'can': False, 'startTimeStr': "2019-08-07", 'endTimeStr': "2020-08-07",
            "userId": userId, "templateName": "免费灰度模板"}
    r = requests.post(url=url, json=data).json()
    if r['state'] == 1:
        return {'template': '免费灰度模板'}
    else:
        return 0

    # if __name__ == '__main__':
    # data = provider_data()
    # for da in data:
    #     contractNo = "lg_20190807_xiaozhao_" + str(da['companyId'])
    #     r = post_hetong_chanping(da['companyId'], contractNo, da['userId'])
    #     if r == 0:
    #         data.remove(da)
    #         continue
    #     da.update(r)
    # print(data)
    pass
