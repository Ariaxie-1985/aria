# coding:utf-8
# @Time  : 2020/5/13 16:01
# @Author: Xiawang
# Description:
from utils.util import form_post, login_home, get_header


def query_risk_labels():
    url = 'http://home.lagou.com/audit/companyApprove/queryRiskLabels.json'
    header = get_header(url='http://home.lagou.com/index.html')
    remark = '查看风险标签'
    return form_post(url=url, headers=header, remark=remark, rd='王豪')


def add_risk_labels_by_company(companyId, labelIds):
    url = 'http://home.lagou.com/audit/companyApprove/addRiskLabelsByCompany.json'
    header = get_header(url='http://home.lagou.com/index.html')
    data = {
        'companyId': companyId,
        'labelIds': labelIds,
    }
    remark = '贴风险标签'
    return form_post(url=url, headers=header, data=data, remark=remark, rd='王豪')


def queryRiskLabelsByCompany(companyId):
    url = 'http://home.lagou.com/audit/companyApprove/queryRiskLabelsByCompany.json'
    header = get_header(url='http://home.lagou.com/index.html')
    data = {
        'companyId': companyId,
    }
    remark = '查询公司的风险标签'
    return form_post(url=url, headers=header, data=data, remark=remark, rd='王豪')


if __name__ == '__main__':
    login_home('betty@lagou.com', '00f453dfec0f2806db5cfabe3ea94a35')
    # r = query_risk_labels()
    # for risk_labels in r['data']:
    #     if risk_labels['type'] == 'A':
    #         risk_label_id = risk_labels['id']
    #         break
    r = queryRiskLabelsByCompany(companyId=119021450)
    print(r)
