"""Services URLs.
"""

# Django
from django.urls import path

# App
from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
