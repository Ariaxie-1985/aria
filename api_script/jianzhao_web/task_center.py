# coding:utf-8
# @Time  : 2020/4/28 10:37
# @Author: Xiawang
# Description:
from utils.util import get_code_token, form_post


def get_newer_task():
    url = 'https://easy.lagou.com/task/center/newer/task.json'
    header = get_code_token(url='https://easy.lagou.com/task/center/index.htm?')
    remark = '任务中心获取新手任务'
    return form_post(url=url, headers=header, remark=remark)


'''


'''


def receive_newer_task_reward(recordId, taskLabel, taskGroup):
    url = 'https://easy.lagou.com/task/center/receive/reward.json'
    header = get_code_token(url='https://easy.lagou.com/task/center/index.htm?')
    data = {
        "recordId": recordId,
        "taskLabel": taskLabel,
        "taskGroup": taskGroup
    }
    remark = '任务中心--新手任务--领取已完成的奖励'
    return form_post(url=url, headers=header, data=data, remark=remark)


def receive_gouyin_weekly_task_points():
    url = 'https://easy.lagou.com/task/center/receive/gouyin/weekly.json'
    header = get_code_token(url='https://easy.lagou.com/task/center/index.htm?')
    remark = '任务中心--获取本周积分数'
    return form_post(url=url, headers=header, remark=remark)


def get_shop_goods_on_sale_goods():
    url = 'https://gate.lagou.com/v1/zhaopin/shop/goods/onSaleGoods'
