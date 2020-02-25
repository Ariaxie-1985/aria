# coding:utf-8
# @Time  : 2019-04-28 11:13
# @Author: Xiawang
from utils.util import delete_requests, get_app_header

host = 'https://gate.lagou.com/v1/entry'
header = get_app_header(100018934)


def delete_orderId(orderIds):
    url = host + '/order/orderId?orderIds={orderIds}'.format(orderIds=orderIds)
    remark = '删除投递记录'
    return delete_requests(url=url, remark=remark)
