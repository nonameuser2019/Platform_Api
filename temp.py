import requests
from variables import *
import json
response = requests.request('GET', endpoint_get_categories, headers=HEADERS)
result = json.loads(response.text)['data']





