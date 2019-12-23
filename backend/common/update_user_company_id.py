# coding:utf-8
# @Time  : 2019-06-19 14:54
# @Author: Xiawang
from backend.common.address import connect_mds_position, connect_testing_platform
from utils.util import get_code_token, form_post


def get_user_company_id():
    refer_createPosition_url = "https://easy.lagou.com/position/multiChannel/createPosition.htm"
    Position_header = get_code_token(refer_createPosition_url)
    url = 'https://easy.lagou.com/member/getMemberInfo.json'
    remark = '获取userId和companyId'
    res = form_post(url=url, headers=Position_header, remark=remark)
    userId = res['content']['data']['memberInfo']['userId']
    companyId = res['content']['data']['memberInfo']['companyId']
    return userId, companyId


def update_user_company_id(address_id, userId, companyId):
    db, cursor = connect_mds_position()
    db.ping(reconnect=True)
    cursor.execute(
        "UPDATE t_work_address set company_id = {}, user_id = {} WHERE id = {}".format(companyId, userId,
                                                                                       address_id))
    db.commit()
    res = cursor.execute(
        "SELECT * FROM t_work_address WHERE id = {} and company_id = {} and user_id = {}".format(address_id, companyId,
                                                                                                 userId,
                                                                                                 ))
    db.close()
    return bool(res)



