from rest_framework import serializers
from .models import OrderRequest
from products.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

class ProductSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']

class BuyerSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class OrderRequestSerializer(serializers.ModelSerializer):
    buyer_username = serializers.CharField(source='buyer.username', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderRequest
        fields = ['id', 'product', 'product_name', 'buyer', 'buyer_username', 'quantity', 'status', 'message', 'created_at']
        read_only_fields = ['id', 'created_at', 'buyer']

