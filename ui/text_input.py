from django.forms.renderers import get_default_renderer
from django.forms.widgets import TextInput as DjangoTextInput
from django.utils.safestring import mark_safe


# class TextInput(Input):
#     """
#     Used for any TextInputs, default type 'text'
#     
#     Attrs:
#         type
#         name - required
#         label - required
#         placeholder
#         error_message
#     """
#     template_name = 'input.html'
# 
#     def get_context(self, name, value, attrs):
#         context = super().get_context(name, value, attrs)
#         context['widget']['type'] = attrs.get('type')
#         context['widget']['name'] = attrs.get('name')
#         context['widget']['label'] = attrs.get('label')
#         context['widget']['placeholder'] = attrs.get('placeholder', '')
#         context['widget']['error'] = attrs.get('error_message', '')
#         return context
# 
#     def render(self, name, value, attrs=None, renderer=None):
#         context = self.get_context(name, value, attrs)
#         return self._render(self.template_name, context, renderer)

class TextInput(DjangoTextInput):
    template_name = 'input.html'

    def render(self, name, value, attrs=None, renderer=None):
        """Render the widget as an HTML string."""
        context = self.get_context(name, value, attrs)
        if renderer is None:
            renderer = get_default_renderer()
        return mark_safe(renderer.render(self.template_name, context))
