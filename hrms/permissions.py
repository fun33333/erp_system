"""
HRMS role-based permissions.
"""
from rest_framework.permissions import BasePermission

class IsHRAdmin(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'is_hr_admin') and request.user.is_hr_admin

class IsHRManager(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'is_hr_manager') and request.user.is_hr_manager
