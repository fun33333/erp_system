from rest_framework import serializers
from accounting.models.ledger import Ledger

class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = '__all__' 