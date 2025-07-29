from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from purchase_management.models.bill import Bill
from purchase_management.serializers.bill_serializer import BillSerializer

class BillViewSet(viewsets.ModelViewSet):
    """API endpoint for Bill CRUD operations."""
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['order', 'bill_date', 'due_date', 'is_paid']
    search_fields = ['order__vendor__name']
    ordering_fields = ['bill_date', 'due_date', 'amount']
    ordering = ['-bill_date'] 