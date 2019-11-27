import requests
import json

from utils.util import get_requests, get_header, login


def get_msgid():
    url = "https://easy.lagou.com/im/session/list.json?pageNo=1&pageSize=30&createBy=0&unReadOnly=0"
    header = get_header(url="https://easy.lagou.com/im/chat/index.htm")
    result = get_requests(url=url, headers=header, remark="获取通知消息ID").json()
    for msg in result['content']['rows']:
        if msg['name'] == '通知':
            msgid = msg['sessionId']
            print(msgid)
            return msgid

def admin_review(userid):
    url = "https://easy.lagou.com/bstatus/auth/manager/assist.json"
    header = get_header(url="https://easy.lagou.com/im/chat/index.htm")
    data = {'applyUserId':userid, 'confirmButton':'True'}
    result = get_requests(url=url, headers=header, data=data, remark="管理员审核通过")