from django.urls import path
from .views import StorageListView, book_storage  

urlpatterns = [
    path('', StorageListView.as_view(), name='storage-list'),
    path('book/<int:storage_id>/', book_storage, name='book_storage'),
]
