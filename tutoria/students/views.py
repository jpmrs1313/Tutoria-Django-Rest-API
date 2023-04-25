from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Student
from .serializers import StudentSerializer
from .filters import StudentFilter


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.select_related("user")
    serializer_class = StudentSerializer
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_class = StudentFilter
    permission_classes = [IsAuthenticated]
