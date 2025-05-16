from rest_framework import viewsets, permissions
from .models import InventoryEntry
from .serializers import InventoryEntrySerializer

class InventoryEntryViewSet(viewsets.ModelViewSet):
    queryset = InventoryEntry.objects.all() 
    serializer_class = InventoryEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return InventoryEntry.objects.filter(product__user=self.request.user)

    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        quantity_added = serializer.validated_data.get('quantity_added', 0)
        quantity_removed = serializer.validated_data.get('quantity_removed', 0)

        new_balance = product.stock_quantity + quantity_added - quantity_removed
        product.stock_quantity = new_balance
        product.save()

        serializer.save(
            updated_by=self.request.user,
            stock_balance=new_balance
        )
