# -*- encoding:utf-8 -*-
'''
Common web-app views
'''
from django.views.generic.base import TemplateView

class Greetings(TemplateView):
    template_name = "web/base.html"
greetings = Greetings.as_view()