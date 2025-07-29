from rest_framework import serializers
from inventory_management.models.stockjournal import StockJournal

class StockJournalSerializer(serializers.ModelSerializer):
    """Serializer for StockJournal model."""
    class Meta:
        model = StockJournal
        fields = '__all__' 