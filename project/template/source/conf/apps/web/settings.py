# -*- encoding:utf-8 -*-
"""
Common web-app settings
"""
from project.utils.settings import append_setting

append_setting('STATICFILES_FINDERS', 'conf.apps.web.staticfinders.StaticRootFinder')
append_setting('INTERNAL_IPS', ('127.0.0.1', 'localhost'))
