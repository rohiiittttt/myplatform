from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from products.models import Product

class InventoryEntry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory_logs')
    quantity_added = models.IntegerField(default=0)
    quantity_removed = models.IntegerField(default=0)
    stock_balance = models.IntegerField()  # New stock level after update
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} updated by {self.updated_by.username}"

