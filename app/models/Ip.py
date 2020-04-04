from datetime import datetime

from app import db


class Ip(db.Model):
 
    __tablename__ = 'ip'

    id = db.Column(db.Integer, primary_key=True)
    sum_ = db.Column(db.Integer, nullable=True, default=0)   # 访问总数
    last_seven_days = db.Column(db.String(80), default='0', nullable=True)  # 过去 7 天访问列表
    today_count = db.Column(db.Integer, nullable=True, default=0)   # 今天访问总数
    today_time = db.Column(db.Date, nullable=True, default=datetime.now())

    # 构造方法
    # def __init__(self, ast_seven_days):

    def __repr__(self):
        return '<IpInfo %r>' % self.sum_

    # 定义返回字典中的键
    @staticmethod
    def keys():
        return ['id', 'sum_', 'last_seven_days', 'today_count']

    # 返回对象对应属性的值
    def __getitem__(self, item):
        return getattr(self, item)
