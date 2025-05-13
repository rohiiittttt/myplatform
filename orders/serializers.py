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
    product = ProductSummarySerializer(read_only=True)
    buyer = BuyerSummarySerializer(read_only=True)

    class Meta:
        model = OrderRequest
        fields = '__all__'
        read_only_fields = ['buyer', 'status', 'created_at', 'updated_at']
