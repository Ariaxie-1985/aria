# coding:utf-8
# @Time  : 2019-03-20 17:58
# @Author: Xiawang
import os
from utils.operate_excel import update_excel
from utils.read_file import record_jsessionid, read_jsessionid
from utils.util import get_header, form_post, login_password


def import_linkManInfo(companyId, contractNo):
    referer_url = 'https://home.lagou.com/#/h_crm/plus/excelImport'
    url = 'http://home.lagou.com/crm/excelImportController/linkManInfo.json'
    header = get_header(url=referer_url)
    project_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    if 'JSESSIONID' in header['Cookie']:
        JSESSIONID = header['Cookie'].split('JSESSIONID')[1]
        record_jsessionid(file_path=project_path, jsessionid=JSESSIONID)
    else:
        header['Cookie'] = header['Cookie'] + ' JSESSIONID' + read_jsessionid(project_path) + ';' + ' login=true'
    project_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    file_Path = '{}/tests/testdata/import1.xls'.format(project_path)
    update_excel(file_Path, companyId, contractNo)
    files = {'file': open(file_Path, 'rb')}
    remark = 'home后台-拉勾加-数据导入-导入公司联系人信息, 其header:{}'.format(header['Cookie'])
    return form_post(url=url, files=files, headers=header, remark=remark, rd='李久超')


def import_contacts(companyId, contractNo):
    referer_url = 'https://home.lagou.com/#/h_crm/plus/excelImport'
    url = 'https://home.lagou.com/crm/excelImportController/contact.json'
    header = get_header(url=referer_url)
    project_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    if not 'JSESSIONID' in header['Cookie']:
        header['Cookie'] = header['Cookie'] + ' JSESSIONID' + read_jsessionid(project_path) + ';' + ' login=true'
    project_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    file_Path = '{}/tests/testdata/import2.xls'.format(project_path)
    update_excel(file_Path, companyId, contractNo)
    files = {'file': open(file_Path, 'rb')}

    remark = 'home后台-拉勾加-数据导入-导入合同信息'
    return form_post(url=url, files=files, headers=header, remark=remark, rd='李久超')


if __name__ == '__main__':
    login_password('autotest@lagou.com', 'a52f33ba89bd7af92982da737cafc8d0')
    r = import_linkManInfo(117448258, 'lg-auto-test-20191219-12')
    # import_contacts(117448258, 'lg-auto-test-20191219-11')
    print(type(r))
    print(r)
    # project_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    # os.chdir(project_path)
    # print(project_path)
    # record_jsessionid(project_path, 'hifewhkrhweakjrhaew84823423')
    # print(read_jsessionid(project_path))
