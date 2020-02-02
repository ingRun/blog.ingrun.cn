import config
from redis import Redis

from app.api.tools import err_response

EXPIRES_TIME = None

def redis_connect():
    return Redis(**config.REDIS_DB_URL)


def get_redis_data(key):
    conn = redis_connect()
    data = conn.get(key)
    return data

def set_redis_data(key, value):
    conn = redis_connect()
    data = value
    conn.set(
        name=key,
        value=data,
        ex=EXPIRES_TIME  # 第三个参数表示Redis过期时间,不设置则默认不过期
    )


# if __name__ == '__main__':
#     set_redis_data('admin', 'password')
#     print(get_redis_data('admin'))
