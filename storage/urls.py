from django.urls import path
from .views import StorageListView, StorageBookView

urlpatterns = [
    path('', StorageListView.as_view(), name='storage-list'),
    path('<int:pk>/', StorageBookView.as_view(), name='storage-book'),
]
