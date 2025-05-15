from django.urls import path
from .views import (
    ProductListView,
    ProductCreateView,
    ProductEditView,
    ProductDeleteView,
)

urlpatterns = [
    path('create-product/', ProductCreateView.as_view(), name='create-product'),
    path('edit-product/<int:pk>/', ProductEditView.as_view(), name='edit-product'),
    path('delete-product/<int:pk>/', ProductDeleteView.as_view(), name='delete-product'),
    path('all-products/', ProductListView.as_view(), name='all-products'),
]
