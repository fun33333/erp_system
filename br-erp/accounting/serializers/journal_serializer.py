"""
Serializer for Journal model.
"""
from rest_framework import serializers
from ..models.journal import Journal

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'
