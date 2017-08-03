from django.conf.urls import url
# from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hello/$', views.hello, name='hello'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^form_page/$', views.form_page, name='form_page'),

]