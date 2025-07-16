import requests
import config
import data

# Создание заказа


def create_order(body):
    return requests.post(
        config.URL_SERVICE +
        config.CREATE_ORDER_PATH,
        json=body,
        headers=data.headers)

# Получаем номер трека созданного заказа


def get_track_order():
    return create_order(data.order_body).json()["track"]

# Получаем заказ по трекномеру


def get_order(track):
    return requests.get(
        config.URL_SERVICE +
        config.GET_ORDER_VIA_TRACK +
        str(track))
