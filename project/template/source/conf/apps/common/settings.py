from project.utils.lists import ordered_item, list_fragment


MIDDLEWARE_CLASSES = list_fragment(
    ordered_item('django.middleware.common.CommonMiddleware', before="*"),
    'django.middleware.csrf.CsrfViewMiddleware',
)