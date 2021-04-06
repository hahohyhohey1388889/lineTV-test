
from datetime import datetime
from voluptuous import Schema, Required, MultipleInvalid
import traceback

def Date(fmt='%Y-%m-%d'):
    return lambda v: datetime.strptime(v, fmt)

Schema = Schema({Required('ad_network'): str, 
               Required('date'): Date(),
               Required('app_name'): str,
               Required('unit_id'): str,
               Required('request'): int,
               Required('revenue'): float,
               Required('imp'): int})
typeRule = {"ad_network": str,
                "date": str,
                "app_name": str,
                "unit_id": str,
                "request": int,
                "revenue": float,
                "imp": int}
def test_regularFormat():
    event = {"ad_network": "FOO",
            "date": "2019-06-05",
            "app_name": "LINETV",
            "unit_id": "55665201314",
            "request": "100",
            "revenue": "0.00365325",
            "imp": "23"}
    try:
        result = {key : value for key, value in event.items() if event.get(key)}
        validateResult = {key : float(value) if typeRule[key] == float else int(value) if typeRule[key] == int else value for key, value in result.items()}
        Schema(validateResult)
        print(result)
        assert True
    except:
        print('API format error')
        assert False

def test_keyloss():
    event = {
            "date": "2019-06-05",
            "app_name": "LINETV",
            "unit_id": "55665201314",
            "request": "100",
            "revenue": "0.00365325",
            "imp": "23"}
    try:
        result = {key : value for key, value in event.items() if event.get(key)}
        validateResult = {key : float(value) if typeRule[key] == float else int(value) if typeRule[key] == int else value for key, value in result.items()}
        Schema(validateResult)
        print(result)
        assert True
    except:
        print('API format error')
        assert False

def test_valueTypeError():
    event = {"ad_network": "FOO",
            "date": "2019-06-05",
            "app_name": "LINETV",
            "unit_id": "55665201314",
            "request": "hi",
            "revenue": "0.00365325",
            "imp": "23"}
    try:
        result = {key : value for key, value in event.items() if event.get(key)}
        validateResult = {key : float(value) if typeRule[key] == float else int(value) if typeRule[key] == int else value for key, value in result.items()}
        Schema(validateResult)
        print(result)
        assert True
    except:
        print('API format error')
        assert False