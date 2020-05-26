# coding:utf-8
# @Time  : 2020/5/14 11:18
# @Author: Xiawang
# Description:
import os
import sys

from loguru import logger


def switch_project_root_directory():
    project_path = os.path.dirname(os.path.dirname(__file__))
    os.chdir(project_path)
    return project_path


def logers():

    project_path = switch_project_root_directory()
    logger.add(f"{project_path}/log/py_auto_test_result.log", encoding='utf-8', colorize=True,
               format="<yellow>{time:YYYY-MM-DD HH:mm:ss}</yellow> <level>{level}</level> <level>{message}</level>")
    return logger


if __name__ == '__main__':
    # loger = loger()
    # loger.debug('debug 信息')
    # loger.success('success 信息')
    # loger.error('error 信息')
    sys.path.append(os.path.dirname(__file__))
    print(os.path.dirname(__file__))
