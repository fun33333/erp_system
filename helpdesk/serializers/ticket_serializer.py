"""
Serializer for Ticket model.
"""
from rest_framework import serializers
from ..models.ticket import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
