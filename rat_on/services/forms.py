"""Services forms."""

# Django
from django import forms


class ServicesResultsForm(forms.Form):
    """Form to filter results to display.
    """

    FILTER_CHOICES = (
        ('LH', 'Last  hour'),
        ('TD', 'Today'),
        ('L7', 'Last 7 days'),
        ('30', 'Last 30 days'),
        ('3M', 'Last trimester'),
        ('6M', 'Last semester'),
        ('LY', 'Last 365 days'),
    )

    interval = forms.ChoiceField(
        label='Filter results',
        choices=FILTER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
