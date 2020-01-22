from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(db.Model, UserMixin):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    password = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    phone = db.Column(db.String(11))

    # 构造方法
    def __init__(self, username, password, email, phone):
        self.username = username
        self.email = email
        self.password = password
        self.phone = phone

    # toString
    def __repr__(self):
        return '<User %r>' % self.username

    # 返回对象对应属性的值
    def __getitem__(self, item):
        return getattr(self, item)

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

    # 定义返回字典中的键
    @staticmethod
    def keys():
        return ['id', 'username', 'email', 'phone']

