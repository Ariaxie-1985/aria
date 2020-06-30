# coding:utf-8
# @Time  : 2019-04-28 14:49
# @Author: Xiawang
import datetime
import time

from api_script.entry.account.passport import password_login
from utils.util import get_app_header, json_post, get_requests, app_header_999, put_requests, json_put

host = 'https://gate.lagou.com/v1/zhaopin'
header = get_app_header(100014641)


def orderResumes_query(userToken, resumeStageCode, ip_port=None, userId=None):
    url = host + '/orderResumes/query'
    data = {
        "pageSize": 20,
        "channelIds": [0],
        "famousCompanyCode": 0,
        "resumeStageCode": resumeStageCode,
        "educationCode": 0,
        "deliverTimeCode": 0,
        "otherCode": 0,
        "famousSchoolCode": 0,
        "workYearCode": 0,
        "catchTag": 0
    }
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = '根据简历状态筛选获取简历列表'
    return json_post(url=url, headers=header, data=data, remark=remark, ip_port=ip_port)


def orderResumes_filter(userToken, ip_port=None, userId=None):
    url = host + '/orderResumes/filter'
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = '简历搜索筛选条目'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port)


def orderResumes_positions_pages(userToken, ip_port=None, userId=None):
    url = host + '/orderResumes/positions/pages?pageNo=1&pageSize=20'
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = '分页查询用于简历查询的职位'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port)


def orderResumes_sameResume_query(userToken, resumeId, pageNo=1, ip_port=None, userId=None):
    url = host + '/orderResumes/sameResume/query?pageNo={}&pageSize=10&resumeId={}'.format(pageNo, resumeId)
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = '多次投递记录'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port)


def orderResumes_process_save(userToken, content, resumeId):
    url = host + '/orderResumes/process/save'
    data = {
        "content": content,
        "resumeId": resumeId
    }
    header = app_header_999(userToken=userToken, DA=False)
    remark = '提交简历评价'
    return json_post(url=url, data=data, headers=header, remark=remark, rd='mandy')


def orderResumes_process_query(userToken, resumeId, ip_port=None, userId=None):
    url = host + '/orderResumes/process/query?resumeId={}'.format(resumeId)
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = '查询简历参与者的评价记录'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port, rd='mandy')


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


def get_strict_pages_positions():
    url = host + "/orderResumes/positions/strict/pages?pageNo=1&pageSize=20"
    remark = "分页查询用于简历查询的职位（排除没有拉勾职位id的职位）"
    return get_requests(url=url, headers=header, remark=remark)


def get_strict_pages_orderResumes():
    url = host + "/orderResumes/positions/pages?pageNo=1&pageSize=20"
    remark = "分页查询用于简历查询的职位"
    return get_requests(url=url, headers=header, remark=remark)


def orderResumes_interview(userToken, resumeId):
    url = "https://gate.lagou.com/v1/zhaopin/orderResumes/interview?resumeId={}".format(resumeId)
    header = app_header_999(userToken=userToken, DA=False)
    remark = "查询面试安排记录"
    return get_requests(url=url, headers=header, remark=remark, rd='mandy')


def orderResumes_resume_interview(userToken, resumeId, positionId, ip_port=None, userId=None):
    url = "https://gate.lagou.com/v1/zhaopin/orderResumes/{}/interview".format(resumeId)
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    ten_min_after = datetime.datetime.now() - datetime.timedelta(minutes=-10)
    ten_min_after_timestamp = time.mktime(ten_min_after.timetuple()) * 1000
    data = {
        "orderResumeId": resumeId,
        "templateId": 0,
        "contact": "王子",
        "positionId": positionId,
        "interviewTime": ten_min_after_timestamp,
        "contactAddress": "北京市海淀区海置创投大厦4楼",
        "contactPhone": "16601010101",
        "addInfo": "请提前10分钟到，谢谢"
    }
    remark = "邀约面试"
    return json_post(url=url, headers=header, data=data, remark=remark, ip_port=ip_port, rd='mandy')


def orderResumes_resume_obsolete(userToken, resumeId, ip_port=None, userId=None):
    url = "https://gate.lagou.com/v1/zhaopin/orderResumes/{}/obsolete?fromIm=true&contactC=false".format(resumeId)
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = "候选人状态调整为不合适"
    return put_requests(url=url, headers=header, remark=remark, ip_port=ip_port, rd='mandy')


def orderResumes_detail(userToken, resumeId, ip_port=None, userId=None):
    url = "https://gate.lagou.com/v1/zhaopin/orderResumes/{}?needImg=false&ignoreNearbyFail=true".format(resumeId)
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = "查询简历详情"
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port, rd='mandy')


def orderResumes_read(userToken, resumeId, ip_port=None, userId=None):
    url = "https://gate.lagou.com/v1/zhaopin/orderResumes/read?orderResumeId={}".format(resumeId)
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = "设置简历已读"
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port, rd='mandy')


def orderResumes_resume_link(userToken, resumeId, ip_port=None, userId=None):
    url = "https://gate.lagou.com/v1/zhaopin/orderResumes/{}/link".format(resumeId)
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = "标记初筛"
    return put_requests(url=url, headers=header, remark=remark, ip_port=ip_port, rd='mandy')


def orderResumes_resume_luyong(userToken, resumeId, ip_port=None, userId=None):
    url = "https://gate.lagou.com/v1/zhaopin/orderResumes/{}/luyong".format(resumeId)
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = "录用候选人"
    return put_requests(url=url, headers=header, remark=remark, ip_port=ip_port, rd='mandy')


def orderResumes_resume_employed(userToken, resumeId, ip_port=None, userId=None):
    url = "https://gate.lagou.com/v1/zhaopin/orderResumes/{}/employed".format(resumeId)
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = "候选人已入职"
    return put_requests(url=url, headers=header, remark=remark, ip_port=ip_port, rd='mandy')


def orderResumes_resume_new(userToken, resumeId, ip_port=None, userId=None):
    url = "https://gate.lagou.com/v1/zhaopin/orderResumes/{}/new".format(resumeId)
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = "将淘汰简历重新恢复为候选人"
    return put_requests(url=url, headers=header, remark=remark, ip_port=ip_port)


def orderResumes_interview_datetime(userToken, resumeId, ip_port=None, userId=None):
    url = "https://gate.lagou.com/v1/zhaopin/orderResumes/{}/interview/datetime".format(resumeId)
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    ten_min_after = datetime.datetime.now() - datetime.timedelta(minutes=-10)
    ten_min_after_timestamp = time.mktime(ten_min_after.timetuple()) * 1000
    data = {
        "interviewTime": ten_min_after_timestamp,
        "orderResumeId": resumeId
    }
    remark = "修改面试时间"
    return json_put(url=url, headers=header, data=data, remark=remark, ip_port=ip_port)


def orderResumes_stage(userToken, resumeId, ip_port=None, userId=None):
    url = "https://gate.lagou.com/v1/zhaopin/orderResumes/{}/stage".format(resumeId)
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = "查询简历阶段"
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port)


if __name__ == '__main__':
    result = password_login("19910626899", "000000")
    userToken = result['content']['userToken']
    orderResumes_stage(userToken, "1235904602201923584")
