from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mingo/', include('mingo.urls')),

]
