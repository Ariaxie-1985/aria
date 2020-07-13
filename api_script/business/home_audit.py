# @Time  : 2020/4/27 17:44
# @Author: Xiawang
# Description:
from utils.util import get_header, form_post


def query_risk_labels_by_company(companyId):
    url = 'http://home.lagou.com/audit/companyApprove/queryRiskLabelsByCompany.json'
    header = get_header(url='http://home.lagou.com/index.html')
    data = {'companyId': companyId}
    remark = '查询公司的风险标签'
    return form_post(url=url, headers=header, data=data, remark=remark, rd='王豪')


def query_risk_labels():
    url = 'http://home.lagou.com/audit/companyApprove/queryRiskLabels.json'
    header = get_header(url='http://home.lagou.com/index.html')
    remark = '查询风险标签'
    return form_post(url=url, headers=header, remark=remark, rd='王豪')


def add_risk_labels_by_company(companyId, labelIds):
    url = 'http://home.lagou.com/audit/companyApprove/addRiskLabelsByCompany.json'
    header = get_header(url='http://home.lagou.com/index.html')
    data = {'companyId': companyId, 'labelIds': labelIds}
    remark = '给公司打风险标签'
    return form_post(url=url, headers=header, data=data, remark=remark, rd='王豪')
