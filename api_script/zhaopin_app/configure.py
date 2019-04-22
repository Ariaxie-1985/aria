# coding:utf-8
# @Time  : 2019-03-07 14:19
# @Author: Xiawang

from utils.util import get_app_header, json_post, get_requests

host = "https://gate.lagou.com/v1/entry"
headers = get_app_header(100014641)


def positionCategories(type=None):
    '''
    :param type: int, 职位分类级别 1-互联网 2-其他 不传则为全部
    :return:
    '''
    if not(type == None):
        url = host + "/config/positionCategories/get?type={}".format(type)
    else:
        url = host + "/config/positionCategories/get"
    remark = "查询职位分类配置信息"
    return get_requests(url=url, headers=headers, remark=remark)


