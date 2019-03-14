# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from utils.util import form_post,get_code_token, login,get_requests


def move_to_stageoffer(positionId,resumeOwnerId):
    refer_listofcandidates_url = "https://easy.lagou.com/can/index.htm"
    listofcandidates_header = get_code_token(refer_listofcandidates_url)
    url = 'https://easy.lagou.com/settings/template/in_temp.json?positionId='+str(positionId)
    get_requests(url,listofcandidates_header)


    stage_url = 'https://easy.lagou.com/can/batch/toStageOffer.json'
    stage_data = {"resumeIds":resumeOwnerId}
    r = form_post(url=stage_url,headers=listofcandidates_header ,data=stage_data,remark='录用')
    return r