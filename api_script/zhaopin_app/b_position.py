# coding:utf-8
# @Time  : 2019-01-14 14:41
# @Author: Xiawang
import random

from api_script.entry.account.passport import password_login
from utils.util import get_app_header, get_requests, json_post, json_put, app_header_999, get_app_header1

host = "https://gate.lagou.com/v1/zhaopin"
headers = get_app_header(100014641)


def positions_category(userToken, userId=None, ip_port=None):
    url = 'https://gate.lagou.com/v1/zhaopin/positions/category'
    header = app_header_999(userToken=userToken, userId=userId)
    remark = '获取职业静态信息'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def positions_static_info():
    url = host + "/positions/static_info"
    remark = "查看职位详情"
    return get_requests(url=url, headers=headers, remark=remark).json()


def category_mapping(userToken, positionName, userId=None, ip_port=None):
    '''
    职位名称映射职位分类
    :param positionName: str, 职位名称
    :return:
    '''
    url = host + "/positions/category_mapping?positionName={}".format(positionName)
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = "职位名称映射职位分类"
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def positions_tag_report(firstCateGory, secCategory, tagName):
    url = host + "/positions/tag_report"
    data = {
        "secCategory": secCategory,
        "firstCateGory": firstCateGory,
        "tagName": tagName
    }
    remark = "职位标签上报"
    return json_post(url=url, headers=headers, data=data, remark=remark)


def publish_position_check():
    '''
    发布职位前校验
    :return:
    '''
    url = host + "/positions/publish_position_check"
    remark = "发布职位前校验"
    return get_requests(url=url, headers=headers, remark=remark).json()


def post_positions(firstType='开发|测试|运维类', workyear='应届毕业生', positionType='后端开发', positionThirdType='Java',
                   positionName='java开发工程师', typeid=None, userid=100014641, workAddressId=191880):
    '''
    发布职位
    :return:
    '''
    url = host + "/positions/publish"
    data = {
        "isConfirm": False,
        "recommend": True,
        "labels": [{
            "name": "旅游",
            "id": 9,
            "isExpanded": False,
            "isSelected": False,
            "isSubTag": False
        }, {
            "name": "本地生活",
            "id": 5,
            "isExpanded": False,
            "isSelected": False,
            "isSubTag": False
        }],
        "positionType": positionType,
        "positionDesc": "<p>11111111111111111111111111111</p>",
        "positionId": 0,
        "workYear": workyear,
        "salaryMin": 20,
        "firstType": firstType,
        "positionName": positionName,
        "positionBrightPoint": "20薪",
        "positionThirdType": positionThirdType,
        "jobNature": "全职",
        "education": "本科",
        "workAddressId": workAddressId,
        # "recruitmentType":1,
        # "workAddressId": 191882,
        "department": "技术部",
        "salaryMax": 30,
        "id": typeid
    }
    remark = "发布职位"
    headers = get_app_header1(userid)
    return json_post(url=url, headers=headers, data=data, remark=remark)


def positions_details(userToken, positionId, userId=None, ip_port=None):
    '''
    查看职位详情
    :param positionId: int
    :return:
    '''
    url = host + "/positions/{}/details".format(positionId)
    header = app_header_999(userToken, DA=False, userId=userId)
    remark = "查看职位详情"
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def update_position(positionId, workAddressId):
    '''
    编辑职位
    :param positionId:
    :return:
    '''
    url = host + "/positions/update"
    data = {
        "education": "本科",
        "positionId": positionId,
        "workAddressId": workAddressId,
        "jobNature": "全职",
        "positionDesc": "22222222222222222222",
        "workYear": "应届毕业生",
        "department": "技术工程部",
        "positionBrightPoint": "50薪",
        "salaryMin": 25,
        "labels": [{
            "name": "旅游",
            "id": 9
        }, {
            "name": "本地生活",
            "id": 5
        }],
        "salaryMax": 30
    }
    remark = "编辑职位"
    return json_put(url=url, headers=headers, data=data, remark=remark)


def get_online_positions(ip_port=None, userToken=None, H9=False, userId=None):
    '''
    获取在线职位列表
    :return:
    '''
    if H9 == True:
        header = app_header_999(userToken, DA=False, userId=userId)
    else:
        userId = 100014641
        header = get_app_header(userId)
    url = host + "/positions/online/pages?pageNo=1&pageSize=80"
    remark = "获取在线职位列表"
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def get_offline_positions(userToken, userId=None, ip_port=None):
    url = host + "/positions/offline/pages"
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = "获取已下线列表"
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def get_other_positions(userToken, userId=None, ip_port=None):
    url = host + "/positions/company/other/pages"
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = "获取其他职位列表"
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def refresh_position(positionId, reqVersion=None, userId=100014641):
    url = host + "/positions/{}/refresh_position".format(positionId)
    data = {
        "isConfirm": False
    }
    headers = get_app_header(userId, reqVersion)
    remark = "刷新职位"
    return json_put(url=url, data=data, headers=headers, remark=remark)


def up_position_ranking(positionId, reqVersion=None, userId=100014641):
    url = host + "/positions/{}/up_position_ranking".format(positionId)
    data = {
        "isConfirm": False
    }
    headers = get_app_header(userId, reqVersion)
    remark = "提升职位排名"
    return json_put(url=url, data=data, headers=headers, remark=remark)


def positions_top_check(positionId):
    url = host + "/positions/top/{}/check".format(positionId)
    remark = "职位置顶卡校验信息"
    return get_requests(url=url, headers=headers, remark=remark).json()


def apply_privilege_position(userId):
    '''
    Args:
    userId: int, 没有被分特权职位的有子账号的分账号的userId
    :return:
    '''
    url = host + "/positions/apply_privilege_position"
    headers = get_app_header(userId)
    remark = "申请特权职位权益"
    return get_requests(url=url, headers=headers, remark=remark).json()


def positions_is_hot(userToken, positionName, userId=None, ip_port=None):
    url = host + "/positions/is_hot?positionName=" + positionName
    headers = app_header_999(userToken, DA=False, userId=userId)
    remark = "是否热门职位"
    return json_post(url=url, headers=headers, remark=remark, ip_port=ip_port)


def positions_invite(userToken, positionId, userId=None, ip_port=None):
    '''
    批量邀约候选人
    :param positionId: int, 职位id
    :param userId: list, 候选人的userId
    :return:
    '''
    url = host + "/positions/invite"
    data = {
        "positionId": positionId,
        "userIds": [userId]
    }
    headers = app_header_999(userToken, DA=False, userId=userId)
    remark = "批量邀约候选人"
    return json_post(url=url, data=data, headers=headers, remark=remark, ip_port=ip_port)


def positions_recommend(positionId):
    '''
    职位推荐
    :param positionId: int, 职位id
    :return:
    '''
    url = host + "/positions/recommend?positionId=" + positionId
    remark = "获取职位推荐"
    return json_post(url=url, headers=headers, remark=remark)


def positions_red_point_hint(userToken,ip_port=None, userId=None):
    url = host + "/positions/red_point_hint"
    header = app_header_999(userToken, DA=False,userId=userId)
    remark = "首页导航职位红点"
    return get_requests(url=url, remark=remark, headers=header,ip_port=ip_port).json()


def positions_details_app(positionId):
    url = host + '/positions/{}/details/app'.format(positionId)
    remark = '获取职位详情新'
    return get_requests(url=url, remark=remark, headers=headers)


def positions_query_position_type(userId=100014641):
    url = host + '/positions/query_position_type'
    remark = '查询可选择的职位分类'
    headers = get_app_header(userId)
    return get_requests(url=url, remark=remark, headers=headers)


def positions_republish(positionId, userId):
    url = host + "/positions/{}/republish".format(positionId)
    data = {
        # "attachParam":"{\"typeId\":3,\"step\":\"TWO\"}",
        # "typeId":typeId,
    }
    remark = "再发布职位"
    headers = get_app_header(userId)
    return json_put(url=url, data=data, headers=headers, remark=remark)


def positions_offline(id, reqVersion=None, userToken=None, H9=False, userId=None, ip_port=None):
    url = host + '/positions/{}/offline'.format(id)
    remark = '下线职位'
    if H9 == True:
        headers = app_header_999(userToken, DA=False, userId=userId)
    else:
        userId = 100014641
        headers = get_app_header(userId, reqVersion)
    return json_put(url=url, data={}, remark=remark, headers=headers, ip_port=ip_port)


def publish_guide(userId):
    url = host + '/positions/publish_guide'
    header = get_app_header(userId=userId)
    remark = '发布职位页引导'
    return get_requests(url=url, headers=header, remark=remark).json()


def publish_position(userToken, userId=None, ip_port=None):
    '''
    发布职位
    :return:
    '''
    url = "https://gate.lagou.com/v1/zhaopin/positions/publish"
    data = {
        "isConfirm": True,
        "recruitmentType": 1,
        "typeId": 0,
        "recommend": False,
        "positionType": "测试",
        "workYear": "3-5年",
        "positionDesc": "<p>由于岗位称谓每个公司不尽相同，所以发布职位时同一职位我们会以不同标题发布多条。</p>",
        "labels": [{
            "name": "电商",
            "id": 1
        }],
        "salaryMin": 15,
        "positionDescPlainText": "\n1、组织完成项目质量计划，针对项目问题组织回溯，推动短板改进；\n2、进行质量文化宣传培训，提升项目的质量效率；",
        "positionName": "拉勾测试测试工程师" + str(random.randint(0, 99)),
        "positionThirdType": "测试工程师",
        "firstType": "开发|测试|运维类",
        "positionBrightPoint": "每年18薪",
        "education": "本科",
        "jobNature": "全职",
        "department": "",
        # "workAddressId" : 1629630,
        "workAddressId": 1560096,
        "salaryMax": 25
    }
    remark = "发布职位"
    headers = app_header_999(userToken, DA=False, userId=userId)
    return json_post(url=url, headers=headers, data=data, remark=remark, ip_port=ip_port)


if __name__ == '__main__':
    r = password_login("19910626899", "000000")
    userToken = r['content']['userToken']
    r = get_online_positions(userToken=userToken, H9=True)
    positionIds = []
    if r['content']['positions']['pageSize'] > 10:
        for position_info in r['content']['positions']['result']:
            positionId = position_info['positionId']
            positionIds.append(positionId)
    for id in positionIds:
        positions_offline(id, userToken=userToken, H9=True)

    # print(get_online_positions())
    # category_mapping("Java开发")
    # post_positions(workyear='3-5年')

    # get_online_positions()
    # 100013384
    # positions_republish(str(13845257))
    # 100013387
    # positions_republish(str(13687179))
    # positions_query_position_type()
    # get_other_positions()
    # get_offline_positions()
    # positions_details(str(13845259))
    # positions_details_app(str(13845370))
