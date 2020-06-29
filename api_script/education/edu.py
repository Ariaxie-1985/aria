# coding:utf-8
# @Time  : 2020/3/6 16:11
# @Author: Xiawang
# Description:

from utils.util import get_requests, get_edu_app_header
import re
course_id =[]
def get_course_list(userToken):
    url = "https://gate.lagou.com/v1/neirong/edu/homepage/getCourseList"
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "获取专栏课程信息"
    result = get_requests(url=url, headers=header, remark=remark)
    a = result['content']['courseCardList'][0]['courseList']
    for k in a:
        if k['hasBuy']:
            course_id.append(k['id'])
    return course_id


if __name__ == '__main__':
    a=get_course_list("e9042e2267491d2de5b6a5864ef33693b8791020ecc26b98da19bb03f4d9ff52")
    print(a[-1])




