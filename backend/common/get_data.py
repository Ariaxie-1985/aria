# coding:utf-8
# @Time  : 2019-07-25 14:46
# @Author: Xiawang
from utils.util import get_header, get_requests, login
import requests
import re
from bs4 import BeautifulSoup


def get_compangy():
    company_id = get_www_company_id()
    compant_mds_Id, userId = get_mds_company_id()
    return company_id, compant_mds_Id, userId


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
    except (IndexError,TypeError):
        userId = 0
    return userId, resumeId


def get_mds_company_id():
    url = 'https://easy.lagou.com/dashboard/index.htm?from=c_index'
    header = get_header('https://www.lagou.com')
    www_result = get_requests(url=url, headers=header).text
    try:
        soup = BeautifulSoup(www_result, "html.parser")
        compant_mds_Id = soup.find(id="UserConpanyId")['value']
    except (IndexError,TypeError):
        compant_mds_Id = 0
    try:
        userId = soup.find(id="UserId")['value']
    except (IndexError,TypeError):
        userId = 0
    return compant_mds_Id, userId


def get_www_company_id():
    url = 'https://www.lagou.com/c/myhome.html'
    header = get_header('https://www.lagou.com')
    get_requests(url=url, headers=header)
    result = requests.get(url=url, headers=header, allow_redirects=False)
    company_url = result.headers['Location']
    try:
        company_id = re.findall(r'http://c.hr.lagou.com/gongsi/(.+?).html', company_url)[0]
    except (IndexError,TypeError):
        company_id = 0
    return company_id


if __name__ == '__main__':
    login('00852', "20181208")
    # get_compangy()
    print(get_mds_company_id())
    print(get_www_company_id())
    # print(get_userId_resumeId())