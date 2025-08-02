"""
ViewSet for Appraisal model.
"""
from rest_framework import viewsets
from ..models.appraisal import Appraisal
from ..serializers.appraisal_serializer import AppraisalSerializer

class AppraisalViewSet(viewsets.ModelViewSet):
    queryset = Appraisal.objects.all()
    serializer_class = AppraisalSerializer
