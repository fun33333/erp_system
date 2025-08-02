"""
ViewSet for Asset model.
"""
from rest_framework import viewsets, filters
from ..models.asset import Asset
from ..serializers.asset_serializer import AssetSerializer

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['asset_name', 'depreciation_method']
    ordering_fields = ['purchase_date', 'current_value']
