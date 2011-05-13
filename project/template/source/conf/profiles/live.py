import os
from project.utils.settings import get_setting

DEBUG = False
TEMPLATE_DEBUG = DEBUG

#EMAIL_HOST = "pleso.net"
#EMAIL_PORT = "25"
#EMAIL_HOST_USER = "bot@inmind.org"
#EMAIL_HOST_PASSWORD = ""
#EMAIL_SUBJECT_PREFIX = "website (local) - "

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'
        'NAME': os.path.join(get_setting('PROJECT_ROOT'), 'source', 'db', 'live.sqlite'),
    }
}
