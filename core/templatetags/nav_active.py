# your_app/templatetags/nav_active.py
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def active_class(context, *url_names):
    """
    Usage: {% active_class 'inbound:admin_list' 'inbound:admin_create' %}
    Returns: 'active submenu' or '' based on current path
    """
    request = context.get('request')
    current_url = request.resolver_match.view_name if request and request.resolver_match else ''
    return 'active submenu' if current_url in url_names else ''

@register.simple_tag(takes_context=True)
def show_class(context, *url_names):
    """
    For collapse divs: {% show_class 'inbound:admin_list' %}
    Returns: 'show' or ''
    """
    request = context.get('request')
    current_url = request.resolver_match.view_name if request and request.resolver_match else ''
    return 'show' if current_url in url_names else ''

@register.simple_tag(takes_context=True)
def li_active(context, *url_names):
    """
    For list items: {% li_active 'inbound:admin_list' %}
    """
    request = context.get('request')
    current_url = request.resolver_match.view_name if request and request.resolver_match else ''
    return 'active' if current_url in url_names else ''
