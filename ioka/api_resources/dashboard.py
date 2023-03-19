import ioka
from ioka.api_resources.abstract.api_resource import APIResource


class Dashboard(APIResource):

    @classmethod
    def search_payments(cls, **params):
        return cls._get(f"{ioka.api_host}/v2/dashboard/payments", params=params)

    @classmethod
    def export_payments(cls, **params):
        return cls._get(f"{ioka.api_host}/v2/dashboard/payments/export", params=params)
