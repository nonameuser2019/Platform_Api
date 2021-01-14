import requests
from variables import *
import json
import pymysql.cursors
from sql_query import *
from pprint import pprint

# def get_db_conf():
#     with open('db.txt', 'r') as f:
#         read_data = f.read()
#     db_conf = json.loads(read_data)
#     return db_conf
#
# db_conf = get_db_conf()
# connection = pymysql.connect(host=db_conf['DB_HOST'],
#                              port=db_conf['DB_PORT'],
#                              user=db_conf['DB_USERNAME'],
#                              password=db_conf['DB_PASSWORD'],
#                              db=db_conf['DB_DATABASE'],
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)
# cursor = connection.cursor()
# cursor.execute(sql_get_categories_guid)
# data = cursor.fetchall()
# pprint(data[0]['category_guid'])


# response = requests.get(endpoint_get_categories, headers=HEADERS)
# print(response.elapsed.microseconds/1000)
response = requests.get('http://api.platform.masterservice.company/api/v1/categories')
print(response.status_code)
print(response.json())
