# -*- encoding:utf-8 -*-
'''
Common web-app urls
'''
from django.conf.urls.defaults import *

urlpatterns = patterns('web.views',
    (r'^$', 'greetings'),
)
