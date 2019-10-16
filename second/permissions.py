from rest_framework import permissions


class TestPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated():
            return False
        # else:
        #     return True
