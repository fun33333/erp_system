from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from purchase_management.models.payment import Payment
from purchase_management.serializers.payment_serializer import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    """API endpoint for Payment CRUD operations."""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['bill', 'payment_date', 'payment_method']
    search_fields = ['reference_no', 'bill__order__vendor__name']
    ordering_fields = ['payment_date', 'amount']
    ordering = ['-payment_date'] 