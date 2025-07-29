"""
DRF DefaultRouter for Helpdesk endpoints.
"""
from rest_framework.routers import DefaultRouter

from .views.automation_views import AutomationViewSet
from .views.ticket_views import TicketViewSet
from .views.workflow_views import WorkflowViewSet
from .views.sla_views import SLAViewSet
from .views.customerrating_views import CustomerRatingViewSet
from .views.customerupdate_views import CustomerUpdateViewSet
from .views.permissionrole_views import PermissionRoleViewSet

router = DefaultRouter()
router.register(r'automations', AutomationViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'workflows', WorkflowViewSet)
router.register(r'slas', SLAViewSet)
router.register(r'customerratings', CustomerRatingViewSet)
router.register(r'customerupdates', CustomerUpdateViewSet)
router.register(r'permissionroles', PermissionRoleViewSet)

urlpatterns = router.urls
