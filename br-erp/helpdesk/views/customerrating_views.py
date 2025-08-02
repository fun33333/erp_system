"""
ViewSet for CustomerRating model.
"""
from rest_framework import viewsets
from ..models.customerrating import CustomerRating
from ..serializers.customerrating_serializer import CustomerRatingSerializer
from ..permissions import IsHelpdeskAgent, IsTeamLead

class CustomerRatingViewSet(viewsets.ModelViewSet):
    queryset = CustomerRating.objects.all()
    serializer_class = CustomerRatingSerializer
    permission_classes = [IsHelpdeskAgent|IsTeamLead]
