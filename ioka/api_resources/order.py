import ioka
from ioka.api_resources.abstract.api_resource import APIResource


class Order(APIResource):

    @classmethod
    def list(cls, **params):
        return cls.get(f"{ioka.api_host}/v2/orders", params=params)

    @classmethod
    def retrieve(cls, order_id: str, **params):
        return cls.get(f"{ioka.api_host}/v2/orders/{order_id}", params=params)

    @classmethod
    def list_events(cls, order_id: str, **params):
        return cls.get(f"{ioka.api_host}/v2/orders/{order_id}/events", params=params)

    @classmethod
    def list_refunds(cls, order_id: str, **params):
        return cls.get(f"{ioka.api_host}/v2/orders/{order_id}/refunds", params=params)

    @classmethod
    def retrieve_refund(cls, order_id: str, refund_id: str, **params):
        return cls.get(f"{ioka.api_host}/v2/orders/{order_id}/refunds/{refund_id}", params=params)

    @classmethod
    def create(cls, **kwargs):
        return cls.post(f"{ioka.api_host}/v2/orders", json_obj=kwargs)

    @classmethod
    def capture(cls, order_id: str, **kwargs):
        return cls.post(f"{ioka.api_host}/v2/orders/{order_id}/capture", json_obj=kwargs)

    @classmethod
    def cancel(cls, order_id: str, **kwargs):
        return cls.post(f"{ioka.api_host}/v2/orders/{order_id}/cancel", json_obj=kwargs)

    @classmethod
    def refund(cls, order_id: str, **kwargs):
        return cls.post(f"{ioka.api_host}/v2/orders/{order_id}/refund", json_obj=kwargs)
