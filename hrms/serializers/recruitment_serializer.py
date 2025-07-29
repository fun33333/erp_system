"""
Serializer for Recruitment model.
"""
from rest_framework import serializers
from ..models.recruitment import Recruitment

class RecruitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitment
        fields = '__all__'
