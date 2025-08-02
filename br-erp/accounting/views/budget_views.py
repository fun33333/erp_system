"""
ViewSet for Budget model.
"""
from rest_framework import viewsets, filters
from ..models.budget import Budget
from ..serializers.budget_serializer import BudgetSerializer

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['department', 'fiscal_year']
    ordering_fields = ['fiscal_year', 'allocated_budget', 'used_budget']
