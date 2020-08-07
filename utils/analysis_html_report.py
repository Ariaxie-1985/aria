import datetime
import re
from bs4 import BeautifulSoup


def get_report_generated_time(soup):
    report_generated_text = soup.p.get_text()
    minutes_seconds = re.findall(r'[0-9]{2}:[0-9]{2}:[0-9]{2}', report_generated_text)[0]
    return datetime.date.today().isoformat() + ' ' + minutes_seconds


def get_summary_result(soup):
    summary_result = ''
    for r in soup.find_all('span'):
        if r.get_text()[0].isdigit() and int(r.get_text()[0]) > 0:
            summary_result += r.get_text() + ','
    return summary_result


def get_failed_results(soup):
    failed_results = {}
    for fail_result in soup.find_all(attrs={'class': 'failed results-table-row'}):

        test_case_name = get_case_name(fail_result)
        error_type = get_failed_error_type(fail_result)
        log = fail_result.find(attrs={'class': 'log'}).get_text()
        if 'Captured log call' not in log:
            continue
        failed_info = get_failed_log(log)
        rd_name, te_name = get_rd_or_te_name(log)
        if '报错500' in failed_info:
            error_type = 'Http500Error'
            failed_log = failed_info

        elif error_type == 'AssertionError':
            expect_value, actual_value, success_message, fail_message = get_assert_info(log)
            failed_log = f'期望结果:{expect_value},实际结果:{actual_value},成功结果:{success_message},失败结果:{fail_message}\n' \
                         f'详细日志:{failed_info}'
        else:
            error_type = error_type
            failed_log = failed_info

        failed_result = {test_case_name: {
            'error_type': error_type,
            'log': failed_log,
            'rd_name': rd_name,
            'tester_name': te_name
        }}
        failed_results = {**failed_results, **failed_result}
    return failed_results


def get_failed_log(log):
    if '该接口URL:http' not in log:
        return '具体看测试报告'
    # failed_log = log[log.index('该接口URL:http'):]
    # print(failed_log)
    # captured_log = re.findall(r'Captured log call(.*)', log)[0]
    # print(captured_log)
    failed_log = re.findall(r'该接口URL:(.*)<分隔', log)[0]
    return failed_log


def get_rd_or_te_name(captured_log):
    try:
        rd_name_list = re.findall(r'开发(.*?)同学', captured_log)
        rd_name = [rd for rd in rd_name_list if rd != 'None'][0]
    except IndexError:
        rd_name = ''
    try:
        te_name = re.findall(r'测试(.*?)同学', captured_log)
        if te_name == []:
            te_name = ''
        else:
            for i in te_name:
                if len(i) <= 10 and i != []:
                    te_name = i
                    break
    except IndexError:
        te_name = ''
    return rd_name, te_name


def get_assert_info(log):
    expect_value = re.findall(r'expect_value = (.+?)', log)[0]
    actual_value = re.findall(r'actual_value = (.+?)', log)[0]
    success_message = re.findall(r"success_message = '(.+?)'", log)[0]
    fail_message = (re.findall(r"fail_message = '(.+?)'", log) or ['暂无'])[0]
    return expect_value, actual_value, success_message, fail_message


def get_failed_error_type(fail_result):
    error_type = fail_result.find(attrs={'class': 'error'}).get_text().split('E       ')[1]
    return error_type


def get_case_name(fail_result):
    test_case_name = fail_result.find(attrs={'class': 'col-name'}).get_text()
    if test_case_name.rfind('['):
        test_case_name = test_case_name.split('[')[0]
    test_case_name = test_case_name.split('::')[-1]
    return test_case_name


def get_error_results(soup):
    error_results = {}
    for error_result in soup.find_all(attrs={'class': 'error results-table-row'}):
        test_case_name = get_case_name(error_result)
        error_type = get_failed_error_type(error_result)
        # print(error_type)
        log = error_result.find(attrs={'class': 'log'}).get_text()
        if 'Captured log' not in log:
            continue
        failed_info = get_failed_log(log)
        rd_name, te_name = get_rd_or_te_name(log)
        if '报错500' in failed_info:
            error_type = 'Http500Error'
            error_log = failed_info

        elif error_type == 'AssertionError':
            expect_value, actual_value, success_message, fail_message = get_assert_info(log)
            error_log = f'期望结果:{expect_value},实际结果:{actual_value},成功结果:{success_message},失败结果:{fail_message}\n' \
                        f'详细日志:{failed_info}'
        else:
            error_type = error_type
            error_log = failed_info

        error_result = {test_case_name: {
            'error_type': error_type,
            'log': error_log,
            'rd_name': rd_name,
            'tester_name': te_name
        }}
        error_results = {**error_results, **error_result}
    return error_results


def get_fail_result(soup):
    failed_results = get_failed_results(soup)
    error_results = get_error_results(soup)
    return {**failed_results, **error_results}


def analysis_html_report(report_path):
    soup = BeautifulSoup(open(report_path, encoding='utf-8'), "html.parser")
    report_generated_time = get_report_generated_time(soup)
    summary_result = get_summary_result(soup)
    fail_detail = get_fail_result(soup)

    parse_report_result = {
        "content": "报告生成成功",
        "report_generated_time": report_generated_time,
        "summary_result": summary_result,
        "fail_result": fail_detail
    }

    return parse_report_result


if __name__ == '__main__':
    # soup = BeautifulSoup(
    #     open('/Users/wang/Desktop/lg-project/lg_api_script/report0806.html',
    #          encoding='utf-8'), "html.parser")
    # r = get_fail_result(soup)
    # r = analysis_html_report('/Users/wang/Desktop/lg-project/lg_api_script/backend/templates/mainprocess_report0529.html')
    # r = analysis_html_report('/Users/wang/Downloads/kaiwu_lagou/open_api_lagou_report.html')
    # r = analysis_html_report('/Users/wang/Desktop/lg-project/lg_api_script/report0807.html')
    # r = analysis_html_report('/Users/wang/Desktop/lg-project/lg_api_script/backend/templates/report0806.html')
    r = analysis_html_report('/Users/wang/Downloads/kaiwu_lagou/report.html')
    print(r)
