from rest_framework.permissions import BasePermission


class IsApprover(BasePermission):
    """Allows access only to users in the Approver group, or superusers."""
    def has_permission(self, request, view):
        user = request.user
        return bool(
            user.is_authenticated and
            (user.is_superuser or user.groups.filter(name='Approver').exists())
        )


class IsOperatorOrAbove(BasePermission):
    """Allows access to Operator, Approver, Admin group members, or superusers."""
    def has_permission(self, request, view):
        user = request.user
        return bool(
            user.is_authenticated and
            (user.is_superuser or user.groups.filter(
                name__in=['Operator', 'Approver', 'Admin']
            ).exists())
        )


class IsViewerOrAbove(BasePermission):
    """Allows read access to any authenticated user in any of the four groups, or superusers."""
    def has_permission(self, request, view):
        user = request.user
        return bool(
            user.is_authenticated and
            (user.is_superuser or user.groups.filter(
                name__in=['Viewer', 'Operator', 'Approver', 'Admin']
            ).exists())
        )