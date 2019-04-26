# -*- coding: utf8 -*-
__author__ = 'Arayang'
import utils
from utils.util import get_app_header,get_requests,json_post

header = utils.util.get_app_header(100012754)

#def companyinfos(con):
    #url='https://gate.lagou.com/v1/entry/bigCompany/query?companyId={}'.format(con)
def companyscores():
    url = "https://gate.lagou.com/v1/entry/interviewExperience/queryCompanyScore?companyId=142475"

    return get_requests(url=url,headers=header, remark='公司评分查询')


#companyscores()
