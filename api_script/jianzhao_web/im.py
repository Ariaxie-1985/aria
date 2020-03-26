# coding:utf-8
# @Time  : 2020/3/20 16:16
# @Author: Xiawang
# Description:
from utils.util import get_requests, get_code_token, get_header, json_post


def settings_template():
    query_url = "https://easy.lagou.com/settings/template/in_temp.json?positionId=0"
    refer_url = "https://easy.lagou.com/im/chat/index.htm"
    query_header = get_header(refer_url)
    remark = "面试模板"
    return get_requests(url=query_url, headers=query_header, remark=remark).json()


def resume_report_reasons():
    query_url = "https://easy.lagou.com/im/resume/reportReasons.json"
    refer_url = "https://easy.lagou.com/im/chat/index.htm"
    query_header = get_header(refer_url)
    remark = "简历举报原因"
    return get_requests(url=query_url, headers=query_header, remark=remark).json()


def im_session_list(createBy):
    query_url = f"https://easy.lagou.com/im/session/list.json?pageNo=1&pageSize=10&createBy={createBy}&unReadOnly=0"
    refer_url = "https://easy.lagou.com/im/chat/index.htm"
    query_header = get_header(refer_url)
    remark = "获取im列表"
    return get_requests(url=query_url, headers=query_header, remark=remark).json()


def im_session_get(session_id):
    query_url = f"https://easy.lagou.com/im/session/get/{session_id}.json"
    refer_url = "https://easy.lagou.com/im/chat/index.htm"
    query_header = get_header(refer_url)
    remark = "获取im某消息框"
    return json_post(url=query_url, headers=query_header, remark=remark)


def count_unRead_messages():
    query_url = "https://easy.lagou.com/im/chat/countUnReadMessages.json"
    refer_url = "https://easy.lagou.com/settings/account/me.htm?"
    query_header = get_header(refer_url)
    remark = "统计未读消息"
    return get_requests(url=query_url, headers=query_header, remark=remark).json()
