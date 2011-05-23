import os
from project.utils.settings import get_setting, install_main_settings, install_apps_settings, cleanup_settings

install_main_settings()
#install_app_settings('conf.apps.contrib') # package that contains settings.py inside
#install_app_settings('conf.apps.django_project') # regular python module
install_apps_settings()
cleanup_settings()

DEBUG = True
TEMPLATE_DEBUG = DEBUG

#EMAIL_HOST = "pleso.net"
#EMAIL_PORT = "25"
#EMAIL_HOST_USER = "bot@inmind.org"
#EMAIL_HOST_PASSWORD = ""
#EMAIL_SUBJECT_PREFIX = "website (local) - "

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'
        'NAME': os.path.join(get_setting('PROJECT_ROOT'), 'source', 'db', 'dev.sqlite'),
    }
}
