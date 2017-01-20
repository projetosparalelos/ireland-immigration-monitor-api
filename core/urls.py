from django.conf.urls import url, include

from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'searchs', views.SearchViewSet)


urlpatterns = [
    url(r'^renewal/$', views.renewal, name='url_renewal'),
    url(r'^new-gnib/$', views.new_GNIB, name='url_new_GNIB'),
    url(r'^work-permit/$', views.work_permit, name='url_work_permit'),
    url(r'^', include(router.urls)),
]
