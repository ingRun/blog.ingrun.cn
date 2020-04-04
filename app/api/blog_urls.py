from datetime import datetime

from flask import request, g

from app import db
from app.api import bp
from app.api.auth import token_auth
from app.utils.ip_count import AccessToday
from app.utils.myRedis import my_redis
from app.api.tools import success_response, err_response
from app.models.Blog import Blog

@bp.route('/addBlog', methods=['POST'])
@token_auth.login_required   # 用户登陆验证
def add_blog() -> str:
    if request.method == 'POST':
        data: dict = request.get_json()    # 获取前端传递的 JSON 字符串

        # 作者根据登陆信息来获取！
        author = g.current_user.id

        check_message = Blog.check_data(data)  # 检测通过返回空字符串  否则返回提示
        if check_message:
            return err_response(message=check_message, status_code=400)

        data['author'] = author
        new_blog = Blog(**data)
        db.session.add(new_blog)
        db.session.commit()
        return success_response(message='添加博客成功！', data=new_blog)


@bp.route('/getBlog/<int:id>', methods=['GET'])
def get_blog(id) -> str:
    blog1 = Blog.query.get_or_404(id)
    blog1.read_count += 1
    db.session.commit()
    blog1.blog_type = eval(blog1.blog_type)
    return success_response(data=blog1)

@bp.route('/getBlogContents/<int:id>', methods=['GET'])
def get_blog_contents(id):
    if request.method == 'GET':
        new_blog = Blog.query.get_or_404(id)
        return success_response(message='success', status_code=200, code=1, data=new_blog.contents)

@bp.route('/getBlogList', methods=['GET'])
def get_blog_list():
    # ip = request.remote_addr
    new_blog = list(Blog.query.filter_by(is_show=True))
    AccessToday.access_toady_add()
    return success_response(message='success', data=new_blog)

@bp.route('/getAllBlogList', methods=['GET'])
@token_auth.login_required   # 用户登陆验证
def get_all_blog_list():
    # new_blog = list(Blog.query.filter_by(is_show=True))
    new_blog = Blog.query.all()
    AccessToday.access_toady_add()
    return success_response(message='success', data=new_blog)

@bp.route('/updBlog', methods=['POST'])
@token_auth.login_required   # 用户登陆验证
def upd_blog():
    data: dict = request.get_json()

    if not ('id' in data):
        return err_response(message='非法请求！', status_code=400)
    check_message = Blog.check_data(data)
    if check_message:
        return err_response(message=check_message, status_code=400)

    blog = Blog.query.get_or_404(data['id'])
    if not g.current_user.id == blog.author:
        return err_response(message='你没有权限修改该博客', status_code=401)

    blog.contents = data['contents']
    blog.blog_title = data['blog_title']
    blog.blog_type = str(data['blog_type'])
    blog.preview = data['preview']
    blog.update_time = datetime.now()
    db.session.commit()
    return success_response(message='success', data=blog)

@bp.route('/delBlog/<int:id>', methods=['POST'])
@token_auth.login_required   # 用户登陆验证
def del_blog(id):
    blog = Blog.query.get_or_404(id)

    if blog.author == g.current_user.id:
        db.session.delete(blog)
        db.session.commit()
        return success_response(message='success')
    return err_response(message='权限不足', status_code=401)

@bp.route('/redisTest', methods=['GET'])
def redis_test():
    my_redis.set_redis_data('message', 'redis 已成功启动！')
    k = my_redis.get_redis_data('message')
    if k:
        return success_response(message=k)
    return err_response(message='redis 未运行！', status_code=500)

@bp.route('/blogSearch/<string:search_value>', methods=['GET'])
def blog_search(search_value):
    blog_li = Blog.query.filter(Blog.blog_title.ilike('%' + search_value + '%'))
    return success_response(data=list(blog_li))

@bp.route('/blog_random_type', methods=['GET'])
def blog_random_type():
    pass
