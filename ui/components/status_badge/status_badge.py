from typing import Any, Dict

from django_components import component


@component.register('StatusBadge')
class StatusBadge(component.Component):
    template_name = 'template.html'

    def get_context_data(self, status: str) -> Dict[str, Any]:
        return {
            'status': status,
        }
