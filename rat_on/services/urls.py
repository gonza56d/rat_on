"""Services URLs.
"""

# Django
from django.urls import path

# App
from .views import results_view


urlpatterns = [
    path('<str:category>/', results_view, name='results_view'),
]
