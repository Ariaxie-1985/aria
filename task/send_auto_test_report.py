# coding:utf-8
# @Time  : 2020/4/21 19:18
# @Author: Xiawang
# Description:

import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time

'''
用于主流程监控定期执行并发送报警信息
'''


def run_pytest():
    url = 'http://127.0.0.1:18980/data/pytest'
    data = {"module": "mainprocess"}
    pytest_result = requests.post(url=url, json=data, verify=False).json()
    return pytest_result


def send_weixin_report(pytest_result):
    if pytest_result['state'] == 0:
        fail_result = ''
        fail_results = ''
        for key, value in pytest_result['data']['result']['info']['result']['fail_result'].items(
        ):
            fail_result = '用例{}报错:{},原因是{}\n\n'.format(
                key, value['error_type'], value['log'])
            fail_results += fail_result

        summary_result = '{},{},{},{},{},{}'.format(
            pytest_result['data']['result']['info']['result']['summary_result']['pass'],
            pytest_result['data']['result']['info']['result']['summary_result']['skip'],
            pytest_result['data']['result']['info']['result']['summary_result']['fail'],
            pytest_result['data']['result']['info']['result']['summary_result']['errors'],
            pytest_result['data']['result']['info']['result']['summary_result']['expect_failures'],
            pytest_result['data']['result']['info']['result']['summary_result']['unexpect_passes'])

        #  url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=b18ce9c0-3d98-411a-9f2a-bbce71c0f09e'
        url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=712278c2-2646-4bc6-aef2-4f26ace22d3f'
        data = {
            "msgtype": "text",
            "text": {
                "mentioned_list": ["xiawang"],
                "content": "主流程测试结果:\n{}\n\n具体失败结果:\n{}".format(
                    summary_result,
                    fail_results)}}
        if len(data['text']['content']) >= 2000:
            data['text']['content'] = data['text']['content'][:2000]

        return requests.post(url=url, json=data, verify=False).json()


def send_mail():
    sender = 'autotest@lagoujobs.com'
    sender_password = 'Lqq123456'
    receivers = ['xiawang@lagou.com', 'betty@lagou.com', 'yqzhang@lagou.com']
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
        report_file_path = '/home/test/lg-apiscript-python/backend/templates/mainprocess_report.html'
        # report_file_path = '/Users/wang/Desktop/lg-project/lg_api_script/backend/templates/mainprocess_report.html'
        att1 = MIMEText(open(report_file_path, 'rb').read(),
                        'base64', 'utf-8')
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


def get_number(string: str):
    number_str = string.split(' ')[0]
    if not number_str.isdigit():
        number_str = '0'
    number = int(number_str)
    return number


def send_oss(pytest_result):
    total_result = pytest_result['data']['result']['info']['result']
    errors = total_result['fail_result']
    name = "main_process_test"
    source = "main_process_test.py"
    for key, value in errors.items():
        test_demo: str = key.strip()
        error_type: str = value['error_type'].strip()
        error_cause: str = value['log'].strip()
        module_name = test_demo
        if error_cause == '具体详情,请查看测试报告':
            cause = error_type
            level = 'WARNING'
            user_ids = 'mornyue'
        else:
            cause = error_cause
            level = 'PROBLEM'
            user_ids = 'mornyue,huifang'
        description = "主流程测试"
        oss_filter_event(module_name=module_name, name=name, cause=cause,
                         level=level, user_ids=user_ids, description=description, source=source)


def oss_filter_event(module_name, name, description, level, user_ids: str, cause, source):
    """
    将消息发送到lg-alarm-filter模块的event接口，用来生成告警
    接口需要参数：["moduleName", "name", "description", "level", "userids", "cause"]
    :param module_name: 模块名抑或主机名
    :param name: 类型
    :param description: 告警描述
    :param level: 告警级别
    :param user_ids: 告警通知人，逗号分隔，且不能存在空格，后端解析没有对空格进行额外处理
    :param cause: 告警引起原因
    :param source: 数据来源
    :return:
    """
    # 防止userids传入有问题，加一层处理逻辑
    if ',' in user_ids:
        user_list = user_ids.split(',')
    elif '，' in user_ids:
        user_list = user_ids.split('，')
    else:
        user_list = [user_ids]
    user_ids = ','.join([item.strip() for item in user_list])
    url = 'http://10.10.5.138:8081/filter/event'
    params = {
        'moduleName': module_name,
        'name': name,
        'description': description,
        'level': level,
        'userids': user_ids,
        'cause': cause,
        'source': source
    }
    requests.post(url, json=params)


if __name__ == '__main__':
    pytest_result = run_pytest()
    if pytest_result['state'] == 0:
        time.sleep(10)
        pytest_result = run_pytest()
        if pytest_result.get('state', 0) == 0:
            send_weixin_result = send_weixin_report(pytest_result)
            send_oss_result = send_oss(pytest_result)
            if send_weixin_result['errcode'] == 0:
                send_mail()
            if not send_oss_result.get('result', False):
                send_oss(pytest_result)
