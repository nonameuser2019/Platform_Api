from sql_query import *
import json
import requests
from variables import *
from support_func import *
import pytest
import random


# тесты для Categories -> GetCategories
@pytest.mark.base
def test_check_status_code():
    # сервер отвечает 200 при корректном запросе(с токеном)
    response = requests.request('GET', endpoint_get_categories, headers=HEADERS)
    assert response.status_code == 200, f'Ответ от сервера {response.status_code}'


@pytest.mark.base
def test_check_response_type():
    # сервер возвращает ответ json
    response = requests.request('GET', endpoint_get_categories, headers=HEADERS)
    print(response.status_code)
    assert response.status_code == 200, f'Ответ от сервера не равен 200: {response.status_code}'
    assert type(response.json()) == dict, 'Сервер вернул ответ не Json'


@pytest.mark.base
def test_check_nonToken():
    # сервер отвечает 4хх при попытке запроса без токена
    response = requests.request('GET', endpoint_get_categories)
    assert response.status_code != 200, f'Ожидаемый ответ сервера 4хх. Ответ сервера: {response.status_code}'


@pytest.mark.base
def test_check_timedelta():
    # время выполнения запроса
    response = requests.request('GET', endpoint_get_categories, headers=HEADERS)
    assert response.status_code == 200, f'Ответ от сервера не равен 200: {response.status_code}'
    assert int(
        response.elapsed.microseconds / 1000) <= 1000, f"Ожидаемое время ответа не более 1000мс, фактическое время " \
                                                      f"{int(response.elapsed.microseconds / 1000)}"


def test_check_count_get_categories(cursor):
    # проверяет что api вернет такое же кол. категорий как в БД.
    cursor.execute(sql_qet_all_categories)
    data = cursor.fetchall()
    response = requests.request('GET', endpoint_get_categories, headers=HEADERS)
    result = json.loads(response.text)['data']
    assert data[0]['cnt'] == count_categories(result), 'Не верное количество категорий'


# Тесты для Categories -> Get Category Info and SubCategories by guid
def test_check_guid_category(cursor):
    # проверка что api возвращает верный guid
    cursor.execute(sql_get_categories_guid)
    data = cursor.fetchall()
    payload = {
        'guid': data[random.randint(0, len(data) - 1)]['guid']
    }
    response = requests.request('GET', endpoint_get_categories_info, headers=HEADERS, params=payload)
    result = json.loads(response.text)['data']
    assert result['category']['guid'] == payload['guid'], f'Не верный guid'

# def test_check_name_category(cursor):
#     cursor.execute(sql_get_categories_guid)
#     data = cursor.fetchall()
#     payload = {
#         'guid': data[random.randint(0, len(data) - 1)]['guid']
#     }
#     response = requests.request('GET', endpoint_get_categories_info, headers=HEADERS, params=payload)
#     result = json.loads(response.text)['data']
#     assert result['category']['guid'] == , f'Не верное название категории'
