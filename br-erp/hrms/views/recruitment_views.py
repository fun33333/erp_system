"""
ViewSet for Recruitment model.
"""
from rest_framework import viewsets, filters
from ..models.recruitment import Recruitment
from ..serializers.recruitment_serializer import RecruitmentSerializer

class RecruitmentViewSet(viewsets.ModelViewSet):
    queryset = Recruitment.objects.all()
    serializer_class = RecruitmentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['full_name', 'email', 'phone', 'position_applied']
    ordering_fields = ['status']
