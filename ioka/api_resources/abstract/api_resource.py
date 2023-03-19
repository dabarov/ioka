from collections import namedtuple

import requests

import ioka


class APIResource:
    @classmethod
    def get_ioka_object(cls, response_data):
        if isinstance(response_data, list):
            return [cls.get_ioka_object(instance) for instance in response_data]
        return namedtuple('ioka_object', response_data.keys())(*response_data.values())

    @classmethod
    def request_call(cls, method, url, **kwargs):
        return_object = None
        headers = {"API-KEY": ioka.api_key}
        try:
            response = requests.request(method, url, headers=headers, **kwargs)
            response.raise_for_status()
            return_object = cls.get_ioka_object(response.json())
        except requests.exceptions.HTTPError as http_error:
            print(f"Http Error: {http_error}")
        except requests.exceptions.ConnectionError as connection_error:
            print("Error Connecting:", connection_error)
        except requests.exceptions.Timeout as timeout_error:
            print("Timeout Error:", timeout_error)
        except requests.exceptions.RequestException as request_error:
            print("OOps: Something Else", request_error)
        return return_object

    @classmethod
    def get(cls, url: str, params: dict):
        return cls.request_call("get", url, params=params)

    @classmethod
    def post(cls, url: str, json_obj: dict):
        return cls.request_call("get", url, json=json_obj)
