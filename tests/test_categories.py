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
def test_check_status_code_with_right_token_get_categories():
    obj = BaseCheck(endpoint_get_categories)
    obj.status_code()


@pytest.mark.base
def test_check_response_type_get_categories():
    # сервер возвращает ответ json
    obj = BaseCheck(endpoint_get_categories)
    obj.response_type()


@pytest.mark.base
def test_check_nonToken():
    # сервер отвечает 4хх при попытке запроса без токена
    obj = BaseCheck(endpoint_get_categories)
    obj.not_token()


@pytest.mark.base
def test_check_timedelta():
    # время выполнения запроса
    obj = BaseCheck(endpoint_get_categories)
    obj.time_delta()


# These test checks API-> Get Category Info & Subcategories By GUID
@pytest.mark.base
def test_check_status_code_get_category_info(cursor):
    # проверка статус код при запросе с валидным токеном и guid
    # guid обязательный параметр
    cursor.execute(sql_get_categories_guid)
    data = cursor.fetchall()
    payload = {
        'guid': data[0]['guid']
    }
    obj = BaseCheck(endpoint_get_subcategories, payload)
    obj.status_code()


@pytest.mark.base
def test_check_get_category_info_with_wrong_guid(cursor):
    # проверка статус код при запросе с невалидным guid
    # guid обязательный параметр
    cursor.execute(sql_get_categories_guid)
    data = cursor.fetchall()
    payload = {
        'guid': data[0]['guid'] + '-sdfertd'
    }
    obj = BaseCheck(endpoint_get_subcategories, payload)
    obj.status_code()


@pytest.mark.base
def test_check_get_category_info_with_wrong_token(cursor):
    # проверка статус код при запросе с невалидным token
    # guid обязательный параметр
    cursor.execute(sql_get_categories_guid)
    data = cursor.fetchall()
    payload = {
        'guid': data[0]['guid']
    }
    obj = BaseCheck(endpoint_get_subcategories, payload)
    obj.wrong_token()


@pytest.mark.base
def test_check_status_code_get_category_info_without_guid():
    # проверка статуса при запросе без guid
    # guid обязательный параметр
    obj = BaseCheck(endpoint_get_subcategories)
    obj.not_params()


@pytest.mark.base
def test_check_status_code_get_category_info_without_token(cursor):
    # проверка статуса при запросе без token
    # guid обязательный параметр
    cursor.execute(sql_get_categories_guid)
    data = cursor.fetchall()
    payload = {
        'guid': data[0]['guid']
    }
    obj = BaseCheck(endpoint_get_subcategories, payload)
    obj.not_token()


@pytest.mark.base
def test_check_status_code_get_categories_info_without_token_and_guid():
    obj = BaseCheck(endpoint_get_subcategories, payload)
    obj.not_params_and_token()


@pytest.mark.base
def test_check_timedelta_get_category_info(cursor):
    # guid обязательный параметр
    cursor.execute(sql_get_categories_guid)
    data = cursor.fetchall()
    payload = {
        'guid': data[0]['guid']
    }
    obj = BaseCheck(endpoint_get_subcategories, payload)
    obj.time_delta()


# These test checks API-> Get Subcategories by URL

@pytest.mark.base
def test_check_status_code_get_subcategory_by_url():
    obj = BaseCheck(endpoint_get_subcategories, payload)
    obj.status_code()


@pytest.mark.base
def test_check_response_message_of_get_subcat_by_url():
    obj = BaseCheck(endpoint_get_subcategories, payload)
    obj.response_message()


@pytest.mark.base
def test_check_timedelta_get_subcat_by_url():
    obj = BaseCheck(endpoint_get_subcategories, payload)
    obj.time_delta()


@pytest.mark.base
def test_check_not_token_get_subcat_by_url():
    obj = BaseCheck(endpoint_get_subcategories, payload)
    obj.not_token()


@pytest.mark.base
def test_check_not_params_get_subcat_by_url():
    obj = BaseCheck(endpoint_get_subcategories, payload)
    obj.not_params()


@pytest.mark.base
def test_check_not_params_and_token_get_subcat_by_url():
    obj = BaseCheck(endpoint_get_subcategories)
    obj.not_params_and_token()


@pytest.mark.base
def test_check_wrong_token_get_subcat_by_url():
    obj = BaseCheck(endpoint_get_subcategories, payload)
    obj.wrong_token()


@pytest.mark.base
def test_check_wrong_params_get_subcat_by_url():
    obj = BaseCheck(endpoint_get_subcategories)
    obj.wrong_params()


@pytest.mark.base
@pytest.mark.xfail
def test_check_response_message_with_wrong_params_get_subcat_by_url():
    obj = BaseCheck(endpoint_get_subcategories)
    obj.response_message_with_wrong_params()

