# coding:utf-8
# @Time  : 2020/2/26 18:58
# @Author: Xiawang
# Description:
from utils.util import app_header_999, get_requests


def wechat_qr_code(qrcodeType, userToken):
    url = "https://gate.lagou.com/v1/zhaopin/wechat/qr_code/common?qrcodeType={}&checkSubscribe=true".format(qrcodeType)
    header = app_header_999(userToken=userToken, DA=False)
    remark = "获取拉勾公众号二维码"
    return get_requests(url=url, headers=header, remark=remark).json()
