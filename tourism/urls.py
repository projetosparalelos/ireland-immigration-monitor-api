from rest_framework import routers
from . views import PlacesViewSet

router = routers.DefaultRouter()
router.register(r'places', PlacesViewSet, base_name='Places')
urlpatterns = router.urls
