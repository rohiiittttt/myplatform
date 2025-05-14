from rest_framework import serializers
from .models import StorageProvider

class StorageProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageProvider
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']
