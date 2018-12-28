### 

```shell
# 切换项目目录
cd lg_api_script
# 未安装pipenv, 先用python3(版本最好是3.6)安装pipenv, 已安装的跳过这一步即可
pip3 install pipenv
# 安装依赖环境
pipenv install Pipfile
# 激活虚拟环境
pipenv shell
# 执行全部测试脚本
pytest
# 若执行部分脚本
pytest api_script/tests/test_b_basic.py api_script/tests/test_*.py
```

