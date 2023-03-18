import requests

import ioka


class Order:

    @classmethod
    def list(cls):
        headers = {"API-KEY": ioka.api_key}
        response = requests.get(f"{ioka.api_host}/v2/orders", headers=headers)
        return response.text
