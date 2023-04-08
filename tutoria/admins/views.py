from rest_framework import viewsets
from .models import Admin
from .serializers import AdminSerializer


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.select_related("user")
    serializer_class = AdminSerializer
