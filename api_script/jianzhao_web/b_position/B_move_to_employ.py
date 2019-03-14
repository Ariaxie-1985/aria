# -*- coding: utf8 -*-
__author__ = 'yqzhang'

from utils.util import form_post,get_code_token, login,get_requests


def move_to_employ(positionId,resumeOwnerId):
    refer_listofcandidates_url = "https://easy.lagou.com/can/index.htm"
    listofcandidates_header = get_code_token(refer_listofcandidates_url)
    url = 'https://easy.lagou.com/settings/template/in_temp.json?positionId='+str(positionId)
    get_requests(url,listofcandidates_header)


    employ_url = 'https://easy.lagou.com/can/batch/toStageEmploy.json'
    employ_data = {"resumeIds":resumeOwnerId}
    r = form_post(url=employ_url,headers=listofcandidates_header ,data=employ_data,remark='已入职')
    return r