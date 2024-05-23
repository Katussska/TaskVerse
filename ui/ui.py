from django.forms.renderers import get_default_renderer
from django.forms.widgets import TextInput as DjangoTextInput
from django.forms.widgets import Textarea as DjangoTextArea
from django.forms.widgets import SelectMultiple as DjangoSelectMultiple
from django.utils.safestring import mark_safe


class TextInput(DjangoTextInput):
    template_name = 'input.html'

    def render(self, name, value, attrs=None, renderer=None):
        """Render the widget as an HTML string."""
        context = self.get_context(name, value, attrs)
        if renderer is None:
            renderer = get_default_renderer()
        return mark_safe(renderer.render(self.template_name, context))


class TextArea(DjangoTextArea):
    template_name = 'textarea.html'

    def __init__(self, attrs=None):
        default_attrs = {'rows': '6'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)


class SelectMultiple(DjangoSelectMultiple):
    template_name = 'select_multiple.html'
   