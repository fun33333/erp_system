"""
ViewSet for Contract model.
"""
from rest_framework import viewsets
from ..models.contract import Contract
from ..serializers.contract_serializer import ContractSerializer

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
