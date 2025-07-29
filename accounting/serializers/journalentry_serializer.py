"""
Serializer for JournalEntry model.
"""
from rest_framework import serializers
from ..models.journalentry import JournalEntry

class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = '__all__'
