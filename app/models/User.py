from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
import base64
from datetime import datetime, timedelta
import os
import re
from config import LOGIN_TOKEN_TIME, LOGIN_TOKEN_EXTENSION_TIME

class User(db.Model, UserMixin):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    password = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    phone = db.Column(db.String(11))
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)

    # 构造方法
    def __init__(self, username, password, email, phone):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.phone = phone

    def __repr__(self):
        return '<User %r>' % self.username

    # 检查用户字典是否规范！  规范传出空字符串  否 传出 提示信息！
    @staticmethod
    def check_register_data(data):
        if not ('username' in data and 'email' in data
                and 'phone' in data and 'password' in data
                and 're_password' in data):
            return '传入用户字段不足或不正确！'
        if not data['password'] == data['re_password']:
            return '两次输入的密码不同！'
        if len(data['password']) < 6:
            return '密码太短！'
        if not len(data['phone']) == 11 and data['phone'].isdigit():
            return '手机号不正确: ' + data['phone']
        if not re.match(r'[0-9a-zA-Z]{4,16}@[0-9a-zA-Z]{2,5}.[com|net]', data['email']):
            return '邮箱格式不合法:' + data['email']
        if not re.match(r'[0-9a-zA-Z_]{4,16}', data['username']):
            return '用户名格式不合法:' + data['email']
        if not User.query.filter_by(username=data['username']).count() == 0:
            return '用户名已存在:' + data['username']
        if not User.query.filter_by(phone=data['phone']).count() == 0:
            return '该手机号已被注册:' + data['phone']
        if not User.query.filter_by(email=data['email']).count() == 0:
            return '该邮箱已被注册:' + data['email']
        return ''

    def check_password(self, password):
        return check_password_hash(self.password, password)

    # 定义返回字典中的键
    @staticmethod
    def keys():
        return ['id', 'username', 'email', 'phone']

    # 返回对象对应属性的值
    def __getitem__(self, item):
        return getattr(self, item)

    def get_token(self, expires_in=LOGIN_TOKEN_TIME):
        now = datetime.utcnow()

        # 如果token 时间剩余大于60秒  直接返回现有token
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token

        # 随机生成token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        if user.token_expiration < datetime.utcnow() + timedelta(minutes=5):
            user.token_expiration = datetime.utcnow() + timedelta(minutes=LOGIN_TOKEN_EXTENSION_TIME)
            db.session.commit()
        return user
