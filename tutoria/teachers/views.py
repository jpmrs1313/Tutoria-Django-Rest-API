from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Teacher
from .serializers import TeacherSerializer
from .filters import TeacherFilter


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.select_related("user")
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TeacherFilter
    permission_classes = [IsAuthenticated]
