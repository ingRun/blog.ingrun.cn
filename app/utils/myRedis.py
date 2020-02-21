import config
from redis import Redis
from redis import ConnectionPool, exceptions

EXPIRES_TIME = None    # Redis过期时间,不设置则默认不过期

def redis_connection_pool():
    return ConnectionPool(**config.REDIS_DB_URL)

def redis_connect():
    r = Redis(connection_pool=redis_connection_pool())
    try:
        key, value = 'testRedisConnect', '测试Redis链接'
        r.set(key, value)
        r.delete(key)
    except exceptions.ConnectionError:
        print('redis 链接失败！')
        return None
    return r

def get_redis_data(key):
    conn = redis_connect()
    if conn:
        data = conn.get(key)
        return str(data, 'utf-8')
    return None

def set_redis_data(key, value):
    conn = redis_connect()
    data = value
    if conn:
        conn.set(
            name=key,
            value=data,
            ex=EXPIRES_TIME  # 第三个参数表示Redis过期时间,不设置则默认不过期
        )

def incr_redis(key='access_sum'):
    conn = redis_connect()
    if conn:
        conn.incr(key)
