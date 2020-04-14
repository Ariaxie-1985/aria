# coding:utf-8
# @Time  : 2020/4/14 16:38
# @Author: Xiawang
# Description:
from utils.util import app_header_999, get_requests


def session_share_info_app_c(userToken, job_id, ip_port=None, userId=None):
    url = f'https://gate.lagou.com/v1/weapp/api/job/{job_id}/session-share-info-app-c'
    header = app_header_999(userToken=userToken, userId=userId)
    return get_requests(url=url, headers=header, remark='c端用户分享职位到微信好友', ip_port=ip_port).json()


def moments_share_info_app_c(userToken, job_id, ip_port=None, userId=None):
    url = f'https://gate.lagou.com/v1/weapp/api/job/{job_id}/moments-share-info-app-c'
    header = app_header_999(userToken=userToken, userId=userId)
    return get_requests(url=url, headers=header, remark='c端用户分享职位到微信朋友圈', ip_port=ip_port).json()
