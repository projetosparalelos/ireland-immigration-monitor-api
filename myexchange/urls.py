from rest_framework import routers
from . views import weather
from django.conf.urls import url, include


router = routers.DefaultRouter()
urlpatterns = router.urls

urlpatterns = [
    url('^weather/(?P<city_code>.+)/$', weather),
]
