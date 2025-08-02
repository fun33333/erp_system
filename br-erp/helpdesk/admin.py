"""
Admin registration for Helpdesk models.
"""
from django.contrib import admin

from .models.automation import Automation
from .models.ticket import Ticket
from .models.workflow import Workflow
from .models.sla import SLA
from .models.customerrating import CustomerRating
from .models.customerupdate import CustomerUpdate
from .models.permissionrole import PermissionRole

@admin.register(Automation)
class AutomationAdmin(admin.ModelAdmin):
    list_display = ('automation_name', 'trigger_event', 'action_type', 'action_target', 'is_active')
    list_filter = ('trigger_event', 'action_type', 'is_active')
    search_fields = ('automation_name', 'action_target')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'subject', 'customer_email', 'priority', 'status', 'channel', 'created_at', 'assigned_to')
    list_filter = ('priority', 'status', 'channel', 'assigned_to')
    search_fields = ('subject', 'customer_email', 'ticket_number')

@admin.register(Workflow)
class WorkflowAdmin(admin.ModelAdmin):
    list_display = ('workflow_name', 'trigger_status', 'next_status')
    list_filter = ('trigger_status', 'next_status')
    search_fields = ('workflow_name',)

@admin.register(SLA)
class SLAAdmin(admin.ModelAdmin):
    list_display = ('sla_name', 'priority_level', 'response_time_minutes', 'resolution_time_minutes', 'apply_to_group')
    list_filter = ('priority_level', 'apply_to_group')
    search_fields = ('sla_name',)

@admin.register(CustomerRating)
class CustomerRatingAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'rating', 'feedback_comment', 'submitted_at')
    list_filter = ('rating', 'submitted_at')
    search_fields = ('feedback_comment',)

@admin.register(CustomerUpdate)
class CustomerUpdateAdmin(admin.ModelAdmin):
    list_display = ('update_type', 'send_email', 'send_sms', 'delay_seconds')
    list_filter = ('update_type', 'send_email', 'send_sms')
    search_fields = ('message_template',)

@admin.register(PermissionRole)
class PermissionRoleAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'can_view_all', 'can_assign', 'can_change_status', 'can_edit_ticket', 'can_view_reports')
    list_filter = ('role_name',)
