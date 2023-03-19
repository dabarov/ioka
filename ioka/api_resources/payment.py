import ioka
from ioka.api_resources.abstract.api_resource import APIResource


class Payment(APIResource):

    @classmethod
    def retrieve(cls, order_id: str, payment_id: str, **params):
        return cls._get(f"{ioka.api_host}/v2/orders/{order_id}/payments/{payment_id}", params=params)

    @classmethod
    def create_card(cls, order_id: str, **kwargs):
        return cls._post(f"{ioka.api_host}/v2/orders/{order_id}/payments/card", json_obj=kwargs)
