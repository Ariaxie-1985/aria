## 安装环境(python version >= 3.6)
```shell

# 切换项目目录
cd lg_api_script

# 安装环境依赖库
pip install -r requirements.txt

```
## 执行脚本
```shell
# 执行全部测试脚本
#pytest
# 若执行部分脚本, 只需写多个文件文件名
#pytest api_script/tests/test_b_basic.py api_script/tests/test_*.py

# 每天早上6点至24点每10分钟执行一次主流程测试脚本，报错则发飞书报警并发送测试报告邮件
*/10 6-23 * * * /apps/oss/python36/bin/python3.6 /home/test/lg-apiscript-python/task/send_auto_test_report.py --module mainprocess 
# 每天凌晨0点至早上10点第0分钟执行一次自动化注销账号脚本
0 0-10 * * * /apps/oss/python36/bin/python3.6 /home/test/lg-apiscript-python/task/regular_batch_cancel_account.py
# 7*24小时每小时的第15，45分钟执行一次API开放平台测试脚本，报错则发飞书报警
15,45 * * * * /apps/oss/python36/bin/python3.6 /home/test/lg-apiscript-python/task/send_auto_test_report.py --module open_api_lagou

```

