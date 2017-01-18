from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^api/gnib/', include('core.urls')),
    url(r'^api/tourism/', include('tourism.urls')),
    url(r'^admin/', admin.site.urls),
]

