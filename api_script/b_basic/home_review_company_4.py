# coding:utf-8

from util.util import form_post, get_header


# home 审核公司
def passCompanyApprove():
	referer_queryPerson_home_url = "https://home.lagou.com/#/h_review/company"
	queryCompany_url = "https://home.lagou.com/audit/companyApprove/queryCompanyByParam.json"
	queryCompany_data = {"startPage":1,"pageSize":1,"approveTimeSort":"desc","auditStatusType":"wait"}
	queryCompany_header = get_header(referer_queryPerson_home_url)
	remark="倒序获取公司的id"
	queryCompany_res = form_post(url=queryCompany_url, data=queryCompany_data, headers=queryCompany_header,remark=remark)
	companyCheckId = queryCompany_res['data']['pageData'][0]['companyCheck']['id']

	passCompanyApprove_url = "https://home.lagou.com/audit/companyApprove/passCompanyApprove.json"
	passCompanyApprove_data = {"companyCheckId":companyCheckId}
	remark = "home后台-公司认证-审核公司"
	return form_post(url=passCompanyApprove_url, data=passCompanyApprove_data,headers=queryCompany_header,remark=remark)