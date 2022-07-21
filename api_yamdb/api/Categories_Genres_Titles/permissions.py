from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            print(request.user)
            return True
        if request.user.is_authenticated and request.user.role == "admin":
            print(request.user)
            return True
