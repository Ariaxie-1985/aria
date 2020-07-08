from utils.util import login, get_code_token, json_post, form_post
import json


# 获取特权账号列表
def queryPriveligeAcount(keyword=None):
    url = 'https://easy.lagou.com/priveligeManage/queryPriveligeAcount.json'
    header = get_code_token('https://easy.lagou.com/priveligeManage/queryPriveligeAcount/index.htm')
    data = {"pageNo": "1", "pageSize": "100", "keyword": keyword, "onlySubAccount": 'false',
            "showNormalAccount": 'false'}
    s = json_post(url=url, headers=header, data=data, remark='获取特权账号列表', rd='李久超')
    a = s.get('state')
    search_result = s.get('content').get('data').get('userPriveligePage').get('result')
    return search_result


# 特权账号调整为高级管理员（高级管理员为PAY_SENIOR,特权账号为PAY_PRIVILEGE，普通账号为NORMAL)
def reAssignRole(userId, accountRole):
    url = 'https://easy.lagou.com/priveligeManage/reAssignRole.json'
    header = get_code_token('https://easy.lagou.com/priveligeManage/queryPriveligeAcount/index.htm')
    data = {"accountRole": accountRole, "userId": userId}
    result = form_post(url=url, headers=header, data=data, remark='调整特权账号角色为高级管理员', rd='李久超')
    message = result.get('message')
    return message


# 获取当前登录账号权益（有权益管理权益的账号）
def queryManagerPriveligeInfo():
    url = 'https://easy.lagou.com/priveligeManage/queryManagerPriveligeInfo.json'
    header = get_code_token('https://easy.lagou.com/priveligeManage/queryPriveligeAcount/index.htm')
    managerPriveligeResult = json_post(url=url, headers=header, remark='获取用户权益', rd='李久超')
    '''state = result.get('state')'''
    '''managerPriveligeInfo = managerPriveligeResult.get('content').get('data').get('managerPriveligeInfo')  # 获取权益列表'''
    return managerPriveligeResult



# 获取调整权益弹框数据
def queryPriveligeAssignInfo(userid):
    url = 'https://easy.lagou.com/priveligeManage/queryPriveligeAssignInfo.json'
    header = get_code_token('https://easy.lagou.com/priveligeManage/queryPriveligeAcount/index.htm')
    data = {'userId': userid}
    result = form_post(url=url, headers=header, data=data, remark='获取调整权益弹框', rd='李久超')
    '''state = result.get('state')'''
    '''info = result.get('content').get('data').get('info')'''
    return result


# 调整权益
def reAssignPrivelige(baseGoodsId, reAssignNum, userid, username, info):
    url = 'https://easy.lagou.com/priveligeManage/reAssignPrivelige.json'
    header = get_code_token('https://easy.lagou.com/priveligeManage/queryPriveligeAcount/index.htm')
    assignInfo = []
    for i in info:
        if i.get('baseGoodsId') == baseGoodsId:
            b = {'userid': userid, 'userName': username, 'email': '',
                 'baseGoodsId': i.get('baseGoodsId'),
                 'totalNum': i.get('user_total'),
                 'num': i.get('user_num'),
                 'reAssignNum': int(reAssignNum) + int(i.get('user_remain'))
                 }
        else:
            b = {'userid': userid, 'userName': username, 'email': '',
                 'baseGoodsId': i.get('baseGoodsId'),
                 'totalNum': i.get('user_total'),
                 'num': i.get('user_num'),
                 'reAssignNum': i.get('user_remain')
                 }
        assignInfo.append(b)
    data = {'userid': userid,
            'assignInfo': assignInfo}
    data["assignInfo"] = json.dumps(data['assignInfo'], ensure_ascii=False)
    print(data)
    result = form_post(url=url, data=data, headers=header, remark="调整权益", rd='李久超')
    message = result.get('message')
    return message


'''
login('0086','17619121001')
print (reAssignPrivelige(baseGoodsId=614, reAssignNum=1000,userid=100030398))'''
