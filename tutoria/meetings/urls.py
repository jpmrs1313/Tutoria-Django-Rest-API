from rest_framework import routers
from .views import MeetingViewSet, RoomViewSet, RoomReservationViewSet

router = routers.DefaultRouter()


router.register(r"rooms", RoomViewSet)
router.register(r"roomreservations", RoomReservationViewSet)
router.register(r"", MeetingViewSet)

urlpatterns = router.urls
