# coding:utf-8
# @Time  : 2019-01-16 10:41
# @Author: Xiawang
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("../report/report.html", encoding='utf-8'), "html.parser")


def get_summary():
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


def get_summary_result():
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
	return passed, skipped, failed, errors, expected_failures, unexpected_passes


def get_testresults_details():
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
