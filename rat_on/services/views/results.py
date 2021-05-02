"""Services result views."""

# Python
from datetime import timedelta

# Django
from django.http import Http404
from django.shortcuts import render
from django.utils import timezone

# App
from rat_on.services.dummies import ServiceDummy
from rat_on.services.models import Service


def results_view(request, category: Service.Categories.EDUCATION):

    if category.upper() not in Service.Categories.__members__:
        raise Http404('Service category does not exist.')

    data = {}
    for dummy in eval(f'ServiceDummy.get_{category.lower()}()'):
        data[dummy.name] = []

    last_hour = timezone.now() - timedelta(hours=4)
    services = Service.objects.filter(
        category=eval(f'Service.Categories.{category.upper()}'),
        request_datetime__gte=last_hour
    )

    for service in services:
        data[service.name].append(
            (service.request_datetime, float(service.response_time))
        )

    return render(
        request,
        'services/results.html',
        {'services_data': data, 'category': category}
    )
