from rest_framework import routers
from .views import ContentTypeViewSet, PolicyViewSet

router = routers.DefaultRouter()

router.register(r"contenttypes", ContentTypeViewSet)
router.register(r"policies", PolicyViewSet)

urlpatterns = router.urls
