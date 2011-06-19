from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from project.utils.install import install_apps_urls

urlpatterns = patterns('')
     
# Adding debug-mappings
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

install_apps_urls()

# Unregister
#from django.contrib.auth.models import User, Group
#admin.site.unregister(User)
#admin.site.unregister(Group)