# coding:utf-8
# @Time  : 2020/4/21 19:18
# @Author: Xiawang
# Description:
import datetime

import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time

'''
用于主流程监控定期执行并发送报警信息
'''


def get_fix_time():
    now_time = datetime.datetime.now()
    if 0 <= now_time.hour <= 8:
        fix_time = now_time.date().strftime("%Y-%m-%d 12:00")
    elif 21 <= now_time.hour <= 24:
        fix_time = (now_time + datetime.timedelta(days=1)).date().strftime("%Y-%m-%d 12:00")
    else:
        fix_time = (now_time + datetime.timedelta(hours=3)).strftime("%Y-%m-%d %H:%M")
    return fix_time


def run_pytest():
    url = 'http://127.0.0.1:18980/data/pytest'
    data = {"module": "mainprocess"}
    pytest_result = requests.post(url=url, json=data, verify=False).json()
    return pytest_result


def send_feishu_report(pytest_result):
    if pytest_result.get('state') == 4:
        content = pytest_result.get('data')
        return send_feishu_bot(content=content)

    if pytest_result.get('state') == 0:
        summary_result = ''
        for k, v in pytest_result['data']['result']['info']['result']['summary_result'].items():
            summary_result += v + ', '

        fail_results = ''

        names = ''
        for key, value in pytest_result['data']['result']['info']['result']['fail_result'].items(
        ):
            if key == 'name':
                names += value['name'] + ','
                fail_result = '用例{}报错:{},原因:{},负责人:{}\n\n'.format(
                    key, value['error_type'], value['log'], value['name'])
            else:
                fail_result = '用例{}报错:{},原因是{}\n\n'.format(
                    key, value['error_type'], value['log'])
            fail_results += fail_result
        if bool(names):
            fix_time = get_fix_time()
            name_template = f'请开发同学{names}在{fix_time}之前，尽快处理并给出反馈'
        else:
            name_template = ''
        content = "{}\n\n具体失败结果:\n{}\n请大家对线上问题保持敬畏之心！\n{}".format(summary_result, fail_results, name_template)
        return send_feishu_bot(content=content)


def send_mail():
    sender = 'autotest@lagoujobs.com'
    sender_password = 'Lqq123456'
    receivers = ['xiawang@lagou.com', 'betty@lagou.com']
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


def send_feishu_bot(content):
    url = 'https://open.feishu.cn/open-apis/bot/hook/03654ef57c4f4418ba8802cfa1cf06a0'
    data = {
        "title": "主流程测试结果:",
        "text": content
    }
    if len(data['text']) >= 2000:
        data['text'] = data['text'][:2000]

    result = requests.post(url=url, json=data, verify=False).json()

    return result.get('ok')


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
        return oss_filter_event(module_name=module_name, name=name, cause=cause,
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


def main():
    pytest_result = run_pytest()
    if pytest_result.get('state', 0) != 1:
        time.sleep(10)
        pytest_result = run_pytest()
        if pytest_result.get('state', 0) != 1:
            send_feishu_result = send_feishu_report(pytest_result)
            send_oss_result = send_oss(pytest_result)
            if send_feishu_result == True:
                send_mail()
            if not send_oss_result.get('result', False):
                send_oss(pytest_result)


if __name__ == '__main__':
    main()
