

from django import template

register = template.Library()

@register.simple_tag
def execute_python_code():
    # Your Python code here
    result = 2 + 2
    return result