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
    a = get_course_list("57341d0db1aa9f9fd03926b7bee0c97ebbd28bb01c324a843a8598d871f42910")
    print(a[1][-1])







