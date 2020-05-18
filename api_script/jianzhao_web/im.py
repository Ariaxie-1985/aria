# coding:utf-8
# @Time  : 2020/3/20 16:16
# @Author: Xiawang
# Description:
from utils.util import get_requests, get_code_token, get_header, json_post, form_post


def settings_template(ip_port=None):
    query_url = "https://easy.lagou.com/settings/template/in_temp.json?positionId=0"
    refer_url = "https://easy.lagou.com/im/chat/index.htm"
    query_header = get_header(refer_url, ip_port=ip_port)
    remark = "面试模板"
    return get_requests(url=query_url, headers=query_header, remark=remark, ip_port=ip_port).json()


def resume_report_reasons(ip_port=None):
    query_url = "https://easy.lagou.com/im/resume/reportReasons.json"
    refer_url = "https://easy.lagou.com/im/chat/index.htm"
    query_header = get_header(refer_url, ip_port=ip_port)
    remark = "简历举报原因"
    return get_requests(url=query_url, headers=query_header, remark=remark, ip_port=ip_port).json()


def im_session_list(createBy, ip_port=None):
    query_url = f"https://easy.lagou.com/im/session/list.json?pageNo=1&pageSize=10&createBy={createBy}&unReadOnly=0"
    refer_url = "https://easy.lagou.com/talent/search/list.htm?pageNo=1&keyword=%E6%8B%89%E5%8B%BE%E7%BD%91&show_id=5a4289c49b6e4c08b7b1cb8e9f9820e1&city=%E5%93%88%E5%B0%94%E6%BB%A8&education=%E4%B8%8D%E9%99%90&workYear=%E4%B8%8D%E9%99%90&industryField=%E4%B8%8D%E9%99%90&expectSalary=%E4%B8%8D%E9%99%90"
    query_header = get_header(refer_url, ip_port=ip_port)
    remark = "获取im列表"
    return get_requests(url=query_url, headers=query_header, remark=remark, ip_port=ip_port).json()


def im_session_get(session_id, ip_port=None):
    query_url = f"https://easy.lagou.com/im/session/get/{session_id}.json"
    refer_url = "https://easy.lagou.com/im/chat/index.htm"
    query_header = get_header(refer_url, ip_port=ip_port)
    remark = "获取im某消息框"
    return json_post(url=query_url, headers=query_header, remark=remark, ip_port=ip_port)


def count_unRead_messages(ip_port=None):
    query_url = "https://easy.lagou.com/im/chat/countUnReadMessages.json"
    refer_url = "https://easy.lagou.com/settings/account/me.htm?"
    query_header = get_header(refer_url, ip_port=ip_port)
    remark = "统计未读消息"
    return get_requests(url=query_url, headers=query_header, remark=remark, ip_port=ip_port).json()


def greeting_list(cUserIds, positionId=0):
    url = 'https://easy.lagou.com/im/session/greetingList.json'
    # refer_url = f'https://easy.lagou.com/talent/index.htm?positionId={positionId}'
    refer_url ='https://easy.lagou.com/talent/search/list.htm?pageNo=1&keyword=%E6%8B%89%E5%8B%BE%E7%BD%91&show_id=5a4289c49b6e4c08b7b1cb8e9f9820e1&city=%E5%93%88%E5%B0%94%E6%BB%A8&education=%E4%B8%8D%E9%99%90&workYear=%E4%B8%8D%E9%99%90&industryField=%E4%B8%8D%E9%99%90&expectSalary=%E4%B8%8D%E9%99%90'

    query_header = get_code_token(refer_url)
    print(query_header.get('Cookies'))
    data = {
        'cUserIds': cUserIds
    }
    remark = '找人才-打招呼'
    return form_post(url=url, data=data, headers=query_header, remark=remark)


def multiChannel_default_invite(positionId):
    url = 'https://easy.lagou.com/position/multiChannel/default-invite.json'
    refer_url = f'https://easy.lagou.com/talent/index.htm?positionId={positionId}'
    query_header = get_code_token(refer_url)
    print(query_header.get('Cookies'))
    data = {
        'positionId': positionId
    }
    remark = '职位邀请人才'
    return form_post(url=url, headers=query_header, data=data, remark=remark)


def session_batchCreate_cUserIds(cUserIds, positionId):
    url = f'https://easy.lagou.com/im/session/batchCreate/{cUserIds}.json'
    refer_url = f'https://easy.lagou.com/talent/search/list.htm?'
    query_header = get_header(refer_url)
    data = {
        'positionId': positionId,
        'greetingContent': '你好，在考虑新的工作机会吗？希望可以和你进一步沟通~',
        'inviteDeliver': 'true'
    }
    remark = '创建会话'
    return form_post(url=url, headers=query_header, data=data, remark=remark)
