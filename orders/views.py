from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.db.models import Q
from .models import OrderRequest
from .serializers import OrderRequestSerializer

class OrderRequestViewSet(viewsets.ModelViewSet):
    queryset = OrderRequest.objects.all()
    serializer_class = OrderRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return OrderRequest.objects.filter(Q(buyer=user) | Q(product__user=user))  

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()

        # ✅ Only the seller can update order status
        if instance.product.user != request.user:
            return Response({"detail": "Only the seller can update this order."}, status=status.HTTP_403_FORBIDDEN)

        new_status = request.data.get("status")
        if new_status not in ['approved', 'declined']:
            return Response({"detail": "Invalid status value."}, status=status.HTTP_400_BAD_REQUEST)

        instance.status = new_status
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
