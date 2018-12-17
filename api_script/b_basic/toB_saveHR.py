# coding:utf-8
from util import get_code_token, form_post, get_header, login_home
import time
import re


# 注册B端-成立公司-提交招聘者审核
b_register_url = 'https://passport.lagou.com/register/register.html?from=b'
phone = 20000215
userName = "英皇容祖儿6"
companyFullName = "英皇容祖儿网测试拉勾6"
resumeReceiveEmail = "test2018@sina.com"
companyShortName = "英皇容祖儿网测试6"
updateCompanyShortName = "英皇容祖儿网测试6"


# 注册B端
b_register_url = 'https://passport.lagou.com/register/register.html?from=b'
register_url = "https://passport.lagou.com/register/register.json"
register_data = {"isValidate": "true", "phone": phone, "phoneVerificationCode": "049281", "challenge": 111,
	                 "type": 1, "countryCode": "00852"}
register_header = get_code_token(b_register_url)
form_post(url=register_url, data=register_data, headers=register_header)


# B端成立公司
step1_url = 'https://hr.lagou.com/corpCenter/openservice/step1.html'
saveHR_url = "https://hr.lagou.com/corpCenter/openservice/saveHR.json"
saveHR_data = {"userAvatar": "i/audio1/M00/01/C5/CgHIk1wQwXuAAz2hAAB1mvl2DME233.JPG", "userName": userName,
               "userPosition": "HR BP", "companyFullName": companyFullName, "resumeReceiveEmail": resumeReceiveEmail}
saveHR_header = get_code_token(step1_url)
form_post(url=saveHR_url, data=saveHR_data, headers=saveHR_header)

step2_url = 'https://hr.lagou.com/corpCenter/openservice/step2.html'
saveCompany_url = "https://hr.lagou.com/corpCenter/openservice/saveCompany.json"
saveCompany_data = {"logo": "i/audio1/M00/01/C5/CgHIk1wQzAuAZ5-EAAmU9-3HjA4414.JPG", "companyShortName": companyShortName,
	                "industryField": "移动互联网", "companySize": "150-500人", "financeStage": "不需要融资"}
saveCompany_header = get_code_token(step2_url)
form_post(url=saveCompany_url, data=saveCompany_data, headers=saveCompany_header)

# B端提交招聘者审核
submit_url = "https://hr.lagou.com/corpCenter/hr/auth/file/submit.json"
submit_data = {"authenticationFileUrl": "i/audio1/M00/01/C5/CgHIk1wQzSaAcR09AAqex8SeJls235.JPG",
	            "holdIDCardPhotoUrl": "i/audio1/M00/01/C5/CgHIk1wQzR6AS8YlAAC5OWWN-yU456.JPG",
	            "updateCompanyShortName": updateCompanyShortName}
submit_header = get_code_token(step2_url)
form_post(url=submit_url, data=submit_data, headers=submit_header)


