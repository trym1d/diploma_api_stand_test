# Дмитрий Горлов 31 когорта, финальный проект. Инженер по тестированию плюс.

import sender_stand_request

def test_positive_order_status():
    response = sender_stand_request.get_order()
    assert response.status_code == 200