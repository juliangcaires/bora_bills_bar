from django import template
register = template.library()

@register.filter
def get_item(obj, key):
    if isinstance(obj, dict):
        return obj.get(key)
    
    try:
        return getattr(obj, key)
    except Exception:
        return None