from flask import request, jsonify

from app import blog
from models.User import User


@blog.route('/')
def hello_world():
    return 'Hello World!'


@blog.route('/api/getUser', methods=['GET', 'POST'])
def get_user():
    if request.method == 'GET':
        username: str = request.values.get('username')
        user = User.query.filter_by(username=username).first()
        return jsonify(user)

