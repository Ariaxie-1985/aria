# coding:utf-8
# @Author: Xiawang
from utils.util import form_post, get_header


# 审核招聘者
def passPersonApprove():
	referer_queryPerson_home_url = "https://home.lagou.com/#/h_review/company"
	queryPerson_url = "https://home.lagou.com/audit/personApprove/queryPersonByParam.json"
	queryPerson_data = {"startPage":1,"pageSize":1,"approveTimeSort":"desc","auditStatusType":"wait"}

	queryPerson_header = get_header(referer_queryPerson_home_url)
	remark="验证home后台-审核中心-倒序获取招聘者的id是否成功"
	queryPerson_res = form_post(url=queryPerson_url, data=queryPerson_data, headers=queryPerson_header,remark=remark)
	personCheckId = queryPerson_res['data']['pageData'][0]['personCheck']['id']
	companyId = queryPerson_res['data']['pageData'][0]['companyCheckVo']['companyId']
	userId = queryPerson_res['data']['pageData'][0]['personCheckVo']['userId']

	passPersonApprove_url = "https://home.lagou.com/audit/personApprove/passPersonApprove.json"
	passPersonApprove_data = {"personCheckId":personCheckId}
	remark = "验证home后台-审核中心-个人认证-审核招聘者是否成功"
	return form_post(url=passPersonApprove_url, data=passPersonApprove_data, headers=queryPerson_header,remark=remark), companyId, userId
