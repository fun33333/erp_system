"""
ViewSet for CustomerUpdate model.
"""
from rest_framework import viewsets
from ..models.customerupdate import CustomerUpdate
from ..serializers.customerupdate_serializer import CustomerUpdateSerializer
from ..permissions import IsHelpdeskManager

class CustomerUpdateViewSet(viewsets.ModelViewSet):
    queryset = CustomerUpdate.objects.all()
    serializer_class = CustomerUpdateSerializer
    permission_classes = [IsHelpdeskManager]
