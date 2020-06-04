# coding:utf-8
# @Time  : 2019-05-21 11:42
# @Author: Xiawang

# 2019-05-21 添加和分配流程优化
import json

from utils.util import get_requests, get_header, get_code_token, form_post, login


def queryParentUser():
    url = 'https://easy.lagou.com/userGoodsRecord/queryParentUser.json'
    header = get_header('https://easy.lagou.com/dashboard/index.htm?')
    remark = '普通账号/子账号申请权益弹框信息接口'
    return get_requests(url=url, headers=header, remark=remark)


def sendApplyAssignGoodsWithNum(parentId, applyForSubAccount, applybaseGoods):
    url = 'https://easy.lagou.com/userGoodsRecord/sendApplyAssignGoodsWithNum.json'
    header = get_code_token('https://easy.lagou.com/dashboard/index.htm?')
    data = {
        'parentId': parentId,
        'applyForSubAccount': applyForSubAccount,
        'applyGoods': [applybaseGoods]
    }
    data["applyGoods"] = json.dumps(data["applyGoods"], ensure_ascii=False)
    remark = '普通账号/子账号权益申请提交接口'
    return form_post(url=url, data=data, headers=header, remark=remark)


def pendingApplyRecords():
    url = 'https://easy.lagou.com/userGoodsRecord/pendingApplyRecords.json'
    header = get_header('https://easy.lagou.com/dashboard/index.htm?')
    remark = '管理员 待处理申请查询接口'
    return get_requests(url=url, headers=header, remark=remark)


def count_pending_apply_records(ip_port=None):
    url = 'https://easy.lagou.com/userGoodsRecord/countPendingApplyRecords.json'
    header = get_header('https://easy.lagou.com/bstatus/auth/index.htm?', ip_port=ip_port)
    remark = '管理员 查询待处理权益申请数量接口'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port)


def addAccountFromApply(applyRecordId):
    url = 'https://easy.lagou.com/subAccount/addAccountFromApply.json'
    header = get_header('https://easy.lagou.com/dashboard/index.htm?')
    data = {
        'applyRecordId': applyRecordId
    }
    remark = '从待处理页面添加子账号接口'
    return form_post(url=url, headers=header, data=data, remark=remark)


def allocateGoodsFromApply(applyRecordId, allocateGoods):
    url = 'https://easy.lagou.com/userGoodsRecord/allocateGoodsFromApply.json'
    header = get_header('https://easy.lagou.com/dashboard/index.htm?')
    data = {
        'applyRecordId': applyRecordId,
        'allocateDetail': [
            allocateGoods
        ]
    }
    data["allocateDetail"] = json.dumps(data["allocateDetail"], ensure_ascii=False)
    remark = '管理员 分配接口'
    return form_post(url=url, headers=header, data=data, remark=remark)

# login('00852', 20021215)
# r = queryParentUser()
# login('00852',20181205)
# pendingApplyRecords()
# countPendingApplyRecords()
