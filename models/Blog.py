from datetime import datetime

from flask_login import UserMixin

from app import db


class Blog(db.Model, UserMixin):

    __tablename__ = 'blog'

    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(100), unique=True, nullable=True, index=True)  # 标题

    # 顺序不能写反， 先指定类型，再是外键 'grade.g_id'必须要小写   作者
    author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True, unique=True)
    create_time = db.Column(db.DateTime, default=datetime.now())  # 创建时间
    update_time = db.Column(db.DateTime, default=datetime.now())  # 最后修改时间
    contents = db.Column(db.Text, nullable=True)     # 内容
    read_count = db.Column(db.Integer, nullable=True, default=1)   # 阅读数
    like_count = db.Column(db.Integer, nullable=True, default=0)   # 点赞数
    blog_type = db.Column(db.String(50), nullable=True, default='other')   # 所属分类

    # 构造方法
    def __init__(self, blog_title, author, contents, blog_type):
        self.blog_title = blog_title
        self.author = author
        self.author = author
        self.contents = contents
        self.blog_type = blog_type

    # toString
    def __repr__(self):
        return '<Blog %r>' % self.username

    # 返回对象对应属性的值
    def __getitem__(self, item):
        return getattr(self, item)

    # 定义返回字典中的键
    @staticmethod
    def keys():
        return ['id', 'blog_title', 'author', 'create_time', 'update_time',
                'read_count', 'like_count', 'blog_type']

