from rest_framework.permissions import BasePermission
from users.permissions import IsSuperUser

class IsOwnerOrSuperUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.owner == request.user