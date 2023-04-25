from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Admin
from .serializers import AdminSerializer


class AdminViewSet(ModelViewSet):
    queryset = Admin.objects.select_related("user")
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated]
