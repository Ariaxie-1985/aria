# coding:utf-8
# @Author: Xiawang

from utils.util import form_post, get_code_token, login
import random
from api_script.jianzhao_web.b_position.B_postposition import get_Address

# 批量发布职位-拉勾渠道
postype = [{'firstType': '开发|测试|运维类', 'positionType': '人工智能', 'positionThirdType': '机器学习', 'positionName': '机器学习'},
           {'firstType': '产品|需求|项目类', 'positionType': '产品经理', 'positionThirdType': '产品经理', 'positionName': '产品经理'},
           {'firstType': '设计类', 'positionType': '交互', 'positionThirdType': '交互设计师', 'positionName': 'UI设计'},
           {'firstType': '运营|编辑|客服类', 'positionType': '运营', 'positionThirdType': '用户运营', 'positionName': '用户运营'},
           {'firstType': '市场|商务类', 'positionType': '市场|营销', 'positionThirdType': '市场营销', 'positionName': '市场营销'},
           {'firstType': '销售类', 'positionType': '销售', 'positionThirdType': '销售经理', 'positionName': '销售经理'},
           {'firstType': '综合职能|高级管理', 'positionType': '人力资源', 'positionThirdType': 'HRBP', 'positionName': 'HRBP'},
           {'firstType': '金融类', 'positionType': '互联网金融', 'positionThirdType': '金融产品经理', 'positionName': '金融产品经理'},
           {'firstType': '非互联网职位', 'positionType': '生产|加工|制造', 'positionThirdType': '技工', 'positionName': '模具工'}]


def post_position(sum):
    '''
    批量发布职位
    :param sum: 发布职位个数
    :return: 发布职位的请求

    '''
    reslist = []
    addressId = get_Address()
    for i in range(sum):
        a = random.randint(0, 7)
        postype_t = postype[a]
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
                               **postype_t}
        remark = "批量发布职位" + str(sum) + "个成功"
        r = form_post(
            url=createPosition_url,
            data=createPosition_data,
            headers=Position_header,
            remark=remark)
        reslist.append(r)
    return reslist
