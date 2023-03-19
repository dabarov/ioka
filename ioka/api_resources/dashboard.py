import ioka
from ioka.api_resources.abstract.api_resource import APIResource


class Dashboard(APIResource):
    GROUP_API_URL = "/v2/dashboard/payments"

    @classmethod
    def search_payments(cls, **params):
        return cls._get(f"{ioka.api_host}{cls.GROUP_API_URL}", params=params)

    @classmethod
    def export_payments(cls, **params):
        return cls._get(f"{ioka.api_host}{cls.GROUP_API_URL}/export", params=params)
