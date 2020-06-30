# coding:utf-8
# @Time  : 2019-01-16 10:41
# @Author: Xiawang
import re

from bs4 import BeautifulSoup


def get_summary(soup):
    '''
    :return:
    generated_report_time: str, 测试报告的生成时间
    summary_time: str, 测试用例执行的总时间
    '''
    p_list = []
    for p in soup.find_all('p'):
        p_list.append(p.get_text())

    generated_report_time = p_list[0]
    summary_time = p_list[1]
    return generated_report_time, summary_time


def get_summary_result(soup):
    '''
    :return:
    passed: 测试用例通过数
    skipped: 跳过测试用例执行数
    failed: 测试用例失败数
    errors: 测试用例报错数
    expected_failures: 期望测试用例失败数
    unexpected_passes: 不希望测试用例通过数
    '''
    span_list = []
    for s in soup.find_all('span'):
        span_list.append(s.get_text())

    passed, skipped, failed, errors, expected_failures, unexpected_passes = span_list[0], span_list[1], span_list[2], \
                                                                            span_list[3], span_list[4], span_list[5]
    return {"pass": passed, 'skip': skipped, 'fail': failed, 'errors': errors, 'expect_failures': expected_failures,
            'unexpect_passes': unexpected_passes}


def get_testresults_details(soup):
    '''
    :return:
    testresults: list, 包含测试用例的执行详情(测试用例的执行结果, 测试用例文件及对应方法名, 测试用例执行时间)
    '''
    testresults = []
    testcase = {}
    for r in soup.find_all(attrs={'class': 'col-result'}):
        testcase['result'] = r.get_text()
        for t in soup.find_all(attrs={'class': 'col-name'}):
            testcase['test'] = t.get_text()
            for d in soup.find_all(attrs={'class': 'col-duration'}):
                testcase['duration'] = d.get_text()
        testresults.append(testcase)
        testcase = {}
    return testresults


def get_fail_detail_result(soup, module):
    fail_results = {}
    for fail_result in soup.find_all(attrs={'class': 'failed results-table-row'}):
        test_name = fail_result.find(attrs={'class': 'col-name'}).get_text().split(
            'tests/test_{}/'.format(module.replace('-', '_')))[
            1].encode(
            'latin-1').decode('unicode_escape')
        try:
            error_type = fail_result.find(attrs={'class': 'error'}).get_text().split('E       ')[1]
        except IndexError:
            error_type = None
        captured_log = fail_result.find(attrs={'class': 'log'}).get_text()
        # print(captured_log)
        captured_demo_log = captured_log[captured_log.rfind('Captured log call'):]
        # print(captured_demo_log)
        try:
            rd_name = re.findall(r'开发([\u4E00-\u9FA5]{2,})同学', captured_demo_log)[0]
        except IndexError:
            rd_name = ''
        try:
            te_name = re.findall(r'测试([\u4E00-\u9FA5]{2,})同学', captured_demo_log)[0]
        except IndexError:
            te_name = ''
        try:
            detail_log = \
                re.findall(
                    r"------------------------------ Captured log call -------------------------------(.*)",
                    captured_log)[0]
            detail_log = '该接口URL' + re.findall('该接口URL(.*)', detail_log, re.S)[0]
        except IndexError:
            detail_log = '具体详情,请查看测试报告'

        test_case = {test_name: {'error_type': error_type, 'log': detail_log, 'rd_name': rd_name, 'te_name': te_name}}
        fail_results = {**fail_results, **test_case}

    for error_result in soup.find_all(attrs={'class': 'error results-table-row'}):
        test_name = error_result.find(attrs={'class': 'col-name'}).get_text().split('tests/test_mainprocess/')[
            1].encode('latin-1').decode('unicode_escape')
        # todo 解决AttributeError异常
        try:
            error_type = error_result.find(attrs={'class': 'error'}).get_text().split('E   ')[1]
            captured_log = error_result.find(attrs={'class': 'log'}).get_text()
        except AttributeError as e:
            print(e)
            pass

        try:
            detail_log = \
                re.findall(
                    r"------------------------------- Captured stderr --------------------------------ERROR:root:(.*)",
                    captured_log)[0][7:]

        except IndexError:
            detail_log = '程序异常,请查看测试报告'
        test_case = {test_name: {'error_type': error_type, 'log': detail_log}}
        fail_results = {**fail_results, **test_case}

    return fail_results


def analysis_html_report(report_path, type, module):
    soup = BeautifulSoup(open(report_path, encoding='utf-8'), "html.parser")
    result_time = None
    result = None
    detail_result = None
    if type == 1:
        result_time = get_summary(soup)
        result = get_summary_result(soup)
    elif type == 2:
        result_time = get_summary(soup)
        result = get_summary_result(soup)
        detail_result = get_testresults_details(soup)
    elif type == 3:
        result_time = get_summary(soup)
        result = get_summary_result(soup)
        fail_detail = get_fail_detail_result(soup, module)
    return {"content": "报告生成成功", "info": {"time": result_time,
                                          "result": {'summary_result': result, 'detail_result': detail_result,
                                                     'fail_result': fail_detail}}}


if __name__ == '__main__':
    # r = analysis_html_report(
    #     '/Users/wang/Desktop/lg-project/lg_api_script/backend/templates/mainprocess_report33.html',
    #     3)
    r = analysis_html_report('/Users/wang/Downloads/kaiwu_lagou/report2.html', 3, 'mainprocess')
    print(r)
