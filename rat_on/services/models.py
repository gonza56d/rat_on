"""Services models."""

# Python
from datetime import timedelta

# Django
from django.db import models
from django.utils import timezone


class ServiceManager(models.Manager):

    @staticmethod
    def get_interval(interval):
        """Get the proper time interval filter intended to get from form.
        """
        if interval == 'LH':
            last_hour = timezone.now() - timedelta(hours=4)
            return last_hour
        elif interval == 'TD':
            today = timezone.now().date()
            return today
        elif interval == 'L7':
            last_seven_days = timezone.now().date() - timedelta(days=6)
            return last_seven_days
        elif interval == '30':
            last_thirty_days = timezone.now().date() - timedelta(days=29)
            return last_thirty_days
        elif interval == '3M':
            last_trimester = timezone.now().date() - timedelta(days=89)
            return last_trimester
        elif interval == '6M':
            last_semester = timezone.now().date() - timedelta(days=179)
            return last_semester
        elif interval == 'LY':
            last_year = timezone.now().date() - timedelta(days=364)
            return last_year

    def from_category_and_interval(self, category, interval):
        return self.filter(
            category=category,
            request_datetime__gte= ServiceManager.get_interval(interval)
        )


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

    objects = ServiceManager()
