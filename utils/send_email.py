# coding:utf-8
# @Time  : 2019-01-27 21:02
# @Author: Xiawang
import logging
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

from utils.util import zip_path

sys.path.append('..')

sender = 'autotest@lagoujobs.com'
sender_password = 'Lqq123456'
receivers = ['xiawang@lagou.com']


def mail():
	ret = True
	try:
		message = MIMEMultipart()
		message['From'] = Header("质量保障中心", 'utf-8')
		message['To'] = Header("测试工程师", 'utf-8')
		subject = 'K8S default环境接口测试报告'
		message['Subject'] = Header(subject, 'utf-8')

		message.attach(MIMEText('测试报告详见附件,解压后打开report.html即可', 'plain', 'utf-8'))

		zipfile_path = zip_path(r"../report", '..', 'report.zip')
		att1 = MIMEText(open(zipfile_path, 'rb').read(), 'base64', 'utf-8')
		att1["Content-Type"] = 'application/octet-stream'
		att1["Content-Disposition"] = 'attachment; filename="report.zip"'
		message.attach(att1)

		server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
		server.login(sender, sender_password)
		server.sendmail(sender, [receivers, ], message.as_string())
		server.quit()
	except Exception:
		ret = False
	return ret


ret = mail()
if ret:
	logging.info("邮件发送成功")
else:
	logging.info("邮件发送失败")
