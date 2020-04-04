import config
from redis import Redis
from redis import ConnectionPool, exceptions

EXPIRES_TIME = None    # Redis过期时间,不设置则默认不过期

class MyRedis:

    IS_RUN_REDIS = 0  # 0 1 2   0：未检测  1：已运行  2：未运行

    @staticmethod
    def redis_connection_pool():
        return ConnectionPool(**config.REDIS_DB_URL)

    def redis_connect(self):
        r = Redis(connection_pool=self.redis_connection_pool())
        if self.IS_RUN_REDIS == 2:
            print('redis未连接！')
            return None
        if self.IS_RUN_REDIS == 0:
            try:
                key, value = 'testRedisConnect', '测试Redis链接'
                r.set(key, value)
                r.delete(key)
            except exceptions.ConnectionError:
                self.IS_RUN_REDIS = 2
                print('测试 redis 链接失败！')
                return None
            self.IS_RUN_REDIS = 1
        return r

    def get_redis_data(self, key):
        conn = self.redis_connect()
        if conn:
            data = conn.get(key)
            if not data:
                return None
            return str(data, 'utf-8')
        return None

    def set_redis_data(self, key, value):
        conn = self.redis_connect()
        data = value
        if conn:
            conn.set(
                name=key,
                value=data,
                ex=EXPIRES_TIME  # 第三个参数表示Redis过期时间,不设置则默认不过期
            )

    def incr_redis(self, key='access_sum'):
        conn = self.redis_connect()
        if conn:
            conn.incr(key)

    def get_hash_data(self, name, key=None):
        conn = self.redis_connect()
        if conn:
            d = conn.hget(name, key)
            if not d:
                return None
            return str(d, 'utf-8')

    def set_hash_data(self, obj):
        conn = self.redis_connect()
        if conn:
            conn.hset()


my_redis = MyRedis()