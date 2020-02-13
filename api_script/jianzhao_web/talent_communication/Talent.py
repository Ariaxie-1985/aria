# coding:utf-8
# @Author: cloudyyuan

from utils.util import login, get_code_token, form_post, get_header, get_requests, assert_equal

'''
人才沟通
'''
login('00852', '20181205')


def session_list():
    '''
    获取会话列表
    :return:
    '''
    header = get_header("https://easy.lagou.com/im/chat/index.htm")
    # data={"pageNo":1,"pageSize":15,"createBy":0,"unReadOnly":0}
    url = "https://easy.lagou.com/im/session/list.json?pageNo=1&pageSize=15&createBy=0&unReadOnly=0"
    object = get_requests(url=url, remark="获取会话列表", headers=header)
    meassage = object.json()['message']
    assert_equal("操作成功", meassage, "获取会话列表成功", "获取会话列表失败")


def allRead():
    '''
    全部标记已读
    :return:
    '''
    header = get_header("https://easy.lagou.com/im/chat/index.htm")
    url = "https://easy.lagou.com/im/session/allRead.json?createBy=0&unReadOnly=0"
    object = get_requests(url=url, remark="全部标记已读", headers=header)
    meassage = object.json()['message']
    assert_equal("操作成功", meassage, "全部标记已读成功", "全部标记已读失败")


def quickReplyList():
    '''
    快捷回复列表
    :return:
    '''
    header = get_header("https://easy.lagou.com/im/chat/index.htm")
    url = "https://easy.lagou.com/im/quickReply/list.json"
    object = get_requests(url=url, remark="快捷回复列表", headers=header)
    meassage = object.json()['message']
    id = object.json()['content']['rows'][0]['id']
    print(id)
    assert_equal("操作成功", meassage, "快捷回复列表成功", "快捷回复列表失败")
    return id


def greetingList():
    '''
    招呼模版列表
    :return:
    '''
    header = get_header("https://easy.lagou.com/im/chat/index.htm")
    url = "https://easy.lagou.com/im/greeting/list.json"
    object = get_requests(url=url, remark="招呼模板列表", headers=header)
    meassage = object.json()['message']
    assert_equal("操作成功", meassage, "招呼模板列表成功", "招呼模板列表失败")


def quickReplySave():
    '''
    快捷回复添加、修改,删除
    :return:
    '''
    id = quickReplyList()
    print(id)
    header = get_header("https://easy.lagou.com/im/chat/index.htm")
    url = "https://easy.lagou.com/im/quickReply/save.json?id=" + str(
        id) + "&content=%E6%B5%8B%E8%AF%95%E6%B5%8B%E8%AF%95%E8%BD%A6%E5%B8%82%E6%98%AF%E6%98%AF%E5%95%A5is%E5%8F%91%E5%9C%B0%E6%96%B9%E7%AE%80%E5%8E%86%E7%82%B9%E5%87%BB%E6%B3%95%E6%8B%89%E7%9B%9B%E8%A7%A3%E6%94%BE%E8%B7%AF%E6%B3%95%E5%BE%8B%E7%9A%84%E8%A7%A3%E6%94%BE%E8%B7%AF%E5%8F%A3"
    object = get_requests(url=url, remark="快捷回复添加、修改", headers=header)
    meassage = object.json()['message']
    assert_equal("操作成功", meassage, "快捷回复添加、修改成功", "快捷回复添加、修改失败")
    url = "https://easy.lagou.com/im/quickReply/delete/" + str(id) + ".json"
    object = get_requests(url=url, remark="删除新增的模版", headers=header)
    meassage = object.json()['message']
    assert_equal("操作成功", meassage, "删除模版成功", "删除模版失败")


def quickReplyTop():
    '''
    快捷回复置顶
    :return:
    '''
    id = quickReplyList()
    print(id)
    header = get_header("https://easy.lagou.com/im/chat/index.htm")
    url = "https://easy.lagou.com/im/quickReply/top/" + str(id) + ".json"
    object = get_requests(url=url, remark="快捷回复置顶", headers=header)
    meassage = object.json()['message']
    assert_equal("操作成功", meassage, "快捷回复置顶成功", "快捷回复置顶失败")


def Save():
    '''
    添加快捷回复模版，不填写id即可
    :return:
    '''
    id = quickReplyList()
    print(id)
    header = get_header("https://easy.lagou.com/im/chat/index.htm")
    url = "https://easy.lagou.com/im/quickReply/save.json?&content=你好，我对你的经历比较感兴趣，目前考虑新的机会吗？"
    object = get_requests(url=url, remark="快捷回复添加、修改", headers=header)
    meassage = object.json()['message']
    assert_equal("操作成功", meassage, "快捷回复添加、修改成功", "快捷回复添加、修改失败")

#
# list()
# allRead()
# quickReplyList()
# greetingList()
# quickReplySave()
# quickReplyTop()
# Save()
