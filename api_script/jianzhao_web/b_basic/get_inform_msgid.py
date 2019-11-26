import requests
def get_msgid():
    url = "https://easy.lagou.com/im/session/list.json"
    headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9'

    }
    params = {'pageNo':'1', 'pageSize':'10', 'createBy': '0', 'unReadOnly':'0' }
    result = requests.get(url=url, headers=headers, params=params)
    r = result.json()
    for i in r.content.rows(0, 10):
        if r.content.rows.lastMsg.name == '通知'
            return r.content.rows.lastMsg.name
    #result.raise_for_status()

if __name__ == 'main':
    get_msgid()