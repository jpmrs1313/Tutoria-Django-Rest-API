from rest_framework import viewsets
from .models import RoomReservation
from .serializers import RoomReservationSerializer


class RoomReservationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RoomReservation.objects.all()
    serializer_class = RoomReservationSerializer
