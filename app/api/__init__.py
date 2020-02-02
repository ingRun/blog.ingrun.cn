from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import users, errors, tokens, tools, blog_urls, myRedis
