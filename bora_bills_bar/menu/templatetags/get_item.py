from django import template
register = template.Library()

@register.filter #@ decorator pega função e encapsula ela

def get_item(obj, key):

  if isinstance(obj,dict):
    return obj.get(key)
  try: #tratamento de erro
    return getattr(obj,key)
  except Exception:
    return None