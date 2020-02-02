from flask import request, jsonify

from app import blog, db
from app.models.User import User

#
# @blog.route('/api/login', methods=['POST'])
# def login() -> str:
#     if request.method == 'POST':
#         data: dict = request.get_json()    # 获取前端传递的 JSON 字符串
#         em = data['email']
#         user = User.query.filter_by(email=em).first()
#         return jsonify(user)
#
#
# @blog.route('/api/register', methods=['POST'])
# def register() -> str:
#     if request.method == 'POST':
#         data: dict = request.get_json() or {}   # 获取前端传递的 JSON 字符串
#         if not data['password'] == data['re_password']:
#             return '两次输入的密码不一致！'
#
#         old_user = User.query.filter_by(username=data['username']).first()
#         if old_user:
#             return jsonify({'message': '用户名已存在！'})
#
#         user = User.from_dict(data)
#         if user:
#             db.session.add(user)
#             db.session.commit()
#             return jsonify(user)
#         return jsonify({'message': '传入的用户字段不足或不正确'})
#
#
# @blog.route('/api/getUser/<int:user_id>', methods=['GET', 'POST'])
# def get_user(user_id):
#     if request.method == 'GET':
#         user = User.query.get_or_404(user_id)
#         return jsonify(user)
#
