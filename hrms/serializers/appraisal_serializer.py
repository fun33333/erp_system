"""
Serializer for Appraisal model.
"""
from rest_framework import serializers
from ..models.appraisal import Appraisal

class AppraisalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appraisal
        fields = '__all__'
