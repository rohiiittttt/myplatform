from rest_framework import viewsets, permissions
from .models import StorageProvider
from .serializers import StorageProviderSerializer

class StorageProviderViewSet(viewsets.ModelViewSet):
    queryset = StorageProvider.objects.all()
    serializer_class = StorageProviderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StorageProvider.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
