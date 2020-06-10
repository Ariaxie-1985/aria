# coding:utf-8
# @Author: Xiawang

from utils.util import form_post, get_code_token, login, get_requests, get_header, login_password
import json

def add_workAddress(header, ip_port=None):
    url = 'https://easy.lagou.com/workAddress/add.json'
    data = {
        "province": "北京",
        "provinceId": 1,
        "provinceCode": "010000000",
        "city": "北京",
        "cityId": 5,
        "cityCode": "010100000",
        "district": "朝阳区",
        "districtId": 2006,
        "districtCode": "010113000",
        "detailAddress": "望京SOHO3",
        "lat": "39.996119",
        "lng": "116.48085",
        "bizAreaIds": 100060,
        "bizAreaCodes": "010113031",
        "bizArea": "望京"
    }
    remark = "创建工作地址"
    r = form_post(url=url, data=data, headers=header, remark=remark, ip_port=ip_port)
    if r.get('state', 0) == 1:
        address_id = r['content']['data']['address']['id']
    else:
        address_id = 0
    return address_id

def createPosition_999(firstType, positionType, positionThirdType, positionName, ip_port=None):
    refer_createPosition_url = "https://easy.lagou.com/position/multiChannel/createPosition.htm"
    Position_header = get_code_token(refer_createPosition_url)
    addressId = add_workAddress(Position_header, ip_port=ip_port)
    createPosition_url = "https://easy.lagou.com/parentPosition/multiChannel/create.json"
    createPosition_data = {'isSchoolJob': '0', 'channelTypes': 'LAGOU', 'firstType': firstType,
                           'positionType': positionType,
                           'positionThirdType': positionThirdType, 'positionName': '拉勾测试' + positionName,
                           'department': '用户价值部',
                           'jobNature': '全职', 'salaryMin': '15', 'salaryMax': '25', 'education': '本科',
                           'positionBrightPoint': '20薪',
                           'positionDesc': '<p>有责任感、认真负责、能承受较大压力、对工作有自己的想法</p>',
                           'workAddressId': addressId,
                           'labels': '[{"id":"1","name":"电商"}]', 'extraInfor': '[{"labels":[{"id":"1","name":"电商"}]}]',
                           'channels': '108', 'useEnergyCard': 'false', 'recommend': 'false', 'workYear': '3-5年',
                           'typeId': '', 'newVersion': 'true'}
    remark = "发布职位"
    return form_post(url=createPosition_url, data=createPosition_data, headers=Position_header, remark=remark,
                     ip_port=ip_port)


# 发布单个职位-拉勾渠道
def post_position():
    refer_createPosition_url = "https://easy.lagou.com/position/multiChannel/createPosition.htm"
    Position_header = get_code_token(refer_createPosition_url)
    address = get_requests(url='https://easy.lagou.com/workAddress/list.json', headers=Position_header).content
    addressId = json.loads(address)['content']['rows'][0]['id']
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
    data = {'pageNo': 1}
    header = get_code_token(url=referer_url)
    r = form_post(url=url, headers=header, data=data, remark='职位类型升级')
    outerPositionId = r['content']['data']['parentPositionVOs'][0]['positions']['outerPositionId']
    return outerPositionId


def get_Address():
    header = get_code_token('https://easy.lagou.com/position/multiChannel/createPosition.htm')
    url = 'https://easy.lagou.com/workAddress/list.json'
    r = get_requests(url=url, headers=header, remark='获取地址id').content
    r = json.loads(r)
    return r['content']['rows'][0]['id']


def myOnlinePositions(pageNo, ip_port=None):
    referer_url = 'https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm?pageNo=1'
    url = 'https://easy.lagou.com/parentPosition/multiChannel/myOnlinePositions.json'
    data = {'pageNo': pageNo}
    header = get_code_token(url=referer_url, ip_port=ip_port)
    return form_post(url=url, headers=header, data=data, remark='获取在线职位', ip_port=ip_port)


def get_online_positions(pageNo=1, ip_port=None):
    referer_url = 'https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm?pageNo=1'
    url = 'https://easy.lagou.com/parentPosition/multiChannel/myOnlinePositions.json'
    data = {'pageNo': pageNo}
    header = get_code_token(url=referer_url, ip_port=ip_port)
    return form_post(url=url, headers=header, data=data, remark='获取在线职位', ip_port=ip_port)

def update_Position_pc(firstType, positionType, positionThirdType, positionName, parentPositionId,ip_port=None):
    refer_updatePosition_url = f"https://easy.lagou.com/position/multiChannel/updatePosition.htm?parentPositionId={parentPositionId}"
    Position_header = get_code_token(refer_updatePosition_url)
    addressId = add_workAddress(Position_header, ip_port=ip_port)
    updatePosition_url = "https://easy.lagou.com/parentPosition/multiChannel/update.json"
    updatePosition_data = {'isSchoolJob': '0', 'firstType': firstType,
                           'positionType': positionType,
                           'positionThirdType': positionThirdType, 'positionName': '拉勾测试' + positionName,
                           'department': '更改部门',
                           'jobNature': '全职', 'salaryMin': '30', 'salaryMax': '50', 'education': '本科',
                           'positionBrightPoint': '福利待遇好',
                           'positionDesc': '<p>编辑职位有责任感、认真负责、能承受较大压力、对工作有自己的想法</p>',
                           'workAddressId': addressId,
                           'labels': '[{"id":"1","name":"电商"}]', 'extraInfor': '[{"labels":[{"id":"1","name":"电商"}]}]',
                           'channels': '108', 'workYear': '1-3年',
                           'parentPositionId':parentPositionId,
                           'channelList': 'LAGOU',
                           'parentExtraInfo':{}}
    remark = "编辑职位"
    return form_post(url=updatePosition_url, data=updatePosition_data, headers=Position_header, remark=remark,
                     ip_port=ip_port)


def offline_position(positionId, ip_port=None):
    url = 'https://easy.lagou.com/position/offlinePosition.json'
    header = get_code_token(url='https://easy.lagou.com/position/my_online_positions.htm?pageNo=1', ip_port=ip_port)
    data = {'positionId': positionId}
    return form_post(url=url, headers=header, data=data, remark='下线职位', ip_port=ip_port)


def www_redirect_easy(ip_port=None):
    url = 'https://easy.lagou.com/dashboard/index.htm?from=c_index'
    header = get_header(url='https://www.lagou.com/', ip_port=ip_port)
    return get_requests(url=url, headers=header, remark='从主站跳转到企业版页', ip_port=ip_port)


def get_all_position_category(ip_port=None):
    url = 'https://easy.lagou.com/position/multiChannel/getAllPositionCategory.json'
    header = get_header(url='https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm?pageNo=1', ip_port=None)
    return get_requests(url=url, headers=header, remark="获取职位的全部分类", ip_port=ip_port)


def multiChannel_filter(ip_port=None):
    url = 'https://easy.lagou.com/parentPosition/multiChannel/filter.json'
    header = get_header(url='https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm?pageNo=1',
                        ip_port=ip_port)
    return form_post(url=url, headers=header, remark="职位类型(特权职位)", ip_port=ip_port)


def my_parent_positions():
    url = 'https://easy.lagou.com/parentPosition/multiChannel/myParentPositions.json'
    header = get_header(url='https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm?pageNo=1')
    return form_post(url=url, headers=header, remark="获取在线职位")


def count_by_status(ip_port=None):
    url = 'https://easy.lagou.com/parentPosition/multiChannel/countByStatus.json'
    header = get_header(url='https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm?pageNo=1',
                        ip_port=ip_port)
    return form_post(url=url, headers=header, remark="统计当前自己和公司的职位数量", ip_port=ip_port)


def my_offline_positions(pageNo, ip_port=None):
    url = 'https://easy.lagou.com/parentPosition/multiChannel/myOfflinePositions.json'
    header = get_header(url='https://easy.lagou.com/position/multiChannel/myOfflinePositions.htm?pageNo=1',
                        ip_port=ip_port)
    data = {
        'pageNo': pageNo
    }
    return form_post(url=url, headers=header, data=data, remark="获取已下线的职位", ip_port=ip_port)


def company_other_positions(pageNo):
    url = 'https://easy.lagou.com/parentPosition/multiChannel/companyOtherPositions.json'
    header = get_header(url='https://easy.lagou.com/position/multiChannel/companyOtherPositions.htm?pageNo=1')
    data = {
        'pageNo': pageNo
    }
    return form_post(url=url, headers=header, data=data, remark="获取公司其他人的职位")


def redirect_original_page(positionId, ip_port=None):
    url = 'https://easy.lagou.com/position/redirectOriginalPage.htm?positionId={}'.format(positionId)
    header = get_header(url='https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm?pageNo=1',
                        ip_port=ip_port)
    remark = '获取职位详情'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port)


def batch_refresh_info(ip_port=None):
    url = 'https://easy.lagou.com/position/batchRefreshInfo.json'
    refer_url = f'https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm?pageNo=1&citys=&publishUserId=&channelTypes=&typeId=&firstTypes=&keyword='
    header = get_code_token(url=refer_url, ip_port=ip_port)
    remark = '批量刷新职位'
    return form_post(url=url, headers=header, remark=remark, ip_port=ip_port)


def plus_search_selector(ip_port=None):
    url = 'https://easy.lagou.com/search/plusSearchSelector.json?from=talentsearch'
    refer_url = 'https://easy.lagou.com/talent/index.htm?'
    header = get_header(url=refer_url, ip_port=ip_port)
    remark = '人才搜索筛选器'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port)


def will_offline_positionCount(ip_port=None):
    url = 'https://easy.lagou.com/parentPosition/multiChannel/willOfflinePositionCount.json'
    refer_url = 'https://easy.lagou.com/bstatus/auth/index.htm?'
    header = get_header(url=refer_url, ip_port=ip_port)
    remark = '统计将要下线的职位'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port)
