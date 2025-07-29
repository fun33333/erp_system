"""
ViewSet for Loan model.
"""
from rest_framework import viewsets
from ..models.loan import Loan
from ..serializers.loan_serializer import LoanSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
