import json
import pymysql
from sql_query import *


def get_db_conf():
    with open('db.txt', 'r') as f:
        read_data = f.read()
    db_conf = json.loads(read_data)
    return db_conf


def get_data(sql_query):
    db_conf = get_db_conf()
    connection = pymysql.connect(host=db_conf['DB_HOST'],
                                 port=db_conf['DB_PORT'],
                                 user=db_conf['DB_USERNAME'],
                                 password=db_conf['DB_PASSWORD'],
                                 db=db_conf['DB_DATABASE'],
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.execute(sql_query)
    data = cursor.fetchall()
    return data

