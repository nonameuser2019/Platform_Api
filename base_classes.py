import requests
from variables import *
import json
from sql_query import *

class BaseCheck():

    def __init__(self, endpoint, payload=None):
        self.endpoint = endpoint
        self.payload = payload

    def status_code(self, method='GET'):
        if method == 'POST':
            response = requests.request(method, self.endpoint, headers=HEADERS, data=json.dumps(self.payload))
        else:
            response = requests.request(method, self.endpoint, headers=HEADERS, params=self.payload)
        assert response.status_code == 200, f'Ответ от сервера {response.status_code}'

    def response_type(self):
        response = requests.request('GET', self.endpoint, headers=HEADERS, params=self.payload)
        assert type(response.json()) == dict
        assert response.status_code == 200, f'Ожидаемый твет от сервера, сервер ответил: {response.status_code}'

    def response_message(self):
        response = requests.request('GET', self.endpoint, headers=HEADERS, params=self.payload)
        response_message = json.loads(response.text)['success']
        assert response.status_code == 200, f'Ответ от сервера {response.status_code}'
        assert response_message, f'Сообщение о статусе запроса API не True, Полученное сообщение: {response_message}'

    def time_delta(self):
        response = requests.request('GET', self.endpoint, headers=HEADERS, params=self.payload)
        assert int(
            response.elapsed.microseconds / 1000) <= 499, f"Ожидаемое время ответа не более 1000мс, фактическое" \
                                                           f" время {int(response.elapsed.microseconds / 1000)}"
        assert response.status_code == 200, f'Ответ от сервера {response.status_code}'

    def not_token(self):
        response = requests.request('GET', self.endpoint, params=self.payload)
        assert response.status_code != 200, f'Ожидаемый ответ от сервера 4XX, ответ от сервера {response.status_code}'

    def not_params(self):
        response = requests.request('GET', self.endpoint, headers=HEADERS)
        assert response.status_code != 200, f'Ожидаемый ответ от сервера 4XX, ответ от сервера {response.status_code}'

    def not_params_and_token(self):
        response = requests.request('GET', self.endpoint)
        assert response.status_code != 200, f'Ожидаемый ответ от сервера 4XX, ответ от сервера {response.status_code}'

    def wrong_token(self):
        wrong_headers = {'Authorization': 'Bearer dkgjsdlkgdlgl'}
        response = requests.request('GET', self.endpoint, headers=wrong_headers, params=self.payload)
        assert response.status_code != 200, f'Ожидаемый ответ от сервера 4XX, ответ от сервера {response.status_code}'

    def wrong_params(self):
        wrong_payload = 'everything'
        response = requests.request('GET', self.endpoint, headers=HEADERS, params=wrong_payload)
        assert response.status_code != 200, f'Ожидаемый ответ от сервера 4XX, ответ от сервера {response.status_code}'

    def response_message_with_wrong_params(self):
        wrong_payload = 'everything'
        response = requests.request('GET', self.endpoint, headers=HEADERS, params=wrong_payload)
        response_message = json.loads(response.text)['success']
        assert response.status_code == 200, f'Ответ от сервера {response.status_code}'
        assert response_message, f'Сообщение о статусе запроса API не True, Полученное сообщение: {response_message}'

    def positive_registeration(self):
        response = requests.post(self.endpoint, headers=HEADERS, data=json.dumps(self.payload))
        assert response.json()['message'] == 'Registered successfully.', f'Registration is not successful ' \
                                                                         f'{response.json()["message"]}'

    def registration_without_wrong_name(self, result, cursor):
        response = requests.post(self.endpoint, headers=HEADERS, data=json.dumps(self.payload))
        cursor.execute(sql_delete_new_user, (self.payload['data']['login'],))
        assert response.json()['success'] == result, f'Registration impossible with name: {self.payload["data"]["name"]}' \
                                                     f' Response: {response.json()["success"]}'

    def registration_with_wrong_login(self, result, cursor):
        response = requests.post(self.endpoint, headers=HEADERS, data=json.dumps(self.payload))
        if response.status_code == 200:
            print('The database entry deleted')
            cursor.execute(sql_delete_new_user, (self.payload['data']['name'],))
        assert response.json()['success'] == result, f'Registration impossible with password: ' \
                                                     f'{self.payload["data"]["login"]} Response: {response.json()["success"]}'

    def registration_with_wrong_password(self, result, cursor):
        response = requests.post(self.endpoint, headers=HEADERS, data=json.dumps(self.payload))
        if response.status_code == 200:
            print('The database entry deleted')
            cursor.execute(sql_delete_new_user, (self.payload['data']['name'],))
        assert response.json()['success'] == result, f'Registration impossible with password: ' \
                                                     f'{self.payload["data"]["password"]} Response: {response.json()["success"]}'

    def login_with_correct_data(self, result):
        response = requests.post(self.endpoint, headers=HEADERS, data=json.dumps(self.payload))
        assert response.json()['success'] == result, f'Registration is not success. Response code: {response.status_code}'