from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

class Message(models.Model):
    MESSAGE_TYPES = [
        ('text', 'Text'),
        ('dm', 'Direct Message'),
        ('comment', 'Social Media Comment'),
    ]

    STATUS_CHOICES = [
        ('sent', 'Sent'),
        ('read', 'Read'),
    ]

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message_content = models.TextField()
    message_type = models.CharField(max_length=20, choices=[('dm', 'DM'), ('comment', 'Comment')])
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='sent')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender.username} → {self.recipient.username}: {self.message_content[:30]}"
