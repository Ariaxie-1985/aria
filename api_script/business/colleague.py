from utils.util import login, get_code_token, json_post

#添加同事为普通账号accounType是NORMAL，为特权账号是PAY_PRIVILEGE
def addColleague(phone,managerId,accountType):
    colleague_url = 'https://easy.lagou.com/colleague/add.json'
    colleague_header = get_code_token('https://easy.lagou.com/priveligeManage/queryPriveligeAcount/index.htm')
    data = {'accountType': accountType,'userName':'安安测试','phone':phone,'receiveResumeEmail':'anan1@lagou.com','positionName':'安安哈哈哈','managerId':managerId}
    s=json_post(url=colleague_url,headers=colleague_header,data=data,remark='添加同事',rd='旭峰')
    return s
