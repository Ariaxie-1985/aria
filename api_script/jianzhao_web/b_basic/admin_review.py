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

def admin_review():
    get_sessionId = get_msgid()
    url = 'https://easy.lagou.com/im/chat/mark_read/{}.json'.format(get_sessionId)
    print(url)
    header = get_header(url="https://easy.lagou.com/im/chat/index.htm")


if __name__ == '__main__':
    l = login(countryCode='00852', username='20181205')
    print(l)
    get_msgid()
    admin_review()

