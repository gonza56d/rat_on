# Python
from datetime import datetime
from typing import List

# App
from .models import Service


class ServiceDummy:

    def __init__(self, name: str, endpoint: str, 
                 category: Service.Categories.choices,
                 response_time: float = None, request_datetime: datetime = None
                ) -> None:
        self.name = name
        self.endpoint = endpoint
        self.category = category
        self.response_time = response_time
        self.request_datetime = request_datetime

    @staticmethod
    def get_all() -> List:
        return ServiceDummy.get_social_media() \
               + ServiceDummy.get_gaming() \
               + ServiceDummy.get_cloud_services() \
               + ServiceDummy.get_education()

    @staticmethod
    def get_social_media() -> List:
        return [
            ServiceDummy(
                name='facebook',
                category=Service.Categories.SOCIAL_MEDIA,
                endpoint='https://www.facebook.com/'
            ),
            ServiceDummy(
                name='twitter',
                category=Service.Categories.SOCIAL_MEDIA,
                endpoint='https://twitter.com/'
            ),
            ServiceDummy(
                name='instagram',
                category=Service.Categories.SOCIAL_MEDIA,
                endpoint='https://www.instagram.com/'
            ),
        ]

    @staticmethod
    def get_gaming() -> List:
        return [
            ServiceDummy(
                name='battle_net',
                category=Service.Categories.GAMING,
                endpoint='https://us.shop.battle.net/en-us'
            ),
            ServiceDummy(
                name='steam',
                category=Service.Categories.GAMING,
                endpoint='https://store.steampowered.com/'
            ),
            ServiceDummy(
                name='origin',
                category=Service.Categories.GAMING,
                endpoint='https://www.origin.com/arg/en-us/store'
            ),
        ]

    @staticmethod
    def get_cloud_services() -> List:
        return [
            ServiceDummy(
                name='amazon_web_services',
                category=Service.Categories.CLOUD_SERVICE,
                endpoint='https://aws.amazon.com/'
            ),
            ServiceDummy(
                name='google_cloud',
                category=Service.Categories.CLOUD_SERVICE,
                endpoint='https://cloud.google.com/'
            ),
            ServiceDummy(
                name='azure',
                category=Service.Categories.CLOUD_SERVICE,
                endpoint='https://azure.microsoft.com/en-us/'
            ),
        ]

    @staticmethod
    def get_education() -> List:
        return [
            ServiceDummy(
                name='platzi',
                category=Service.Categories.EDUCATION,
                endpoint='https://platzi.com/'
            ),
            ServiceDummy(
                name='udemy',
                category=Service.Categories.EDUCATION,
                endpoint='https://www.udemy.com/'
            ),
            ServiceDummy(
                name='coursera',
                category=Service.Categories.EDUCATION,
                endpoint='https://www.coursera.org/'
            ),
        ]
