        # coding:utf-8
# @Time  : 2019-06-28 15:09
# @Author: Xiawang
from utils.util import get_requests, login
import re
from bs4 import BeautifulSoup


def get_userId_resumeId():
    url = 'https://www.lagou.com/resume/myresume.html'
    page = get_requests(url=url, remark="我的简历页面--获取简历id").text
    try:
        resumeId = re.findall("resumeId: '(.*?)',", page, re.S)[0]
    except IndexError:
        resumeId = 0

    try:
        soup = BeautifulSoup(page, "html.parser")
        userId = soup.find(id="userid")['value']
    except IndexError:
        userId = 0
    return userId, resumeId


def get_userId():
    url = 'https://www.lagou.com/'
    page = get_requests(url=url, remark="拉勾网页面--获取userId").text
    try:
        soup = BeautifulSoup(page, "html.parser")
        userId = soup.find(id="userid")['value']
    except IndexError:
        userId = 0
    return userId


if __name__ == '__main__':
    login('00852', "20030100")
    print(get_userId_resumeId())
