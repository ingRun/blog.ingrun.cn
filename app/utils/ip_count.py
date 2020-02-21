from app.utils.myRedis import get_redis_data, incr_redis
from datetime import datetime, timedelta
import threading

access_sum = 'access_sum'
access_today = 'access_today'

class AccessSum:

    @staticmethod
    def access_sum_add():
        incr_redis(access_sum)

    @staticmethod
    def access_sum_get():
        return get_redis_data(access_sum)

class AccessToday:
    @staticmethod
    def access_toady_add():
        incr_redis(access_today)
        AccessSum.access_sum_add()

    @staticmethod
    def access_today_get():
        return get_redis_data(access_today)

    @staticmethod
    def access_today_time():
        pass

    @staticmethod
    def timer_():
        pass
        # now = datetime.now()
        # next_day = now + timedelta(days=1)
        # d2 = datetime(next_day.year, next_day.month, next_day.day, 0, 0, 0) - now
        #
        # print(d2.total_seconds())
        # timer = threading.Timer(timer_start_time, func)
        # timer.start()
