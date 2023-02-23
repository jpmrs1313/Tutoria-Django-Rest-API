from rest_framework import viewsets
from .serializers import CustomUserSerializer
from .models import CustomUser

class CustomUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer