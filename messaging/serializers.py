from rest_framework import serializers
from .models import Message
from django.contrib.auth import get_user_model

User = get_user_model()

class MessageSerializer(serializers.ModelSerializer):
    recipient = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )
    sender_username = serializers.CharField(source='sender.username', read_only=True)

    class Meta:
        model = Message
        fields = [
            'id', 'sender', 'recipient', 'message_content',
            'message_type', 'status', 'product', 'created_at',
            'sender_username'
        ]
        read_only_fields = ['sender']
