from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
import base64
from datetime import datetime, timedelta
import os


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
        self.password = password
        self.phone = phone

    def __repr__(self):
        return '<User %r>' % self.username

    @staticmethod
    def from_dict(data):
        if 'username' in data and 'email' in data and 'phone' in data and 'password' in data:
            return User(
                username=data['username'],
                email=data['email'],
                phone=data['phone'],
                password=generate_password_hash(data['password'])
            )
        return None

    def check_password(self, password):
        return check_password_hash(self.password, password)

    # 定义返回字典中的键
    @staticmethod
    def keys():
        return ['id', 'username', 'email', 'phone']

    # 返回对象对应属性的值
    def __getitem__(self, item):
        return getattr(self, item)

    def get_token(self, expires_in=1200):
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
        return user
