from rest_framework.permissions import BasePermission, SAFE_METHODS


class NetaPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['create', 'update']:
            return request.user.is_superuser
        elif view.action in ['list', 'retrive']:
            return request.user.is_authenticated
        else:
            return False
## OR ###

class Test(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return False