#Convert data to JSON format
from rest_framework import serializers
from .models import Store, Product


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_id', 'store_location', 'store_created_date', 'store_updated_date']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'product_created_date', 'product_updated_date']