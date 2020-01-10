import json

from flask import request, jsonify
from flask_login import login_required

from app import blog, db
from models.User import User


@blog.route('/api/login', methods=['POST'])
def login() -> str:
    if request.method == 'POST':
        data: dict = request.get_json()    # 获取前端传递的 JSON 字符串
        em = data['email']
        user = User.query.filter_by(email=em).first()
        return jsonify(user)


@blog.route('/api/register', methods=['POST'])
def register() -> str:
    if request.method == 'POST':
        data: dict = request.get_json()    # 获取前端传递的 JSON 字符串
        if data['password'] is not data['re_password']:
            return '两次输入的密码不一致！'

        user = User(username=data['username'], password=data['password'], email=data['email'], phone=data['phone'])
        db.Session.add(user)
        db.Session.commit()

        return jsonify(user)


