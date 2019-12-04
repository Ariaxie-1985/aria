# coding:utf-8
# @Time  : 2019-01-27 21:02
# @Author: Xiawang
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = 'autotest@lagoujobs.com'
sender_password = 'Lqq123456'
receivers = ['xiawang@lagou.com']


def mail():
    ret = True
    try:
        message = MIMEMultipart()
        message['From'] = Header("主流程测试报告", 'utf-8')
        message['To'] = Header("测试工程师", 'utf-8')
        subject = '主流程测试报告'
        message['Subject'] = Header(subject, 'utf-8')

        message.attach(
            MIMEText('主流程测试报告详见附件', 'plain', 'utf-8')
        )
        # /home/test/lg-apiscript-python/backend/templates/mainprocess_report.html
        report_file_path = '/Users/wang/Desktop/lg-project/lg_api_script/backend/templates/mainprocess_report.html'
        att1 = MIMEText(open(report_file_path, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="mainprocess_report.html"'
        message.attach(att1)

        server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        server.login(sender, sender_password)
        server.sendmail(sender, receivers, message.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret


if __name__ == '__main__':
    ret = mail()
