"""
ViewSet for PermissionRole model.
"""
from rest_framework import viewsets
from ..models.permissionrole import PermissionRole
from ..serializers.permissionrole_serializer import PermissionRoleSerializer
from ..permissions import IsHelpdeskManager

class PermissionRoleViewSet(viewsets.ModelViewSet):
    queryset = PermissionRole.objects.all()
    serializer_class = PermissionRoleSerializer
    permission_classes = [IsHelpdeskManager]
