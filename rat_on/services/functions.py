"""Service functions."""

# Python
from multiprocessing import Process
import requests
from requests.exceptions import Timeout

# Django
from django.utils import timezone

# App
from .dummies import ServiceDummy
from .models import Service
from rat_on.utils.exceptions import ResponseException


def hit_service(dummy=ServiceDummy) -> None:
    """Hit a service endpoint and persist result in database with the Service
    model.

    Parameters
    ----------
    dummy : ServiceDummy to perform the request.
    """
    request_datetime = timezone.now()
    response_result = 'Success'
    try:
        request = requests.get(dummy.endpoint, timeout=60)
        if request.status_code != 200:
            raise ResponseException(
                f'Expected status code 200 but got {request.status_code}'
            )
    except Timeout:
        response_result = 'Request timeout'
    except ResponseException as re:
        response_result = re
    finally:
        request_finish = timezone.now()
        response_time = (request_finish - request_datetime).total_seconds()
        Service(
            name=dummy.name,
            category=dummy.category,
            endpoint=dummy.endpoint,
            request_datetime=request_datetime,
            response_time=response_time,
            response_status_code=request.status_code,
            response_result=response_result
        ).save()
