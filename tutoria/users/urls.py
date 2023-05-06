from rest_framework import routers
from .views import (
    CustomUserViewSet,
    PasswordView,
    AdminViewSet,
    TeacherViewSet,
    StudentViewSet,
)

router = routers.DefaultRouter()

router.register(r"password", PasswordView, basename="password")
router.register(r"admins", AdminViewSet)
router.register(r"teachers", TeacherViewSet)
router.register(r"students", StudentViewSet)
router.register(r"", CustomUserViewSet)

urlpatterns = router.urls
