import os
from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def get_react_asset(start, asset_type):
    build_dir = os.path.join(
        settings.BASE_DIR,
        'home_pizzaria',
        'static',
        'react_app',
        'static',
        asset_type
    )
    try:
        for filename in os.listdir(build_dir):
            if filename.startswith(start):
                return f'react_app/static/{asset_type}/{filename}'
    except FileNotFoundError:
        return ''
    return ''
