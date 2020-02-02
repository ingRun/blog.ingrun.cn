from ..app.api.myRedis import redis_connect

redis = redis_connect()

redis.set_redis_data('admin', 'password')

print(redis.get_redis_data('admin'))
