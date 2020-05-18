# coding:utf-8
# @Time  : 2020/3/18 12:13
# @Author: Xiawang
# Description:
from bs4 import BeautifulSoup

from utils.util import get_header, get_requests, form_post, get_code_token


def jump_easy_index_html(ip_port=None):
    url = "https://easy.lagou.com/dashboard/index.htm?from=c_index"
    header = get_header(url='https://www.lagou.com/', ip_port=ip_port)
    remark = '从拉勾主站进入企业版'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port)

def hr_jump_easy_index_html(ip_port=None):
    url = "https://easy.lagou.com/dashboard/index.htm"
    header = get_header(url='https://hr.lagou.com/corpCenter/openservice/step1.html', ip_port=ip_port)
    remark = '从 hr.lagou.com 进入企业版'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port)

def search_plusSearchSelector(ip_port=None):
    url = 'https://easy.lagou.com/search/plusSearchSelector.json?from=talentsearch'
    header = get_header(url='https://easy.lagou.com/dashboard/index.htm?from=c_index', ip_port=ip_port)
    remark = '人才查找'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def get_easy_plus_privilegeCount(ip_port=None):
    url = 'https://easy.lagou.com/dashboard/getEasyPlusPrivilegeCount.json'
    header = get_header(url='https://easy.lagou.com/dashboard/index.htm?from=c_index', ip_port=ip_port)
    remark = '获取当前用户的拉勾加权限信息'
    return form_post(url=url, headers=header, remark=remark, ip_port=ip_port)


def get_business_user_info(ip_port=None):
    url = 'https://easy.lagou.com/businessUser/getBusinessUserInfo.json'
    header = get_header(url='https://easy.lagou.com/dashboard/index.htm?from=c_index', ip_port=ip_port)
    remark = '获取用户的商业信息'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def get_user_goods_info(ip_port=None):
    url = 'https://easy.lagou.com/dashboard/getUserGoodsInfo.json'
    header = get_header(url='https://easy.lagou.com/dashboard/index.htm?from=c_index', ip_port=ip_port)
    remark = '获取用户的权益信息'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def get_yun_additional_info(ip_port=None):
    url = 'https://easy.lagou.com/dashboard/getYunAdditionalInfo.json'
    header = get_header(url='https://easy.lagou.com/dashboard/index.htm?from=c_index', ip_port=ip_port)
    remark = '获取用户的简历的待办事项'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def is_hunting_gray(ip_port=None):
    url = 'https://easy.lagou.com/api/onlinehunting/isHuntingGray.json'
    header = get_header(url='https://easy.lagou.com/dashboard/index.htm?from=c_index', ip_port=ip_port)
    remark = '？'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def personal_assistant(ip_port=None):
    url = 'https://easy.lagou.com/dashboard/personal_assistant.json'
    header = get_header(url='https://easy.lagou.com/dashboard/index.htm?from=c_index', ip_port=ip_port)
    remark = '获取当前公司的招聘顾问'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def get_product_version(ip_port=None):
    url = 'https://easy.lagou.com/productContract/productVersion.json'
    header = get_header(url='https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm?pageNo=1',
                        ip_port=ip_port)
    remark = '获取当前公司的拉勾加版本号'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def get_all_members(ip_port=None):
    url = 'https://easy.lagou.com/member/allMembers.json?pageNum=1&pageSize=1'
    header = get_header(url='https://easy.lagou.com/position/multiChannel/companyOtherPositions.htm?pageNo=1',
                        ip_port=ip_port)
    remark = '获取公司内的所有成员'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def head_notifications(ip_port=None):
    url = 'https://easy.lagou.com/notification/headNotifications.json?start=0&size=5'
    header = get_code_token(url='https://easy.lagou.com/settings/account/me.htm?', ip_port=ip_port)
    remark = '通知'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def account_my_role(ip_port=None):
    url = 'https://easy.lagou.com/user/account/my/role.json'
    header = get_code_token(url='https://easy.lagou.com/settings/account/me.htm?', ip_port=ip_port)
    remark = '获取当前用户的角色权限'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def get_shield_expire(ip_port=None):
    url = 'https://easy.lagou.com/im/chat/getShieldExpire.json'
    header = get_code_token(url='https://easy.lagou.com/settings/account/me.htm?', ip_port=ip_port)
    remark = '获取当前消息是否过期'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def account_portrait(ip_port=None):
    url = 'https://easy.lagou.com/settings/account/portrait.json'
    header = get_code_token(url='https://easy.lagou.com/settings/account/me.htm?', ip_port=ip_port)
    remark = '获取当前用户的头像'
    return form_post(url=url, headers=header, remark=remark, ip_port=ip_port)


def notice_show(ip_port=None):
    url = 'https://easy.lagou.com/notice/show.json'
    header = get_code_token(url='https://easy.lagou.com/settings/account/me.htm?', ip_port=ip_port)
    data = {
        'noticeType': 'FIRST_PUBLISH_POSITION'
    }
    remark = '是否显示通知'
    return form_post(url=url, headers=header, data=data, remark=remark, ip_port=ip_port)


def check_upgrade_to_share(ip_port=None):
    url = 'https://easy.lagou.com/productContract/checkUpgradeToShare.json'
    header = get_code_token(url='https://easy.lagou.com/bstatus/auth/index.htm?', ip_port=ip_port)
    remark = '检查产品升级更新'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def get_my_member_info(ip_port=None):
    url = 'https://easy.lagou.com/member/getMyMemberInfo.json'
    header = get_header(url='https://easy.lagou.com/member/all_members.htm?', ip_port=ip_port)
    remark = '获取当前用户信息'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def search_colleague(ip_port=None):
    url = 'https://easy.lagou.com/member/searchColleague.json'
    header = get_header(url='https://easy.lagou.com/member/all_members.htm?', ip_port=ip_port)
    data = {
        'isRecruiter': 'false'
    }
    remark = '寻找同事'
    return form_post(url=url, headers=header, data=data, remark=remark, ip_port=ip_port)


def sub_account_button(ip_port=None):
    url = 'https://easy.lagou.com/colleague/subAccountButton/display.json'
    header = get_header(url='https://easy.lagou.com/member/all_members.htm?', ip_port=ip_port)
    remark = '是否显示子账号按钮'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def is_show_position_notice(ip_port=None):
    url = 'https://easy.lagou.com/position/multiChannel/isShowPositionNotice.json'
    header = get_header(url='https://easy.lagou.com/settings/new/channel/my_channels.htm?', ip_port=ip_port)
    remark = '是否显示职位通知'
    return form_post(url=url, headers=header, remark=remark, ip_port=ip_port)


def dashboard_index_get_user_id():
    url = 'https://easy.lagou.com/dashboard/index.htm?from=c_index'
    r = get_requests(url=url).text
    soup = BeautifulSoup(r, "html.parser")
    try:
        userId = soup.find(id="UserId")['value']
    except TypeError:
        r = get_requests(url=url, remark='获取easy主页的用户id').text
        soup = BeautifulSoup(r, "html.parser")
        userId = soup.find(id="UserId")['value']
    return userId