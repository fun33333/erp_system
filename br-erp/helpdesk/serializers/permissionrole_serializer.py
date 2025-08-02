"""
Serializer for PermissionRole model.
"""
from rest_framework import serializers
from ..models.permissionrole import PermissionRole

class PermissionRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionRole
        fields = '__all__'
