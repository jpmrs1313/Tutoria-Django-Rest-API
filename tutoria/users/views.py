from rest_framework import viewsets, mixins, filters, permissions
from django_filters import rest_framework
from .models import CustomUser, Admin, Teacher, Student
from .serializers import (
    CustomUserSerializer,
    PasswordSerializer,
    AdminSerializer,
    TeacherSerializer,
    StudentSerializer,
)
from .filters import UserBaseFilter, StudentFilter, TeacherFilter

FILTERS_BACKEND = [
    rest_framework.DjangoFilterBackend,
    filters.SearchFilter,
    filters.OrderingFilter,
]


class CustomUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filterset_class = UserBaseFilter
    permission_classes = [permissions.IsAuthenticated]


class PasswordView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = PasswordSerializer
    permission_classes = [permissions.AllowAny]


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.select_related("user")
    serializer_class = AdminSerializer
    filterset_class = UserBaseFilter
    permission_classes = [permissions.IsAuthenticated]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.select_related("user")
    serializer_class = TeacherSerializer
    filter_backends = FILTERS_BACKEND
    filterset_class = TeacherFilter
    permission_classes = [permissions.IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related("user")
    serializer_class = StudentSerializer
    filter_backends = FILTERS_BACKEND
    filterset_class = StudentFilter
    permission_classes = [permissions.IsAuthenticated]
