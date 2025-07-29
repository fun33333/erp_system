"""
Custom permissions for Helpdesk roles.
"""
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsHelpdeskAgent(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'is_helpdesk_agent') and request.user.is_helpdesk_agent

class IsTeamLead(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'is_team_lead') and request.user.is_team_lead

class IsHelpdeskManager(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'is_helpdesk_manager') and request.user.is_helpdesk_manager
