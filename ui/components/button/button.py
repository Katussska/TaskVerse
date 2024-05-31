from typing import Any, Dict

from django_components import component


@component.register('Button')
class Button(component.Component):
    template_name = 'template.html'

    def get_context_data(self, label: str, href: str = None, icon: str = '', primary: bool = True, submit: bool = False,
                         disabled: bool = False) -> Dict[
        str, Any]:
        return {
            'label': label,
            'disabled': disabled,
            'href': href,
            'icon': icon,
            'submit': submit,
            'primary': primary,
        }
