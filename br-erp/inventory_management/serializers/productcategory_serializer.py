from rest_framework import serializers
from inventory_management.models.productcategory import ProductCategory

class ProductCategorySerializer(serializers.ModelSerializer):
    """Serializer for ProductCategory model."""
    class Meta:
        model = ProductCategory
        fields = '__all__' 