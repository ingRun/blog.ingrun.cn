from flask import request, jsonify, g
from app import blog, db
from app.api import bp
from app.api.auth import token_auth
from app.api.tools import err_response, success_response
from app.models.User import User

# 登陆
@bp.route('/login', methods=['POST'])
def login() -> str:
    data: dict = request.get_json() or {}    # 获取前端传递的 JSON 字符串
    if 'username' in data and 'password' in data:
        user = User.query.filter_by(username=data['username']).first()
        if user.check_password(data['password']):
            token = user.get_token()
            db.session.commit()
            return success_response(message='登陆成功！', data={'token': token})
        return err_response(message='用户名或密码错误！', status_code=401)
    return err_response(message='数据提交失败！', status_code=400)

# 注销
@bp.route('/logout', methods=['POST'])
@token_auth.login_required
def logout() -> str:
    g.current_user.revoke_token()
    db.session.commit()
    return success_response(message='注销成功')

# 注册
@bp.route('/register', methods=['POST'])
def register() -> str:
    data: dict = request.get_json() or {}   # 获取前端传递的 JSON 字符串

    # 检测用户提交数据是否符合规范！
    register_message = User.check_register_data(data)
    if not register_message:

        # 删除多余的字段
        del(data['re_password'])
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return success_response(message='注册用户成功！', code=1, status_code=200, data=user)
    return err_response(register_message, status_code=400)

# 获取用户信息
@bp.route('/getUserInfo', methods=['GET'])
@token_auth.login_required
def get_user_info():
    return success_response(data=g.current_user)

# 获取用户名
@bp.route('/getUserName/<int:id>', methods=['GET'])
def get_username(id):
    user = User.query.get_or_404(id)
    return success_response(data=user.username)

# 修改用户密码
@bp.route('/updPassword', methods=['POST'])
@token_auth.login_required
def upd_password():
    data: dict = request.get_json() or {}
    if 'old_password' not in data and 'new_password' not in data and 're_password' not in data:
        return err_response(message='数据提交不正确！', status_code=401)
    old_password = data['old_password']
    new_password = data['new_password']
    re_password = data['re_password']
    if not new_password == re_password:
        return err_response(message='两次输入的密码不一致', status_code=401)
    user = g.current_user
    if not user.check_password(password=old_password):
        return err_response(message='原密码错误！', status_code=403)
    if old_password == new_password:
        return err_response(message='修改后的密码不能与原密码相同！', status_code=401)
    if len(data['new_password']) < 6:
        return err_response(message='密码太短！', status_code=401)
    user.set_password(password=new_password)
    db.session.commit()
    return success_response(message='修改密码成功,请重新登陆')
