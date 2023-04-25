from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import CustomUserSerializer
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password


class CustomUserViewSet(ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]


class PasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        token = request.data.get("token")

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({"detail": f"No user with email {email}"}, status=400)

        if user.is_active:
            return Response({"detail": "User already set the password"}, status=400)

        if not token:
            return Response({"detail": "Verification code is required"}, status=400)

        if token != user.define_password_token:
            return Response({"detail": "Invalid verification code"}, status=400)

        if not password:
            return Response({"detail": "Password is required"}, status=400)

        try:
            validate_password(password=password)
        except Exception as e:
            return Response({"detail": str(e)}, status=400)

        user.set_password(password)
        user.is_active = True
        user.save()

        return Response({"detail": "Password updated successfully"})
