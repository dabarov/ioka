import ioka
from ioka.api_resources.abstract.api_resource import APIResource


class Customer(APIResource):

    @classmethod
    def list(cls, **params):
        return cls._get(f"{ioka.api_host}/v2/customers", params=params)

    @classmethod
    def retrieve(cls, customer_id: str, **params):
        return cls._get(f"{ioka.api_host}/v2/customers/{customer_id}", params=params)

    @classmethod
    def list_events(cls, customer_id: str, **params):
        return cls._get(f"{ioka.api_host}/v2/orders/{customer_id}/events", params=params)

    @classmethod
    def create(cls, **kwargs):
        return cls._post(f"{ioka.api_host}/v2/customers", json_obj=kwargs)

    @classmethod
    def _delete(cls, customer_id: str, **kwargs):
        return cls._delete(f"{ioka.api_host}/v2/customers/{customer_id}", json_obj=kwargs)
