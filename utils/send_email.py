# coding:utf-8
# @Time  : 2019-01-27 21:02
# @Author: Xiawang
import logging
import os
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

from utils.analysis_html_report import get_summary, get_summary_result

sender = 'autotest@lagoujobs.com'
sender_password = 'Lqq123456'
receivers = ['xiawang@lagou.com', 'cloudyyuan@lagou.com', 'wanqiangliu@lagou.com', 'yqzhang@lagou.com']


def mail():
	ret = True
	try:
		message = MIMEMultipart()
		message['From'] = Header("质量保障中心", 'utf-8')
		message['To'] = Header("测试工程师", 'utf-8')
		subject = 'K8S default环境接口测试报告'
		message['Subject'] = Header(subject, 'utf-8')

		generated_report_time, summary_time = get_summary()
		passed, skipped, failed, errors, expected_failures, unexpected_passes = get_summary_result()

		# message.attach(
		# 	MIMEText('测试报告详见附件report.html, 大致如下:\n'
		# 	         '该报告生成时间:{} \n'
		# 	         '本次测试用例执行的总时间是:{} \n'
		# 	         '本次测试用例执行的总结果如下:\n'
		# 	         '测试用例通过数:{}\n'
		# 	         '跳过测试用例执行数:{}\n'
		# 	         '测试用例失败数:{}\n'
		# 	         '测试用例报错数:{}'
		# 	         '期望测试用例失败数:{}'
		# 	         '不希望测试用例通过数:{}', 'plain', 'utf-8').format(generated_report_time, summary_time, passed, skipped,
		# 	                                                   failed, errors, expected_failures, unexpected_passes)
		# )
		message.attach(
			MIMEText('测试报告详见附件report.html', 'plain', 'utf-8')
		)
		zipfile_path = '/Users/wang/Desktop/lg-project/lg_api_script/report/report.html'
		# zipfile_path = '/var/lib/jenkins/workspace/python_api/report/report.html'
		att1 = MIMEText(open(zipfile_path, 'rb').read(), 'base64', 'utf-8')
		att1["Content-Type"] = 'application/octet-stream'
		att1["Content-Disposition"] = 'attachment; filename="report.html"'
		message.attach(att1)

		server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
		server.login(sender, sender_password)
		server.sendmail(sender, receivers, message.as_string())
		server.quit()
	except Exception:
		ret = False
	return ret


ret = mail()
if ret:
	logging.info("邮件发送成功")
else:
	logging.info("邮件发送失败")
