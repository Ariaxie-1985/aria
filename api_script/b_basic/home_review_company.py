# coding:utf-8

from api_script.util import form_post, get_header, login_home


# 登录home后台
username = 'anan@lagou.com'
password = "990eb670f81e82f546cfaaae1587279a"
login_home(username,password)


# 审核公司
referer_queryPerson_home_url = "https://home.lagou.com/#/h_review/company"
queryCompany_url = "https://home.lagou.com/audit/companyApprove/queryCompanyByParam.json"
queryCompany_data = {"startPage":1,"pageSize":1,"approveTimeSort":"desc","auditStatusType":"wait"}
queryCompany_header = get_header(referer_queryPerson_home_url)
queryCompany_res = form_post(url=queryCompany_url, data=queryCompany_data, headers=queryCompany_header)
companyCheckId = queryCompany_res['data']['pageData'][0]['companyCheck']['id']

passCompanyApprove_url = "https://home.lagou.com/audit/companyApprove/passCompanyApprove.json"
passCompanyApprove_data = {"companyCheckId":companyCheckId}
form_post(url=passCompanyApprove_url, data=passCompanyApprove_data,headers=queryCompany_header)
