# Дмитрий Горлов 31 когорта, финальный проект. Инженер по тестированию плюс.

import data
import sender_stand_request


def test_positive_order_status():
    # Запрос на создание заказа
    sender_stand_request.create_order(
        data.order_body)
    # Сохраняем трек-номер в переменную
    track = sender_stand_request.get_track_order()
    # Запрос заказа по сохранённой переменной
    response = sender_stand_request.get_order(track)
    # Проверка кода ответа
    assert response.status_code == 200
