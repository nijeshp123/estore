
from rest_framework import serializers
from api.models import Products

class ProductsSerializer(serializers.ModelSerializer):

    id=serializers.CharField(read_only=True)

    class Meta:
        model=Products
        fields="__all__"