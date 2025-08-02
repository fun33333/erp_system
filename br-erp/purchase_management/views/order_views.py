from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from purchase_management.models.order import Order
from purchase_management.serializers.order_serializer import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """API endpoint for Order CRUD operations."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'vendor', 'order_date', 'delivery_date']
    search_fields = ['vendor__name', 'requisition__product__name']
    ordering_fields = ['order_date', 'delivery_date', 'status']
    ordering = ['-order_date'] 