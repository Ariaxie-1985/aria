# coding:utf-8
# @Time  : 2020/4/27 14:44
# @Author: Xiawang
# Description:
import json

import pysnooper

from utils.util import get_requests, login_password, get_header

@pysnooper.snoop()
def get_rights_info_list():
    url = 'https://gate.lagou.com/v1/zhaopin/rights/getRightsInfoList'
    header = get_header(url='https://easy.lagou.com/userGoodsRecord/queryGoods/index.htm?')
    header.update({'Referer': 'https://easy.lagou.com/userGoodsRecord/queryGoods/index.htm?',
                   'X-L-REQ-HEADER': json.dumps({'deviceType': 1})})
    remark = '获取基础权益'
    return get_requests(url=url, headers=header, remark=remark).json()


if __name__ == '__main__':
    login_password('0085220200427', 'c47eeb69fa4e64971fb29cb1e9163a19')
    # jump_easy_index_html()
    r = get_rights_info_list()
    print(r)
