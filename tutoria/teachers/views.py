from rest_framework import viewsets
from rest_framework.response import Response
from .models import Teacher
from .serializers import TeacherSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "first_name",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Filter by first name",
            ),
            openapi.Parameter(
                "last_name",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Filter by last name",
            ),
            openapi.Parameter(
                "number",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Filter by number",
            ),
            openapi.Parameter(
                "email",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Filter by email",
            ),
        ]
    )
    def list(self, request):
        first_name = self.request.query_params.get("first_name", None)
        last_name = self.request.query_params.get("last_name", None)
        number = self.request.query_params.get("number", None)
        email = self.request.query_params.get("email", None)

        teachers = Teacher.objects.all()

        if email is not None:
            teachers = teachers.filter(user__email=email)

        if first_name is not None:
            teachers = teachers.filter(user__first_name=first_name)

        if last_name is not None:
            teachers = teachers.filter(user__last_name=last_name)

        if number is not None:
            teachers = teachers.filter(number=number)

        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
