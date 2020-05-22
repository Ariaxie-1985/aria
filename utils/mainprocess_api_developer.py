# coding:utf-8
# @Time  : 2020/5/21 15:27
# @Author: Xiawang
# Description:
import re
from urllib.parse import urlparse


def new_list(l: list) -> list:
    new_l = []
    new_l.append(l[0] + l[1])
    new_l.append(l[2])
    return new_l


def parse_api_developer():
    api_developer = {}
    with open('api_develop.csv', 'r') as f:
        for line in f.readlines():
            line_list = line.split(',')[:3]
            result_parse = new_list(line_list)
            api_developer[result_parse[0]] = result_parse[1]
        return api_developer


def return_api_developer(url):
    api_developers = parse_api_developer()
    if url in api_developers:
        return api_developers.get(url)

    url_parse_result = urlparse(url=url)
    hostname, url_path = url_parse_result.hostname, url_parse_result.path
    pattern = re.compile(r'[.a-zA-z0-9]+')
    url_path_parse_result = pattern.findall(url_path)
    if ('v1' or 'zhaopin' or 'neirong' or 'entry') in url_path_parse_result:
        url_path_parse_result = url_path_parse_result[2:]
    exec_url = []
    for a in list(api_developers.keys()):
        for i in url_path_parse_result:
            if i in a and (i not in set(exec_url)):
                exec_url.append(a)
            break
    for i in url_path_parse_result:
        for e in exec_url:
            if i not in e:
                continue
            else:
                return api_developers.get(e)
        return None
    else:
        return None


if __name__ == '__main__':
    # url = 'https://gate.lagou.com/v1/zhaopin/shop/goodsOrder/check/312312312321'
    # url = 'https://easy.lagou.com/session/batchCreate/2132134.json'
    # url = 'https://gate.lagou.com/v1/zhaopin/talent/app/search'
    # url = 'https://home.lagou.com/audit/companyApprove/addRiskLabelsByCompany.json'
    # url = 'https://hr.lagou.com/corpCenter/openservice/saveCompany.json'
    url = 'https://gate.lagou.com/v1/neirong/course/comment/getCourseCommentList'
    name = return_api_developer(url=url)
    print(url, name)
