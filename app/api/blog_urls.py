from datetime import datetime

from flask import request, jsonify

from app import db
from app.api import bp
from app.api.myRedis import set_redis_data, get_redis_data
from app.api.tools import success_response, err_response
from app.models.Blog import Blog

@bp.route('/addBlog', methods=['POST'])
def add_blog() -> str:
    if request.method == 'POST':
        data: dict = request.get_json()    # 获取前端传递的 JSON 字符串
        # 作者根据登陆信息来获取！
        author = 1
        new_blog = Blog(blog_title=data['blog_title'], author=author,
                        contents=data['contents'], blog_type=data['blog_type'])

        db.session.add(new_blog)
        db.session.commit()

        return success_response(message='添加博客成功！', data=new_blog)


@bp.route('/getBlog/<int:id>', methods=['GET'])
def get_blog(id) -> str:
    blog1 = Blog.query.get_or_404(id)
    return success_response(data=blog1)

@bp.route('/getBlogContents/<int:id>', methods=['GET'])
def get_blog_contents(id):
    if request.method == 'GET':
        new_blog = Blog.query.get_or_404(id)
        return success_response(message='success', status_code=200, code=1, data=new_blog.contents)

@bp.route('/getBlogList', methods=['GET'])
def get_blog_list():
    new_blog = Blog.query.all()
    return success_response(message='success', data=new_blog)

@bp.route('/updBlog', methods=['POST'])
def upd_blog():
    data: dict = request.get_json()
    blog = Blog.query.get_or_404(data['id'])
    if 'contents' in data:
        blog.contents = data['contents']
    if 'blog_title' in data:
        blog.blog_title = data['blog_title']
    if 'blog_type' in data:
        blog.blog_type = data['blog_type']
    blog.update_time = datetime.now()
    db.session.commit()
    return success_response(message='success', data=blog)

@bp.route('/delBlog/<int:id>', methods=['POST'])
def del_blog(id):
    blog = Blog.query.get_or_404(id)

    db.session.delete(blog)
    db.session.commit()
    return success_response(message='success')

    # if blog.id == g.current_user.id:
    #     db.session.delete(blog)
    #     db.session.commit()
    #     return success_response(message='success')
    # return err_response(message='权限不足', status_code=401)

@bp.route('/redisTest', methods=['GET'])
def redis_test():
    set_redis_data('admin', '123456')
    k = str(get_redis_data('admin'), 'utf-8')
    return success_response(message=k)
