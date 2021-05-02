"""Project URLs.
"""

# Django
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'services/',
        include(('rat_on.services.urls', 'services'),
        namespace='services')
    ),
]
