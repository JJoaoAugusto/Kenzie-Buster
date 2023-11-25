from rest_framework.views import APIView, Request, Response, status
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomJWTSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsUserOwnerOrAdmin


class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer


class UserDetailView(APIView):
    permission_classes = [
        IsUserOwnerOrAdmin
    ]
    authentication_classes = [
        JWTAuthentication
    ]

    def get(self, request: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, found_user)
        serializer = UserSerializer(found_user)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, found_user)
        serializer = UserSerializer(
            found_user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
