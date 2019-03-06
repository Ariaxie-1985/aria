# coding:utf-8
# @Author: Xiawang
from utils.util import form_post, get_code_token, login


# 发布单个职位-拉勾渠道
def post_position():
    refer_createPosition_url = "https://easy.lagou.com/position/multiChannel/createPosition.htm"
    Position_header = get_code_token(refer_createPosition_url)
    createPosition_url = "https://easy.lagou.com/parentPosition/multiChannel/create.json"
    createPosition_data = {'isSchoolJob': '1', 'channelTypes': 'LAGOU', 'firstType': '开发|测试|运维类',
                           'positionType': '后端开发',
                           'positionThirdType': 'Python', 'positionName': 'python后端开发拉勾测试', 'department': '111',
                           'jobNature': '全职', 'salaryMin': '11', 'salaryMax': '12', 'education': '不限',
                           'positionBrightPoint': '11111',
                           'positionDesc': '<p>111111111111111111111111111111111111111111111</p>',
                           'workAddressId': '7',
                           'labels': '[{"id":"1","name":"电商"}]', 'extraInfor': '[{"labels":[{"id":"1","name":"电商"}]}]',
                           'channels': '108', 'useEnergyCard': 'false', 'recommend': 'false', "useEnergyCard": "false",
                           'workYear': '1-3年', 'typeId': ''}
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


# login('00853', '05180001')
# post_position()
# republish_position()
# update_position()
