"""Services models."""

# Django
from django.db import models


class Service(models.Model):
    """Represent each endpoint test results.
    """

    class Categories(models.TextChoices):
        EDUCATION = 'ED', 'Education'
        SOCIAL_MEDIA = 'SM', 'Social Media'
        GAMING = 'GA', 'Gaming'
        CLOUD_SERVICES = 'CS', 'Cloud Service'

    name = models.CharField(
        'name of the site to identify and compare with other results',
        max_length=30
    )
    category = models.CharField(
        'service category',
        max_length=2,
        choices=Categories.choices
    )
    endpoint = models.CharField(
        'endpoint to hit when testing',
        max_length=5000
    )
    request_datetime = models.DateTimeField(
        'datetime when the request was sent'
    )
    response_time = models.DecimalField(
        'response time in seconds',
        max_digits=12,
        decimal_places=3
    )
    response_status_code = models.PositiveIntegerField()
    response_result = models.CharField(max_length=1000)

    @property
    def name_pretty(self):
        return str(self.name).replace('_', ' ').title()
