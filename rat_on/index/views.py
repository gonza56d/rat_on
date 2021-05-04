"""Index views."""

# Python
from typing import Any, Dict

# Django
from django.views.generic import TemplateView

# App
from rat_on.services.models import Service


class IndexView(TemplateView):

    template_name = 'index/index.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return {
            'categories': Service.Categories.__members__
        }
