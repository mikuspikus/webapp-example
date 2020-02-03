from django import template

register = template.Library()

@register.inclusion_tag('application/custom_tags/custom_render.html')
def custom_render(form):
    return {'form': form}