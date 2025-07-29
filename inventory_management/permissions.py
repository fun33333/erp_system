"""
Custom permissions for Inventory Management roles.
"""
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminUser(BasePermission):
    """Allows access only to admin users."""
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsInventoryManager(BasePermission):
    """Allows access to inventory managers."""
    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'is_inventory_manager') and request.user.is_inventory_manager

class IsReadOnlyUser(BasePermission):
    """Allows read-only access."""
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
