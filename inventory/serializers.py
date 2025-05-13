from rest_framework import serializers
from .models import InventoryEntry

class InventoryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryEntry
        fields = '__all__'
        read_only_fields = ['updated_by', 'stock_balance', 'created_at']
