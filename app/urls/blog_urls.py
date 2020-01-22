import json

from flask import request, jsonify

from app import blog, db
from models.Blog import Blog


@blog.route('/api/addBlog', methods=['POST'])
def add_blog() -> str:
    if request.method == 'POST':
        data: dict = request.get_json()    # 获取前端传递的 JSON 字符串
        new_blog = Blog(blog_title=data['blog_title'], author=data['author'],
                        contents=data['contents'], blog_type=data['blog_type'])

        db.session.add(new_blog)
        db.session.commit()

        return jsonify(new_blog)


@blog.route('/api/getBlog', methods=['POST'])
def get_blog() -> str:
    if request.method == 'POST':
        data: dict = request.get_json()    # 获取前端传递的 JSON 字符串
        new_blog = Blog.query.filter_by(id=data['id']).first()

        return jsonify(new_blog)


@blog.route('/api/getBlogContents', methods=['GET'])
def get_blog_contents() -> str:
    if request.method == 'GET':
        blog_id = request.values.get('id')

        new_blog = Blog.query.filter_by(id=blog_id).first()

        return jsonify(new_blog.contents)


@blog.route('/api/getBlogList', methods=['GET'])
def get_blog_list() -> str:
    if request.method == 'GET':
        new_blog = Blog.query.all()

        return jsonify(new_blog)


