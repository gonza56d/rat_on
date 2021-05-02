"""Service model admin."""

# Django
from django.contrib import admin

# App
from rat_on.services.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Service model admin."""

    pass
