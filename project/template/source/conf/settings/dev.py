import os
from project.utils.settings import get_setting, import_settings
from project.utils.install import install_settings, install_app

install_settings('conf.settings.main')
install_app('django.contrib.admin', 'conf.apps.admin')
install_app('web', 'conf.apps.web')
import_settings(globals())

DEBUG = TEMPLATE_DEBUG = True

#EMAIL_HOST = ''
#EMAIL_PORT = ''
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_USE_TLS = True
#EMAIL_HOST_PASSWORD = ''
#EMAIL_SUBJECT_PREFIX = '[website] '

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'
        'NAME': os.path.join(get_setting('PROJECT_ROOT'), 'source', 'db', 'dev.sqlite'),
    }
}
