from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from django.db.models import Q

User = get_user_model()

class OrderRequest(models.Model):  # ✅ Exact name
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='placed_orders')
    quantity = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('approved', 'Approved'), ('declined', 'Declined')],
        default='pending'
    )
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
