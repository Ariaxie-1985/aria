# coding:utf-8
# @Time  : 2020-02-18 15:00
# @Author: Xiawang
from api_script.entry.account.passport import password_login
from utils.util import get_requests, app_header_999


def query_positions(userToken, companyId):
    url = 'https://gate.lagou.com/v1/entry/position/queryPositions?companyId={}&pageNo=0&pageSize=0'.format(companyId)
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, headers=header, remark="查询公司的在招职位").json()


def query_by_company(userToken, companyId, positionType):
    url = 'https://gate.lagou.com/v1/entry/position/queryByCompany?companyId={}&positionType={}&pageNo=1&pageSize=10'.format(
        companyId, positionType)
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, headers=header, remark='根据筛选条件查询公司的在招职位').json()


def get_jd(userToken, positionId):
    url = 'https://gate.lagou.com/v1/entry/position/jd?positionId={}&isCInspectB=1'.format(positionId)
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, headers=header, remark="获取职位jd页").json()


# new
def get_position_detail(userToken, positionId):
    url = 'https://gate.lagou.com/v1/entry/position/positionDetail?id={}'.format(positionId)
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, headers=header, remark="根据职位id查询职位详情").json()


def get_position_publisher(userToken, hr_Id):
    url = 'https://gate.lagou.com/v1/entry/position/publisher?hrId={}&showId=5&pageNo=1&pageSize=10'.format(hr_Id)
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, headers=header, remark="HR发布职位列表").json()


def get_communicate_positions(userToken, hr_Id):
    url = 'https://gate.lagou.com/v1/entry/position/communicatePositions?hrId={}&showId=5&pageNo=1&pageSize=10'.format(
        hr_Id)
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, headers=header, remark="查询沟通职位列表").json()


if __name__ == '__main__':
    result = password_login("19910626899", "000000")
    userToken = result['content']['userToken']
    print(get_position_detail(userToken=userToken, positionId=2590692))
    print(get_position_publisher(userToken=userToken, hr_Id=15130154))
    print(get_communicate_positions(userToken=userToken, hr_Id=15130154))
