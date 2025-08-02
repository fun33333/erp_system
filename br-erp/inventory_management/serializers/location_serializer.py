from rest_framework import serializers
from inventory_management.models.location import Location

class LocationSerializer(serializers.ModelSerializer):
    """Serializer for Location model."""
    class Meta:
        model = Location
        fields = '__all__' 