from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from goods.views import *
from customer.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'e_shop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^index/', 'goods.views.all_products', name='home'),
    url(r'^contact/', 'customer.views.contactUs', name='contact'),
    url(r'^all_prod/', 'goods.views.all_products', name='all_prod'),
]
