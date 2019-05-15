# coding:utf-8
# @Time  : 2019-05-13 20:20
# @Author: Xiawang
from utils.util import get_code_token, form_post, login, get_requests

host = 'https://easy.lagou.com'


def recruitcard_pop():
    refer_url = 'https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm?pageNo=1'
    header = get_code_token(refer_url)
    url = host + '/integral/mall/recruitcard/pop.json'
    remark = '领取月度职位卡'
    return get_requests(url=url, headers=header, remark=remark)


login('00852', 20181205)
recruitcard_pop()
