"""Services result views."""

# Django
from django.http import Http404
from django.shortcuts import render

# App
from .forms import ServicesResultsForm
from .dummies import ServiceDummy
from .models import Service


def results_view(request, category: Service.Categories.EDUCATION):

    if category.upper() not in Service.Categories.__members__:
        raise Http404('Service category does not exist.')

    form = ServicesResultsForm(data=request.GET)
    data = {}

    if form.is_valid():
        
        for dummy in eval(f'ServiceDummy.get_{category.lower()}()'):
            data[dummy.name] = []

        services = Service.objects.from_category_and_interval(
            category=eval(f'Service.Categories.{category.upper()}'),
            interval=form.cleaned_data.get('interval')
        )

        for service in services:
            data[service.name].append(
                (service.request_datetime, float(service.response_time))
            )

    return render(
        request,
        'services/results.html',
        {
            'services_data': data,
            'category': category,
            'form': form,
            'categories': Service.Categories.__members__
        }
    )
