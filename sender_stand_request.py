import requests
import config
import data

# Создание заказа
def create_order(body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH, json=body, headers=data.headers)
response = create_order(data.order_body)

# Получаем номер трека созданного заказа
def get_track_order():
    return response.json()["track"]
track = get_track_order()

# Получаем заказ по трекномеру
def get_order():
    return requests.get(config.URL_SERVICE + config.GET_ORDER_VIA_TRACK + str(track))