import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + basedir + '/db/blog.db'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

JSON_AS_ASCII = False    # 设置 json 返回的字符串支持中文

LOGIN_TOKEN_TIME = 60 * 20  # 登陆token 持续时间 20分钟
LOGIN_TOKEN_EXTENSION_TIME = LOGIN_TOKEN_TIME  # token 剩余5分钟自动延期后时间

# redis 配置
REDIS_DB_URL = {
    'host': '127.0.0.1',
    'port': 6379,
    'password': '',
    'db': 0
}
