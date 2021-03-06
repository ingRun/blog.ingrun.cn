import os
from datetime import datetime, date

from flask import Flask
from flask.json import JSONEncoder as _JSONEncoder
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

blog = Flask(__name__)
blog.config.from_object('config')
db = SQLAlchemy(blog)

blog.secret_key = os.urandom(24)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'un_login'
login_manager.login_message = u"用户未登录，请先登录。"
login_manager.init_app(blog)

from app.models.User import User
from app.models.Blog import Blog
from app.models.Ip import Ip

# 自定义json 序列化器
class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise super(self, o)


# 使用自己定义的 json 序列化器
blog.json_encoder = JSONEncoder

from app.api import bp as api_bp
from app.urls import user_url

blog.register_blueprint(api_bp, url_prefix='/api')
