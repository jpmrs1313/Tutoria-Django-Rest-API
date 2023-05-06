from rest_framework import routers
from .views import MeetingViewSet, RoomViewSet, RoomReservationViewSet

router = routers.DefaultRouter()

router.register(r"", MeetingViewSet)
router.register(r"", RoomViewSet)
router.register(r"", RoomReservationViewSet)

urlpatterns = router.urls
