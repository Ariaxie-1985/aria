# coding:utf-8
# @Author: cloudyyuan
from api_script.jianzhao_web.talent_communication.Talent import allRead, quickReplyList, greetingList, quickReplySave, \
    quickReplyTop, Save
from util.util import login,get_code_token,form_post,get_header,get_requests,assert_equal

'''
人才沟通
'''
login('00852','20181205')

def test_list():
    '''
    获取会话列表
    :return:
    '''
    list()
    '''
    全部标记已读
    :return:
    '''
    allRead()
    '''
    快捷回复列表
    :return:
    '''
    quickReplyList()
    '''
    招呼模版列表
    :return:
    '''
    greetingList()
    '''
    快捷回复添加、修改,删除
    :return:
    '''
    quickReplySave()
    '''
    快捷回复置顶
    :return:
    '''
    quickReplyTop()
    '''
    添加快捷回复模版，不填写id即可
    :return:
    '''
    Save()