"""Services URLs.
"""

# Django
from django.urls import path

# App
from .views import general


urlpatterns = [
    path('general/', general, name='general'),
]
