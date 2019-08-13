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
    except (IndexError, TypeError):
        userId = 0
    return userId, resumeId


def get_mds_company_id():
    url = 'https://easy.lagou.com/dashboard/index.htm?from=c_index'
    header = get_header('https://www.lagou.com')
    www_result = get_requests(url=url, headers=header).text
    try:
        soup = BeautifulSoup(www_result, "html.parser")
        compant_mds_Id = soup.find(id="UserConpanyId")['value']
    except (IndexError, TypeError):
        compant_mds_Id = 0
    try:
        userId = soup.find(id="UserId")['value']
    except (IndexError, TypeError):
        userId = 0
    return compant_mds_Id, userId


def get_www_company_id():
    url = 'https://www.lagou.com/c/myhome.html'
    header = get_header('https://www.lagou.com')
    get_requests(url=url, headers=header)
    result = requests.get(url=url, headers=header, allow_redirects=False, verify=False)
    company_url = result.headers['Location']
    try:
        company_id = re.findall(r'http://c.hr.lagou.com/gongsi/(.+?).html', company_url)[0]
    except (IndexError, TypeError):
        company_id = 0
    return company_id


if __name__ == '__main__':

    # get_compangy()
    # print(get_userId_resumeId())
    # print(get_www_company_id())
    # print(get_userId_resumeId())
    new_phone_list = [20030252, 20030253, 20030254, 20030255, 20030256, 20030257, 20030258, 20030259, 20030260,
                      20030261,
                      20030262, 20030263, 20030264, 20030265, 20030266, 20030267, 20030268, 20030269, 20030270,
                      20030271,
                      20030272, 20030273, 20030274, 20030275, 20030276, 20030277, 20030278, 20030279, 20030280,
                      20030281,
                      20030282, 20030283, 20030284, 20030285, 20030286, 20030287, 20030288, 20030289, 20030290]
    sss = []
    for phone in new_phone_list:
        aaa = {}
        login('00853', phone)
        com_id = get_www_company_id()
        aaa['phone'] = phone
        aaa['companyId'] = com_id
        sss.append(aaa)
    print(sss)
