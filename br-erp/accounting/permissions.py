"""
Role-based permissions for Accounting system.
"""
from rest_framework.permissions import BasePermission

class IsAccountant(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'is_accountant') and request.user.is_accountant

class IsFinanceManager(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'is_finance_manager') and request.user.is_finance_manager

class IsAuditor(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'is_auditor') and request.user.is_auditor
