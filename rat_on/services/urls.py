"""Services URLs.
"""

# Django
from django.urls import path

# App
from .views import education


urlpatterns = [
    path('education/', education, name='education'),
]
