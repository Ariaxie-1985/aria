# coding:utf-8
# @Time  : 2020/3/5 11:55
# @Author: Xiawang
# Description:
from api_script.entry.account.passport import password_login
from utils.util import app_header_999, get_requests, json_post


def talent_recTalent(userToken, positionId):
    url = "https://gate.lagou.com/v1/zhaopin/talent/recTalent?pageNo=1&pageSize=10&positionId={}&showId=&currentContainerSize=10".format(
        positionId)
    header = app_header_999(userToken=userToken, DA=False)
    remark = "推荐人才"
    return get_requests(url=url, headers=header, remark=remark).json()


def talent_newTalent(userToken, positionId):
    url = "https://gate.lagou.com/v1/zhaopin/talent/newTalent?pageNo=1&pageSize=10&positionId={}&showId=".format(
        positionId)
    header = app_header_999(userToken=userToken, DA=False)
    remark = "最新人才"
    return get_requests(url=url, headers=header, remark=remark).json()


def talent_collections(userToken):
    url = "https://gate.lagou.com/v1/zhaopin/talent/collections?lastCUserId=0&pageSize=10"
    header = app_header_999(userToken=userToken, DA=False)
    remark = "人才收藏"
    return get_requests(url=url, headers=header, remark=remark).json()


def talent_app_search(userToken, city, positionName, pageNo=1):
    url = "https://gate.lagou.com/v1/zhaopin/talent/app/search"
    header = app_header_999(userToken=userToken, DA=False)
    data = {
        "keyword": "",
        "isOversea": 0,
        "showId": "",
        "isFamouseCollege": 0,
        "salary": "",
        "isOnlinePrioritySort": 0,
        "workYear": "",
        "positionName": positionName,
        "city": city,
        "isFamouseCompany": 0,
        "education": "",
        "pageNo": pageNo,
        "pageSize": 10
    }
    remark = "人才搜索"
    return json_post(url=url, headers=header, data=data, remark=remark)


def talent_info_get(userToken, userId):
    url = "https://gate.lagou.com/v1/zhaopin/talent/info/get?userId={}&comeFrom=7".format(userId)
    header = app_header_999(userToken=userToken, DA=False)
    remark = "获取人才详细信息"
    return get_requests(url=url, headers=header, remark=remark).json()


if __name__ == '__main__':
    result = password_login("19910626899", "000000")
    userToken = result['content']['userToken']
    r = talent_recTalent(userToken, positionId=6868116)
    for talent in r['content']['result']:
        if bool(talent['portrait']):
            print(talent['portrait'].split(".")[-1])
