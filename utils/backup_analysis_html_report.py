'''
{
	"state": 0,
	"content": "报告生成成功",
	"report_generated_time": datetime.date.today().isoformat() + re.findall(r'[0-9]{2}:[0-9]{2}:[0-9]{2}', t)[0],
	"summary_result": "71 passed, 4 skipped, 5 failed, 1 errors, 95 expected failures, 0 unexpected passes"
	"fail_result": {
		"test_function": {
			"error_type": "AssertionError",
			"log": "密码登录 报错500,  其调用链:http://oss.pard.inter.lagou.com/#/traDetail?traceId=30369.46138011.15907189279724995, 负责人:旭峰",
			"name": "旭峰"
		}
	}
}
'''
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
    for fail_result in soup.find_all(attrs={'class': 'failed results-table-row'}):
        test_case_name = get_case_name(fail_result)
        error_type = get_failed_error_type(fail_result)
        log = fail_result.find(attrs={'class': 'log'}).get_text()
        failed_info = get_failed_log(log)
        if error_type == 'AssertionError':
            expect_value, actual_value, success_message, fail_message = get_assert_info(log)
            failed_log = f'期望结果:{expect_value},实际结果:{actual_value},success_message:{success_message},失败结果:{fail_message}\n' \
                         f'详细日志:{failed_info}'
        elif 'Http500Error' in error_type:
            pass


def get_failed_log(log):
    captured_log = re.findall(r'Captured log call (.*)', log)[0]
    failed_log = re.findall(r'该接口URL:(.*)', captured_log)[0]
    return failed_log


def get_assert_info(log):
    expect_value = re.findall(r'expectvalue = (.+?)', log)[0]
    actual_value = re.findall(r'actualvalue = (.+?)', log)[0]
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


def get_error_results():
    pass


def get_fail_result(soup):
    failed_results = get_failed_results(soup)
    error_results = get_error_results()
    return {**failed_results, **error_results}


def analysis_html_report(report_path, module):
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
    soup = BeautifulSoup(
        open('/Users/wang/Desktop/lg-project/lg_api_script/backend/templates/mainprocess_report0529.html',
             encoding='utf-8'), "html.parser")
    get_failed_results(soup)
