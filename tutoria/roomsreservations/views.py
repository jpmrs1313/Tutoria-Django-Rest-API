from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import RoomReservation
from .serializers import RoomReservationSerializer


class RoomReservationViewSet(ReadOnlyModelViewSet):
    queryset = RoomReservation.objects.all()
    serializer_class = RoomReservationSerializer
    permission_classes = [IsAuthenticated]
