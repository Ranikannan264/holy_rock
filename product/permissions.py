from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrAdmin(BasePermission):
    """
    Only the owner of the object or an admin can edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Allow read-only access for anyone
        if request.method in SAFE_METHODS:
            return True

        # Allow write/delete only to the owner or admin
        return obj.owner == request.user or request.user.is_staff
