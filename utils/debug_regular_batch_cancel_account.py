# coding:utf-8
# @Time  : 2020/4/17 13:09
# @Author: Xiawang
# Description:
import logging
import sys
import os
import time

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import requests

from utils.read_file import read_cancel_account, batch_cancel_account, rewrite_cancel_account

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler('/home/test/cancel_account_output.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


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
    if not bool(result):
        logger.info(f'无需注销的数据\n')
        return
    logger.info(f'开始注销手机号:{",".join(result)}\n')
    if len(result) > 0:
        try:
            batch_cancel_account(result)
            send_cancel_result(message='注销手机号成功', result=result)
            rewrite_cancel_account()
        except AssertionError:
            send_cancel_result(message='注销手机号失败', result=result)


if __name__ == "__main__":
    regular_batch_cancel_account()
