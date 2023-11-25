from rest_framework import permissions
from rest_framework.views import Request, View


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        # Se for GET, todos terão acesso
        # if request.method == "GET":
        #     return True
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # # Se for POST, somente usuários administradores terão acesso
        # if request.user.is_authenticated and request.user.is_superuser:
        #     return True
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_superuser
        )
