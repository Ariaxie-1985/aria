from utils.util import form_post, get_requests, login, get_header, json_post, get_code_token
import requests
import json


def upload_permit():
    '''
    招聘者提交认证之上传营业执照
    提交审核记录到Home平台
    :return:
    '''
    # com_header = get_header("https://easy.lagou.com/dashboard/index.htm?from=c_index")headers=com_header
    get_requests("https://hr.lagou.com/corpCenter/staff/index.html")
    verify_url = "https://hr.lagou.com/corpCenter/staff/next/enterprise.json"
    verify_data = {"fileUrl": "i/image2/M01/AF/EF/CgoB5l3mDqWAPbXyAACQ9vLCc5I534.png", "force": True}
    verify_header = get_code_token("https://hr.lagou.com/corpCenter/staff/index.html")
    remark = "上传营业执照"
    return json_post(url=verify_url, data=verify_data, headers=verify_header, remark=remark)


def upload_identity_card():
    pass
