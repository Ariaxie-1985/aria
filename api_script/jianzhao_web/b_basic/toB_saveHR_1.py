# coding:utf-8
# @Author: Xiawang
import json
import time
from typing import Dict

from utils.util import get_code_token, form_post, login, json_post


# 注册B端
def b_register(phone, countryCode):
    b_register_url = 'https://passport.lagou.com/register/register.html?from=b'
    register_url = "https://passport.lagou.com/register/register.json"
    register_data = {"isValidate": "true", "phone": phone, "phoneVerificationCode": "049281", "challenge": 111,
                     "type": 1, "countryCode": countryCode}
    register_header = get_code_token(b_register_url)
    remark = "验证B端注册"
    return form_post(url=register_url, data=register_data, headers=register_header, remark=remark)


# 上传B端用户信息
def saveHR(companyFullName, userName, resumeReceiveEmail, userPosition='HR'):
    step1_url = 'https://hr.lagou.com/corpCenter/openservice/step1.html'
    saveHR_url = "https://hr.lagou.com/corpCenter/openservice/saveHR.json"
    saveHR_data = {"userAvatar": "i/audio1/M00/01/C5/CgHIk1wQwXuAAz2hAAB1mvl2DME233.JPG", "userName": userName,
                   "userPosition": userPosition, "companyFullName": companyFullName,
                   "resumeReceiveEmail": resumeReceiveEmail}
    saveHR_header = get_code_token(step1_url)
    remark = "验证上传B端用户信息是否成功"
    return form_post(url=saveHR_url, data=saveHR_data, headers=saveHR_header, remark=remark)

# B端成立公司
def saveCompany(companyShortName, industryField="电商", financeStage='未融资'):
    financeStage, stages = get_financeStage(financeStage)
    step2_url = 'https://hr.lagou.com/corpCenter/openservice/step2.html'
    saveCompany_url = "https://hr.lagou.com/corpCenter/openservice/saveCompany.json"
    if stages is None:
        saveCompany_data = {"logo": "i/audio1/M00/01/C5/CgHIk1wQzAuAZ5-EAAmU9-3HjA4414.JPG",
                            "companyShortName": companyShortName,
                            "industryField": industryField, "companySize": "150-500人", "financeStage": financeStage}
    else:
        stages = json.dumps(stages)
        saveCompany_data = {"logo": "i/audio1/M00/01/C5/CgHIk1wQzAuAZ5-EAAmU9-3HjA4414.JPG",
                            "companyShortName": companyShortName,
                            "industryField": industryField, "companySize": "150-500人", "financeStage": financeStage,
                            'stages': stages}
    saveCompany_header = get_code_token(step2_url)
    remark = "验证B端成立公司是否成功"
    return form_post(url=saveCompany_url, data=saveCompany_data, headers=saveCompany_header, remark=remark)


# B端提交招聘者审核
def submit(updateCompanyShortName):
    submit_url = "https://hr.lagou.com/corpCenter/hr/auth/file/submit.json"
    submit_data = {"authenticationFileUrl": "i/audio1/M00/01/C5/CgHIk1wQzSaAcR09AAqex8SeJls235.JPG",
                   "holdIDCardPhotoUrl": "i/audio1/M00/01/C5/CgHIk1wQzR6AS8YlAAC5OWWN-yU456.JPG",
                   "updateCompanyShortName": updateCompanyShortName}
    step2_url = 'https://hr.lagou.com/corpCenter/openservice/step2.html'
    submit_header = get_code_token(step2_url)
    remark = "验证B端提交招聘者审核是否成功"
    return form_post(url=submit_url, data=submit_data, headers=submit_header, remark=remark)


# 新B端提交招聘者审核
def submit_new():
    submit_url = "https://hr.lagou.com/corpCenter/auth/person/idcard/submit.json"
    submit_data = {"imgUrl" : "i/audio1/M00/01/C5/CgHIk1wQzR6AS8YlAAC5OWWN-yU456.JPG"}
    step2_url = 'https://hr.lagou.com/corpCenter/openservice/step2.html'
    submit_header = get_code_token(step2_url)
    remark = "验证B端提交招聘者审核是否成功"
    return json_post(url=submit_url, data=submit_data, headers=submit_header, remark=remark)


# 加入B端的公司
def add_saveCompany():
    step2_url = 'https://hr.lagou.com/corpCenter/openservice/step2.html'
    saveCompany_url = "https://hr.lagou.com/corpCenter/openservice/saveCompany.json"
    saveCompany_header = get_code_token(step2_url)
    remark = "验证B端成立公司是否成功"
    return form_post(url=saveCompany_url, headers=saveCompany_header, remark=remark)


def saveHR_process(phone, countryCode, companyShortName, companyFullName, userName, resumeReceiveEmail,
                   updateCompanyShortName):
    r1, r2, r3, r4 = None, None, None, None
    r1 = b_register(phone, countryCode)
    if r1['state'] == 1:
        r2 = saveHR(companyFullName, userName, resumeReceiveEmail)
        r3 = saveCompany(companyShortName)
        r4 = submit(updateCompanyShortName)
    return r1, r2, r3, r4


def add_people_into_company(phone, countryCode, companyFullName, userName, resumeReceiveEmail, userPosition='HR'):
    r1, r2, r3, r4 = {'state': 0}, {'state': 0}, {'state': 0}, {'state': 0}
    r1 = b_register(phone, countryCode)
    if r1['state'] == 1:
        r2 = saveHR(companyFullName, userName, resumeReceiveEmail, userPosition)
        r3 = add_saveCompany()
        r4 = submit(companyFullName)
    return r1, r2, r3, r4


def creatCompany_process(phone, countryCode, companyShortName, companyFullName, userName,
                         resumeReceiveEmail, userPosition, updateCompanyShortName, industryField, financeStage):
    r1, r2, r3, r4 = None, None, None, None
    r1 = login(countryCode, phone)
    if r1['state'] == 1:
        r2 = saveHR(companyFullName, userName, resumeReceiveEmail, userPosition)
        r3 = saveCompany(companyShortName, industryField, financeStage)
        r4 = submit(updateCompanyShortName)
    return r1, r2, r3, r4


def get_financeStage(financeStage):
    financeStage_stages = {'天使轮': [{"stage": "天使轮", "investTime": "2016-07-07", "org": "真格基金", "investMoney": "100w"},
                                   {"stage": "A轮", "investTime": "", "org": "", "investMoney": ""},
                                   {"stage": "B轮", "investTime": "", "org": "", "investMoney": ""},
                                   {"stage": "C轮", "investTime": "", "org": "", "investMoney": ""},
                                   {"stage": "D轮及以上", "investTime": "", "org": "", "investMoney": ""}],
                           'A轮': [{"stage": "天使轮", "investTime": "2019-01-07", "org": "真格基金", "investMoney": "100w"},
                                  {"stage": "A轮", "investTime": "2019-02-07", "org": "腾讯", "investMoney": "1000w"},
                                  {"stage": "B轮", "investTime": "", "org": "", "investMoney": ""},
                                  {"stage": "C轮", "investTime": "", "org": "", "investMoney": ""},
                                  {"stage": "D轮及以上", "investTime": "", "org": "", "investMoney": ""}],
                           'B轮': [{"stage": "天使轮", "investTime": "2019-01-07", "org": "真格基金", "investMoney": "100w"},
                                  {"stage": "A轮", "investTime": "2019-02-07", "org": "腾讯", "investMoney": "1000w"},
                                  {"stage": "B轮", "investTime": "2019-03-07", "org": "真格基金", "investMoney": "5000w"},
                                  {"stage": "C轮", "investTime": "", "org": "", "investMoney": ""},
                                  {"stage": "D轮及以上", "investTime": "", "org": "", "investMoney": ""}],
                           'C轮': [{"stage": "天使轮", "investTime": "2019-01-07", "org": "真格基金", "investMoney": "100w"},
                                  {"stage": "A轮", "investTime": "2019-02-07", "org": "腾讯", "investMoney": "1000w"},
                                  {"stage": "B轮", "investTime": "2019-03-07", "org": "真格基金", "investMoney": "5000w"},
                                  {"stage": "C轮", "investTime": "2019-04-07", "org": "腾讯", "investMoney": "8000w"},
                                  {"stage": "D轮及以上", "investTime": "", "org": "", "investMoney": ""}],
                           'D轮及以上': [{"stage": "天使轮", "investTime": "2019-01-07", "org": "真格基金", "investMoney": "100w"},
                                     {"stage": "A轮", "investTime": "2019-02-07", "org": "腾讯", "investMoney": "1000w"},
                                     {"stage": "B轮", "investTime": "2019-03-07", "org": "真格基金", "investMoney": "5000w"},
                                     {"stage": "C轮", "investTime": "2019-04-07", "org": "腾讯", "investMoney": "8000w"},
                                     {"stage": "D轮及以上", "investTime": "2019-05-07", "org": "腾讯",
                                      "investMoney": "一亿美金"}]}
    stages = financeStage_stages.get(financeStage, None)
    return financeStage, stages


if __name__ == '__main__':
    # print(get_financeStage('未融资'))
    # b_register(20030100,'00853')
    success_list = [i for i in range(20030252, 20030291)]
    # phone_list = [i for i in range(20030252,20030352)]
    # for phone in phone_list:
    #     res = b_register(phone, '00853')
    #     if res['state'] == 1:
    #         success_list.append(phone)
    #     if len(success_list) == 39:
    #         break
    print(success_list)
