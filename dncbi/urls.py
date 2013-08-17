from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^pubmed/', include('pubmed.urls')),
    url(r'^demo/', include('demo.urls')),
)
