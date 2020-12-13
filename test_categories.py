from sql_query import *
import json
import requests
from variables import *

def test_check_status_code():
    response = requests.request('GET', endpoint_get_categories, headers=HEADERS)
    assert response.status_code == 200, f'Ответ от сервера {response.status_code}'


def test_check_response_type():
    response = requests.request('GET', endpoint_get_categories, headers=HEADERS)
    assert type(response.json()) == dict


def test_check_nonToken():
    response = requests.request('GET', endpoint_get_categories)
    assert response.status_code != 200, f'Оэидаемый ответ сервера 4хх. Ответ сервера: {response.status_code}'


def test_check_count_get_categories(cursor):
    cursor.execute(sql_qet_all_categories)
    data = cursor.fetchall()
    response = requests.request('GET', endpoint_get_categories, headers=HEADERS)
    result = json.loads(response.text)
    assert data[0]['cnt'] == len(result['data']), 'Не верное количество категорий'

