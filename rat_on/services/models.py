"""Services models."""

# Python
from datetime import timedelta
from typing import Dict, List

# Django
from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone


class ServiceManager(models.Manager):

    def promediate(self) -> List[object]:
        """Promediate results in the proper interval.
        When selected interval is 'last hour', results are not promediated.

        Return
        ------
        List[Service] : List with promediated results.
        """
        splitted_results = {}
        if self.interval == 'TD':
            splitted_results = self.split_between_hours()
        elif self.interval != 'LH' and self.interval != 'TD':
            splitted_results = self.split_between_days()
        if splitted_results:
            self.results = []
            for key in splitted_results:
                value = 0.0
                for service in splitted_results[key]:
                    value += float(service.response_time)
                value = value / len(splitted_results[key])
                dummy = splitted_results[key][0]
                dummy.response_time = value
                self.results.append(dummy)
        return self.results

    def split_between_hours(self) -> Dict[str, List[object]]:
        """Separate queryset results by hours in a dict of objects lists.

        Return
        ------
        Dict[str, List[Service]] : Dictionary with hour number as key and list
            of values with that hour in their dates as value. Key format is
            'name_hour', e.g. 'platzi_15'
        """
        between_hours = {}
        for element in self.results:
            try:
                between_hours[
                    f'{element.name}_{element.request_datetime.hour}'
                ].append(element)
            except KeyError:
                between_hours[
                    f'{element.name}_{element.request_datetime.hour}'
                ] = [element]
        return between_hours

    def split_between_days(self) -> Dict[int, List[object]]:
        """Separate queryset results by days in a dict of objects lists.

        Return
        ------
        dict[int, List[object]] : Dictionary with day number as key and list
            of values with that day in their dates as value. Key format is
            'name_day', e.g. 'steam_27'
        """
        between_days = {}
        for element in self.results:
            try:
                between_days[
                    f'{element.name}_{element.request_datetime.hour}'
                ].append(element)
            except KeyError:
                between_days[
                    f'{element.name}_{element.request_datetime.hour}'
                ] = [element]
        return between_days

    def get_interval(self) -> None:
        """Get the proper time interval filter intended to get from form.
        """
        if self.interval == 'LH':
            last_hour = timezone.now() - timedelta(hours=4)
            return last_hour
        elif self.interval == 'TD':
            today = timezone.now().date()
            return today
        elif self.interval == 'L7':
            last_seven_days = timezone.now().date() - timedelta(days=6)
            return last_seven_days
        elif self.interval == '30':
            last_thirty_days = timezone.now().date() - timedelta(days=29)
            return last_thirty_days
        elif self.interval == '3M':
            last_trimester = timezone.now().date() - timedelta(days=89)
            return last_trimester
        elif self.interval == '6M':
            last_semester = timezone.now().date() - timedelta(days=179)
            return last_semester
        elif self.interval == 'LY':
            last_year = timezone.now().date() - timedelta(days=364)
            return last_year

    def from_category_and_interval(self, category, interval):
        """Filter by indicated category and interval.
        """
        self.interval = interval
        self.results = self.filter(
            category=category,
            request_datetime__gte=self.get_interval()
        )
        return self.results


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
