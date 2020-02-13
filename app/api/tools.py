from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def json_response(message: str, status_code: int = 200, code: int = 1, data=''):
    response = jsonify({'code': code, 'message': message, 'data': data})
    response.status_code = status_code
    return response

def success_response(message: str = 'success', status_code: int = 200, code: int = 1, data=''):
    return json_response(message=message, status_code=status_code, code=code, data=data)

def err_response(message: str = '', status_code=404, code: int = 0, data=''):
    payload = {'message': message, 'status_message': HTTP_STATUS_CODES.get(status_code, 'Unknown error'),
               'code': code, 'data': data}
    response = jsonify(payload)
    response.status_code = status_code
    return response
