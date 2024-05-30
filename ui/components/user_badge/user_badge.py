from typing import Any, Dict

from django_components import component

from users.models import User


@component.register('UserBadge')
class StatusBadge(component.Component):
    template_name = 'template.html'

    def get_context_data(self, user: User = None) -> Dict[str, Any]:
        return {
            'user': user,
        }
