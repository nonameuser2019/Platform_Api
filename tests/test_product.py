from sql_query import *
import json
import requests
from variables import *
from support_func import *
import pytest
from base_classes import *
import random


@pytest.mark.smoke
def test_get_product_by_id_positive():
    payload = {
        'id': '364144'
    }
    obj = BaseCheck(endpoint_get_product_by_id, payload)
    obj.status_code()


