# coding:utf-8
# @Time  : 2019-01-08 19:00
# @Author: Xiawang

# 命令处理
from flask_script import Manager
from flask_migrate import  Migrate, MigrateCommand

from backend import app
from backend.exts import db

manager = Manager(app)

# 使用Migrate绑定app和db
migrate = Migrate(app, db)

# 添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
	manager.run()
