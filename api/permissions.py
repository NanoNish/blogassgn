from rest_framework import permissions

class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if (request.user and request.user.is_authenticated):
            return True
        return False 