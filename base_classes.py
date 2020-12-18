import requests


class BaseCheck():

    # def __init__(self, method, endpoint, headers, params=None):
    #     self.method = method
    #     self.endpoint = endpoint
    #     self.headers = headers
    #     self.params = params

    def status_code(self, method, endpoint, headers, pararms=None):
        response = requests.request(method, endpoint, headers, pararms)
        assert response.status_code == 200, f'Ответ от сервера {response.status_code}'
