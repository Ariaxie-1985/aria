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
python app.py

# 启动服务方法2
在run.py右键点击 Run 'app'

# 访问接口文档
http://0.0.0.0:9000/docs/api/
```


## restful api规范

### 业务模块
- customer  C端
- jianzhao  简招
- zhaopin   招聘
- business  商业