# coding:utf-8
# @Time  : 2020/5/14 11:18
# @Author: Xiawang
# Description:
import os

from loguru import logger


def loger():
    logger.add("log/py_auto_test_result.log", encoding='utf-8', colorize=True,
               format="<yellow>{time:YYYY-MM-DD HH:mm:ss}</yellow> <level>{level}</level> <level>{message}</level>")
    return logger


if __name__ == '__main__':
    loger = loger()
    loger.debug('debug 信息')
    loger.success('success 信息')
    loger.error('error 信息')
