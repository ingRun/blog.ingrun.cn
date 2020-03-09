from app.api import bp
from app.api.tools import success_response, err_response
from app.utils.ip_count import AccessSum, AccessToday


@bp.route('/testAccessSum', methods=['GET'])
def test_access_sum():
    AccessSum.access_sum_add()
    k = AccessSum.access_sum_get()
    if k:
        return success_response(message=k)
    return err_response(message='redis 未运行！', status_code=500)

@bp.route('/getAccessSum', methods=['GET'])  # 总访问量
def get_access_sum():
    k = AccessSum.access_sum_get()
    if k:
        return success_response(message=k, data=k)
    return err_response(message='redis 未运行！', status_code=500)

@bp.route('/getAccessToday', methods=['GET'])  # 今日访问量
def get_access_today():
    k = AccessToday.access_today_get()
    if k:
        return success_response(message=k, data=k)
    return err_response(message='redis 未运行！', status_code=500)

