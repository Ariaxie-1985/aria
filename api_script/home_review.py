# coding:utf-8

from util import get_code_token, form_post, get_header

# 登录home后台
referer_login_home_url = "https://home.lagou.com/"
login_home_url = "https://passport.lagou.com/login/login.json"
login_home_data = {"isValidate": "true", "username": "anan@lagou.com", "password": "990eb670f81e82f546cfaaae1587279a"}
login_home_header = get_code_token(referer_login_home_url)
r = form_post(url=login_home_url, data=login_home_data, headers=login_home_header)

# 审核招聘者
referer_queryPerson_home_url = "https://home.lagou.com/#/h_review/company"
queryPerson_url = "https://home.lagou.com/audit/personApprove/queryPersonByParam.json"
queryPerson_data = {"startPage":1,"pageSize":1,"approveTimeSort":"desc","auditStatusType":"wait"}
queryPerson_header = get_header(referer_queryPerson_home_url)
queryPerson_res = form_post(url=queryPerson_url, data=queryPerson_data, headers=queryPerson_header)
personCheckId = queryPerson_res['data']['pageData'][0]['personCheck']['id']

passPersonApprove_url = "https://home.lagou.com/audit/personApprove/passPersonApprove.json"
passPersonApprove_data = {"personCheckId":personCheckId}
form_post(url=passPersonApprove_url, data=passPersonApprove_data)

# 审核公司
referer_queryPerson_home_url = "https://home.lagou.com/#/h_review/company"
queryCompany_url = "https://home.lagou.com/audit/companyApprove/queryCompanyByParam.json"
queryCompany_data = {"startPage":1,"pageSize":1,"approveTimeSort":"desc","auditStatusType":"wait"}
queryCompany_header = get_header(referer_queryPerson_home_url)
queryCompany_res = form_post(url=queryPerson_url, data=queryPerson_data, headers=queryPerson_header)
companyCheckId = queryCompany_res['data']['pageData'][0]['companyCheck']['id']

passCompanyApprove_url = "https://home.lagou.com/audit/companyApprove/passCompanyApprove.json"
passCompanyApprove_data = {"companyCheckId":companyCheckId}
form_post(url=passCompanyApprove_url, data=passCompanyApprove_data)
