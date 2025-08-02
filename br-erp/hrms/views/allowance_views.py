"""
ViewSet for Allowance model.
"""
from rest_framework import viewsets
from ..models.allowance import Allowance
from ..serializers.allowance_serializer import AllowanceSerializer

class AllowanceViewSet(viewsets.ModelViewSet):
    queryset = Allowance.objects.all()
    serializer_class = AllowanceSerializer
