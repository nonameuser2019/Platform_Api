from sql_query import *
import json
import requests
from variables import *
from support_func import *
import pytest
from base_classes import *
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


# These test checks API-> Get Category Info & Subcategories By GUID
@pytest.mark.base
def test_check_status_code_get_category_info(cursor):
    # проверка статус код при запросе с валидным токеном и guid
    # guid обязательный параметр
    cursor.execute(sql_get_categories_guid)
    data = cursor.fetchall()
    payload = {
        'guid': data[0]['category_guid']
    }
    response = requests.request('GET', endpoint_get_categories_info, headers=HEADERS, params=payload)
    assert response.status_code == 200, f'Не верынй ответ сервера, ответ от сервера {response.status_code}'


@pytest.mark.base
def test_check_get_category_info_with_wrong_guid(cursor):
    # проверка статус код при запросе с невалидным guid
    # guid обязательный параметр
    cursor.execute(sql_get_categories_guid)
    data = cursor.fetchall()
    payload = {
        'guid': data[0]['category_guid'] + '-sdfertd'
    }
    response = requests.request('GET', endpoint_get_categories_info, headers=HEADERS, params=payload)
    assert response.status_code != 200, f'Не верынй ответ сервера, ответ от сервера {response.status_code}'


@pytest.mark.base
def test_check_get_category_info_with_wrong_token(cursor):
    # проверка статус код при запросе с невалидным token
    # guid обязательный параметр
    cursor.execute(sql_get_categories_guid)
    data = cursor.fetchall()
    payload = {
        'guid': data[0]['category_guid']
    }
    WRONG_HEADERS = {}
    WRONG_HEADERS['Authorization'] = 'asddgdsddgsdgdsgsddgegmdgvioboiobshheiobjsoidbhushvuseghuihvuigseuy'
    response = requests.request('GET', endpoint_get_categories_info, headers=WRONG_HEADERS, params=payload)
    assert response.status_code != 200, f'Не верынй ответ сервера, ответ от сервера {response.status_code}'


@pytest.mark.base
def test_check_status_code_get_category_info_without_guid():
    # проверка статуса при запросе без guid
    # guid обязательный параметр
    response = requests.request('GET', endpoint_get_categories_info, headers=HEADERS)
    assert response.status_code != 200, f'Не верынй ответ сервера, ответ от сервера {response.status_code}'


@pytest.mark.base
def test_check_status_code_get_category_info_without_token(cursor):
    # проверка статуса при запросе без token
    # guid обязательный параметр
    cursor.execute(sql_get_categories_guid)
    data = cursor.fetchall()
    payload = {
        'guid': data[0]['category_guid']
    }
    response = requests.request('GET', endpoint_get_categories_info, params=payload)
    assert response.status_code != 200, f'Не верынй ответ сервера, ответ от сервера {response.status_code}'


@pytest.mark.base
def test_check_status_code_get_categories_info_without_token_and_guid():
    response = requests.request('GET', endpoint_get_categories_info)
    assert response.status_code != 200, f'Не верынй ответ сервера, ответ от сервера {response.status_code}'


@pytest.mark.base
def test_check_timedelta_get_category_info(cursor):
    # guid обязательный параметр
    cursor.execute(sql_get_categories_guid)
    data = cursor.fetchall()
    payload = {
        'guid': data[0]['category_guid']
    }
    response = requests.request('GET', endpoint_get_categories_info, headers=HEADERS, params=payload)
    assert response.status_code == 200, f'Не верынй ответ сервера, ответ от сервера {response.status_code}'
    assert int(
        response.elapsed.microseconds / 1000) <= 500, f"Ожидаемое время ответа не более 1000мс, фактическое время " \
                                                      f"{int(response.elapsed.microseconds / 1000)}"


# These test checks API-> Get Subcategories by URL

@pytest.mark.base
def test_check_status_code_get_subcategory_by_url():
    obj = BaseCheck(endpoint_get_subcategories)
    obj.status_code()


@pytest.mark.base
def test_check_response_message_of_get_subcat_by_url():
    obj = BaseCheck(endpoint_get_subcategories)
    obj.response_message()


@pytest.mark.base
def test_check_timedelta_get_subcat_by_url():
    obj = BaseCheck(endpoint_get_subcategories)
    obj.time_delta()

@pytest.mark.base
def test_check_not_token_get_subcat_by_url():
    obj = BaseCheck(endpoint_get_subcategories)
    obj.not_token()


@pytest.mark.base
def test_check_not_params_get_subcat_by_url():
    obj = BaseCheck(endpoint_get_subcategories)
    obj.not_params()


@pytest.mark.base
def test_check_not_params_and_token_get_subcat_by_url():
    obj = BaseCheck(endpoint_get_subcategories)
    obj.not_params_and_token()


@pytest.mark.base
def test_check_wrong_token_get_subcat_by_url():
    obj = BaseCheck(endpoint_get_subcategories)
    obj.wrong_token()


@pytest.mark.base
def test_check_wrong_params_get_subcat_by_url():
    obj = BaseCheck(endpoint_get_subcategories)
    obj.wrong_params()


@pytest.mark.base
def test_check_response_message_with_wrong_params_get_subcat_by_url():
    obj = BaseCheck(endpoint_get_subcategories)
    obj.response_message_with_wrong_marams()





# def test_check_count_get_categories(cursor):
#     # проверяет что api вернет такое же кол. категорий как в БД.
#     cursor.execute(sql_qet_all_categories)
#     data = cursor.fetchall()
#     response = requests.request('GET', endpoint_get_categories, headers=HEADERS)
#     result = json.loads(response.text)['data']
#     assert data[0]['cnt'] == count_categories(result), 'Не верное количество категорий'


# Тесты для Categories -> Get Category Info and SubCategories by guid
# def test_check_guid_category(cursor):
#     # проверка что api возвращает верный guid
#     cursor.execute(sql_get_categories_guid)
#     data = cursor.fetchall()
#     payload = {
#         'guid': data[random.randint(0, len(data) - 1)]['category_guid']
#     }
#     response = requests.request('GET', endpoint_get_categories_info, headers=HEADERS, params=payload)
#     result = json.loads(response.text)['data']
#     assert result['category']['guid'] == payload['guid'], f'Не верный guid'

# def test_check_name_category(cursor):
#     cursor.execute(sql_get_categories_guid)
#     data = cursor.fetchall()
#     payload = {
#         'guid': data[random.randint(0, len(data) - 1)]['guid']
#     }
#     response = requests.request('GET', endpoint_get_categories_info, headers=HEADERS, params=payload)
#     result = json.loads(response.text)['data']
#     assert result['category']['guid'] == , f'Не верное название категории'
