## 安装依赖
```shell

# 在项目目录下激活虚拟环境, pycharm选择好虚拟环境的解释器后自动激活
pipenv shell

# 安装依赖方法1
pipenv install Pipfile 

# 安装依赖方法2
pip install -r requirements.txt


# 启动服务方法1
cd backend
python run.py

# 启动服务方法2
在run.py右键点击 Run 'run'

# 访问接口文档
http://0.0.0.0:9000/docs/api/
```