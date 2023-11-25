from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


class IsUserOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        if request.method in permissions.SAFE_METHODS and request.user.is_authenticated and obj.username == request.user.username:
            return True
        if obj.username == request.user.username:
            return True
        return request.user.is_superuser
