import requests
from variables import *
import json
import pymysql.cursors
from sql_query import *

def get_db_conf():
    with open('db.txt', 'r') as f:
        read_data = f.read()
    db_conf = json.loads(read_data)
    return db_conf





