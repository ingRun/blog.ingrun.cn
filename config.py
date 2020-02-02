import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + basedir + '/db/blog.db'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

JSON_AS_ASCII = False    # json 返回的字符串支持中文

REDIS_DB_URL = {
    'host': '127.0.0.1',
    'port': 6379,
    'password': '',
    'db': 0
}
