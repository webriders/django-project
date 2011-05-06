from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

MEDIA_ROOT = getattr(settings, 'MEDIA_ROOT', '/media/')
MEDIA_URL = getattr(settings, 'MEDIA_URL', '/media/')
STATIC_ROOT = getattr(settings, 'STATIC_ROOT', '/static/')
STATIC_URL = getattr(settings, 'STATIC_URL', '/static/')

urlpatterns = patterns('',
    ## External applications mappings
    #(r'^admin_tools/', include('admin_tools.urls')),
    #(r'^admin/filebrowser/', include('filebrowser.urls')),
    #(r'^admin/', include(admin.site.urls)),
    #(r'^tinymce/', include('tinymce.urls')),
    #(r'^rosetta/', include('rosetta.urls')),
	#(r'^robots\.txt$', 'django.views.generic.simple.redirect_to', {'url': '%srobots.txt' % STATIC_URL[1:]}),
	## Internal applications mappings
    (r'', include('website.urls')),
)
     
# Adding debug-mappings
if settings.DEBUG:
    # Debug media and static
    urlpatterns += patterns('',
                            (r'^%s(?P<path>.*)$' % MEDIA_URL[1:], 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                            (r'^%s(?P<path>.*)$' % STATIC_URL[1:], 'django.views.static.serve', {'document_root': STATIC_ROOT}),
                            )

# Unregister
from django.contrib.auth.models import User, Group
admin.site.unregister(User)
admin.site.unregister(Group)