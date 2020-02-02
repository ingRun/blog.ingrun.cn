from flask import request, jsonify, g
from app import blog, db
from app.api import bp
from app.api.auth import token_auth
from app.api.tools import err_response, success_response
from app.models.User import User


@bp.route('/login', methods=['POST'])
def login() -> str:
    data: dict = request.get_json() or {}    # 获取前端传递的 JSON 字符串
    if 'username' in data and 'password' in data:
        user = User.query.filter_by(username=data['username']).first()
        if user.check_password(data['password']):
            token = user.get_token()
            db.session.commit()
            return success_response(message='登陆成功！', data={'token': token})
        return err_response(message='用户名或密码错误！', status_code=500)
    return err_response(message='数据提交失败！', status_code=400)

@bp.route('/logout', methods=['POST'])
@token_auth.login_required
def logout() -> str:
    g.current_user.revoke_token()
    db.session.commit()
    return success_response(message='注销成功')

@bp.route('/api/register', methods=['POST'])
def register() -> str:
    data: dict = request.get_json() or {}   # 获取前端传递的 JSON 字符串
    if not data['password'] == data['re_password']:
        return '两次输入的密码不一致！'

    old_user = User.query.filter_by(username=data['username']).first()
    if old_user:
        return err_response('用户名已存在')

    user = User.from_dict(data)
    if user:
        db.session.add(user)
        db.session.commit()
        return success_response(message='', code=1, status_code=200, data=user)
    return err_response('传入的用户字段不足或不正确')


@bp.route('/api/getUser/<int:user_id>', methods=['GET', 'POST'])
def get_user(user_id):
    if request.method == 'GET':
        user = User.query.get_or_404(user_id)
        return jsonify(user)
    return ''

@bp.route('/getUserInfo', methods=['GET'])
@token_auth.login_required
def get_user_info():
    return success_response(data=g.current_user)
