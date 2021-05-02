"""Services result views."""

# Django
from django.shortcuts import render

# App
from rat_on.services.models import Service


def general(request):
    labels = []
    data = []
    services = Service.objects.all()
    for service in services:
        labels.append(service.name_pretty)
        data.append(float(service.response_time))
    return render(
        request,
        'services/results/general.html',
        {'services_labels': labels, 'services_data': data}
    )
