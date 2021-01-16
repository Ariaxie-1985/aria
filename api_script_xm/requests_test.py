from utils.util import get_requests, json_post, form_post, gethtml


def get_requests_json():
    url = 'http://127.0.0.1:18980/data/'
    return get_requests(url)


def post_requests_json():
    payload = {"positionId": 8834,
               "positionName": "高级市场营销经理",
               "firstType": "市场|商务类",
               "positionType": "市场|营销",
               "positionThirdType": "市场营销",
               "workAddress": "北京市海淀区时代网络大厦4层"}
    r = json_post('http://127.0.0.1:18980/data/position', data=payload)
    return r


def post_requests_form():
    payload = {"positionId": 1234,
               "positionName": "高级市场营销经理",
               "firstType": "市场|商务类",
               "positionType": "市场|营销",
               "positionThirdType": "市场营销",
               "workAddress": "北京市海淀区时代网络大厦4层"}
    r = form_post('http://127.0.0.1:18980/data/position', data=payload)
    return r


def get_requests_html():
    r = gethtml('http://127.0.0.1:18980/data/html')
    return r

# if __name__ == '__main__':
#     #r = get_requests_json()
#     r = post_requests_json()
