from flask import Flask
from flask.json import JSONEncoder as _JSONEncoder


from flask_sqlalchemy import SQLAlchemy

blog = Flask(__name__)
blog.config.from_object('config')
db = SQLAlchemy(blog)

from app import urls


# 自定义json 序列化器
class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        raise super(self, o)


# 使用自己定义的方法
blog.json_encoder = JSONEncoder
