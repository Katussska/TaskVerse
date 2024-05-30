from typing import Any, Dict

from django_components import component


@component.register('PriorityBadge')
class StatusBadge(component.Component):
    template_name = 'template.html'

    def get_context_data(self, priority: str) -> Dict[str, Any]:
        return {
            'priority': priority,
        }
