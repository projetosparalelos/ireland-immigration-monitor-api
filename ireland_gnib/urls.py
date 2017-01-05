from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'searchs', views.SearchViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^site/', include('core.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

