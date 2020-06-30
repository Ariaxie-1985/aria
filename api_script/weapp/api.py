# coding:utf-8
# @Time  : 2020/4/14 16:38
# @Author: Xiawang
# Description:

from api_script.entry.account.passport import password_login
from api_script.zhaopin_app.talent import talent_recTalent, talent_info_get
from utils.util import app_header_999, get_requests


def session_share_info_app_c(userToken, job_id, ip_port=None, userId=None):
    url = f'https://gate.lagou.com/v1/weapp/api/job/{job_id}/session-share-info-app-c'
    header = app_header_999(userToken=userToken, userId=userId)
    return get_requests(url=url, headers=header, remark='c端用户分享职位到微信好友', ip_port=ip_port, rd='李久超')


def moments_share_info_app_c(userToken, job_id, ip_port=None, userId=None):
    url = f'https://gate.lagou.com/v1/weapp/api/job/{job_id}/moments-share-info-app-c'
    header = app_header_999(userToken=userToken, userId=userId)
    return get_requests(url=url, headers=header, remark='c端用户分享职位到微信朋友圈', ip_port=ip_port, rd='李久超')


def session_share_info_app_b_corp(userToken, resumeId, ip_port=None, userId=None):
    url = f'https://gate.lagou.com/v1/weapp/api-corp/talent/{resumeId}/session-share-info-app-b?resumeRestrict=false'
    header = app_header_999(userToken=userToken, userId=userId, DA=False)
    return get_requests(url=url, headers=header, remark='B端用户分享人才简历到微信好友', ip_port=ip_port, rd='李久超')


def session_share_info_app_b_yun(userToken, orderResumeId, ip_port=None, userId=None):
    url = f'https://gate.lagou.com/v1/weapp/api-yun/resume/{orderResumeId}/session-share-info-app-b'
    header = app_header_999(userToken=userToken, userId=userId, DA=False)
    return get_requests(url=url, headers=header, remark='B端用户与C端用户的消息里分享简历到微信好友', ip_port=ip_port, rd='李久超')


if __name__ == '__main__':
    r = password_login("19910626899", "000000")
    userToken = r['content']['userToken']
    r = talent_recTalent(userToken=userToken, positionId=7027611)
    resumeId = r['content']['result'][0]['resumeId']
    r = session_share_info_app_b_corp(userToken=userToken, resumeId=resumeId)
    print(r)
    r = talent_info_get(userToken=userToken, userId=15166231)
    long_resumeId = r['content']['resumeId']
    r = session_share_info_app_b_yun(userToken=userToken, orderResumeId=long_resumeId)
    print(r)
