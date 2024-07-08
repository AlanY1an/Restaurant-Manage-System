from django import template

register = template.Library()

@register.filter(name='truncatewords_custom')
def truncatewords_custom(value, arg):
    """
    Truncates a string to a certain number of words.
    """
    try:
        arg = int(arg)
    except ValueError:  # invalid literal for int()
        return value  # Fail silently.

    words = value.split()[:arg]
    if len(words) >= arg:
        words.append('...')
    return ' '.join(words)