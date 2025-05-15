from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import StorageProvider
from .serializers import StorageProviderSerializer

class StorageListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        storage = StorageProvider.objects.all()
        serializer = StorageProviderSerializer(storage, many=True)
        return Response(serializer.data)


class StorageBookView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            storage = StorageProvider.objects.get(pk=pk)
        except StorageProvider.DoesNotExist:
            return Response({'error': 'Storage not found'}, status=status.HTTP_404_NOT_FOUND)

        if storage.status == 'rented':
            return Response({'error': 'This storage is already rented.'}, status=status.HTTP_400_BAD_REQUEST)

        storage.status = 'rented'
        storage.current_occupancy = storage.storage_capacity
        storage.save()

        return Response({'message': f'Storage {storage.storage_location} has been rented.'})
