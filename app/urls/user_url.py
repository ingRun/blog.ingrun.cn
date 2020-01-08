import json

from flask import request, jsonify
from flask_login import login_required

from app import blog
from models.User import User


@blog.route('/api/login', methods=['POST'])
def login() -> str:
    if request.method == 'POST':
        data: dict = request.get_json()
        em = data['email']
        user = User.query.filter_by(email=em).first()
        return jsonify(user)


