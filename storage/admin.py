from django.contrib import admin
from .models import StorageProvider

@admin.register(StorageProvider)
class StorageProviderAdmin(admin.ModelAdmin):
    list_display = ('storage_location', 'storage_capacity', 'current_occupancy', 'status', 'user')
