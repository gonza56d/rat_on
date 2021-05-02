"""Services result views."""

# Python
from datetime import timedelta

# Django
from django.shortcuts import render
from django.utils import timezone

# App
from rat_on.services.models import Service


def education(request):
    last_hour = timezone.now() - timedelta(hours=4)
    print('last_hour:', last_hour)
    data = {
        'platzi': [],
        'udemy': [],
        'coursera': [],
    }
    services = Service.objects.filter(
        category=Service.Categories.EDUCATION,
        request_datetime__gte=last_hour
    )
    for service in services:
        data[service.name].append(
            (service.request_datetime, float(service.response_time))
        )
    return render(
        request,
        'services/results/general.html',
        {'services_data': data}
    )
