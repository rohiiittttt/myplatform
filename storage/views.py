from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import StorageProvider
from .serializers import StorageProviderSerializer


class StorageListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        storages = StorageProvider.objects.all()
        serializer = StorageProviderSerializer(storages, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_storage(request, storage_id):
    try:
        storage = StorageProvider.objects.get(id=storage_id)

        if storage.status != "available":
            return Response({"detail": "Storage not available."}, status=status.HTTP_400_BAD_REQUEST)

     
        storage.status = "rented"
        storage.current_occupancy = storage.storage_capacity  
        storage.save()

        return Response({"message": "Storage booked successfully."}, status=status.HTTP_200_OK)

    except StorageProvider.DoesNotExist:
        return Response({"detail": "Storage not found."}, status=status.HTTP_404_NOT_FOUND)
