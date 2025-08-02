from rest_framework import serializers
from purchase_management.models.vendor import Vendor

class VendorSerializer(serializers.ModelSerializer):
    """Serializer for Vendor model."""
    class Meta:
        model = Vendor
        fields = '__all__' 