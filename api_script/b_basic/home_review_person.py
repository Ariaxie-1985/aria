# coding:utf-8

from util import form_post, get_header, login_home

# 登录home后台
username = 'anan@lagou.com'
password = "990eb670f81e82f546cfaaae1587279a"
login_home(username,password)

# 审核招聘者
referer_queryPerson_home_url = "https://home.lagou.com/#/h_review/company"
queryPerson_url = "https://home.lagou.com/audit/personApprove/queryPersonByParam.json"
queryPerson_data = {"startPage":1,"pageSize":1,"approveTimeSort":"desc","auditStatusType":"wait"}
queryPerson_header = get_header(referer_queryPerson_home_url)
queryPerson_res = form_post(url=queryPerson_url, data=queryPerson_data, headers=queryPerson_header)
personCheckId = queryPerson_res['data']['pageData'][0]['personCheck']['id']

passPersonApprove_url = "https://home.lagou.com/audit/personApprove/passPersonApprove.json"
passPersonApprove_data = {"personCheckId":personCheckId}
form_post(url=passPersonApprove_url, data=passPersonApprove_data, headers=queryPerson_header)

