from django.conf.urls import patterns, url

from contacts import views

urlpatterns = patterns('',
    # Examples:

    # url(r'^$', 'contactmgr.views.home', name='home'),
    # url(r'^contactmgr/', include('contactmgr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.ListContactsView.as_view(), name='contacts-list',),
    url(r'^new$', views.CreateContactView.as_view(), name='contacts-new',),
)
