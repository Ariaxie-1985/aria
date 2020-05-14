# coding:utf-8
# @Time  : 2020/5/14 11:18
# @Author: Xiawang
# Description:
from loguru import logger


def loger():
    logger.add("../log/py_auto_test_result.log", rotation="0:00", encoding='utf-8', colorize=True,
               format="<yellow>{time}</yellow> <level>{message}</level>")
    return logger


if __name__ == '__main__':
    loger = loger()
    loger.debug('debug 信息')
    loger.info('info 信息')
    loger.success('success 信息')
    loger.error('error 信息')
