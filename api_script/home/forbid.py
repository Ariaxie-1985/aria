# coding:utf-8
# @Time  : 2019-11-21 15:26
# @Author: Xiawang
# Description:
from utils.util import get_header, form_post, login_home, login_password


def forbid_user(userId):
    url = 'http://home.lagou.com/forbid/user/forbidUser.json'
    header = get_header(url='http://home.lagou.com/')
    data = {'forbidAccount': '删除已投递简历,关闭简历,', 'reason': '冒用他人信息,', 'forbidAccountReason': '冒用他人信息,', 'userId': userId}
    return form_post(url=url, headers=header, data=data, remark="封禁账号")['success']


def verify_user_is_forbid(userId):
    url = 'http://home.lagou.com/forbid/user/queryUser.json'
    header = get_header(url='http://home.lagou.com/')
    data = {'searchContent': userId, 'limit': 15, 'currentPage': 0, 'typeSearch': 1}
    result = form_post(url=url, headers=header, data=data, remark='校验用户是否禁用成功')
    if result['success'] == True and result['data']['pageData'][0]['id'] == userId:
        return result['data']['pageData'][0]['isForbid']
    else:
        return False


def home_query_user_id(telephone):
    url = 'http://home.lagou.com/forbid/user/queryUser.json'
    header = get_header(url='http://home.lagou.com/')
    data = {'searchContent': "+{}".format(telephone), 'limit': 15, 'currentPage': 0, 'typeSearch': 1}
    result = form_post(url=url, headers=header, data=data, remark='查询成功')
    if result['success'] == True and result['data']['pageData'][0]['isForbid'] == True:
        return result['data']['pageData'][0]['id']
    else:
        return False


def forbid_company(companyId):
    url = 'http://home.lagou.com/forbid/companyController/forbid.json'
    data = {'companyId': companyId, 'forbidReason': '公司信息不实（发布职位与公司经营范围不符）,'}
    header = get_header(url='http://home.lagou.com/')
    return form_post(url=url, headers=header, data=data, remark='封禁公司')['success']


def verify_company_is_forbid(companyId):
    url = 'http://home.lagou.com/forbid/companyController/queryCompanys.json'
    header = get_header(url='http://home.lagou.com/')
    data = {'searchContent': companyId, 'limit': 35, 'limitEnd': 30, 'currentPage': 0, 'type': 1}
    result = form_post(url=url, headers=header, data=data, remark='校验用户是否禁用成功')
    if result['success'] == True and result['data']['pageData'][0]['id'] == companyId:
        return result['data']['pageData'][0]['status']
    else:
        return False


if __name__ == '__main__':
    login_password(username='betty@lagou.com', password='00f453dfec0f2806db5cfabe3ea94a35')
    # ids = [15576859, 15576821, 15576816, 15576806, 15576799, 15587425, 15576660, 15576652, 15576430, 15576423, 15576405]
    # ids = [15568389, 15568375, 15568364, 15568304, 15568256, 15568233, 15568220, 15241840, 15309651, 15545942,
    #          15431115, 15470085, 15222746, 15231268, 15232802]
    ids = [15232864, 15470242, 15470246, 15470379, 15594841, 15592474, 15577156, 15577149, 15577090, 15577085,
           15576954, 15576950, 15576937, 15576763]
    # ids = [15576757, 15576695, 15576688, 15576666, 15568195, 15568178, 15568153, 15568130, 15567700, 15567691, 15567400,
    #        15567390, 15562495, 15562483, 15558634]
    # ids = [15558629, 15554148, 15554140, 15553909, 15553655, 15252648, 15255408, 15232933, 15233096, 15233116,
    #          15255474, 15255485, 15429912]
    # for id in ids:
    # forbid_user(id)
    print(type(verify_user_is_forbid(15754261)))
    print('用户封禁结果是{}'.format(verify_user_is_forbid(15754261)))
    print('公司封禁结果是{}'.format(verify_company_is_forbid(117437231)))
