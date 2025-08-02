from rest_framework import serializers
from purchase_management.models.bill import Bill

class BillSerializer(serializers.ModelSerializer):
    """Serializer for Bill model."""
    class Meta:
        model = Bill
        fields = '__all__' 