from flask import request, jsonify
from flask_login import login_required

from app import blog, login_manager
from models.User import User


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@blog.route('/')
def hello_world():
    return 'Hello World!'


@blog.route('/un_login')
def un_login():
    return '当前用户未登陆！'


@blog.route('/api/getUser', methods=['GET', 'POST'])
@login_required   # 权限认证必须写在 url 下面
def get_user_by_username():
    if request.method == 'GET':
        username: str = request.values.get('username')
        user = User.query.filter_by(username=username).first()
        return jsonify(user)

