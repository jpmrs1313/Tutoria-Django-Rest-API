from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password


class CustomUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    @action(detail=True, methods=["post"])
    def set_password(self, request, pk=None):
        user = self.get_object()
        password = request.data.get("password")
        token = request.data.get("token")

        if user.is_active:
            return Response(
                {"detail": "The user already define the password"}, status=400
            )

        if not token:
            return Response({"detail": "Verification code is required"}, status=400)

        if token != user.define_password_token:
            return Response({"detail": "Invalid verification code"}, status=400)

        if password:
            validate_password(password=password)
            user.set_password(password)
            user.is_active = True
            user.save()
            return Response({"detail": "Password updated successfully"})
        else:
            return Response({"detail": "Password is required"}, status=400)
