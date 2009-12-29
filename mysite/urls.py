from django.conf.urls.defaults import *
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^texts/', include('closecommenting.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^wmd/js/$', 'wmd.views.wmd_js', name='wmd-js'),
    url(r'^wmd-settings/js/$', 'wmd.views.wmd_settings_js', name='wmd-settings-js'),
    url(r'^wmd/css/$', 'wmd.views.wmd_css', name='wmd-css'),
)

if settings.LOCAL_DEV:
    baseurlregex = r'^static/(?P<path>.*)$'
    urlpatterns += patterns('',
        (baseurlregex, 'django.views.static.serve',
        {'document_root':  settings.MEDIA_ROOT}),
    )
