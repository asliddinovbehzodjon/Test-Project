from rest_framework.permissions import BasePermission


# Custom permission for users with "is_active" = True.
class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
