# coding:utf-8
from util import get_code_token, form_post, get_header
import time


# 注册B端-成立公司-提交招聘者审核
b_register_url = 'https://passport.lagou.com/register/register.html?from=b'
phone = 20000208
userName = "千山万水"
companyFullName = "千山万水网测试拉勾"
resumeReceiveEmail = "test2018@sina.com"
companyShortName = "千山万水网测试"
updateCompanyShortName = "千山万水网测试"


# 注册B端
b_register_url = 'https://passport.lagou.com/register/register.html?from=b'
register_url = "https://passport.lagou.com/register/register.json"
register_data = {"isValidate": "true", "phone": phone, "phoneVerificationCode": "049281", "challenge": 111,
	                 "type": 1, "countryCode": "00852"}
register_header = get_code_token(b_register_url)
form_post(url=register_url, data=register_data, headers=register_header)


# 成立公司
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

# 提交招聘者审核
submit_url = "https://hr.lagou.com/corpCenter/hr/auth/file/submit.json"
submit_data = {"authenticationFileUrl": "i/audio1/M00/01/C5/CgHIk1wQzSaAcR09AAqex8SeJls235.JPG",
	            "holdIDCardPhotoUrl": "i/audio1/M00/01/C5/CgHIk1wQzR6AS8YlAAC5OWWN-yU456.JPG",
	            "updateCompanyShortName": updateCompanyShortName}
submit_header = get_code_token(step2_url)
form_post(url=submit_url, data=submit_data, headers=submit_header)

time.sleep(40)
# 申请认证公司
referer_com_url = "https://easy.lagou.com/bstatus/auth/index.htm"
headers = get_header(referer_com_url)
com_step1_url = "https://hr.lagou.com/corpCenter/company/auth/step1.html"
auth_file_url = "https://hr.lagou.com/corpCenter/company/auth/file.json"
auth_file_data = {"fileUrl":"i/audio1/M00/01/C5/CgHIk1wQzSaAcR09AAqex8SeJls235.JPG"}
auth_file_header = get_code_token(com_step1_url)
r = form_post(url=auth_file_url, data=auth_file_data, headers=auth_file_header)
print(r)

com_step2_url = "https://hr.lagou.com/corpCenter/company/auth/step2.html"
completeInfo_url = "https://hr.lagou.com/corpCenter/company/auth/completeInfo.json"
# todo：获取id
completeInfo_data = {"id":74, "logo":"i/audio1/M00/01/C6/CgHIk1wSFMeAeIoaAAB1mvl2DME518.JPG", "officialWebsite":"www.lagou.com","fullIntro":"愿天下没有难找的工作","shortIntro":"一天就能找到满意的工作","detailAddress":"海置创投大厦4层","provinceId":1,"cityId":5,"districtId":2005,"businessArea":"苏州街","companyLng":"116.307747","companyLat":"39.982128"}
completeInfo_header = get_code_token(com_step2_url)
r = form_post(url=completeInfo_url, data=completeInfo_data, headers=completeInfo_header)
print(r)
