import pytest
from base_classes import *
import requests
import json
from sql_query import *


def test_check_positive_reg():
    obj = BaseCheck(endpoint_registration, payload=payload)
    obj.positive_registeration()


def test_check_registration_phone_number(cursor):
    cursor.execute(sql_get_new_user_phone)
    data = cursor.fetchall()
    assert data[0]['phone'] == payload['data']['login'], f'Database return wrong number'
    cursor.execute(sql_delete_new_user, (payload['data']['login'],))
    print('\nData of new user was be deleted')


@pytest.mark.parametrize('name, result', name_list)
def test_check_possibility_reg_with_different_names(name, result, cursor):
    payload = {
        "data":{
            "name": name,
            "login": "0665315679",
            "password": "P123qwerty"
        }
    }
    obj = BaseCheck(endpoint_registration, payload=payload)
    obj.registration_without_wrong_name(result, cursor)


@pytest.mark.parametrize('login, result', login_list)
def test_reg_with_different_login(login, result, cursor):
    payload = {
        "data":{
            "name": "Alex",
            "login": login,
            "password": "P123qwerty"
        }
    }
    obj = BaseCheck(endpoint_registration, payload=payload)
    obj.registration_with_wrong_login(result, cursor)


@pytest.mark.parametrize('password, result', pass_list)
def test_reg_with_different_password(password, result, cursor):
    payload = {
        "data":{
            "name": "Alex",
            "login": "380685340603",
            "password": password
        }
    }
    obj = BaseCheck(endpoint_registration, payload=payload)
    obj.registration_with_wrong_password(result, cursor)


@pytest.mark.parametrize('login, password, result', auth_list)
@pytest.mark.t
def test_login_with_correct_data(login, password, result):
    payload = {
        "data": {
            "login": login,
            "password": password
        }
    }
    obj = BaseCheck(endpoint_login, payload=payload)
    obj.login_with_correct_data(result)