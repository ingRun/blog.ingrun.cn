from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

from app import db, blog
from app.api.tools import json_response, err_response


# def error_response(status_code):
#     payload = {'message': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
#     response = jsonify(payload)
#     response.status_code = status_code
#     return response
#
#
# def bad_request(message=None):
#     return error_response(400, message)


@blog.errorhandler(404)
def not_found_error(e):
    return err_response(message='未找到所请求资源', status_code=404)

@blog.errorhandler(500)
def internal_error(e):
    db.session.rollback()
    return err_response(message='服务器错误！', status_code=500)
