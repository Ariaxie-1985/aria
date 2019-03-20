# coding:utf-8
# @Time  : 2019-03-20 17:58
# @Author: Xiawang
import os

from utils.operate_excel import update_excel
from utils.util import get_header, form_post


def import_linkManInfo(companyId, contractNo):
    referer_url = 'https://home.lagou.com/#/h_crm/plus/excelImport'
    url = 'https://home.lagou.com/crm/excelImportController/linkManInfo.json'
    header = get_header(referer_url)

    project_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    file_Path = '{}/tests/testdata/import1.xls'.format(project_path)
    update_excel(file_Path, companyId, contractNo)
    files = {'file': open(file_Path, 'rb')}

    remark = 'home后台-拉勾加-数据导入-导入公司联系人信息'
    return form_post(url=url, files=files, headers=header, remark=remark)


def import_contacts(companyId, contractNo):
    referer_url = 'https://home.lagou.com/#/h_crm/plus/excelImport'
    url = 'https://home.lagou.com/crm/excelImportController/contact.json'
    header = get_header(referer_url)

    project_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    file_Path = '{}/tests/testdata/import2.xls'.format(project_path)
    update_excel(file_Path, companyId, contractNo)
    files = {'file': open(file_Path, 'rb')}

    remark = 'home后台-拉勾加-数据导入-导入合同信息'
    return form_post(url=url, files=files, headers=header, remark=remark)



