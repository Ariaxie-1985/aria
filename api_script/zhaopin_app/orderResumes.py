# coding:utf-8
# @Time  : 2019-04-28 14:49
# @Author: Xiawang
from utils.util import get_app_header, json_post, get_requests

host = 'https://gate.lagou.com/v1/zhaopin'
header = get_app_header(100014641)


def orderResumes_query(resumeStageCode):
    url = host + '/orderResumes/query'
    data = {
        "catchTag": 0,
        "channelIds": [
            0
        ],
        "deliverTimeCode": 0,
        "educationCode": 0,
        "famousCompanyCode": 0,
        "famousSchoolCode": 0,
        "otherCode": 0,
        "pageSize": 0,
        "positionIds": [
            0
        ],
        "resumeStageCode": resumeStageCode,
        "resumeSubStage": "NOT_READ",
        "workYearCode": 0
    }
    remark = '根据条件筛选获取简历列表'
    return json_post(url=url, headers=header, data=data, remark=remark)


def orderResumes_filter():
    url = host + '/orderResumes/filter'
    remark = '简历搜索筛选条目'
    return get_requests(url=url, headers=header, remark=remark).json()


def orderResumes_positions_pages():
    url = host + '/orderResumes/positions/pages?pageNo=1&pageSize=2'
    remark = '分页查询用于简历查询的职位'
    return get_requests(url=url, headers=header, remark=remark).json()


def orderResumes_sameResume_query(resumeId):
    url = host + '/orderResumes/sameResume/query?pageNo=1&pageSize=10&resumeId={}'.format(resumeId)
    remark = '多次投递记录'
    return get_requests(url=url, headers=header, remark=remark).json()


def orderResumes_process_save(content, resumeId):
    url = host + '/orderResumes/process/save'
    data = {
        "content": content,
        "resumeId": resumeId
    }
    remark = '提交简历评价'
    return json_post(url=url, data=data, headers=header, remark=remark)


def orderResumes_process_query(resumeId):
    url = host + '/orderResumes/process/query?resumeId={}'.format(resumeId)
    remark = '查询简历参与者的评价记录'
    return get_requests(url=url, headers=header, remark=remark).json()


def orderResumes_process_forward(atIds, resumeId):
    url = host + '/orderResumes/process/forward'
    data = {
        "atIds": [
            atIds
        ],
        "resumeId": resumeId
    }
    remark = '在简历评价里@同事'
    return json_post(url=url, data=data, headers=header, remark=remark)
