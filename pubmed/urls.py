from django.conf.urls import patterns, include, url

from pubmed import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', views.dispatch),
    #url(r'^search', views.dosearch),
    # Examples:
    # url(r'^$', 'dncbi.views.home', name='home'),
    # url(r'^dncbi/', include('dncbi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
