from rest_framework import permissions


class AdminOnly(permissions.BasePermission):
    """Permission for superuser and user with admin role"""

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return (
                request.user.is_superuser
                or request.user.role == 'admin'
            )
        return False
