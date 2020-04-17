# coding:utf-8
# @Time  : 2020/4/17 13:09
# @Author: Xiawang
# Description:
import logging

import requests

from utils.read_file import read_cancel_account, batch_cancel_account, rewrite_cancel_account, record_cancel_account

from threading import Timer


def send_cancel_result(message, result):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=b18ce9c0-3d98-411a-9f2a-bbce71c0f09e'
    data = {
        "msgtype": "text",
        "text": {
            "mentioned_list": ["xiawang"],
            "content": f'{message}: {",".join(result)}'}}
    requests.post(url=url, json=data, verify=False).json()


# 每隔300秒执行一次任务
def regular_batch_cancel_account():
    result = read_cancel_account()
    logging.info(f'注销手机号:{",".join(result)}')
    if len(result) > 0:
        try:
            batch_cancel_account(result)
            send_cancel_result(message='注销手机号成功', result=result)
            rewrite_cancel_account()
        except AssertionError:
            send_cancel_result(message='注销手机号失败', result=result)
    t = Timer(420, regular_batch_cancel_account)
    t.start()


if __name__ == "__main__":
    regular_batch_cancel_account()
