from django.conf import settings
from project.utils.modules import get_module


def get_urlpatterns():
    urls = get_module(settings.ROOT_URLCONF)
    return getattr(urls, 'urlpatterns', ())


def set_urlpatterns(urlpatterns):
    urls = get_module(settings.ROOT_URLCONF)
    return setattr(urls, 'urlpatterns', urlpatterns)


def append_urlpatterns(urlpatterns):
    return set_urlpatterns(get_urlpatterns() + urlpatterns)


def prepend_urlpatterns(urlpatterns):
    return set_urlpatterns(urlpatterns + get_urlpatterns())