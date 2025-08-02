"""
ViewSet for BankStatement model.
"""
from rest_framework import viewsets, filters
from ..models.bankstatement import BankStatement
from ..serializers.bankstatement_serializer import BankStatementSerializer

class BankStatementViewSet(viewsets.ModelViewSet):
    queryset = BankStatement.objects.all()
    serializer_class = BankStatementSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['bank_account__account_name']
    ordering_fields = ['statement_date']
