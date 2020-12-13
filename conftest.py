import pytest
import json
import pymysql.cursors
from sql_query import *
import requests


def get_db_conf():
    with open('db.txt', 'r') as f:
        read_data = f.read()
    db_conf = json.loads(read_data)
    return db_conf


@pytest.fixture
def cursor():
    db_conf = get_db_conf()
    connection = pymysql.connect(host=db_conf['DB_HOST'],
                                 port=db_conf['DB_PORT'],
                                 user=db_conf['DB_USERNAME'],
                                 password=db_conf['DB_PASSWORD'],
                                 db=db_conf['DB_DATABASE'],
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            yield cursor
            print('\nSuccessful connection to database')
    finally:
        connection.close()
        print('\nClosed db connect')

