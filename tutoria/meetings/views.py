from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Meeting, Room, RoomReservation
from .serializers import MeetingSerializer, RoomSerializer, RoomReservationSerializer
from permissions.utils import HasPermission


class RoomReservationViewSet(ReadOnlyModelViewSet):
    queryset = RoomReservation.objects.all()
    serializer_class = RoomReservationSerializer
    permission_classes = [IsAuthenticated, HasPermission]


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated, HasPermission]


class MeetingViewSet(ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [AllowAny]
