# coding:utf-8
# @Time  : 2019-08-01 12:32
# @Author: Xiawang
from utils.util import get_code_token, get_requests,login


def address_id(code):
    '''code: 市的code'''
    url = 'https://easy.lagou.com/lbs/getChildLbsInfoByCode.json?code={}'.format(code)
    header = get_code_token(url='https://easy.lagou.com/position/multiChannel/createPosition.htm')
    remark = '获取地址id'
    content = get_requests(url=url,headers=header,remark=remark).json()
    return content['content']['data']['lbsList']



if __name__ == '__main__':
    login('00852', 20181205)
    print(address_id('110100000'))