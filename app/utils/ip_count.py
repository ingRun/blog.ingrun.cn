from app.utils.myRedis import my_redis
from datetime import datetime, timedelta

access_sum = 'access_sum'
access_today = 'access_today'
access_today_date = 'access_today_date'

# 总访问量
class AccessSum:

    @staticmethod
    def access_sum_add():
        my_redis.incr_redis(access_sum)

    @staticmethod
    def access_sum_get():
        return my_redis.get_redis_data(access_sum)

# 日访问量
class AccessToday:
    @staticmethod
    def access_toady_add():
        AccessToday.set_today_date()
        my_redis.incr_redis(access_today)
        AccessSum.access_sum_add()

    @staticmethod
    def access_today_get():
        return my_redis.get_redis_data(access_today)

    # 判断今日日期  重置今日访问量计数
    @staticmethod
    def set_today_date():
        now_date = datetime.now().strftime('%Y-%m-%d')
        old_date = my_redis.get_redis_data(access_today_date)
        if not old_date:
            # 若今日日期为空  则设置为当前日期
            my_redis.set_redis_data(access_today_date, now_date)
            return
        if not old_date == now_date:
            my_redis.set_redis_data(access_today_date, now_date)
            my_redis.set_redis_data(access_today, 0)


class SaveIp:
    pass




