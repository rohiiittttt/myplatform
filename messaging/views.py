from rest_framework import viewsets, permissions
from .models import Message
from .serializers import MessageSerializer
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        message = serializer.save(sender=self.request.user)

        # Keyword-based auto-reply logic
        if message.message_type in ['dm', 'comment'] and message.product:
            content = message.message_content.lower()

            if 'price' in content:
                reply = f"The price of {message.product.name} is £{message.product.price}."
            elif 'available' in content or 'stock' in content:
                reply = (
                    f"Yes, {message.product.name} is in stock!"
                    if message.product.stock_quantity > 0
                    else f"Sorry, {message.product.name} is currently out of stock."
                )
            else:
                reply = f"Thanks for your message about {message.product.name}. We'll get back to you soon."

            Message.objects.create(
                sender=message.recipient,
                recipient=message.sender,
                message_content=reply,
                message_type='dm',
                status='sent',
                product=message.product
            )

    @action(detail=False, methods=['get'], url_path='seller-inbox')
    def seller_inbox(self, request):
        user = request.user
        messages = Message.objects.filter(product__user=user).order_by('-created_at')
        serializer = self.get_serializer(messages, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        user = self.request.user
        queryset = Message.objects.filter(Q(sender=user) | Q(recipient=user))

        # Optional filters
        sender_id = self.request.query_params.get('sender_id')
        recipient_id = self.request.query_params.get('recipient_id')
        message_type = self.request.query_params.get('message_type')
        status = self.request.query_params.get('status')

        if sender_id:
            queryset = queryset.filter(sender_id=sender_id)
        if recipient_id:
            queryset = queryset.filter(recipient_id=recipient_id)
        if message_type:
            queryset = queryset.filter(message_type=message_type)
        if status:
            queryset = queryset.filter(status=status)

        return queryset.order_by('-created_at')
