## 安装环境(python version >= 3..6)
```shell

# 切换项目目录
cd lg_api_script

# 安装环境依赖库
pip install -r requirements.txt

```
## 执行脚本
```shell
# 执行全部测试脚本
pytest
# 若执行部分脚本, 只需写多个文件文件名
pytest api_script/tests/test_b_basic.py api_script/tests/test_*.py

```

