from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class StorageProvider(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    storage_location = models.CharField(max_length=255)
    storage_capacity = models.PositiveIntegerField()
    current_occupancy = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default='available')  

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.storage_location} ({self.user.username})"
