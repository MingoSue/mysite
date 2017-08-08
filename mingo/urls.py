from django.conf.urls import url
# from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^show_data/$', views.show_data, name='show_data'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^form_page/$', views.form_page, name='form_page'),

]