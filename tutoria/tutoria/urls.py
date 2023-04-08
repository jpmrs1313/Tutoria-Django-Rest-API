"""tutoria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from users.views import CustomUserViewSet
from admins.views import AdminViewSet
from teachers.views import TeacherViewSet
from students.views import StudentViewSet
from meetings.views import MeetingViewSet
from rooms.views import RoomViewSet
from roomsreservations.views import RoomReservationViewSet

router = routers.DefaultRouter()
router.register(r"users", CustomUserViewSet)
router.register(r"admins", AdminViewSet)
router.register(r"students", StudentViewSet)
router.register(r"teachers", TeacherViewSet)
router.register(r"meetings", MeetingViewSet)
router.register(r"rooms", RoomViewSet)
router.register(r"roomsreservations", RoomReservationViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("__debug__/", include("debug_toolbar.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
]
