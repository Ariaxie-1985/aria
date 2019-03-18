# coding:utf-8
# @Author: Xiawang
from utils.util import get_code_token, form_post



# 注册B端
def b_register(phone, countryCode):
	b_register_url = 'https://passport.lagou.com/register/register.html?from=b'
	register_url = "https://passport.lagou.com/register/register.json"
	register_data = {"isValidate": "true", "phone": phone, "phoneVerificationCode": "049281", "challenge": 111,
		                 "type": 1, "countryCode": countryCode}
	register_header = get_code_token(b_register_url)
	remark = "验证B端注册"
	return form_post(url=register_url, data=register_data, headers=register_header,remark=remark)


# 上传B端用户信息
def saveHR(companyFullName,userName,resumeReceiveEmail):
	step1_url = 'https://hr.lagou.com/corpCenter/openservice/step1.html'
	saveHR_url = "https://hr.lagou.com/corpCenter/openservice/saveHR.json"
	saveHR_data = {"userAvatar": "i/audio1/M00/01/C5/CgHIk1wQwXuAAz2hAAB1mvl2DME233.JPG", "userName": userName,
	               "userPosition": "HR BP", "companyFullName": companyFullName, "resumeReceiveEmail": resumeReceiveEmail}
	saveHR_header = get_code_token(step1_url)
	remark="验证上传B端用户信息是否成功"
	return form_post(url=saveHR_url, data=saveHR_data, headers=saveHR_header,remark=remark)

# B端成立公司
def saveCompany(companyShortName):
	step2_url = 'https://hr.lagou.com/corpCenter/openservice/step2.html'
	saveCompany_url = "https://hr.lagou.com/corpCenter/openservice/saveCompany.json"
	saveCompany_data = {"logo": "i/audio1/M00/01/C5/CgHIk1wQzAuAZ5-EAAmU9-3HjA4414.JPG", "companyShortName": companyShortName,
		                "industryField": "移动互联网", "companySize": "150-500人", "financeStage": "不需要融资"}
	saveCompany_header = get_code_token(step2_url)
	remark = "验证B端成立公司是否成功"
	return form_post(url=saveCompany_url, data=saveCompany_data, headers=saveCompany_header,remark=remark)

# B端提交招聘者审核
def submit(updateCompanyShortName):
	submit_url = "https://hr.lagou.com/corpCenter/hr/auth/file/submit.json"
	submit_data = {"authenticationFileUrl": "i/audio1/M00/01/C5/CgHIk1wQzSaAcR09AAqex8SeJls235.JPG",
		            "holdIDCardPhotoUrl": "i/audio1/M00/01/C5/CgHIk1wQzR6AS8YlAAC5OWWN-yU456.JPG",
		            "updateCompanyShortName": updateCompanyShortName}
	step2_url = 'https://hr.lagou.com/corpCenter/openservice/step2.html'
	submit_header = get_code_token(step2_url)
	remark="验证B端提交招聘者审核是否成功"
	return form_post(url=submit_url, data=submit_data, headers=submit_header,remark=remark)

# 加入B端的公司
def add_saveCompany():
	step2_url = 'https://hr.lagou.com/corpCenter/openservice/step2.html'
	saveCompany_url = "https://hr.lagou.com/corpCenter/openservice/saveCompany.json"
	saveCompany_header = get_code_token(step2_url)
	remark = "验证B端加入已有的公司是否成功"
	return form_post(url=saveCompany_url, headers=saveCompany_header,remark=remark)


def saveHR_process(phone,countryCode,companyShortName,companyFullName,userName,resumeReceiveEmail,updateCompanyShortName):
	r1, r2, r3, r4 = None, None, None, None
	r1 = b_register(phone,countryCode)
	if r1['state'] == 1:
		r2 = saveHR(companyFullName,userName,resumeReceiveEmail)
		r3 = saveCompany(companyShortName)
		r4 = submit(updateCompanyShortName)
	return r1,r2,r3,r4

def add_people_into_company(phone,countryCode,companyFullName, userName, resumeReceiveEmail):
	r1, r2, r3, r4 = None, None, None, None
	r1 = b_register(phone, countryCode)
	if r1['state'] == 1:
		r2 = saveHR(companyFullName, userName, resumeReceiveEmail)
		r3 = add_saveCompany()
		r4 = submit(companyFullName)
	return r1, r2, r3, r4
