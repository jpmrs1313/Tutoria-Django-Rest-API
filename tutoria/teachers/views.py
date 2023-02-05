from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher
from .serializers import TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def list(self, request):
        first_name = self.request.query_params.get("firtst_name", None)
        last_name = self.request.query_params.get("last_name", None)
        number = self.request.query_params.get("number", None)
        email = self.request.query_params.get("email", None)

        teachers = Teacher.objects.all()

        if email is not None:
            email = teachers.filter(user__email__startswith=email)

        if first_name is not None:
            teachers = teachers.filter(user__first_name__startswith=first_name)

        if last_name is not None:
            teachers = teachers.filter(user__last_name__startswith=last_name)

        if number is not None:
            teachers = teachers.filter(number__startswith=number)

        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
