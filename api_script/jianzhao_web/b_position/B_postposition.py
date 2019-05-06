# coding:utf-8
# @Author: Xiawang
from utils.util import form_post, get_code_token, login ,get_requests
import json

# 发布单个职位-拉勾渠道
def post_position():
    refer_createPosition_url = "https://easy.lagou.com/position/multiChannel/createPosition.htm"
    Position_header = get_code_token(refer_createPosition_url)
    address=get_requests(url='https://easy.lagou.com/workAddress/list.json',headers=Position_header).content
    addressId=json.loads(address)['content']['rows'][0]['id']
    createPosition_url = "https://easy.lagou.com/parentPosition/multiChannel/create.json"
    createPosition_data = {'isSchoolJob': '1', 'channelTypes': 'LAGOU', 'firstType': '开发|测试|运维类',
                           'positionType': '后端开发',
                           'positionThirdType': 'Python', 'positionName': 'python后端开发拉勾测试', 'department': '111',
                           'jobNature': '全职', 'salaryMin': '11', 'salaryMax': '12', 'education': '不限',
                           'positionBrightPoint': '11111',
                           'positionDesc': '<p>111111111111111111111111111111111111111111111</p>',
                           'workAddressId': addressId,
                           'labels': '[{"id":"1","name":"电商"}]', 'extraInfor': '[{"labels":[{"id":"1","name":"电商"}]}]',
                           'channels': '108', 'useEnergyCard': 'false', 'recommend': 'false', 'workYear': '应届毕业生',
                           'typeId': ''}
    remark = "发布职位"
    return form_post(url=createPosition_url, data=createPosition_data, headers=Position_header, remark=remark)


def republish_position():
    url = 'https://easy.lagou.com/parentPosition/multiChannel/republishOfflinePosition.json'
    header = get_code_token('https://easy.lagou.com/position/multiChannel/myOfflinePositions.htm')
    data = {
        'parentPositionId': '1787471',
        # 'parentPositionId': 1628497,
        'attachParam': ''
    }
    return form_post(url=url, headers=header, data=data, remark='重新发布')


def update_position():
    url = 'https://easy.lagou.com//parentPosition/multiChannel/upgradePosition.json'
    header = get_code_token('https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm')
    data = {
        # 'parentPositionId':1787474,
        'parentPositionId': 1628497
        # 'attachParam':'{"typeId":2,"step":"TWO"}'
    }
    return form_post(url=url, headers=header, data=data, remark='职位类型升级')


def get_outerPositionId():
    referer_url = 'https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm?pageNo=1'
    url = 'https://easy.lagou.com/parentPosition/multiChannel/myOnlinePositions.json'
    data = {'pageNo':1}
    header = get_code_token(url=referer_url)
    r=form_post(url=url, headers=header, data=data, remark='职位类型升级')
    outerPositionId = r['content']['data']['parentPositionVOs'][0]['positions']['outerPositionId']
    return outerPositionId

def get_Address():
    header = get_code_token('https://easy.lagou.com/position/multiChannel/createPosition.htm')
    url = 'https://easy.lagou.com/workAddress/list.json'
    r=get_requests(url=url,headers=header,remark='获取地址id').content
    r=json.loads(r)
    return r['content']['rows'][0]['id']


def myOnlinePositions(pageNo):
    referer_url = 'https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm?pageNo=1'
    url = 'https://easy.lagou.com/parentPosition/multiChannel/myOnlinePositions.json'
    data = {'pageNo': pageNo}
    header = get_code_token(url=referer_url)
    return form_post(url=url, headers=header, data=data, remark='获取在线职位')