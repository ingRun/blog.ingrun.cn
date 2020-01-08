import json

from flask import request, jsonify
from flask_login import login_required

from app import blog
from models.User import User


@blog.route('/api/login', methods=['POST'])
def get_user():
    if request.method == 'POST':
        data = request.get_json()

        user = User.query.filter_by(email=data['email']).first()
        return jsonify(user)

