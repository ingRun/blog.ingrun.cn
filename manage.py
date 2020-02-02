from flask_script import Manager
from app import blog
from flask_migrate import Migrate, MigrateCommand
from app import db

manager = Manager(blog)
# init  migrate upgrade
# 模型 -> 迁移文件 -> 表
# 1.要使用flask_migrate,必须绑定app和DB
migrate = Migrate(blog, db)

# 2.把migrateCommand命令添加到manager中。
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()


# 数据库迁移
# 首次运行 先初始化
# python .\manage.py db init

#  python .\manage.py db migrate
#  python .\manage.py db upgrade
