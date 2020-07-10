# coding:utf-8
# @Time  : 2020/3/6 16:11
# @Author: Xiawang
# Description:

from utils.util import get_requests, get_edu_app_header
import re
hasBuy_course_id =[]
nohasBuy_course_id =[]
def get_course_list(userToken):
    url = "https://gate.lagou.com/v1/neirong/edu/homepage/getCourseList"
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "获取专栏课程信息"
    result = get_requests(url=url, headers=header, remark=remark,rd='Yuwei Cheng')
    a = result['content']['courseCardList'][0]['courseList']
    for k in a:
        if k['hasBuy']:
            hasBuy_course_id.append(k['id'])
        else:
            nohasBuy_course_id.append(k['id'])
    return result,hasBuy_course_id,nohasBuy_course_id

if __name__ == '__main__':
    print(get_course_list("f7ce1c1b65e5c6d4457985e43e5491295c57a3d71b6fbeaf27a3b167660f0a3a"))







