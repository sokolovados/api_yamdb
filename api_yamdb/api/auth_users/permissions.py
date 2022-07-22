from rest_framework import permissions


class AdminOnly(permissions.BasePermission):
    """Permission for superuser and user with admin role"""

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return (
                    request.user.is_superuser or
                    request.user.role == 'admin'
            )
        return False


class UserOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
                obj.username == request.user.username
        )


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        role = request.data.get('role')
        if not user.is_authenticated:
            return False
        if role and user.role != role:
            return False
        return True
