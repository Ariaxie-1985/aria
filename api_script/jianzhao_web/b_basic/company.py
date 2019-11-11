# coding:utf-8
# @Time  : 2019-07-31 18:20
# @Author: Xiawang
import json

from backend.common.data import provider_data
from utils.util import get_code_token, form_post, login, get_header


def saveCompanyProfile(companyId):
    url = 'https://hr.lagou.com/company/cm/saveCompanyProfile.json'
    pictures_json = json.dumps(
        [{"id": 206, "position": "1", "companyPicUrl": "/i/audio1/M00/05/F3/CgHIk10lnHSANkTQAAC6itmGn1w448.png"},
         {"id": "", "position": 0, "companyPicUrl": "/i/audio1/M00/06/05/CgHIk11BaWKALtpVAAEoI9bVYwY969.jpg"},
         {"id": "", "position": 0, "companyPicUrl": "/i/audio1/M00/06/05/CgHIk11BaWeAUOqcAABMcB8E_pY121.jpg"},
         {"id": "", "position": 0, "companyPicUrl": "/i/audio1/M00/06/05/CgHIk11BaWuASAN7AAA1YWgPAhY478.jpg"},
         {"id": "", "position": 0, "companyPicUrl": "/i/audio1/M00/06/05/CgHIk11BaXCABl1PAABBmgrr02I143.jpg"},
         {"id": "", "position": 0, "companyPicUrl": "/i/audio1/M00/06/05/CgHIk11BaXSAUshdAABvs1jNIJ8266.jpg"}])
    data = {
        'companyId': companyId,
        'companyProfile': '<p>愿天下没有难找的工作</p>',
        'pictures': pictures_json
    }
    header = get_code_token(url='https://hr.lagou.com/company/gongsi/{}.html'.format(companyId))
    remark = '公司介绍添加图片'
    return form_post(url=url, data=data, headers=header, remark=remark)


def isHuntingGray():
    succ_list = []
    url = 'https://easy.lagou.com/api/onlinehunting/isHuntingGray.json'
    header = get_header(url='https://easy.lagou.com/bstatus/auth/index.htm')
    r = form_post(url=url, headers=header, remark='判断公司是否认证')
    if r['content']['data']['isGray'] == True:
        return True
    else:
        return False


