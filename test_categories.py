from sql_query import *
import json
import requests
from variables import *
from support_func import *
from base_classes import BaseCheck
import pytest
import random

def test_check_status_code():
    response = requests.request('GET', endpoint_get_categories, headers=HEADERS, params=None)
    assert response.status_code == 200, f'Ответ от сервера {response.status_code}'


def test_check_response_type():
    response = requests.request('GET', endpoint_get_categories, headers=HEADERS)
    assert type(response.json()) == dict


def test_check_nonToken():
    response = requests.request('GET', endpoint_get_categories)
    assert response.status_code != 200, f'Ожидаемый ответ сервера 4хх. Ответ сервера: {response.status_code}'


def test_check_count_get_categories(cursor):
    cursor.execute(sql_qet_all_categories)
    data = cursor.fetchall()
    response = requests.request('GET', endpoint_get_categories, headers=HEADERS)
    result = json.loads(response.text)['data']
    assert data[0]['cnt'] == count_categories(result), 'Не верное количество категорий'

@pytest.mark.t
def test_check_parentguid_category(cursor):
    cursor.execute(sql_get_categories_guid)
    data = cursor.fetchall()
    payload = {
        'guid': data[random.randint(0, len(data) - 1)]['guid']
    }
    print(payload['guid'])
    response = requests.request('GET', endpoint_get_categories_info, headers=HEADERS, params=payload)
    result = json.loads(response.text)['data']
    assert result[0]['guid'] == data[0]['guid']

